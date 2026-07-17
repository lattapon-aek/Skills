#!/usr/bin/env python3
"""Fail when a local Markdown link in the suite points to a missing artifact."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


REPO = Path(__file__).resolve().parents[3]
SUITE = REPO / "suites" / "software-engineering"
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REMOTE_SCHEMES = {"http", "https", "mailto"}


def local_target(raw: str) -> str | None:
    target = raw.strip().strip("<>").split("#", 1)[0]
    if not target:
        return None
    if urlsplit(target).scheme.lower() in REMOTE_SCHEMES:
        return None
    return unquote(target)


def main() -> int:
    failures: list[str] = []
    checked = 0

    for document in sorted(SUITE.rglob("*.md")):
        text = document.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            target = local_target(match.group(1))
            if target is None:
                continue
            checked += 1
            resolved = (document.parent / target).resolve()
            if not resolved.exists():
                line = text.count("\n", 0, match.start()) + 1
                try:
                    label = document.relative_to(REPO)
                except ValueError:
                    label = document
                failures.append(
                    f"{label}:{line}: missing local link target {target}"
                )

    for failure in failures:
        print(f"Markdown link check failed: {failure}", file=sys.stderr)
    if failures:
        return 1

    print(f"Markdown link check passed: {checked} local links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
