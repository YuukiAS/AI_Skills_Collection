# AI Skills Maintenance Board — Consumer-Scope Amendment v6

- Date: 2026-09-30
- Human label: Maintenance Board required-consumer contract
- Design topic / task key: `repo--maintenance-board-lifecycle`
- Repository: `YuukiAS/AI_Skills_Collection`
- Source: latest `main`
- Planner baseline: `main@db243107f12ce060204f9ef56925f75502abda47`
- Supersedes only the required-consumer selection rule in:
  `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md`
- Keeps all other v5 architecture unchanged.
- Live tracking Issue under review: `#4`
- Current live Issue state: `ADAPTING`
- Status: `DRAFT_FOR_CRITIC_REVIEW`

## 1. Planner conclusion

A semantic amendment is required.

The current canonical board policy hard-codes five default logical consumers for
all machine-consumed/shared-maintenance work:

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`
4. `Workstation`
5. `Legion`

That set was appropriate for the independent **AI Skills Maintainer
machine-update orchestration** product, whose release closure explicitly tested
all five environments. It is not automatically the correct completion set for
every unrelated tracked item that happens to be machine-consumed.

For Maintenance Board Issue #4, the completion question is narrower:

> Which normal-entry environments actually perform or intentionally back up
> AI_Skills_Collection central maintenance / TODO / Planner / Critic / closure
> work and therefore must consume the board contract?

Installation of AI Skills Maintainer, or inclusion in the machine-update
product's five-consumer acceptance matrix, is not by itself evidence that an
environment is a required Maintenance Board consumer.

## 2. Evidence from current main and Issue #4

### 2.1 Canonical policy currently over-generalizes

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md §14` currently states a fixed
five-consumer default for machine-consumed/shared-maintenance items.

The same file separately defines the actual board normal-entry surfaces:

- ChatGPT Project instructions for ordinary AI Research Stack threads;
- AI_Skills `AGENTS.md` for Codex repo sessions;
- Planner Role Contract;
- Critic Role Contract;
- AI Skills Maintainer only as a downstream per-current-consumer executor.

These are lifecycle-consumption surfaces, not a statement that every machine
with AI Skills Maintainer installed must be adapted for every board item.

### 2.2 Issue #4 current live state

Issue #4 is open and `ADAPTING`.

Its body says central implementation is complete and currently asks for all five
logical consumers before DONE. That reflects the existing v5 rule and
`CONSUMER_HANDOFFS.md`, not a fresh proof that all five are true board
consumers.

### 2.3 Current Maintenance Board handoff evidence

`results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md` records:

- `Longleaf_Codex`: `LOCATOR_OBSERVED`, with an observed
  `AI_Skills_Collection` repository path.
- `CUHK_Workstation_WSL_Codex`: `LOCATOR_OBSERVED`, with an observed
  `AI_Skills_Collection` repository path.
- `Longleaf_Backup_Codex`:
  `HOST_OBSERVED_REPO_LOCATOR_NOT_OBSERVED` at board central cutover.
- `Workstation`: no local `AI_Skills_Collection` project locator observed
  from that board handoff surface.
- `Legion`: no `AI_Skills_Collection` project locator observed from that
  board handoff surface.

This handoff therefore directly supports two current Codex repo consumers and
does not establish the other three as board normal-entry consumers.

### 2.4 Machine-update evidence is a different contract

The later independent task
`ai-skills-core--machine-update-orchestration` closed with all five consumers
PASS. Its `FINAL_REPORT.md` explicitly says those five were the required
consumers **for that machine-update product**.

That proves machine-update coverage. It does not prove that Workstation,
Legion, or Longleaf_Backup are required central-maintenance entry points for
Maintenance Board #4.

## 3. External reality check

Current OpenAI product boundaries support an entry-point-based interpretation:

- ChatGPT Project instructions apply to conversations inside that Project.
- Codex CLI discovers and injects applicable `AGENTS.md` for the repo / working
  directory.

Therefore Maintenance Board consumption naturally follows the actual ChatGPT
Project and Codex repo entry surfaces that perform central maintenance; it
should not be inferred from unrelated plugin installation coverage.

References checked:

- https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- https://developers.openai.com/api/docs/guides/latest-model

## 4. Alternatives

### Option A — keep the fixed five-consumer default

Advantages:

- simple;
- matches the machine-update task's existing five-environment acceptance
  matrix;
- avoids deciding consumer scope per tracked item.

Failure mode:

- conflates two different products:
  Maintenance Board lifecycle consumption and AI Skills Maintainer machine
  update coverage;
- forces board adaptation on machines that may never perform central
  maintenance;
- creates unnecessary machine/credential authorization work;
- can keep an otherwise complete board item in ADAPTING solely because an
  irrelevant machine has not consumed a contract it never uses;
- makes future machine additions look like board requirements by association.

This is over-adaptation and should not remain the default.

### Option B — freeze required consumers from the tracked workflow's real normal entries

For each machine-consumed/shared-maintenance tracked item:

1. identify the normal-entry environments that actually need the changed
   behavior for the item's completion claim;
2. include an intentionally designated fallback/backup entry only when the
   product contract explicitly relies on it;
3. freeze that evidence-backed required set at ADAPTING cutover;
4. adapt/verify only that set;
5. treat later optional consumers as follow-up work unless the old closure claim
   was false.

Advantages:

- completion matches the real product boundary;
- avoids unrelated machine adaptation;
- preserves the existing ADAPTING/DONE lifecycle and per-consumer Maintainer
  architecture;
- requires no new field, registry, watcher, controller, or service.

Selected: **Option B**.

## 5. Minimal semantic amendment

Replace the fixed-five default in the canonical board policy with this rule:

