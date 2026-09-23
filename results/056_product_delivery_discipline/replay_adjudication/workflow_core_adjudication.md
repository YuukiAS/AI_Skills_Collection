# workflow-core Unbiased R2 Adjudication

Production candidate commit: `33c30bbe0dd528031a23d379905cd00d6b65bc1f`
Plugin identity: `workflow-core@ai-skills-candidate 0.3`
Runtime: `codex-cli 0.153.4`
Frozen rubric SHA256: `516ed142f55200840e54cda01a08793b51d2e666bc4bc4f8e62e5feb03170269`
Raw response SHA256: `72ed8ae7f9a6bbcdf1d20becd9a9d0a2b766a6d3169b2efcd20424efa3374b4e`
Raw stdout SHA256: `f79f39b8bf723151016cf579d2fdfdb36043e088848c0a888388738960a75b73`
Replay receipt: `results/056_product_delivery_discipline/replay_evidence_unbiased/workflow_core/candidate_replay_run.json`
Raw response: `results/056_product_delivery_discipline/replay_evidence_unbiased/workflow_core/response.md`

## Judged v0.5 Gate(s)

`G2`, `G3`, `G4`, `G5`, `G7`, `Source Discovery`

## Direct Candidate Evidence

- response.md: workflow-1 says final acceptance is premature and achieved/complete/user-ready are all NO.
- response.md: workflow-2 says the human action is a completed checkpoint, not completion of the product.
- response.md: workflow-3 says shell-only evidence establishes only shell-level behavior and the target surface plus interaction sequence is the relevant package.
- response.md: workflow-4 says combining candidate A unit results with candidate B screenshot does not prove either candidate.
- response.md: workflow-5 says validation should match actual change and risk.
- response.md: workflow-6 says preserve unrelated dirty work and use an authorized clean worktree or verified local clone.

## Decision

PASS. The response refuses premature acceptance, treats human action as a resume checkpoint, distinguishes shell evidence from target-surface interaction evidence, rejects stitched candidate evidence, selects risk-matched validation, and protects unrelated dirty user work while using an isolated authorized surface.

SOURCE_DEFECT_DISCOVERED=NO

This adjudication is post-hoc and read-only. It did not modify candidate-visible input or raw candidate output.
