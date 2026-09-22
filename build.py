#!/usr/bin/env python3
"""Walk the entity tree, validate it, and inline the graph into dashboard.html.

Git is the database; this is the read model. Run after editing any .md file:

    python3 build.py
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
SOURCES = ["entities", "notes", "tasks", "streams"]
TEMPLATE = ROOT / "dashboard.template.html"
OUTPUT = ROOT / "dashboard.html"
MARKER = "/*__DATA__*/null"
REPO_BLOB = "https://github.com/mauhcs/J-job/blob/main/"

TYPES = {"org", "person", "venue", "artifact", "note", "task", "stream"}
STATUSES = {"idea", "researching", "confirmed", "contacted", "active", "parked", "done"}
REQUIRED = ("id", "type", "name", "status", "updated")

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
            if meta.get("status") not in STATUSES:
                problems.append(f"{rel}: unknown status {meta.get('status')!r}")
            meta["updated"] = str(meta.get("updated", ""))
            if meta.get("due"):
                meta["due"] = str(meta["due"])
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

    payload = {
        "built": date.today().isoformat(),
        "repo": REPO_BLOB,
        "items": items,
    }
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    OUTPUT.write_text(html.replace(MARKER, blob), encoding="utf-8")

    counts = {}
    for item in items:
        counts[item.get("type")] = counts.get(item.get("type"), 0) + 1
    summary = ", ".join(f"{v} {k}" for k, v in sorted(counts.items()))
    print(f"built {OUTPUT.name}: {len(items)} items ({summary}), {len(problems)} warnings")


if __name__ == "__main__":
    main()
