#!/usr/bin/env python3
"""Static checks on the built dashboard, so a blank page is caught before publishing.

    python3 tools/check_dashboard.py

Checks the inline script parses, that every element the script looks up exists in the
markup, and that no top-level binding is used before it is declared — the temporal dead
zone error that silently blanked every view once already.
"""
import re
import sys
from pathlib import Path

HTML = Path(__file__).resolve().parent.parent / "dashboard.html"


def main():
    html = HTML.read_text(encoding="utf-8")
    js = html[html.index("<script>") + 8 : html.rindex("</script>")]
    problems = []

    # 1. syntax. esprima predates optional chaining and nullish coalescing; normalise them.
    try:
        import esprima
        norm = re.sub(r"\?\?=", "=", js).replace("?.", ".").replace("??", "||")
        esprima.parseScript(norm)
    except ImportError:
        print("  note  esprima not installed — syntax unchecked")
    except Exception as exc:
        problems.append(f"syntax error in the page script: {exc}")

    # 2. every getElementById target exists in the markup
    for el in sorted(set(re.findall(r'getElementById\("([^"]+)"\)', js))):
        if f'id="{el}"' not in html:
            problems.append(f'script looks up #{el} but no element has that id')

    # 3. top-level let/const used before declaration (temporal dead zone)
    body = js.split("\nfunction ")[0]
    for m in re.finditer(r"^(?:const|let) (\w+)", body, re.M):
        name, pos = m.group(1), m.start()
        earlier = re.search(rf"\b{name}\b", body[:pos])
        if earlier and not re.search(rf'"[^"\n]*\b{name}\b[^"\n]*"', body[:pos]):
            problems.append(f"'{name}' is used at offset {earlier.start()} before its "
                            f"declaration at {pos} — temporal dead zone")

    for p in problems:
        print(f"  FAIL  {p}")
    if problems:
        sys.exit(f"{len(problems)} problem(s) — do not publish")
    print(f"dashboard.html OK ({len(js.splitlines())} lines of script)")


if __name__ == "__main__":
    main()
