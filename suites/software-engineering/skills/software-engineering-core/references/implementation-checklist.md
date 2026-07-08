# Execution Checklist

## Clarify

- State the objective and expected result
- Identify the working document or create a work packet before substantial action
- Identify the decisions that still need clarification
- Define how success will be proven
- If the task is still underspecified, push it back to intake instead of guessing

## Inspect

- Read the relevant files and code paths
- Check config, tests, logs, or command output as needed
- Separate observed facts from assumptions
- Pull external docs only when they materially affect the next safe implementation step
- Trace until you know the concrete change location

## Locate Fix

- Name the exact file(s) to change
- Name the exact function, block, query, config, or template to change
- State why this is the narrowest safe patch point
- State what should remain untouched
- State what nearby behavior could be affected
- State the likely blast radius if the patch is wrong
- Confirm whether the patch can be reverted cleanly without extra migration work
- Note if the change alters caller contracts or requires a staged rollout
- If reversibility is weak, look for a narrower patch before proceeding
- Do this even for very small fixes

## During Editing

- Keep steps small
- Stay within the narrowed scope
- Expand the diff only when evidence shows it is necessary
- Stop if the work turns into redesign, research drift, or stale-brief execution
- Prefer the smallest working patch over broad cleanup

## Impact

- Note affected modules, APIs, data paths, and user-visible behavior
- Call out compatibility or migration concerns
- Explain when a larger refactor is justified
- Identify callers, downstream consumers, contracts, and runtime side effects around the patch

## Verify And Handoff

- Run the lightest meaningful proof
- Confirm the target behavior and touched adjacent paths
- State open risks, assumptions, and out-of-scope items
- Confirm that the likely blast-radius areas still behave correctly
- Do not call the work done until the failure is gone or the target behavior is observed to work
- If proof has not been run yet, say explicitly that no observed result exists yet
