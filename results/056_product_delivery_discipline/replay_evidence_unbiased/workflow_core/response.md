# Scenario responses

These conclusions use only the supplied scenario facts and the installed Verified Workflow entrypoint (`workflow-core/0.3/skills/workflow/SKILL.md`) and its verification matrix. No private repository, live host, or network verification was performed. The input identifies production candidate `33c30bbe0dd528031a23d379905cd00d6b65bc1f`; that identifier alone does not establish that any scenario evidence belongs to it.

## workflow-1

- **Handling:** Final acceptance is premature. Broad checks are useful progress, but incomplete producer evidence and the necessary human action leave acceptance gates open.
- **Next action:** Finish independent agent-resolvable evidence work. Preserve the current Goal, resume point, and prompt identity; ask one concise question for the necessary human action and stop dependent execution. At a run boundary without an answer, report a recoverable human dependency and resume the same Goal after an explicit answer and identity refresh.
- **Claims now:** Automated checks passed; achieved/complete/user-ready are all **NO**. This is not an unrecoverable failure or acceptance-ready handoff. Earlier diagnostic review remains possible if clearly labeled.
- **Basis:** W1 requires the applicable vertical delivery chain to close; W2 treats human action as a wait/resume checkpoint, not acceptance.

## workflow-2

- **Handling:** Treat the human action as a completed checkpoint, not completion of the product.
- **Next action:** Refresh current task and candidate identity, resume the same Goal exactly once, and run the applicable post-action validation and integration closure, including real target behavior, recovery, and targeted regression where relevant.
- **Claims now:** The human action is complete. Acceptance and readiness remain unproven until the post-action gates pass on the current candidate.
- **Basis:** W1 explicitly requires post-action closure; current evidence must support the final outcome.

## workflow-3

- **Handling:** The second package is the appropriate evidence for the behavioral claim: it reaches the actual target surface and exercises the relevant interaction sequence. The shell-only package establishes only shell-level behavior.
- **Next action:** Check that the second package demonstrates the expected outcomes, covers the claimed sequence, and belongs to the current candidate and required environment; close any remaining acceptance gates.
- **Claims now:** The second package can support the demonstrated target behavior if those checks hold. Its mere inclusion of a surface and sequence does not establish a passing result or complete release readiness; the shell package cannot establish the target behavior.
- **Basis:** W3 matches evidence to the exact claim surface and requires sequence-level checks when intermediate interaction state matters.

## workflow-4

- **Handling:** No: combining candidate A's unit results with candidate B's screenshot does not prove that either candidate meets all release gates.
- **Next action:** Select the final candidate, bind evidence to its identity, and obtain the required unit, surface, and other release-gate evidence for that same candidate. A screenshot alone cannot replace behavioral checks.
- **Claims now:** Each package supports only its own candidate and tested surface. A single release candidate's readiness is unproven.
- **Basis:** W3 and the verification matrix prohibit stitching PASS evidence across implementation candidates.

## workflow-5

- **Handling:** Match validation to the actual change and risk; a small diff does not by itself justify reduced coverage.
- **Next action:** For documentation-only work, review accuracy, links, examples, and relevant formatting; render when layout or rendering is part of the claim. For backend/server-only work, run targeted server tests and exercise the affected API/runtime path, including persistence and failure handling when applicable. For a tiny nonvisual adjustment, inspect the diff and run a focused regression or direct behavior check, including adjacent behavior it could affect. Use configured-target evidence for hosted/provider claims when safely available; otherwise disclose that gap.
- **Claims now:** Each task may be complete when its applicable gates pass. UI screenshots are not automatically required for these scopes, and unrelated broad suites are not automatic substitutes for relevant checks. No task is verified by the supplied facts alone.
- **Basis:** The verification matrix favors targeted checks, escalating with blast radius. W3 requires fidelity to the claimed surface; W5 protects accepted adjacent behavior.

## workflow-6

- **Handling:** Keep the existing canonical repository as the source and preserve the user's unrelated dirty work.
- **Next action:** Inspect local identity, branch/ref, configured origin, status, and available freshness evidence without network access. Identify dirty-file ownership, then use an authorized clean worktree or a verified known-good local clone at the intended ref. Do not reset, overwrite, stash, or commit unrelated user changes. If exact branch/worktree authorization is required and absent, obtain it before creation.
- **Claims now:** The facts establish that a suitable local repository exists, not that its ref is remotely current or that an isolated implementation is ready. Dirty work is a reason for isolation, not abandonment of the canonical source.
- **Basis:** Source Discovery Enforcement requires canonical local-source discovery and dirty-work protection; the verification matrix requires ownership and status checks. Remote freshness remains unverified under this task's no-network constraint.
