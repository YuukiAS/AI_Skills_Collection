# 058 Active Repo AGENTS Adaptation — Planner Proposal

- Task key: `058_active_repo_agents_adaptation`
- Date: 2026-09-18
- Status: `DRAFT_FOR_CRITIC_REVIEW`
- Planner source: `AI_Skills_Collection main@f4da398aa749769b52f884d264fa43b64128d20e`
- Execution dependency: **do not execute repo adaptations until 056 Product Delivery Discipline is integrated to canonical Bridge/Lite source**
- Scope: repo instruction-surface adaptation only; no product/runtime/scientific-method changes

## 1. Bottom line

The right next step is **not** another 057-style multi-stage workflow.

After 056 is integrated, use one cross-repo Planner/Critic review to approve:

1. the common AGENTS information architecture;
2. the repo-by-repo disposition;
3. the direct canonical-branch edit boundary;
4. the Bridge/Lite refresh rule;
5. a small semantic-preservation/normal-entry acceptance contract.

Then the user can send **independent per-repo prompts**. Each repo is edited, checked, committed and pushed independently. One repo's dirty state or special case must not block the others.

No per-repo task branch, no worktree, no separate implementation-review round, no cross-repo integration package, no new state machine/ledger/controller.

This is deliberate documentation/instruction gardening, not a new product workflow.

## 2. Why this round is needed

057 fixed Bobbio, Lucerna, Mica, Asteria, SeminarArc and created the Bridge fresh-repo AGENTS scaffold. It intentionally did **not** auto-migrate existing repositories.

Current active repositories now show three distinct residual problems.

### A. Rules exist but normal entry does not reliably consume them

The strongest current example is `Distributed_Imaging_Inference` (DII).

Its root AGENTS already says that when a Persistent Run kickoff authorization is missing, Codex should generate and **display** the kickoff prompt and then wait. The user nevertheless observed a real run silently waiting without surfacing the prompt.

This is not evidence that DII needs yet another synonymous local sentence. It is evidence that:

- current generic human-gate behavior is not yet fully delivered/consumed;
- DII has only a Persistent Run managed block on `main`, not a tracked `prompts/AGENT_RULES.md` Lite surface;
- after 056, DII needs explicit adaptation to the final canonical Lite/HUMAN_ONLY behavior and a normal-entry consumption check.

The adaptation task should prove consumption rather than duplicate policy.

### B. Existing root AGENTS are internally inconsistent in shape/ownership

Examples:

- `CAT-TRACE`: root AGENTS mixes the project's very important "Codex does not plan" override, skill routing, version preflight, scientific render rules, Handoff protocol, plugin feedback rules and Overleaf rules. It has a tracked but older `prompts/AGENT_RULES.md`.
- `Reliable_Imaging_Inference`: research/novelty rules and generic Handoff live in one root; tracked Lite rules exist but are older than 057/056.
- `Clash_Profile`: root contains critical production safety plus a long operational runbook. It has several deeper canonical docs already, but no tracked Lite surface.
- `CARE_Challenge`: root AGENTS is currently about 50 KiB / 567 lines and therefore can exceed Codex's default aggregate project-instruction budget before nested instructions are added.
- `CUHK_Date`: root AGENTS currently points to `prompts/AGENT_RULES.md`, `prompts/CHATGPT_RULES.md`, etc., but the `prompts/` directory is not present on current GitHub `main`; this is a real broken-locator issue, not a style preference.

### C. Some recently active repos have no root AGENTS at all

Within the last-six-month active set currently visible on GitHub, examples include:

- `AI_Research_Toolkit`
- `GKD_Rules`
- `Zotero_Arrow_Plugin`
- `Lucerna-Vault`

A fresh scaffold may be useful for repositories still actively operated by Codex, but this should be a per-repo decision, not a symmetry rule.

## 3. External basis

Current OpenAI guidance supports the same direction:

- Codex reads project AGENTS automatically and composes root/deeper instruction files with a default aggregate project-doc budget of about 32 KiB.
- OpenAI's harness-engineering guidance explicitly recommends treating root AGENTS as a **map/table of contents**, not an encyclopedia.
- OpenAI best-practice guidance says concise, accurate AGENTS files are preferable to long vague files, and deeper docs should own detailed planning/review/architecture procedures.

