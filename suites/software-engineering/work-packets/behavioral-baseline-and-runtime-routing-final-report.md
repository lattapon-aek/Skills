# Final Report: Suite Review, Runtime Routing, and Behavioral Baseline

Date: 2026-07-16. Session machine: Windows (Thai locale) with skills junction-linked into `~/.claude/skills`. This report doubles as the cross-machine handoff packet; read `Resume Instructions` before continuing work elsewhere.

## Objective

Review the suite, close the runtime loading gap, build an automated behavioral evaluation harness, and capture a first measured baseline of agent behavior against the skills.

## Merged Work (all on `master`, linear history)

| PR | Commit(s) | Content |
| --- | --- | --- |
| #1 | `b2a1ba2` | Packaging/portability: `context-continuity.md` moved into `skills/software-engineering-core/references/` (skills now self-contained); validator rejects out-of-skill SKILL.md links; Node and `SKILL_VALIDATE_PY` prerequisites documented; hardcoded user paths removed; idempotent link scripts; stale "Phase Handoff" wording fixed and scanned |
| #2 | `27aadbf` | Runtime contracts in entrypoints: core gains `## Preflight`, `## Suite Routing` (earliest unmet gate, no gate re-entry without new evidence), `## Reporting`, expected-observation loop step; verification-hazards gains `## Required Input` and a still-a-lead loop guard; context-continuity gains `## Compaction Checkpoint` and `## Adaptive Reporting`; all enforced by `check-skill-architecture.py` |
| #3 | `0cd35af`, `2bdd0e6`, `f213cfc` | Behavioral eval harness: `scripts/run-behavioral-eval.py`, 30 machine-gradable cases in `tests/behavioral/cases.json`, good/bad fixture oracle wired into `validate-suite.sh`, stdin agent mode, first sonnet baseline recorded in `tests/skill-flow/assessment.md` |

## Intended vs Observed State

Intended: runtime-loaded routing contracts, measurable behavior, no doctrine weakened. Observed: full `./scripts/validate-suite.sh` passes on merged `master` (`f213cfc`) — 3/3 skills valid, 3,755/4,200 entrypoint words, behavioral self-test 30 cases + 6 fixtures, node fixtures 14/14, stale scans clean. Conformance: `conforms`; no unresolved deviation.

## Measured Baseline (claude -p, model sonnet, clean cwd, no AGENTS.md)

| Metric | master (pre-#2) | runtime-routing (#2) |
| --- | --- | --- |
| cases passed | 7/30 | 9/30 |
| routing_accuracy | 0.111 | 0.111 |
| shape_compliance | 0.417 | 0.5 |
| false_acceptance_rate | 0.667 | 0.556 |
| conformance_integrity | 0.25 | 0.5 |

Key finding: prompts naming a skill behave well (vh cases 6–7/8); implicit selection almost always fails to route (1/9, unchanged by #2 — entrypoint text loads only after invocation). Routing is the binding constraint; the lever is frontmatter `description` wording, project `AGENTS.md` policy, and user phrasing — not more entrypoint content. Full record with caveats: `tests/skill-flow/assessment.md`.

Raw transcripts/reports are machine-local (not in git) on the session machine under `%LOCALAPPDATA%\Temp\claude\skills-eval\` (`baseline/`, `pr2/`, `*-report.json`, plus discarded `baseline-contaminated/`).

## Next Planned Work (not started)

1. Tune the three frontmatter `description` fields for real task language (include Thai trigger phrases such as แก้บั๊ก / ปิดงาน / review diff); keep them within skill-description length conventions.
2. Re-run the harness and compare against the recorded baseline:
   `PYTHONUTF8=1 python suites/software-engineering/scripts/run-behavioral-eval.py --agent-cmd "cd /d C:\\claude-eval\\cwd && claude -p --model sonnet" --out <dir> --report <file>` (run from an empty cwd outside the user profile so no CLAUDE.md leaks in).
3. Only after routing moves: revisit whether any skill split (candidate: causal-analysis) is still worth it.
4. Open older gaps, unchanged: Analyze Case 4 fixture underspecified; `four-principles.md`/`orchestration-policy.md` remain doc-level (runtime-critical subset now duplicated in core — watch for drift, validator guards the core side only).

## Resume Instructions (other machine — read before merging)

- Remote branch `codex/refine-software-engineering-suite` currently has **no commits beyond `f825d43`**; local work there predates all three PRs. Rebase onto latest `master` (≥ `f213cfc`) before continuing.
- Conflict hotspots this session touched: core and verification-hazards `SKILL.md`, `check-skill-architecture.py`, `validate-suite.sh`, suite `README.md`, `AGENTS.md`, `tests/skill-flow/assessment.md`.
- `context-continuity.md` **moved** to `skills/software-engineering-core/references/`. Edits made against the old `suites/software-engineering/references/context-continuity.md` path will rebase as modify/delete conflicts — re-apply them at the new path.
- The validator now enforces new required strings (e.g. `## Preflight`, `## Required Input`, `## Compaction Checkpoint`, "without new evidence", "Rigor is constant", self-contained SKILL.md links, behavioral self-test). Run `PYTHONUTF8=1 ./scripts/validate-suite.sh` after rebase; do not delete required contract text to resolve conflicts.
- Machine notes: Thai-locale Windows needs `PYTHONUTF8=1` for all suite Python; node fixtures need Node 23.6+ (or 22.6+ with `--experimental-strip-types`); on the session machine `~/.claude/skills` junctions point at this repo's **working tree**, so whatever branch is checked out is what Claude Code loads live.

## Deviations

None unresolved. Two eval incidents were detected, corrected, and recorded in `assessment.md`: a first baseline attempt leaked home-directory CLAUDE.md context (discarded, re-run from a clean cwd) and four transcripts captured a session-limit message (re-run after reset).
