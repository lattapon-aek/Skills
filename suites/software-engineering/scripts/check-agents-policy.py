#!/usr/bin/env python3
"""Validate and optionally emit the canonical AGENTS.md policy block."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
SUITE = REPO / "suites" / "software-engineering"
POLICY = SUITE / "references" / "agents-enforcement-policy.md"
README = SUITE / "README.md"
ROOT_AGENTS = REPO / "AGENTS.md"
START = "<!-- agents-policy:start -->"
END = "<!-- agents-policy:end -->"
WORD_LIMIT = 260

REQUIRED_POLICY_TEXT = (
    "software-engineering-core",
    "do X because Y",
    "Clarify",
    "Plan",
    "Implement",
    "mechanism claims, not mechanism evidence",
    "complete decision-changing claim ledger",
    "Mechanism Verdict: established",
    "do not mutate the target",
    "verification-hazards",
    "change-review",
)

REQUIRED_ROOT_TEXT = (
    "do X because Y",
    "Mechanism Verdict: established",
    "do not mutate the target",
)


def fail(message: str) -> None:
    print(f"AGENTS policy check failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def extract_policy(text: str) -> str:
    if text.count(START) != 1 or text.count(END) != 1:
        fail("canonical policy must contain exactly one start and end marker")
    before, remainder = text.split(START, 1)
    block, after = remainder.split(END, 1)
    if not before.strip() or not after.strip():
        fail("canonical policy needs usage guidance outside the copy block")
    return block.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--emit",
        action="store_true",
        help="print the canonical block for a temporary AGENTS.md",
    )
    args = parser.parse_args()

    policy_text = POLICY.read_text(encoding="utf-8")
    block = extract_policy(policy_text)
    word_count = len(block.split())
    if word_count > WORD_LIMIT:
        fail(f"copy block has {word_count} words; limit is {WORD_LIMIT}")

    for required in REQUIRED_POLICY_TEXT:
        if required not in block:
            fail(f"copy block is missing required contract text: {required}")

    readme_text = README.read_text(encoding="utf-8")
    if "references/agents-enforcement-policy.md" not in readme_text:
        fail("suite README does not link the canonical policy")

    root_text = ROOT_AGENTS.read_text(encoding="utf-8")
    for required in REQUIRED_ROOT_TEXT:
        if required not in root_text:
            fail(f"root AGENTS.md is missing dogfood contract text: {required}")

    if args.emit:
        print(block)
    else:
        print(f"AGENTS policy check passed: {word_count} words")


if __name__ == "__main__":
    main()
