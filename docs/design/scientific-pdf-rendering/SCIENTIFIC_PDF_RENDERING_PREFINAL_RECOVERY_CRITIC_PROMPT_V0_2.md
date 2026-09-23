# Scientific PDF Rendering Reliability — Pre-Final Recovery Critic Handoff v0.2

Review only the remaining `PDF-PREFINAL-004` sequencing issue and the revised resume contract.

Repository: `YuukiAS/AI_Skills_Collection`  
Task: `documents-media--scientific-pdf-rendering-reliability`  
Review stage: `PRE_FINAL_RECOVERY_R2`  
Approved architecture package: `fe4351d0606488abfb5247f0bc172cab6c2c5905`  
Implementation candidate under recovery: `ccc3ebdc22c85203512e1c6bc84de0e36d4fc8a1`  
Previous recovery package: `cb8cb7873f3cd1818b0b7d1836eedcb6260542ce`  
Revised recovery package commit: `66987bdf1cc516a3b06d901d37b6b8a992f7fdec`  
Execution branch: `reviewed/documents-media--scientific-pdf-rendering-reliability`  
Execution worktree: `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`

Revised recovery amendment:
`docs/design/scientific-pdf-rendering/SCIENTIFIC_PDF_RENDERING_PREFINAL_RECOVERY_AMENDMENT_V0_2.md`

Revised Codex resume draft:
`docs/operations/prompts/SCIENTIFIC_PDF_RENDERING_PREFINAL_RECOVERY_RESUME_V0_2.md`

Previous Critic result to preserve:

- `PDF-PREFINAL-001 = ACCEPT_CLOSED`
- `PDF-PREFINAL-002 = ACCEPT_CLOSED`
- `PDF-PREFINAL-003 = ACCEPT_CLOSED`
- `PDF-PREFINAL-004 = STILL_OPEN`

Do not reopen 001/002/003 unless this v0.2 sequencing amendment directly regresses them. Do not reopen architecture, G1–G7 taxonomy, version choice, plugin topology, renderer ownership, engine choice, paid-review boundary, or Research Authoring redesign.

## Required reads

Read latest `main`, then actually read:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- approved v0.2 Proposal / Goal / Kickoff at `fe4351d0606488abfb5247f0bc172cab6c2c5905`
- the revised v0.2 recovery amendment and resume draft at `66987bdf1cc516a3b06d901d37b6b8a992f7fdec`
- latest-main release identity and the current reviewed branch only as needed to verify that no new release/source fact invalidates the sequencing correction.

The commits after the verified release baseline `0f00eec88879a925b623bdde34835f98b0120883` through this recovery package are planning/review docs only. At the time Planner prepared v0.2, released main identity was still repository `5.0.7` with workflow-core `0.3`, ai-skills-core `0.4`, web-development `0.2`, research-writing `0.1`, presentations `0.3`.

## The only old blocker to re-review: PDF-PREFINAL-004

The previous package had an internal contradiction:

- it said to add the new `5.0.8` scientific-PDF changelog section only after the repaired candidate passed release gates;
- it also required one exact final candidate to pass G1–G7 including release/version/changelog/README/generated checks.

That would make the post-gate metadata commit a new candidate and violate same-final-candidate evidence.

The v0.2 amendment now requires this exact sequence:

1. conditional preflight and ordinary non-force merge latest main into the same reviewed branch;
2. perform the already-closed 001/002/003 repairs;
3. **before final-candidate freeze**, prepare the entire intended unreleased release metadata:
   - VERSION `5.0.8`;
   - preserve main's historical `5.0.7` changelog unchanged;
   - add the new `5.0.8` scientific-PDF changelog section above it;
   - research-writing `0.2`;
   - preserve every other latest-main released plugin version;
   - README `5.0.8` + Research Authoring `0.2` + truthful companion wording;
   - regenerated registry/catalog/Marketplace/generated payloads from reconciled source;
4. freeze one exact commit containing implementation, tests/evidence contracts, reconciled main state, and all intended release metadata;
5. run G1–G7, including G7 version/changelog/README/generated/profile checks, on that exact commit;
6. if any source or release metadata changes after candidate freeze/gates, it is a new candidate and every affected candidate-bound gate must be rerun;
7. return that same exact candidate to independent pre-final Critic;
8. only after Critic PASS may a later separately-authorized integration/release-to-main occur.

The amendment also states explicitly that `5.0.8` metadata on the reviewed branch means **unreleased release candidate**, not that main has released 5.0.8.

## What must remain unchanged

Confirm the revised resume preserves, without semantic weakening:

- PDF-PREFINAL-001 recovery requirements;
- PDF-PREFINAL-002 recovery requirements;
- PDF-PREFINAL-003 recovery requirements;
- same task / same reviewed branch / same worktree;
- conditional repository `5.0.8` choice only while current released main remains `5.0.7`;
- research-writing `0.1 -> 0.2`;
- presentations NO_BUMP;
- latest-main released workflow-core / ai-skills-core / web-development and all other plugin versions;
- ordinary non-force main-into-task-branch reconciliation;
- no main merge/PR integration before later authorization;
- no force/rebase/history rewrite;
- no paid API/Terra/new private/provider/credential/network/Host Policy scope;
- no architecture/Gate changes.

## Review output

For `PDF-PREFINAL-004`, return:

- `ACCEPT_CLOSED` or `STILL_OPEN`
- direct evidence from the revised amendment/resume
- causal risk if still open
- minimal closing condition if still open

Also state whether the revised resume contract is internally consistent with the approved v0.2 package and previous recovery requirements.

If `PDF-PREFINAL-004 = ACCEPT_CLOSED` and no new direct blocker was introduced, return `PASS` for this recovery R2 package and approve:

`docs/operations/prompts/SCIENTIFIC_PDF_RENDERING_PREFINAL_RECOVERY_RESUME_V0_2.md`

for same-task bounded Codex resume.

This PASS does not approve implementation completion or release; it only authorizes resuming the existing task under the revised recovery contract.

If REVISE, retain stable finding ID `PDF-PREFINAL-004` unless a genuinely new fact creates a distinct direct blocker, and automatically provide the complete next Planner prompt required by the Critic Role Contract.