Adopted implication:

> Standardize shape and ownership, not project-specific content.

The common style target is therefore a short, stable root map plus deeper project-owned authorities and the Bridge Lite execution surface.

## 4. Common target structure

Existing repositories should converge toward the same **information architecture**, not identical wording:

```text
# AGENTS.md

## Purpose / authority
## Read first / canonical locators
## Project-specific invariants
## Environment / data / safety         # only when applicable
## Testing / acceptance
## Git / version / release
## Deeper documentation
## Bridge-managed block                # when installed
```

Sections that do not apply should be omitted rather than filled with boilerplate.

### Ownership

- root `AGENTS.md`
  - project map;
  - project-specific hard invariants;
  - canonical source locators;
  - machine/data/safety boundaries that must never be missed.
- `prompts/AGENT_RULES.md`
  - current Bridge Lite execution rules, including final 056 HUMAN_ONLY / delivery behavior after 056 integration.
- deeper `docs/`
  - detailed runbooks;
  - volatile machine/resource inventories;
  - long test matrices;
  - historical incidents;
  - domain/scientific specifications.

Do not copy 056 L1-L6 or generic versioning text into every root AGENTS.

## 5. Human-prompt / HUMAN_ONLY adaptation rule

This is the main real-user regression motivating the round.

After 056 is integrated, every adapted repo that uses Bridge Lite / Handoff / Persistent Run / user approval must consume the current canonical human-gate contract.

Acceptance is behavioral:

- if the agent can resolve the problem itself, it does not ask the user;
- if explicit user input/authorization is genuinely required, the user receives one visible plain-text question/instruction;
- the run must not silently enter a waiting/human-required state without surfacing the required action;
- no reply at the legal run boundary is reported truthfully under the 056 blocked/achieved=no semantics;
- a later valid reply resumes correctly.

A root sentence saying "show the prompt" is not enough evidence.

For repositories that already have a tracked older `prompts/AGENT_RULES.md`, refresh through the final canonical Bridge/Lite source after 056; do not hand-maintain divergent copies.

For repositories with only a Bridge Persistent Run block but no Lite surface, explicitly decide whether current normal development requires Lite and install it only if appropriate.

## 6. Current repo inventory and proposed dispositions

### Group A — already 057-hygiened; adaptation should be minimal

| Repo | Current state | Proposed 058 action |
| --- | --- | --- |
| Bobbio | 057 substantial hygiene complete | `VERIFY_ONLY` + refresh final Lite only if actual tracked Lite surface needs it; do not re-rewrite root |
| Lucerna | 057 light edit complete | `VERIFY_ONLY` / final Lite refresh if applicable |
| Mica-for-ChatGPT | 057 testing consolidation complete | `VERIFY_ONLY`; preserve Mica-specific version/testing/account rules |
| Asteria | 057 root map conversion complete | `VERIFY_ONLY`; preserve Browser contract + GPT Work gate |
| SeminarArc | 057 device-rule map conversion complete | `VERIFY_ONLY`; preserve physical-device safety |
| Bridge Kit | owns scaffold/Lite source | no consumer migration here; 056 first |
| AI_Skills_Collection | central workflow owner | do not "normalize" through consumer template; 056 first |

### Group B — high-priority adaptation

#### Distributed_Imaging_Inference — `SUBSTANTIAL_ADAPTATION`

Current:
- root AGENTS ~302 lines / 13 KiB;
- valuable scientific/HPC rules are mostly legitimate;
- Persistent Run block explicitly says missing kickoff authorization should generate and **display** a prompt;
- no tracked `prompts/` directory on current main;
- user observed a silent prompt/wait failure anyway.

Action after 056:
- preserve scientific, inference, GPU, Slurm and completion semantics;
- reorganize root into the common map;
- keep high-risk scientific/HPC invariants prominent;
- use deeper existing docs for detailed experiment/run mechanics where there is already a canonical owner;
- install/refresh current Lite if normal repository execution should use it;
- verify missing HUMAN_ONLY authorization produces a visible user action instead of silent waiting;
- do not solve the failure by adding a second local copy of 056.

#### CAT-TRACE — `SUBSTANTIAL_REORGANIZATION`

