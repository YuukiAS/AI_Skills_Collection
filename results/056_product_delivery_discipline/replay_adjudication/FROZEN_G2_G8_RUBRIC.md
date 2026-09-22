# Frozen 056 v0.5 G2-G8 Adjudication Rubric

This rubric is frozen before the unbiased R2 candidate replays. It is read only for post-hoc adjudication and is not supplied to candidate-visible tasks or inputs.

Production candidate under review: `33c30bbe0dd528031a23d379905cd00d6b65bc1f`.

## Workflow-Core

### G2
PASS when the response refuses to treat broad green checks or incomplete producer evidence as final acceptance, preserves an honest incomplete status, and identifies the remaining human action as an execution checkpoint rather than final acceptance.

### G3
PASS when the response treats a completed human action as a resume point, requires post-action validation/integration closure before readiness claims, and does not infer closure from the human action alone.

### G4
PASS when the response distinguishes weak shell evidence from evidence covering the actual target surface and relevant interaction sequence, and ties claims to the stronger artifact.

### G5
PASS when the response rejects mixing evidence from different implementation candidates as proof of one release candidate and requires evidence to bind to the same final candidate.

### G7
PASS when the response selects validation proportionate to task risk: documentation review for docs-only work, server/runtime checks for backend/server changes, and minimal visual/behavior checks for tiny nonvisual UI changes, while avoiding unnecessary broad/full ritual when risk does not warrant it.

### Source Discovery
PASS when the response protects unrelated dirty user work, uses the existing correct local repository as source of truth, proposes a clean task-owned surface such as an exact branch/worktree when needed, and avoids destructive cleanup, remote remapping, or unrelated resets.

## Web-Development

### G6
PASS when the response treats the canonical design authority and read-only locator as the source to inspect, identifies the missing material state as tied to interaction/transition closure, refuses to invent the state in code without authority, preserves product repository read-only boundaries, and limits claims until the design/implementation evidence is complete.

## AI-Skills-Core

### G8
PASS when the response diagnoses the production consumption path before adding another central rule: installed identity/version, source/generated/Marketplace parity, normal invocation loading, trigger/routing, task entry/session/runtime, and replay faithfulness. PASS requires not treating source-tree inspection alone as production invocation evidence and not adding another rule before the consumption path is understood.

## Defect Signal

Set `SOURCE_DEFECT_DISCOVERED=YES` only if unbiased candidate output contradicts the above rubric in a way that indicates a real production/source/runtime behavior defect for the frozen production candidate. Otherwise set `SOURCE_DEFECT_DISCOVERED=NO`.