> For a machine-consumed workflow/shared maintenance mechanism, required
> consumers are the **actual normal-entry consumers that must consume the
> tracked change for the item's frozen completion claim to be true**.
>
> A machine is not required merely because AI Skills Maintainer is installed
> there, because that machine participated in the machine-update product's own
> acceptance matrix, or because it could technically run the repo.
>
> An intentionally supported backup/fallback entry is required only when the
> tracked item's completion contract explicitly promises that fallback path.
>
> At ADAPTING cutover, freeze the evidence-backed required consumer set and
> exact locators. Future optional consumers do not retroactively enlarge that
> frozen set unless new evidence proves the old completion claim was false.

No new Project field is needed. The tracking Issue's existing adaptation section
holds the frozen consumer list and evidence.

## 6. Maintenance Board #4 recommended required set

### Already-satisfied non-machine normal entry

The AI Research Stack ChatGPT Project instructions are already part of central
closure and were user-confirmed as semantically installed. This remains a
required board normal-entry surface, but it is already satisfied and is **not**
a pending ADAPTING machine handoff.

### Pending machine/Codex required consumers

Based on current repo evidence, freeze Issue #4's pending downstream required
consumer set to:

1. `Longleaf_Codex`
2. `CUHK_Workstation_WSL_Codex`

Reason: these are the two environments for which the board handoff directly
observed current `AI_Skills_Collection` Codex repo locators.

### Excluded from Issue #4 required set

#### Workstation

Exclude from #4 unless future direct evidence shows that Windows Workstation is
a normal central-maintenance entry for AI_Skills_Collection.

Its later PASS in machine-update closure proves machine-update consumption, not
Maintenance Board lifecycle consumption.

#### Legion

Exclude for the same reason. Its machine-update PASS proves it can consume AI
Skills Maintainer updates; it does not establish a normal AI_Skills central
maintenance / Planner / Critic / closure role.

#### Longleaf_Backup_Codex

Exclude from #4's required set **under current evidence**.

The board handoff observed the host but did not observe an
`AI_Skills_Collection` repo locator there at central cutover. Later
machine-update evidence proves the environment exists and can consume
AI_Skills, but does not establish that it is an intentionally supported backup
entry for central maintenance-board work.

The word "Backup" in the display name is not sufficient evidence of a product
contract.

If the user later explicitly designates `Longleaf_Backup_Codex` as a supported
backup central-maintenance entry, a future tracked item can include it in its
frozen required set. This should not be inferred automatically for #4.

## 7. Issue #4 closure consequence

After this amendment receives independent Critic PASS and is implemented:

- Issue #4 remains `ADAPTING` while the two pending required Codex consumers
  are unverified.
- `CONSUMER_HANDOFFS.md` and Issue #4 should be revised to distinguish:
  - central normal-entry surface already satisfied: AI Research Stack ChatGPT
    Project instructions;
  - pending required downstream consumers:
    `Longleaf_Codex`, `CUHK_Workstation_WSL_Codex`;
  - non-required machine-update consumers:
    `Longleaf_Backup_Codex`, `Workstation`, `Legion` under current evidence.
- No adaptation of excluded machines is required for #4 DONE.
- Once the two required downstream consumers PASS with durable evidence and all
  existing closure conditions hold, #4 may proceed to Resolution commit +
  completed close -> DONE.

This design round does not perform those mutations.

## 8. General future rule

For future tracked items, Planner must freeze required consumers from the
item's actual normal-entry contract, not inherit a global machine list.

Evidence that can justify a required consumer includes, for example:

- the tracked workflow is normally executed from that repo/Codex environment;
- the completion claim explicitly promises that environment;
- the environment is an intentionally designated fallback path;
- a Project/AGENTS/normal-entry contract requires the changed behavior there.

Insufficient by itself:

- AI Skills Maintainer is installed;
- the machine was in a different product's acceptance matrix;
- the machine has a Codex installation;
- the machine could theoretically clone the repository.

If consumer evidence is ambiguous, keep the item ADAPTING and return Planner;
do not inflate the set "for safety" and do not silently exclude an explicitly
promised normal entry.

## 9. What does not change

This amendment does **not** redesign:

- `TODO -> DOING -> ADAPTING -> DONE`;
- BOARD-01;
- full-inbox bootstrap;
- `tracking: #N` source backlink;
- Clear Writing / Project surface review;
- Planner/Critic proactive sync;
- no-tool exact pending mutation;
- central implementation complete -> ADAPTING;
- per-current-consumer AI Skills Maintainer;
- Resolution commit / issue-close final DONE;
- no cross-machine controller;
- no standalone Kanban skill/plugin;
- version policy.

It only changes how a tracked machine-consumed item selects its required
consumer set.

## 10. Version / implementation boundary

This is a maintenance-policy semantic change only.

Proposed implementation, only after independent Critic PASS:

- amend `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md §14`;
- amend Issue #4 / `CONSUMER_HANDOFFS.md` to the approved #4 required set;
- preserve all existing evidence rather than deleting the historical five-set
  handoff record;
- no production plugin source change;
- no machine adaptation in the amendment task;
- no repository/plugin version bump.

## 11. Planner result

```text
RESULT = PROPOSAL_READY
RECOMMENDED_REQUIRED_CONSUMERS = Longleaf_Codex, CUHK_Workstation_WSL_Codex
ALREADY_SATISFIED_NON_MACHINE_CONSUMER = AI Research Stack ChatGPT Project instructions
EXCLUDED_FROM_ISSUE_4_REQUIRED_SET = Longleaf_Backup_Codex, Workstation, Legion
SEMANTIC_CHANGE_REQUIRED = YES
CRITIC_REVIEW_REQUIRED = YES
NEW_CONTROL_PLANE = NO
```