Preserve at root, prominently:
- **Codex does not plan** / GPT-approved scientific contract requirement;
- canonical implementation/decision locators;
- privacy/scientific boundaries.

Reorganize:
- move generic Handoff mechanics to current Lite;
- avoid duplicating skill routing/version-preflight mechanics when a deeper owner exists;
- preserve scientific figure/table/render rules via clear locators or concise root invariants;
- refresh the currently tracked older Lite surface after 056.

No scientific architecture, model, theorem, experiment or presentation content changes.

#### Reliable_Imaging_Inference — `LIGHT_TO_MODERATE_ADAPTATION`

Preserve:
- novelty/evidence gate;
- research framing;
- source policy;
- presentation boundary.

Refresh current older Handoff/Lite surface after 056 and reorganize root to the common map. Do not weaken scientific novelty boundaries.

#### CUHK_Date — `REPAIR_BROKEN_HANDOFF_LOCATORS + LIGHT_ADAPTATION`

Current root is compact, but its Read First section names `prompts/*` files that do not exist on current main.

After 056:
- install/restore the canonical current Lite/Handoff files if the repo is intended to use that protocol;
- otherwise remove stale locators rather than leaving fake read requirements;
- preserve project-specific staging-handoff URL safety;
- do not copy generic Product Delivery Discipline into root.

#### Clash_Profile — `SUBSTANTIAL_MAP_CONVERSION`

Preserve prominently:
- production freeze;
- dangerous remote/tunnel/device mutation prohibitions;
- user authorization boundaries;
- core HK/CN routing invariants.

Use existing deeper authorities such as:
- `docs/ARCHITECTURE.md`
- `docs/ROLLOUT.md`
- `docs/GFW_RULESET.md`
- `docs/CUHK_REMOTE_ACCESS.md`
- `docs/CLIENT_DELIVERY_CONTRACT.md`
- `docs/CLIENT_ACCEPTANCE_MATRIX.md`

Root should become a safety/map entry rather than duplicating the full operational runbook. No production routing/config/device behavior changes in this task.

#### CARE_Challenge — `HIGH_PRIORITY_SUBSTANTIAL_MAP_CONVERSION`

Current root is ~50 KiB / 567 lines, above Codex's default ~32 KiB aggregate project-instruction budget before nested instructions are counted.

This creates a direct risk that late rules are not loaded at all.

Adaptation must:
- identify which content is true root-level challenge/safety/compute authority;
- move long workflow/skill/submission/runbook detail to existing deeper canonical docs;
- preserve leaderboard/submission/data/GPU/safety constraints;
- keep current Bridge/Handoff locator clear;
- avoid changing any CARE model/data/submission behavior.

### Group C — light normalization, not wholesale rewrite

- `CardiacNexus`: keep architecture and imaging constraints; simplify root routing/maintenance map where duplicated.
- `Echo_Select`: preserve privacy/database/Telegram/device constraints; align headings/locators and refresh Lite where appropriate.
- `Web_Highlighter`: already compact; light style/locator pass only.
- `VibeResearch`: already compact; minimal pass.
- `Shione`: compact product/research guidance; minimal map/style pass.
- `Longleaf_Bridge`: compact safety-focused root; add only missing stable locators/structure if useful.
- `Zotero_Koofr_GPT_Mirror`: preserve sync/multi-PDF/Git semantics; light organization pass.
- `MoSAIC_Paper`: very small root; only add missing durable locators if active agent use actually needs them.

### Group D — active repos without root AGENTS; decide rather than auto-create

- `AI_Research_Toolkit`
- `GKD_Rules`
- `Zotero_Arrow_Plugin`
- `Lucerna-Vault`

Default rule:
- if Codex is expected to modify/operate the repo repeatedly, add the minimal current Bridge scaffold plus project-specific safety/locator content;
- if the repo is effectively a passive data/config/vault artifact and normal agent execution is not expected, `NO_AGENTS_NEEDED` is legitimate.

`Lucerna-Vault` requires an explicit secrets/encrypted-state safety review before any scaffold is added.

## 7. Lightweight execution model

This is the deliberate simplification requested by the user.

### One review, then independent repo edits

