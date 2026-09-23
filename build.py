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
TEMPLATE = ROOT / "dashboard.template.html"

# Two projects, two separate databases. Nothing crosses between them: separate trees,
# separate intake, separate dashboards, separate published artifacts.
PROJECTS = {
    "model-validation": {
        "title": "Model Verification",
        "lede": "Independent external verification of quantitative models "
                "\u2014 Japan, Hong Kong, East Asia.",
    },
    "data-signal": {
        "title": "Data Signal Research",
        "lede": "Scoping the trading value of a dataset for the people who own it, "
                "so they can sell it.",
    },
    "game-ml": {
        "title": "Game ML Services",
        "lede": "Applied machine learning for Japanese game companies \u2014 the "
                "quantitative problems their AI vendors do not cover.",
    },
}
MARKER = "/*__DATA__*/null"
TITLE_MARKER = "__TITLE__"
REPO_BLOB = "https://github.com/mauhcs/J-job/blob/main/"

TYPES = {"org", "person", "venue", "artifact", "note", "task", "stream"}
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


def collect(root):
    items, problems = [], []
    for src in SOURCES:
        for path in sorted((root / src).rglob("*.md")):
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
            pipeline = meta.get("role") == "buyer" and meta.get("scope") != "segment"
            allowed = PIPELINE if pipeline else STATUSES
            if meta.get("status") not in allowed:
                kind = "pipeline" if pipeline else "general"
                problems.append(
                    f"{rel}: status {meta.get('status')!r} is not a {kind} state "
                    f"({', '.join(sorted(allowed))})")
            if meta.get("status") == "retired" and not meta.get("retired_reason"):
                problems.append(f"{rel}: retired without a retired_reason — use tools/retire.py")
            if meta.get("type") == "task" and meta.get("priority") == 1 and not meta.get("decides"):
                problems.append(f"{rel}: priority-1 task without 'decides' — say what it settles")
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


def pool(root):
    """Harvested rows that are not cards.

    The pool is the universe a source gives us; a card is a company someone has formed a
    judgement about. Keeping the pool in TSV rather than minting a stub per row is what
    stops entities/org filling with entries nobody has read.
    """
    intake = root / "intake"
    if not (intake / "sources.yaml").exists():
        return [], []
    registry = yaml.safe_load((intake / "sources.yaml").read_text(encoding="utf-8"))["sources"]
    rows, sources = [], []
    for source in registry:
        # Some sources are evidence for a research question, not lists of prospects.
        # They keep a source card but their rows never enter the prospect pool.
        tsv = intake / f"{source['id']}.tsv"
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
                        | {"source": source["id"]})
    return sources, rows


def build(slug, meta):
    """Build one project's dashboard from its own tree. Projects never see each other."""
    root = ROOT / slug
    items, problems = collect(root)
    problems += link_graph(items)

    seen = {}
    for item in items:
        if item.get("id") in seen:
            problems.append(f"{item['path']}: duplicate id, also in {seen[item['id']]}")
        seen[item.get("id")] = item["path"]

    for p in problems:
        print(f"  warn  {p}", file=sys.stderr)

    sources, pool_rows = pool(root)
    payload = {
        "built": date.today().isoformat(),
        "repo": REPO_BLOB,
        "project": {"slug": slug, **meta},
        "items": items,
        "sources": sources,
        "pool": pool_rows,
    }
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8")
    if MARKER not in html or TITLE_MARKER not in html:
        sys.exit(f"template needs both {MARKER} and {TITLE_MARKER} markers")
    # The artifact gallery reads the <title> tag from the file, so it has to be baked
    # in per project rather than set by script at runtime.
    html = html.replace(TITLE_MARKER, meta["title"], 1)
    out = root / "dashboard.html"
    out.write_text(html.replace(MARKER, blob), encoding="utf-8")

    counts = {}
    for item in items:
        counts[item.get("type")] = counts.get(item.get("type"), 0) + 1
    summary = ", ".join(f"{v} {k}" for k, v in sorted(counts.items()))
    live = [i for i in items
            if i.get("type") == "task" and i.get("priority") == 1
            and i.get("status") not in ("done", "parked")]
    print(f"{slug}: {len(items)} items ({summary}), {len(live)} live tasks, "
          f"{len(problems)} warnings -> {out.relative_to(ROOT)}")
    if len(live) > 4:
        print(f"  warn  {len(live)} priority-1 tasks — that is a reading list, not a plan",
              file=sys.stderr)
    return len(problems)


def main():
    if not TEMPLATE.exists():
        sys.exit(f"missing template: {TEMPLATE}")
    total = 0
    for slug, meta in PROJECTS.items():
        total += build(slug, meta)
    if total:
        print(f"\n{total} warnings total", file=sys.stderr)


if __name__ == "__main__":
    main()
