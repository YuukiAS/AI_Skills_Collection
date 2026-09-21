# Scientific PDF Rendering Reliability — Kickoff Draft v0.1

Only use this prompt after an independent Critic has reviewed the exact v0.1 Proposal + Goal + this Kickoff and returned `READY_FOR_CODEX=YES`.

## Kickoff

Repository: `YuukiAS/AI_Skills_Collection`

Exact task: `documents-media--scientific-pdf-rendering-reliability`  
Exact branch to create from kickoff-time verified compatible `origin/main`: `reviewed/documents-media--scientific-pdf-rendering-reliability`  
Exact task-owned worktree: `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`

Canonical Proposal:
`docs/design/scientific-pdf-rendering/SCIENTIFIC_PDF_RENDERING_RELIABILITY_PROPOSAL_V0_1.md`

Canonical Goal:
`docs/goals/SCIENTIFIC_PDF_RENDERING_RELIABILITY_GOAL_V0_1.md`

Your job is implementation only. Do not redesign the architecture.

First read current `AGENTS.md`, the approved Proposal/Goal, the required workflow/policy files they reference, and latest relevant source/TODO. Verify kickoff-time `origin/main` has no semantic drift that invalidates the approved package.

Implement the bounded refinement:

1. make `render-chinese-math-pdf` use a repo-owned canonical Pandoc + XeLaTeX production entry;
2. keep Chromium only as explicit diagnostic, never automatic fallback;
3. add the frozen formal-note profile and semantic Pandoc AST handling;
4. harden math/font/page-identity/whole-document QA;
5. remove/avoid heuristic prose downscaling such as `tableline -> \\footnotesize`;
6. add complete-page render/montage evidence;
7. add Research Authoring handoff through `research-reporting` and install renderer in `research-main`;
8. keep renderer standalone and do not rename it;
9. do not add renderer to Research Authoring Marketplace skill membership;
10. run Proposal G1–G7 and all Goal validation/compatibility checks;
11. save task evidence under `results/documents-media--scientific-pdf-rendering-reliability/`;
12. complete required version/changelog/README/generated-layer closure if and only if release gates pass.

Current approved release expectation, if behavior changes and all gates pass:

- repository `5.0.6 -> 5.0.7`;
- `research-writing 0.1 -> 0.2`;
- `presentations` and all other central plugins: NO_BUMP.

Authorization granted by the user sending this approved Kickoff is limited to:

- ordinary read/fetch of this repository;
- creating the exact branch/worktree above;
- modifying only the Goal-approved source/test/profile/generated/release/evidence paths;
- running local deterministic tests, rendering, profile install smokes, existing generators and existing zero-paid CI normally required by the Goal;
- ordinary non-force commits and push of the exact reviewed branch;
- reading repo-safe fixtures and already-authorized local render resources needed by the existing renderer contract.

Not authorized:

- force push/rebase/history rewrite/branch deletion;
- main merge or PR unless a later approved integration step explicitly authorizes it;
- Host Policy/execpolicy changes;
- Bridge Kit changes;
- new provider/credential/data scope;
- paid API/Terra;
- network font/resource downloads not already allowed;
- copying private research content into public tracked paths;
- changing Presentations/Clear Writing production behavior;
- renaming the skill or creating a new plugin;
- expanding into a Research Authoring redesign.

If implementation reveals that the approved architecture is insufficient, stop with a precise blocker and return to Planner. Do not silently switch to Typst/Quarto, add a Marketplace renderer entry, or ask the user to debug ordinary implementation failures.

Before yielding, commit and push all task-owned tracked changes to the exact branch, verify remote tip, and report real remaining gates. A test PASS is not completion; the same final candidate must reach the Goal’s pre-final independent Critic review with complete rendered artifacts.
