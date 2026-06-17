#!/usr/bin/env python3
"""Internal link checker for the main repo.

Scans every tracked markdown file for backtick-quoted, repo-relative file references
(e.g. `shared/checkpoint_protocol.md`, `scripts/check_passport.py`) and verifies each
resolves — relative to the repo root OR to the referencing file's own directory (both
conventions are used: `shared/...` is repo-root, `templates/...` is skill-local). Catches
dangling cross-file references before they ship. The Codex package already had this
guard in its tests; this brings the main repo to parity.

Usage: python3 scripts/check_links.py [repo_root]
Exit: 0 = all resolve · 1 = broken references · 2 = error
"""

import re
import sys
from pathlib import Path

# backtick path token: at least one slash (bare filenames are prose shorthand, not links),
# ends in a known extension. The suite's convention: refs resolve relative to the enclosing
# skill root, so we try the repo root and every ancestor directory of the file.
TOKEN = re.compile(r"`([A-Za-z0-9_][\w.-]*(?:/[\w.-]+)+\.(?:md|py|json|ya?ml))`")
SKIP_DIRS = {".git", "dist", "node_modules"}
PLACEHOLDER = re.compile(r"\{\{|<[a-z]|\.\.\.|/X/|<skill>|<id>|<hash>|<passport>|<file>|<mode>|<name>")


SOURCE_ROOTS = {"shared", "scripts", "docs", "examples", "commands", "tests",
                "references", "templates", "agents"}


def resolves(root, md, ref):
    bases = [root]
    p = md.parent
    while True:
        bases.append(p)
        if p == root:
            break
        p = p.parent
    return any((b / ref).exists() for b in bases)


def main(argv=None):
    root = Path(argv[0]) if argv else Path(__file__).resolve().parent.parent
    # a checkable reference points at a SOURCE location; runtime output paths
    # (audit/, comms/, bilingual/, assessments/, …) are produced, not in the repo.
    source_roots = SOURCE_ROOTS | {d.name for d in root.iterdir()
                                   if d.is_dir() and (d / "SKILL.md").exists()}
    broken, checked = [], 0
    for md in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in md.relative_to(root).parts):
            continue
        text = md.read_text(encoding="utf-8")
        for m in TOKEN.finditer(text):
            ref = m.group(1)
            if ref.split("/")[0] not in source_roots:
                continue  # runtime output path or external — not a source link
            ctx = text[max(0, m.start() - 12):m.end() + 2]
            if PLACEHOLDER.search(ctx) or ref.endswith("X.md"):
                continue
            checked += 1
            if resolves(root, md, ref):
                continue
            broken.append((md.relative_to(root).as_posix(), ref))
    for f, ref in broken:
        print(f"BROKEN  {f}  ->  `{ref}`")
    print(f"{'BROKEN LINKS' if broken else 'OK'} — checked {checked} references, {len(broken)} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
