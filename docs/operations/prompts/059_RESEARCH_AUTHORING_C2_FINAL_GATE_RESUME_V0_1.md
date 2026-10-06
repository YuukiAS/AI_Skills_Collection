# 059 Research Authoring C2 — Final Gate Resume v0.1

Authority:

- C2 pre-final Critic PASS:
  `docs/design/059_RESEARCH_AUTHORING_C2_PREFINAL_GATE_ADMISSION_CRITIC_REVIEW_V0_1_2026-10-06.md`
- Critic commit:
  `4b428c297587d68085d56f15decaf00277c2e63f`

Repository:

`YuukiAS/AI_Skills_Collection`

Task:

`research-authoring--formal-production-authoring`

Branch:

`work/research-authoring--formal-production-authoring`

Worktree:

`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

Exact final candidate:

`ac501d988f00cb6672fec105ae5fd51a0679cae0`

Frozen pre-final packet:

`2ebd8f3de0597b9549a7528c9917222b44c4cb59`

## 0. Immutable boundaries

Do not modify Research Authoring candidate-owned production source.

Do not change final task, input manifest, Phase 2 delta, rubric, reviewer contract, natural prompt, or C2 identity after seeing outputs.

Do not stitch predecessor final PASS into C2.

Do not use paid API.

Do not update the live Research Authoring Plugin yet.

Do not merge/release main.

If any final Gate produces a real product FAIL, preserve it and stop. Do not rerun until PASS, switch tasks, weaken the rubric, or alter C2.

## 1. Preflight

In the exact worktree:

1. verify repo/origin/branch/dirty ownership;
2. `git fetch origin main`;
3. verify current branch contains the Critic PASS;
4. verify candidate-owned Research Authoring surface remains byte-identical to C2;
5. read:
   - `results/research-authoring--formal-production-authoring/PREFINAL_GATE_FREEZE.md`
   - `results/research-authoring--formal-production-authoring/C2_REVIEWER_ACCESS_RUBRIC_MANIFEST.md`
   - G1/G2/G3/G4 frozen packets under `private/exports/research-authoring--formal-production-authoring/c2_pre_final/`.

If candidate-owned drift exists, stop without final execution.

## 2. G1 — execute final C2 normal-entry evidence

Use the frozen:

- `c2_pre_final/G1/G1_CASE_BANK.md`
- `c2_pre_final/G1/G1_RUBRIC.md`

Run the frozen natural cases against exact C2 using normal candidate/runtime entry.

Required evidence must show actual runtime consumption; static trigger metadata does not count.

In particular, the frozen advisor-PDF natural request must consume Research Authoring first and, on standalone/no-renderer entry, stop at stable scientific source + complete downstream production handoff.

Do not append evaluation-only wording such as “do not XeLaTeX / pdftotext / render”.

Near-miss cases must retain their correct owner.

Store complete G1 evidence under task-local results/private exports and bind hashes.

Executor does not self-declare G1 PASS; prepare it for independent review.

## 3. G2 — execute Phase 1 only

Frozen project:

`YuukiAS/Reliable_Imaging_Inference`

Frozen Phase 1 ref:

`dc0b2ea471e79c29963d2ed92575a77540d23425`

Materialize only the exact five blobs listed in:

`private/exports/research-authoring--formal-production-authoring/c2_pre_final/G2/PHASE1_INPUT_MANIFEST.md`

Do not run from the full repository checkout.

Do not materialize, read into authoring context, or use any Phase 2 file.

Use the exact natural task and rubric in the frozen G2 packet.

Produce the complete Phase 1 advisor-facing research update plus complete route/runtime evidence and claim/evidence/provenance evidence required by the rubric.

Then STOP G2.

Do not start Phase 2 until an independent reviewer explicitly records:

`G2_PHASE1=PASS`

Executor must not self-authorize Phase 2.

## 4. G3 — execute the frozen real manuscript Gate

Frozen source:

`YuukiAS/CARE_Challenge@75a40e454de43b64e59a0b0b438ff57ef2bb8345`

Use only the frozen source/authority contract under:

`private/exports/research-authoring--formal-production-authoring/c2_pre_final/G3/`

CARE repo remains read-only.

Build the real manuscript package under the AI_Skills private export:

- `main.tex`
- `references.bib`
- only scientifically necessary `figures/`
- `main.pdf`
- `MANUSCRIPT_EVIDENCE_MAP.md`
- `MANUSCRIPT_PACKAGE.md`
- build/log/reference QA required for review

Use the approved Research Authoring production route and appropriate renderer for manuscript mechanics.

The manuscript must preserve the verified negative result and unresolved hypotheses; the `DEFERRED_BLUEPRINT_ONLY` rescue blueprint must not become a completed method.

No external submission or fabricated venue state.

Materialize any binary/source needed by the Reviewer with exact hashes.

Executor does not self-declare G3 PASS; prepare complete full-material evidence for independent review.

## 5. Pre-build the G4 C2 wrapper offline

To avoid another delay later, prepare the actual complete offline skills-only wrapper archive now, without any Plugin Creator/live account mutation.

Use only the frozen C2 composition:

- Research Authoring generated payload from exact C2;
- Clear Writing support snapshots from the same C2;
- wrapper name `research-authoring`;
- expected distribution version `0.3.1`;
- USER / PRIVATE target semantics;
- skills-only;
- no renderer runtime;
- no MCP/connector/database/watcher.

Write the archive and a complete file/hash/composition manifest under:

`private/exports/research-authoring--formal-production-authoring/c2_pre_final/G4/`

The archive must be reproducibly bound to:

`ac501d988f00cb6672fec105ae5fd51a0679cae0`

Do not call Plugin Creator and do not change the current live release.

## 6. Combined independent-review checkpoint

After G1 evidence, G2 Phase 1 evidence, G3 evidence, and the offline G4 wrapper archive are complete:

1. commit only task-owned evidence/control files;
2. ordinary non-force push exact task branch;
3. stop.

Return exactly enough locators for one combined independent review:

```text
FINAL_CANDIDATE_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0
G1_FINAL_EVIDENCE_READY=YES|NO
G2_PHASE1_EVIDENCE_READY=YES|NO
G2_PHASE2_NOT_STARTED=YES
G3_FINAL_EVIDENCE_READY=YES|NO
G4_OFFLINE_WRAPPER_ARCHIVE_READY=YES|NO
G4_LIVE_PLUGIN_MUTATION=NO
FINAL_GATES_COMPLETE=NO
EVIDENCE_HEAD=<commit>
NEXT_HANDOFF=CRITIC_REVIEWER
```

If any G1/G2-Phase1/G3 final task genuinely fails, report the immutable failure and stop; do not replace or rerun the task.

## 7. Still prohibited

- Research Authoring production changes;
- changing C2;
- G2 Phase 2 before independent Phase 1 PASS;
- live Plugin Creator/update;
- G4 ChatGPT final run;
- G4 Codex/render stage;
- paid API;
- main merge/release;
- force/destructive Git;
- new Gate / successor task / task substitution.