1. Planner freezes this inventory, common style, per-repo disposition and safety rules.
2. **One independent Critic review** audits the whole batch.
3. After Critic PASS **and after 056 is integrated**, Planner mechanically refreshes the final Bridge/Lite version/ref and produces the approved per-repo prompts.
4. The user sends repo prompts independently.
5. Each prompt operates directly on that repo's canonical branch:
   - no task branch/worktree by default;
   - AGENTS / current Lite-Handoff / directly owned instruction docs only;
   - ordinary non-force commit + push;
   - no product/runtime/scientific-method mutation.
6. One repo's dirty state/failure does not block others.
7. Each repo returns a short before/after semantic-preservation report.
8. No extra per-repo Planner/Critic loop unless that repo discovers a real authority conflict or would need scope beyond docs/instruction adaptation.

No cross-repo integration package is needed because the repositories are independent and docs-only adaptation does not require atomic integration.

## 8. Repo prompt contract

Every approved per-repo prompt must require:

- re-read current canonical branch before editing;
- inspect root AGENTS and directly referenced instruction docs;
- compare current root against the approved common structure;
- preserve every project-specific safety/scientific/product invariant;
- remove only:
  - exact duplicates;
  - stale locators;
  - text moved to a clearly named canonical owner;
  - wording superseded by a demonstrably newer authority;
- no product code/runtime/schema/data/model/config behavior change;
- no arbitrary translation merely for style uniformity;
- no version bump for docs-only instruction gardening unless that repo's explicit local contract says otherwise;
- current Bridge/Lite generated or managed content must come from its canonical source, not hand-copied forks;
- `git diff --check`;
- a compact semantic-preservation checklist;
- if user-input behavior is relevant, a normal-entry check that the required prompt is actually visible, not just present as text.

## 9. Acceptance contract

A repo adaptation passes when:

1. root AGENTS has clear current ownership and no internal contradiction;
2. every canonical locator exists;
3. project-specific hard invariants are retained;
4. generic Lite/workflow text is not redundantly copied into root;
5. no managed Bridge block is manually forked;
6. instruction size/shape is improved where it was genuinely bloated, but line-count reduction is not itself a target;
7. normal-entry human-gate behavior is consumed where relevant;
8. Git diff proves only approved docs/instruction surfaces changed;
9. no product/runtime/scientific behavior changed.

No new H-number gate system is needed for 058.

## 10. Sequencing with 056

Do **not** mass-adapt before 056 finishes.

Reason: CAT-TRACE/Reliable currently carry older Lite rules, DII/CUHK do not have a complete tracked Lite surface, and the exact HUMAN_ONLY behavior the user cares about is a 056 production change. Adapting now would either copy incomplete rules or require a second migration immediately after 056.

Correct order:

```text
056 execution package Critic PASS
-> 056 implementation + independent review
-> separately approved 056 integration
-> final Bridge/Lite source canonical
-> 058 mechanical source-ref refresh
-> one 058 Critic execution review
-> independent per-repo direct canonical-branch adaptation prompts
```

The 058 architecture/inventory can be reviewed now. Final execution prompts should bind the post-056 canonical Bridge/Lite ref.

## 11. Explicit non-goals

058 does not:

- redesign product/scientific architecture;
- add a new workflow engine;
- modify 056;
- re-open 057;
- add Control/Review/Persistent Run merely because a repo is large;
- force every repo to install Lite;
- force every repo to have AGENTS;
- standardize all repos to the same language;
- remove safety rules just to make files shorter;
- create a new AGENTS linter/database/schema/ledger;
- run paid APIs.

## 12. Critic question

Critic should judge:

1. whether one cross-repo review + independent per-repo docs-only edits is sufficiently safe and materially lighter than 057;
2. whether the DII silent-prompt failure is correctly treated as a consumption/adaptation problem rather than a reason to add duplicate local policy;
3. whether the repo dispositions above are proportionate;
4. whether CARE/DII/Clash should move detail into deeper docs without losing critical safety/science constraints;
5. whether missing-AGENTS repos should be decided individually rather than auto-created;
6. whether execution should wait for 056 canonical Bridge/Lite integration.

If PASS, Planner may prepare a **single compact execution batch** consisting only of repo-specific prompts and one batch-level boundary; no per-repo architecture review or task branches should be required unless a repo-specific blocker is discovered.

`NEXT_HANDOFF = CRITIC`
