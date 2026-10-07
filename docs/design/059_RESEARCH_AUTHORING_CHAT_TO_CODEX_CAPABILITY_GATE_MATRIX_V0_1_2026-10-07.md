# 059 Research Authoring — ChatGPT to Codex capability gate matrix v0.1

Date: 2026-10-07
Task: `research-authoring--formal-production-authoring`

## Gate taxonomy

```text
ADD_G5=NO
G1=Research Authoring normal entry and boundary
G2=research-document semantics and incremental update
G3=real manuscript/source package and cross-file consistency
G4=ChatGPT -> Codex production chain
```

## Scope correction

```text
RAW_CODEX_AUTHORING_OWNER_COMPETITION=
REMOVED_FROM_CURRENT_0_3_RELEASE_BLOCKER

CHATGPT_RESEARCH_AUTHORING_NORMAL_ENTRY=
REQUIRED

CODEX_HANDOFF_PRODUCTION_CONSUMER=
REQUIRED
```

Codex raw natural authoring owner competition is not a current G1/G4 release blocker. It is a future standalone Codex enhancement.

## G1 corrected

G1 validates Research Authoring natural entry and boundaries.

Primary natural-entry evidence now belongs to ChatGPT wrapper / ChatGPT Web:

- Methods;
- research update;
- related work;
- existing research document revision.

Near-miss coverage still protects:

- citation verification;
- paper lookup;
- single-sentence content-preserving polish;
- README / email;
- PPT / Beamer;
- render-only;
- ordinary research Q&A.

Codex-side G1 evidence is limited to its actual role: when handed exact source/handoff, Codex must not invent, rewrite, or silently change scientific meaning beyond the authorized production contract.

## G2 unchanged

G2 continues to test research-document semantics and incremental authoring, including the approved two-phase DII-style contract when frozen for final evidence.

## G3 unchanged

G3 continues to test real manuscript/source package production, cross-file consistency, venue/template boundaries, claim ledger boundaries, citation/figure/label correctness, and buildable/readable package requirements when frozen for final evidence.

## G4 corrected

G4 is the end-to-end product chain:

```text
ChatGPT natural Research Authoring request
-> exact candidate Research Authoring source/handoff
-> Codex consumes exact handoff/source
-> production/render/file QA
-> final artifact
-> post-render Research Authoring scientific QA
```

G4 must verify:

- ChatGPT wrapper and Codex candidate identity match;
- source/handoff preserves scientific meaning;
- Codex does not re-invent scientific content;
- final artifact exists and is readable;
- renderer/file QA actually ran;
- final scientific QA directly checks the final artifact.

## Retired development blocker

```text
PROFILE_SCOPED_EXPLICIT_DELEGATE_RECOVERY=RETIRED
P2_FROM_FAILED_PREFLIGHT=NOT_CREATED
```

The failed preflight remains evidence that project-local explicit-only copies do not contain same-name user/global Skills in the current pinned runtime. That fact does not imply failure of the ChatGPT -> Codex production chain.

## Final Gate boundary

Final G1-G4 must not start until a revised pre-final packet is frozen and independently approved.

```text
FINAL_GATES_NOT_STARTED=YES
LIVE_PLUGIN_MUTATION_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
```
