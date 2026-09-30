# AI Skills Maintenance Board — Consumer-Scope Amendment v6.1

- Date: 2026-09-30
- Human label: Maintenance Board required-consumer contract
- Design topic / task key: `repo--maintenance-board-lifecycle`
- Repository: `YuukiAS/AI_Skills_Collection`
- Source: latest `main`
- Planner baseline: `main@97de8aa3cf36a379aa978ec4f90535df5b04a538`
- Supersedes: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_PROPOSAL_2026-09-30.md`
- Previous proposal commit: `abdbf8ce571f7890889a774dd0f4740648769d57`
- Previous Critic review:
  `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_CRITIC_REVIEW_2026-09-30.md`
- Previous Critic review commit:
  `97de8aa3cf36a379aa978ec4f90535df5b04a538`
- Stable blocker: `BOARD-CONSUMER-NORMATIVE-01`
- Tracking Issue: `#4`
- Review stage: `DESIGN_AMENDMENT_REVISION`
- Execution branch/worktree: NONE
- Status: `DRAFT_FOR_CRITIC_REVIEW_R2`

## 1. Planner disposition

```text
BOARD-CONSUMER-NORMATIVE-01 = ACCEPT
```

The Critic's blocker is correct.

v6 changed the intended required-consumer selection rule, but its implementation
boundary named only canonical policy §14. Current canonical
`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` also contains a fixed-five
normative statement in §15:

```text
五 consumer aggregate truth 属于 tracking Issue / Project lifecycle。
```

Leaving §15 unchanged would reintroduce fixed-five semantics immediately after
§14 moved to a per-item required set.

v6.1 therefore changes only the **normative convergence scope** of the proposed
implementation. The already accepted consumer-selection direction and Issue #4
recommended set do not change.

## 2. Accepted direction remains unchanged

The following are accepted from v6 and are not reopened:

- required consumers come from the tracked item's actual normal-entry /
  explicitly promised fallback contract;
- required consumers do not mechanically inherit the AI Skills Maintainer
  machine-update product's five-machine acceptance matrix;
- Issue #4 pending Codex consumers are:
  - `Longleaf_Codex`
  - `CUHK_Workstation_WSL_Codex`
- AI Research Stack ChatGPT Project instructions are an already-satisfied board
  normal-entry surface;
- under current evidence, the following are not Issue #4 required consumers:
  - `Longleaf_Backup_Codex`
  - `Workstation`
  - `Legion`
- a future workflow that explicitly promises multiple environments still
  requires every environment needed by that real completion claim;
- no new Project field, registry, watcher, controller, skill, plugin, daemon,
  service, or cross-machine control plane is introduced.

## 3. Current normative inconsistency

Latest-main canonical policy currently says:

### §14

