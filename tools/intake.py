#!/usr/bin/env python3
"""Mint candidate org cards from a harvested source file.

    python3 tools/intake.py <source-id>            # dry run
    python3 tools/intake.py <source-id> --write    # write the stubs

Reads intake/<source-id>.tsv (header row, required columns: name, url; optional:
name_ja, size, country, industry, note, licence). `url` must be the OPERATING
COMPANY's site, not a product page — cashari is the product, ガレージバンク株式会社
is the company, and the company is who signs a contract. and creates one stub per row that
is not already carded. Dedupes on slug id AND on website host, so re-running a source
after it updates adds only what is new. Existing cards are never overwritten.
"""
import csv
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ORG = ROOT / "entities" / "org"
INTAKE = ROOT / "intake"
SOURCES = INTAKE / "sources.yaml"

FM = re.compile(r"\A---\n(.*?)\n---", re.S)


def host(url):
    """Bare hostname, lowercased, no scheme/www/trailing slash — the dedupe key."""
    if not url:
        return ""
    u = re.sub(r"^https?://", "", url.strip().lower())
    return u.split("/")[0].removeprefix("www.")


# Suffixes stripped when deriving an id from a hostname, longest first.
TLDS = (".co.jp", ".or.jp", ".ne.jp", ".com.hk", ".com.tw", ".co.uk",
        ".com", ".jp", ".net", ".org", ".io", ".hk", ".sg", ".insurance")


def slug(name, url=""):
    """A filesystem-safe id fragment, derived from the website host wherever there is one.

    Host-first is deliberate. Deriving ids from names looks friendlier but breaks on
    mixed-script Japanese company names: "SBIいきいき少額短期保険" strips down to "sbi",
    as do the four other SBI micro-insurers, and five distinct companies collapse into
    one id. Hosts are unique by construction, and stripping the TLD keeps them readable
    (ribon.com -> ribon, www.n-ssi.co.jp -> n-ssi).
    """
    h = host(url)
    if h:
        for tld in TLDS:
            if h.endswith(tld):
                h = h[: -len(tld)]
                break
        out = re.sub(r"[^a-z0-9]+", "-", h).strip("-")
        if out:
            return out
    s = unicodedata.normalize("NFKC", name).lower()
    s = re.sub(r"[（(].*?[)）]", "", s)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def existing():
    """Map every carded org to its id and its website hosts."""
    by_id, by_host = {}, {}
    for path in ORG.glob("*.md"):
        m = FM.match(path.read_text(encoding="utf-8"))
        if not m:
            continue
        meta = yaml.safe_load(m.group(1)) or {}
        oid = meta.get("id")
        if not oid:
            continue
        by_id[oid] = path.name
        for link in meta.get("links") or []:
            h = host(link.get("url", ""))
            if h:
                by_host.setdefault(h, path.name)
    return by_id, by_host


STUB = """---
id: {oid}
type: org
name: {name}
{name_ja}role: buyer
scope: company
country: {country}
industry: [{industry}]
size: {size}
status: candidate
confidence: low
source: {source}
first_seen: {today}
site: {url}
tags: [target, candidate, {source}]
rel: []
links:
  - label: Corporate site
    url: {url}
updated: {today}
---

Candidate, harvested from **{source_name}** on {today}. Not yet reviewed.

{note}To qualify this card, establish and write up:

- Is `site` the operating company, or did the source give a product page? Find the company.
- What model does the business actually depend on, and what does it decide?
- Is it licensed or supervised, and under which regime?
- Who would ask them for an independent opinion — a regulator, a funding counterparty, a
  bank or insurer partner, or an investor?
- Roughly what size, and can they pay?

Then set `size`, `priority` and a one-line `pitch`, replace this body, and move `status` to
`qualified`. If it does not fit, retire it with a reason rather than deleting it:

    python3 tools/retire.py {oid} "reason"
"""


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    source_id = sys.argv[1]
    write = "--write" in sys.argv

    registry = yaml.safe_load(SOURCES.read_text(encoding="utf-8"))["sources"]
    source = next((s for s in registry if s["id"] == source_id), None)
    if not source:
        sys.exit(f"unknown source {source_id!r}; register it in intake/sources.yaml first")

    tsv = INTAKE / f"{source_id}.tsv"
    if not tsv.exists():
        sys.exit(f"missing {tsv.relative_to(ROOT)} — harvest the source into it first")

    by_id, by_host = existing()
    rows = list(csv.DictReader(tsv.read_text(encoding="utf-8").splitlines(), delimiter="\t"))
    today = date.today().isoformat()
    new, known, bad = [], [], []

    for row in rows:
        name = (row.get("name") or "").strip()
        url = (row.get("url") or "").strip()
        if not name:
            bad.append(f"row without a name: {row}")
            continue
        h = host(url)
        base = slug(name, url)
        if not base:
            bad.append(f"cannot derive an id for {name!r} (no latin name, no url)")
            continue
        oid = f"org-{base}"
        if oid in by_id:
            known.append(f"{name} -> {by_id[oid]} (id)")
            continue
        if h and h in by_host:
            known.append(f"{name} -> {by_host[h]} (host {h})")
            continue

        note = (row.get("note") or "").strip()
        body_note = f"Source note: {note}\n\n" if note else ""
        stub = STUB.format(
            oid=oid, name=name,
            name_ja=f"name_ja: {row['name_ja'].strip()}\n" if row.get("name_ja", "").strip() else "",
            country=(row.get("country") or source.get("jurisdiction") or "JP").strip(),
            industry=(row.get("industry") or "banking").strip(),
            size=(row.get("size") or "sme").strip(),
            source=source_id, source_name=source["name"],
            url=url, today=today, note=body_note,
        )
        new.append((oid, stub))
        by_id[oid] = f"{base}.md"
        if h:
            by_host[h] = f"{base}.md"

    for b in bad:
        print(f"  skip   {b}")
    for k in known:
        print(f"  known  {k}")
    for oid, _ in new:
        print(f"  NEW    {oid}")

    print(f"\n{source_id}: {len(rows)} rows, {len(new)} new, {len(known)} already carded, {len(bad)} unusable")
    if not write:
        print("dry run — pass --write to create the stubs")
        return
    for oid, stub in new:
        (ORG / f"{oid.removeprefix('org-')}.md").write_text(stub, encoding="utf-8")
    print(f"wrote {len(new)} candidate stubs to entities/org/")
    if new:
        print("next: review each one, write its pitch and body, set status: qualified")


if __name__ == "__main__":
    main()
