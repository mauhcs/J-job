#!/usr/bin/env python3
"""Retire a card without deleting it.

    python3 tools/retire.py org-example "Acquired by a megabank; now inside group MRM"

Sets status to retired and stamps the reason and date. The card stays in the repo and
stays searchable; it drops out of the Targets view. Reverse it by editing the file.
"""
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def yaml_scalar(text):
    """Quote a reason so colons, hashes and quotes survive YAML parsing."""
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"' 
SEARCH = [f"{proj}/entities/{kind}"
          for proj in ("model-validation", "data-signal")
          for kind in ("org", "person", "venue", "artifact")]


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    target, reason = sys.argv[1], sys.argv[2].strip()
    if not reason:
        sys.exit("a reason is required — the reason is the whole point of retiring")

    for d in SEARCH:
        for path in (ROOT / d).glob("*.md"):
            text = path.read_text(encoding="utf-8")
            if not re.search(rf"^id: {re.escape(target)}\s*$", text, re.M):
                continue
            if re.search(r"^status: retired\s*$", text, re.M):
                sys.exit(f"{target} is already retired")
            today = date.today().isoformat()
            text = re.sub(r"^status: .*$", "status: retired", text, count=1, flags=re.M)
            text = re.sub(r"^updated: .*$", f"updated: {today}", text, count=1, flags=re.M)
            text = re.sub(
                r"^status: retired$",
                f"status: retired\nretired_on: {today}\n"
                f"retired_reason: {yaml_scalar(reason)}",
                text, count=1, flags=re.M)
            text = text.rstrip("\n") + f"\n\n## Retired {today}\n\n{reason}\n"
            path.write_text(text, encoding="utf-8")
            print(f"retired {target} ({path.relative_to(ROOT)})\n  {reason}")
            print("run: python3 build.py")
            return
    sys.exit(f"no card with id {target!r}")


if __name__ == "__main__":
    main()