It hard-codes the five default logical consumers:

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`
4. `Workstation`
5. `Legion`

and says ordinary non-machine work does not inherit five-machine validation.

### §15

It correctly says AI Skills Maintainer is a per-current-consumer executor, but
then hard-codes the aggregation owner as:

```text
五 consumer aggregate truth 属于 tracking Issue / Project lifecycle。
```

### §16

It is already generic:

```text
all required consumers PASS/N/A
+ durable evidence complete
+ Resolution commit
+ tracking Issue completed close
+ issue-closed workflow -> DONE
```

Therefore only §14 and §15 are normatively inconsistent with the accepted v6
direction. §16 already matches the desired dynamic required-set semantics.

## 4. Required canonical-policy convergence

After independent Critic PASS, implementation must update **all normative
fixed-five wording in the canonical board policy**, not only the list in §14.

At minimum this includes §14 and §15.

### 4.1 §14 — selection rule becomes evidence-backed and per item

Replace the fixed-five default with this normative contract:

> For a machine-consumed workflow or shared maintenance mechanism, required
> consumers are the actual normal-entry consumers and explicitly promised
> fallback environments that must consume the tracked change for that item's
> frozen completion claim to be true.
>
> A machine is not required merely because AI Skills Maintainer is installed
> there, because it appeared in another product's machine-update acceptance
> matrix, because it has Codex installed, or because it could technically clone
> the repository.
>
> A backup/fallback environment is required only when the tracked item or its
> frozen product contract explicitly promises that fallback path.
>
> At ADAPTING cutover, the tracking Issue freezes the evidence-backed required
> consumer set and the exact current locators needed for those consumers.
>
> If the normal-entry / fallback evidence is ambiguous, keep the item ADAPTING
> and return Planner. Do not add environments "for safety", and do not silently
> omit an environment explicitly promised by the product contract.
>
> Future optional consumers do not retroactively enlarge the frozen DONE
> contract unless new evidence shows the prior completion claim was false.

Per-consumer PASS evidence remains the same kind already required by the current
policy: actual target identity, approved adaptation/update action,
installed/loaded identity, normal-entry consumption, relevant fresh-session /
restart boundary, risk-matched safety, and durable evidence.

### 4.2 §15 — aggregation wording becomes quantity-neutral

Keep the current Maintainer boundary:

> AI Skills Maintainer is a per-current-consumer adaptation executor, not a
> cross-machine controller.

Change only the fixed-five aggregation wording from:

```text
五 consumer aggregate truth 属于 tracking Issue / Project lifecycle。
```

to the quantity-neutral equivalent:

```text
required-consumer aggregate truth 属于 tracking Issue / Project lifecycle。
```

or a semantically equivalent Chinese sentence such as:

> 当前 tracked item 的 required-consumer 聚合真值属于 tracking Issue /
> Project lifecycle。

Keep the existing non-goals:

- Maintainer does not own a machine registry;
- Maintainer is not a multi-machine orchestrator;
- Maintainer is not a credential broker.

### 4.3 §16 remains normative and unchanged

§16 already uses:

```text
all required consumers PASS/N/A
```

This is exactly the desired generic closure rule.

No blocker-driven rewrite of §16 is required.

## 5. Scope of "all normative fixed-five wording"

Implementation must search the **current canonical board policy only** for
normative fixed-five wording that would contradict the new required-set rule.

The minimum known changes are §14 and §15.

If another current sentence inside
`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` normatively says that all
machine-consumed work requires exactly those five consumers, that sentence must
be made quantity-neutral in the same bounded amendment.

This does not authorize rewriting unrelated lifecycle, admission, Clear
Writing, tracking-locator, Planner/Critic, version, or Project rules.

## 6. Historical design/execution artifacts remain historical evidence

Do **not** rewrite old design or execution artifacts merely because they record
the historical five-consumer contract.

In particular, do not modify for this amendment:

- v4/v5 design Proposals;
- v4/v5 Critic reviews;
- historical v0.3-v0.5 Goals / Kickoffs / execution packages;
- prior review artifacts that accurately record what the contract was at that
  time.

Those files are historical evidence, not the current canonical policy.

The amendment should change current normative truth prospectively, without
rewriting history.

## 7. Planner / Critic role contracts remain unchanged

Current latest-main role contracts already use generic required-consumer
language.

Planner Role Contract currently states, in substance:

> central implementation complete but machine-consumed workflow still has
> required consumers pending -> ADAPTING and freeze exact consumer
> identities/locators.

It does not hard-code five consumers.

Critic Role Contract likewise consumes lifecycle truth generically and does not
need a fixed-five repair for this blocker.

Therefore this amendment does **not** modify Planner or Critic role contracts.

If a future independent review discovers an actual fixed-five normative string
in those contracts, that would be new evidence and a separate bounded repair;
it is not assumed here.

## 8. Issue #4 current required set remains unchanged

After Critic PASS and later implementation, Issue #4 current truth should be:

### Already satisfied normal entry

- AI Research Stack ChatGPT Project instructions

This was part of central closure and is not a pending machine adaptation.

### Pending required downstream consumers

1. `Longleaf_Codex`
2. `CUHK_Workstation_WSL_Codex`

### Not required for #4 under current evidence

- `Longleaf_Backup_Codex`
- `Workstation`
- `Legion`

Reason remains exactly as accepted by the v6 Critic:

- the Maintenance Board handoff directly observed
  `AI_Skills_Collection` Codex repo locators for the first two;
- the other three were later proven as machine-update consumers, but that does
  not establish a Maintenance Board central-maintenance normal-entry or promised
  fallback contract;
- "Backup" in a display name is not itself a product promise.

## 9. Issue #4 and CONSUMER_HANDOFFS implementation rule

This design round does not mutate Issue #4 or
`results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md`.

After Critic PASS, a bounded implementation may update their **current truth**
while preserving history.

Required behavior:

- preserve the original five-consumer handoff evidence as historical evidence;
- do not delete or rewrite evidence merely because the normative contract has
  changed;
- add/update a clearly labeled current required-set section or equivalent
  current-state wording;
- distinguish:
  - already-satisfied ChatGPT Project normal entry;
  - current pending required consumers:
    `Longleaf_Codex`, `CUHK_Workstation_WSL_Codex`;
  - historically listed but currently non-required machine-update consumers:
    `Longleaf_Backup_Codex`, `Workstation`, `Legion`;
- keep Issue #4 `ADAPTING` until its current required set satisfies the
  existing closure requirements.

No excluded machine requires adaptation solely for Issue #4 closure.

## 10. Future selection rule remains evidence-based

For every future machine-consumed tracked item, Planner freezes the required
set from the item's real completion contract.

Evidence that can make an environment required includes:

- that environment is a real normal-entry execution surface for the tracked
  workflow;
- the completion claim explicitly promises that environment;
- the product contract explicitly designates it as a supported fallback;
- a Project / AGENTS / repo normal-entry contract requires the changed behavior
  there.

Insufficient by itself:

- AI Skills Maintainer is installed;
- that machine passed a different product's machine-update acceptance;
- the machine has Codex;
- the machine could theoretically host the repo.

The goal is not "fewer consumers"; the goal is the **correct** required set.

## 11. Why this closes BOARD-CONSUMER-NORMATIVE-01

The Critic's blocker was a contradiction inside the one canonical policy:

```text
§14 dynamic required set
vs.
§15 fixed-five aggregate truth
```

v6.1 removes that contradiction by requiring:

```text
§14 = evidence-backed frozen required set
§15 = required-consumer aggregate truth, quantity-neutral
§16 = all required consumers closure, unchanged
```

All three sections therefore describe the same object: the tracked item's frozen
required consumer set.

## 12. External-research note

No new external technical unknown is introduced by this revision.

The previous v6 Critic independently rechecked current OpenAI Projects and Codex
instruction surfaces. This v6.1 repair is solely an internal normative
consistency fix between canonical policy §§14–16, so no new external mechanism
or capability is assumed.

## 13. Version and capability-gate boundary

This amendment changes maintenance policy / tracking completion semantics only.

It does not change formal plugin runtime behavior, plugin packaging, profiles,
Marketplace payload, or machine-update production source.

Therefore the proposed later implementation remains:

```text
Repository bump decision: NONE
Affected plugins:
- all: NO_BUMP
```

No new production Plugin Capability Gate is introduced by this amendment.

## 14. Explicit non-goals

This design revision does not:

- implement the canonical policy change;
- modify Issue #4;
- modify `CONSUMER_HANDOFFS.md`;
- execute machine adaptation;
- modify AI Skills Maintainer production source;
- modify Planner/Critic role contracts;
- rewrite historical v4/v5 or historical execution artifacts;
- create Project fields;
- add a registry, watcher, controller, daemon, skill, plugin, profile, or
  service;
- change BOARD-01, lifecycle, full-inbox, Clear Writing, tracking locator, or
  no-tool pending mutation semantics;
- bump repository/plugin versions.

## 15. Alternatives check

### A. Change §14 only

Rejected.

That reproduces the Critic blocker because §15 would still normatively say
"five consumer aggregate truth".

### B. Change every historical file containing five-consumer wording

Rejected.

That rewrites historical evidence, expands scope, and is unnecessary because
the canonical current policy owns present semantics.

### C. Converge current canonical §§14–15 and leave generic §16 intact

Selected.

This is the smallest change that makes the single canonical policy internally
consistent while preserving history and the accepted required-set direction.

## 16. Planner result

```text
RESULT = PROPOSAL_READY
PROPOSAL_VERSION = v6.1
BOARD-CONSUMER-NORMATIVE-01 = ACCEPTED_AND_REVISED
ISSUE_4_PENDING_REQUIRED_CONSUMERS = Longleaf_Codex, CUHK_Workstation_WSL_Codex
ISSUE_4_ALREADY_SATISFIED_NORMAL_ENTRY = AI Research Stack ChatGPT Project instructions
ISSUE_4_NON_REQUIRED_UNDER_CURRENT_EVIDENCE = Longleaf_Backup_Codex, Workstation, Legion
CANONICAL_POLICY_SECTIONS_TO_CONVERGE = §14, §15, plus any other current normative fixed-five sentence found in the same canonical file
SECTION_16 = KEEP_GENERIC_ALL_REQUIRED_CONSUMERS
ROLE_CONTRACT_CHANGES = NONE
HISTORICAL_ARTIFACT_REWRITE = NO
PRODUCTION_SOURCE_CHANGE = NO
MACHINE_ADAPTATION = NO
VERSION_BUMP = NONE
NEW_BLOCKERS_FOUND_BY_PLANNER = NONE
NEXT_HANDOFF = CRITIC
```
