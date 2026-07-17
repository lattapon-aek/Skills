#!/usr/bin/env python3
"""Validate context budgets and progressive-disclosure contracts for the suite."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
SUITE = REPO / "suites" / "software-engineering"

LIMITS = {
    "software-engineering-core": {"lines": 240, "words": 1550},
    "verification-hazards": {"lines": 150, "words": 1100},
    "change-review": {"lines": 160, "words": 1120},
}

REQUIRED_TEXT = {
    "software-engineering-core": [
        "## Preflight",
        "Intent-to-Outcome Conformance",
        "Allowed Variations",
        "unresolved deviation",
        "verification-hazards",
        "change-review",
        "references/intake-template.md",
        "references/planning-template.md",
        "references/mechanism-design-protocol.md",
        "references/causal-debugging-protocol.md",
        "references/implementation-checklist.md",
        "earliest unmet gate",
        "without new evidence",
        "expected observation",
        "Rigor is constant",
    ],
    "verification-hazards": [
        "Bypassed-Layer Green",
        "Subset Green",
        "Wrong-Theory Green",
        "Wrong-Tree Green",
        "Not-Your-Red",
        "Weak-Oracle Green",
        "Conformance",
        "still a lead",
        "## Required Input",
        "without new evidence",
        "Wrong-Mechanism Green",
        "Mechanism Validity",
    ],
    "change-review": [
        "Intent Conformance",
        "unresolved deviation",
        "Acceptance Coverage",
        "Proof Sufficiency",
        "Mechanism Validity",
        "return to <owner/mode>",
    ],
}

DELETED_RUNTIME_REFERENCES = ("analysis-playbook.md", "output-patterns.md")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")


def fail(message: str) -> None:
    print(f"skill architecture check failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def local_links(path: Path, text: str) -> list[Path]:
    links: list[Path] = []
    for raw in LINK_PATTERN.findall(text):
        if "://" in raw or raw.startswith("#"):
            continue
        links.append((path.parent / raw).resolve())
    return links


def main() -> None:
    total_words = 0
    direct_references: set[Path] = set()

    for skill, limits in LIMITS.items():
        entry = SUITE / "skills" / skill / "SKILL.md"
        text = entry.read_text(encoding="utf-8")
        line_count = len(text.splitlines())
        word_count = len(text.split())
        total_words += word_count

        if line_count > limits["lines"]:
            fail(f"{entry.relative_to(REPO)} has {line_count} lines; limit is {limits['lines']}")
        if word_count > limits["words"]:
            fail(f"{entry.relative_to(REPO)} has {word_count} words; limit is {limits['words']}")

        for required in REQUIRED_TEXT[skill]:
            if required not in text:
                fail(f"{entry.relative_to(REPO)} is missing required contract text: {required}")

        skill_dir = entry.parent.resolve()
        for link in local_links(entry, text):
            if not link.is_file():
                fail(f"broken direct reference from {entry.relative_to(REPO)} to {link}")
            if not link.is_relative_to(skill_dir):
                fail(
                    f"{entry.relative_to(REPO)} links outside its skill directory: {link}; "
                    "installed skills must be self-contained"
                )
            direct_references.add(link)

    if total_words > 3750:
        fail(f"activated entrypoint budget is {total_words} words; suite limit is 3750")

    for reference in direct_references:
        nested = local_links(reference, reference.read_text(encoding="utf-8"))
        if nested:
            rendered = ", ".join(str(path) for path in nested)
            fail(f"nested reference chain from {reference.relative_to(REPO)}: {rendered}")

    for root in (SUITE / "skills", SUITE / "references"):
        for path in root.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for stale in DELETED_RUNTIME_REFERENCES:
                if stale in text:
                    fail(f"stale runtime reference {stale} in {path.relative_to(REPO)}")
            if re.search(r"\b(always|must) browse (the internet )?(for|before) (every|all)\b", text, re.IGNORECASE):
                fail(f"universal browsing rule found in {path.relative_to(REPO)}")

    continuity = (
        SUITE
        / "skills"
        / "software-engineering-core"
        / "references"
        / "context-continuity.md"
    ).read_text(encoding="utf-8")
    for required in (
        "Continuity choices affect only artifact durability",
        "never reduce evidence gathering",
        "Never edit the original plan after implementation",
        "## Compaction Checkpoint",
        "## Adaptive Reporting",
        "Never omit a deviation or proof gap",
    ):
        if required not in continuity:
            fail(f"context continuity is missing full-rigor contract: {required}")

    print(f"skill architecture check passed: {total_words} entrypoint words")


if __name__ == "__main__":
    main()
