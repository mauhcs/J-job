#!/usr/bin/env python3
"""The company pool: browse a harvested source, and promote rows into cards.

    python3 tools/intake.py                         # pool status across all sources
    python3 tools/intake.py shotan-kyokai           # list that source's pool rows
    python3 tools/intake.py shotan-kyokai --promote kenko-nenrei.co.jp
    python3 tools/intake.py shotan-kyokai --exclude ribon.com "pet cover only, no model"

A harvested row is NOT a card. `intake/<source-id>.tsv` is the pool — the full universe
from a source, committed to git, browsable in the dashboard. A file under entities/org/
means a human looked at a company and formed a judgement about it. Minting a card per
row just duplicates the TSV with no added information, and fills the repo with entries
nobody has read.

TSV columns: name, url (both required), then name_ja, country, industry, size, captive,
note, and the three the pool is managed with:

    state   pool | carded | excluded
    reason  why it was excluded (required when state is excluded)
    card    the org id, once promoted

`url` must be the OPERATING COMPANY, not a product page — cashari is the product,
ガレージバンク株式会社 is the company, and the company signs the contract.
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
FIELDS = ["name", "name_ja", "url", "country", "industry", "size", "captive", "note",
          "state", "reason", "card"]
TLDS = (".co.jp", ".or.jp", ".ne.jp", ".com.hk", ".com.tw", ".co.uk",
        ".com", ".jp", ".net", ".org", ".io", ".hk", ".sg", ".insurance")
FM = re.compile(r"\A---\n(.*?)\n---", re.S)


def host(url):
    if not url:
        return ""
    return re.sub(r"^https?://", "", url.strip().lower()).split("/")[0].removeprefix("www.")


def slug(name, url=""):
    """Id fragment from the website host, which is unique by construction.

    Name-derived ids break on mixed-script Japanese names: "SBIいきいき少額短期保険"
    strips to "sbi", as do the four other SBI micro-insurers, collapsing five companies
    into one id. Fall back to the name only when there is no URL at all.
    """
    h = host(url)
    if h:
        for tld in TLDS:
            if h.endswith(tld):
                h = h[: -len(tld)]
                break
        if out := re.sub(r"[^a-z0-9]+", "-", h).strip("-"):
            return out
    s = unicodedata.normalize("NFKC", name).lower()
    s = re.sub(r"[（(].*?[)）]", "", s)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def registry():
    return {s["id"]: s for s in yaml.safe_load(SOURCES.read_text(encoding="utf-8"))["sources"]}


def load(source_id):
    path = INTAKE / f"{source_id}.tsv"
    if not path.exists():
        sys.exit(f"missing {path.relative_to(ROOT)} — harvest the source into it first")
    rows = list(csv.DictReader(path.read_text(encoding="utf-8").splitlines(), delimiter="\t"))
    return path, [{k: (r.get(k) or "").strip() for k in FIELDS} for r in rows]


def save(path, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, FIELDS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def find(rows, needle):
    needle = needle.lower()
    hits = [r for r in rows if needle in host(r["url"]) or needle in r["name"].lower()]
    if not hits:
        sys.exit(f"no pool row matching {needle!r}")
    if len(hits) > 1:
        sys.exit("ambiguous:\n  " + "\n  ".join(f"{r['name']} ({host(r['url'])})" for r in hits))
    return hits[0]


CARD = """---
id: {oid}
type: org
name: {name}
{name_ja}role: buyer
scope: company
country: {country}
industry: [{industry}]
size: {size}
status: researching
priority: 3
confidence: low
source: {source}
first_seen: {today}
site: {url}
pitch: TODO - one line on why this tier buys
tags: [target, {source}]
rel: []
links:
  - label: Corporate site
    url: {url}
updated: {today}
---

Promoted from the **{source_name}** pool on {today}. Write the judgement that justified
promoting it, then set `status: qualified`, a real `pitch`, `size` and `priority`.

{note}Establish:

- Is `site` the operating company, or a product page? Find the entity that signs contracts.
- What model does the business depend on, and what does it decide?
- Licensed or supervised, and under which regime?
- Who would ask them for an independent opinion — a regulator, a funding counterparty, a
  bank or insurer partner, or an investor?
- Roughly what size, and can they pay?
"""


def promote(source_id, needle):
    source = registry()[source_id]
    path, rows = load(source_id)
    row = find(rows, needle)
    if row["state"] == "carded":
        sys.exit(f"{row['name']} is already carded as {row['card']}")
    oid = "org-" + slug(row["name"], row["url"])
    target = ORG / f"{oid.removeprefix('org-')}.md"
    if target.exists():
        sys.exit(f"{target.relative_to(ROOT)} already exists — edit it instead")
    today = date.today().isoformat()
    target.write_text(CARD.format(
        oid=oid, name=row["name"],
        name_ja=f"name_ja: {row['name_ja']}\n" if row["name_ja"] else "",
        country=row["country"] or source.get("jurisdiction", "JP"),
        industry=row["industry"] or "banking", size=row["size"] or "sme",
        source=source_id, source_name=source["name"], url=row["url"], today=today,
        note=f"Pool note: {row['note']}\n\n" if row["note"] else "",
    ), encoding="utf-8")
    row["state"], row["card"] = "carded", oid
    save(path, rows)
    print(f"promoted {row['name']} -> {target.relative_to(ROOT)}\nnext: write the card, then python3 build.py")


def exclude(source_id, needle, reason):
    if not reason:
        sys.exit("a reason is required — an exclusion without a reason is just a deletion")
    path, rows = load(source_id)
    row = find(rows, needle)
    if row["state"] == "carded":
        sys.exit(f"{row['name']} is carded as {row['card']} — retire the card instead:\n"
                 f"  python3 tools/retire.py {row['card']} \"{reason}\"")
    row["state"], row["reason"] = "excluded", reason
    save(path, rows)
    print(f"excluded {row['name']}\n  {reason}")


def report(source_id=None):
    reg = registry()
    ids = [source_id] if source_id else [s for s in reg if (INTAKE / f"{s}.tsv").exists()]
    for sid in ids:
        _, rows = load(sid)
        counts = {}
        for r in rows:
            counts[r["state"] or "pool"] = counts.get(r["state"] or "pool", 0) + 1
        print(f"\n{sid}  ({reg[sid]['kind']}, {len(rows)} rows)  "
              + "  ".join(f"{k} {v}" for k, v in sorted(counts.items())))
        if source_id:
            for r in rows:
                mark = {"carded": "*", "excluded": "-"}.get(r["state"], " ")
                extra = r["card"] if r["state"] == "carded" else r["reason"][:60]
                print(f"  {mark} {r['name'][:40]:<42}{host(r['url']):<28}{extra}")
    if not source_id:
        print("\npython3 tools/intake.py <source-id>  to list one source's pool")


def main():
    args = [a for a in sys.argv[1:]]
    if not args:
        return report()
    source_id = args[0]
    if source_id not in registry():
        sys.exit(f"unknown source {source_id!r}; register it in intake/sources.yaml first")
    if "--promote" in args:
        return promote(source_id, args[args.index("--promote") + 1])
    if "--exclude" in args:
        i = args.index("--exclude")
        return exclude(source_id, args[i + 1], " ".join(args[i + 2:]))
    report(source_id)


if __name__ == "__main__":
    main()
