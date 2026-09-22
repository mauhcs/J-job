#!/usr/bin/env python3
"""Walk the entity tree, validate it, and inline the graph into dashboard.html.

Git is the database; this is the read model. Run after editing any .md file:

    python3 build.py
"""
import csv
import datetime
import json
import re
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
SOURCES = ["entities", "notes", "tasks", "streams"]
INTAKE = ROOT / "intake"
TEMPLATE = ROOT / "dashboard.template.html"
OUTPUT = ROOT / "dashboard.html"
MARKER = "/*__DATA__*/null"
REPO_BLOB = "https://github.com/mauhcs/J-job/blob/main/"

TYPES = {"org", "person", "venue", "artifact", "note", "task", "stream"}
# Two independent ventures share this repo. "shared" is profile-level material
# (affiliations, capacity, sales constraints) that bears on both.
SPACES = {"mrm", "data", "shared"}
# General lifecycle, used by everything except buyer companies.
STATUSES = {"idea", "researching", "confirmed", "contacted", "active", "parked", "done"}
# Buyer companies run a sales pipeline instead. See INTAKE.md.
PIPELINE = {"researching", "qualified", "contacted", "engaged", "client", "retired"}
REQUIRED = ("id", "type", "name", "status", "updated")
SIZES = {"startup", "sme", "mid", "large", "mega"}

FM = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)


def parse(path):
    """Split a file into (front-matter dict, body). Returns None if malformed."""
    m = FM.match(path.read_text(encoding="utf-8"))
    if not m:
        return None
    meta = yaml.safe_load(m.group(1)) or {}
    return meta, m.group(2).strip()


def collect():
    items, problems = [], []
    for src in SOURCES:
        for path in sorted((ROOT / src).rglob("*.md")):
            rel = path.relative_to(ROOT).as_posix()
            parsed = parse(path)
            if parsed is None:
                problems.append(f"{rel}: no YAML front-matter")
                continue
            meta, body = parsed
            for field in REQUIRED:
                if not meta.get(field):
                    problems.append(f"{rel}: missing required field '{field}'")
            if meta.get("type") not in TYPES:
                problems.append(f"{rel}: unknown type {meta.get('type')!r}")
            if meta.get("space") not in SPACES:
                problems.append(f"{rel}: space {meta.get('space')!r} not in {sorted(SPACES)}")
            pipeline = meta.get("role") == "buyer" and meta.get("scope") != "segment"
            allowed = PIPELINE if pipeline else STATUSES
            if meta.get("status") not in allowed:
                kind = "pipeline" if pipeline else "general"
                problems.append(
                    f"{rel}: status {meta.get('status')!r} is not a {kind} state "
                    f"({', '.join(sorted(allowed))})")
            if meta.get("status") == "retired" and not meta.get("retired_reason"):
                problems.append(f"{rel}: retired without a retired_reason — use tools/retire.py")
            if pipeline and meta.get("status") not in ("researching", "retired"):
                for field in ("pitch", "priority"):
                    if not meta.get(field):
                        problems.append(f"{rel}: qualified target missing '{field}'")
            if meta.get("size") and meta["size"] not in SIZES:
                problems.append(f"{rel}: unknown size {meta.get('size')!r}")
            if pipeline and meta.get("status") != "retired" and not meta.get("site"):
                problems.append(f"{rel}: company without a 'site' (operating company URL)")
            if meta.get("role") == "buyer" and not meta.get("size"):
                problems.append(f"{rel}: buyer without a size tier — absent from Targets view")
            # YAML parses bare ISO dates into date objects; JSON wants strings.
            for key, value in meta.items():
                if isinstance(value, (datetime.date, datetime.datetime)):
                    meta[key] = value.isoformat()
            meta["updated"] = str(meta.get("updated", ""))
            meta["body"] = body
            meta["path"] = rel
            items.append(meta)
    return items, problems


def link_graph(items):
    """Make `rel` edges undirected and drop the ones that point nowhere."""
    by_id = {i["id"]: i for i in items}
    edges = {i["id"]: set() for i in items}
    dangling = []
    for item in items:
        for target in item.get("rel") or []:
            if target not in by_id:
                dangling.append(f"{item['path']}: rel -> '{target}' does not exist")
                continue
            edges[item["id"]].add(target)
            edges[target].add(item["id"])
    for item in items:
        item["rel"] = sorted(edges[item["id"]])
    return dangling


def pool():
    """Harvested rows that are not cards.

    The pool is the universe a source gives us; a card is a company someone has formed a
    judgement about. Keeping the pool in TSV rather than minting a stub per row is what
    stops entities/org filling with entries nobody has read.
    """
    registry = yaml.safe_load((INTAKE / "sources.yaml").read_text(encoding="utf-8"))["sources"]
    rows, sources = [], []
    for source in registry:
        # Some sources are evidence for a research question, not lists of prospects.
        # They keep a source card but their rows never enter the prospect pool.
        tsv = INTAKE / f"{source['id']}.tsv"
        sources.append({k: str(v) for k, v in source.items() if k != "note"}
                       | {"note": source.get("note", ""), "harvested_rows": 0})
        if not tsv.exists():
            continue
        parsed = list(csv.DictReader(tsv.read_text(encoding="utf-8").splitlines(), delimiter="\t"))
        sources[-1]["harvested_rows"] = len(parsed)
        if source.get("purpose") == "evidence":
            continue
        for r in parsed:
            rows.append({k: (v or "").strip() for k, v in r.items()}
                        | {"source": source["id"], "space": source.get("space", "mrm")})
    return sources, rows


def main():
    items, problems = collect()
    problems += link_graph(items)

    seen = {}
    for item in items:
        if item.get("id") in seen:
            problems.append(f"{item['path']}: duplicate id, also in {seen[item['id']]}")
        seen[item.get("id")] = item["path"]

    for p in problems:
        print(f"  warn  {p}", file=sys.stderr)

    if not TEMPLATE.exists():
        sys.exit(f"missing template: {TEMPLATE}")
    html = TEMPLATE.read_text(encoding="utf-8")
    if MARKER not in html:
        sys.exit(f"template has no {MARKER} marker to inject into")

    sources, pool_rows = pool()
    payload = {
        "built": date.today().isoformat(),
        "repo": REPO_BLOB,
        "items": items,
        "sources": sources,
        "pool": pool_rows,
    }
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    OUTPUT.write_text(html.replace(MARKER, blob), encoding="utf-8")

    counts = {}
    for item in items:
        counts[item.get("type")] = counts.get(item.get("type"), 0) + 1
    summary = ", ".join(f"{v} {k}" for k, v in sorted(counts.items()))
    spaces = {}
    for item in items:
        spaces[item.get("space")] = spaces.get(item.get("space"), 0) + 1
    print(f"built {OUTPUT.name}: {len(items)} items ({summary}), {len(problems)} warnings")
    print("spaces: " + " | ".join(f"{k} {v}" for k, v in sorted(spaces.items())))

    pipe = {}
    for item in items:
        if item.get("role") == "buyer" and item.get("scope") != "segment":
            pipe[item["status"]] = pipe.get(item["status"], 0) + 1
    if pipe:
        order = ["qualified", "contacted", "engaged", "client", "retired"]
        print("pipeline: " + " | ".join(f"{s} {pipe[s]}" for s in order if s in pipe))
    states = {}
    for r in pool_rows:
        states[r.get("state") or "pool"] = states.get(r.get("state") or "pool", 0) + 1
    if states:
        print("pool: " + " | ".join(f"{k} {v}" for k, v in sorted(states.items())))


if __name__ == "__main__":
    main()
