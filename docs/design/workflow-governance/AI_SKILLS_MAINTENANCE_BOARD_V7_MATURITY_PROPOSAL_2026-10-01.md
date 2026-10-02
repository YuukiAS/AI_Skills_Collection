# AI Skills Maintenance Board — Issue Maturity Proposal v7

- Date: 2026-10-01
- Human label: Maintenance Board Issues 成熟化
- Design topic / task key: `repo--maintenance-board-issue-maturity`
- Repository: `YuukiAS/AI_Skills_Collection`
- Source: latest `main`
- Planner baseline: `main@7566eb5726e92c4aff813e11b0d7addbf9852e6b`
- Prerequisite design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md`
- Prerequisite Critic PASS: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_CRITIC_REVIEW_2026-09-30.md`
- v6.1 reviewed proposal commit: `515c42623c55f368eb84a1628839459afa909c09`
- v6.1 review commit: `7566eb5726e92c4aff813e11b0d7addbf9852e6b`
- Review stage: `MATURITY_DESIGN_PROPOSAL`
- Execution branch/worktree: NONE
- Status: `DRAFT_FOR_CRITIC_REVIEW`

## 1. Conclusion

The current Maintenance Board lifecycle is already real and usable:

- canonical TODO inboxes preserve problem/evidence/maturity;
- `tracking: #N` is the durable source-to-Issue backlink;
- Project `Status` owns `TODO -> DOING -> ADAPTING -> DONE`;
- Project `Area` owns the primary execution owner;
- false-DONE guards, Clear Writing, full-inbox coverage and proactive
  Planner/Critic synchronization are already in production;
- current Project bootstrap evidence shows a real private Project with 82
  initial Issue items, and the live repository now has roughly 60 open and 25
  closed `maintenance-track` Issues.

The missing layer is **Issue maturity**. Current tracked Issues generally carry
only `maintenance-track`, so the repository lacks a stable searchable taxonomy,
a useful human intake path, native hierarchy/dependencies, and bounded triage
automation.

v7 should mature the GitHub Issues layer without creating a second lifecycle or
a custom issue database.

Selected direction:

1. add a small orthogonal label taxonomy;
2. make Project `Area`, Issue labels, and canonical TODO ownership explicit;
3. add two minimal Issue Forms for human intake;
4. use native GitHub dependencies and sub-issues narrowly;
5. add only bounded, GitHub-native automation where it removes real manual
   drift;
6. do **not** add a Rust-scale custom bot, stale closing for maintenance backlog,
   CODEOWNERS, Dependabot, or a new service merely for maturity optics.

## 2. Current-repo gap analysis

### 2.1 What is already mature

Current `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` already owns:

- admission and source backlink;
- one canonical lifecycle;
- Project shape;
- Issue reader-facing copy;
- Planner/Critic maintenance responsibilities;
- no-tool pending mutation;
- ADAPTING / DONE closure semantics.

Current Project evidence shows:

- private `AI Skills Maintenance` Project;
- `Status`, `Area`, `Resolution commit`;
- `Board`, `Active`, `By area`, `History`;
- label-gated Issue admission;
- PR-merged false-DONE path disabled;
- full-inbox bootstrap and durable source locators.

Current representative Issues confirm the system is real:

- #4 is an open repo-level board item in `ADAPTING`;
- #5 is an open `workflow-core` maintenance backlog item;
- #35 is an open `presentations` real-quality issue;
- #63 is a completed `web-development` item;
- #86 is a completed `ai-skills-core` machine-update capability.

### 2.2 Current Issue-layer gap

Representative open and closed Issues carry only:

`maintenance-track`

There is no durable Issue-level distinction for:

- regression vs enhancement vs new capability vs governance;
- plugin vs standalone skill vs repo workflow vs cross-repo work;
- searchable area labels;
- Bridge integration metadata.

This means Project users can see Area and Status inside the Project, but normal
GitHub Issues search/filtering is much weaker.

### 2.3 Current intake gap

Targeted latest-main search found no:

- `.github/ISSUE_TEMPLATE/*.yml` issue forms;
- Issue template chooser config;
- issue-triage workflow;
- labeler config;
- stale config.

The repository's current `.github/workflows` is already used for real CI and
review work such as:

- `codex-marketplace.yml`;
- `ai-bridge-text-review.yml`;
- `ai-bridge-visual-review.yml`.

So the repo has a mature Actions surface, but not an Issue-intake/triage surface.

### 2.4 Current hierarchy gap

The board uses Issues as independent top-level maintenance ideas. There is no
native sub-issue/dependency contract.

That is acceptable for the initial bootstrap, but makes it harder to express:

- one genuine parent maintenance goal decomposed into smaller issues;
- an issue blocked by another plugin/cross-repo issue.

## 3. External practice check

### 3.1 GitHub-native capabilities

Current GitHub supports:

- Issue Forms under `.github/ISSUE_TEMPLATE`, including default labels;
- native sub-issues with parent/child hierarchy;
- native issue dependencies (`blocked by` / `blocking`);
- issue metadata such as labels and Projects;
- official `actions/labeler` for PR path/branch-based labels;
- `actions/stale`, which by default can mark and later close inactive Issues.

Adoption decision:

- use Issue Forms;
- use sub-issues/dependencies narrowly;
- do not use stale closing for tracked maintenance backlog;
- evaluate PR path labeler separately from Issue taxonomy.

### 3.2 Rust

Rust uses orthogonal label families such as:

- `T-*` team;
- `A-*` area;
- `C-*` category;
- `P-*` priority;
- `S-*` state;
- `needs-triage`.

Its triagebot can relabel, autolabel from files/labels, ping teams and perform
other commands.

Adopt:

- the idea of visibly orthogonal label dimensions;
- an explicit needs-triage queue.

Do not adopt now:

- a large custom command bot;
- Rust-scale priority/team/status taxonomies;
- automation that assumes a many-maintainer organization.

AI_Skills currently does not have the scale or organizational structure that
justifies that control plane.

### 3.3 VS Code

VS Code triage expects a type label plus a feature-area classification, with a
bot handling commands and `needs more info`.

Adopt:

- one primary kind;
- one primary area;
- a small pre-admission triage queue.

Do not adopt:

- automatic issue closing merely because information was not supplied within a
  short timeout;
- the full custom issue-bot command language.

Maintenance backlog can legitimately remain quiet for long periods.

### 3.4 PyTorch

PyTorch uses labels such as:

- `module: ...`;
- `oncall: ...`;
- `triaged`;
- `actionable`;
- specialized regression/correctness labels;

and uses automated labeling to route a very large tracker.

Adopt:

- module/area-style searchable ownership projection;
- a clear difference between intake and triaged work.

Do not adopt now:

- oncall routing;
- large bot-owned classification;
- an `actionable` state label duplicating AI_Skills TODO maturity /
  Project lifecycle.

## 4. Source-of-truth matrix

v7 must prevent three metadata systems from drifting.

| Concern | Canonical source of truth | Issue label role | Project role |
|---|---|---|---|
| Problem / evidence / maturity | canonical plugin/skill TODO entry | none | none |
| Source -> Issue mapping | source `tracking: #N` | Issue number is target | none |
| Lifecycle | Project `Status` | **never** encode lifecycle | canonical |
| Primary execution owner | Project `Area` | `area:*` searchable mirror | canonical |
| Kind | Issue taxonomy label | canonical searchable classification | none |
| Scope | Issue taxonomy label | canonical searchable classification | none |
| Bridge integration | optional `integration:bridge-kit` | searchable metadata only | none |
| Blocked-by relation | GitHub native dependency | no duplicate blocked label required | visible relation |
| Parent/child relation | GitHub native sub-issue relation | no custom hierarchy label | visible relation |

Rules:

- never add `status:todo`, `status:doing`, `status:adapting`,
  `status:done` labels;
- Project `Area` wins if an `area:*` label drifts;
- canonical source maturity does not get copied into labels;
- Issue `kind:*` and `scope:*` are Issue-native classification, not lifecycle.

## 5. Proposed label taxonomy

Keep the taxonomy deliberately small.

### 5.1 Admission / triage

Existing:

- `maintenance-track` — admitted lifecycle Issue and Project auto-add key.

Add:

- `triage:needed` — pre-admission Issue still needs central triage;
- `triage:needs-info` — optional pre-admission intake that cannot yet be
  classified because evidence is insufficient.

These labels are **pre-admission only**. Once an Issue becomes
`maintenance-track`, remove `triage:needed` / `triage:needs-info` unless a
future independently reviewed rule proves a need.

They are not Project lifecycle states.

### 5.2 Kind — exactly one on every maintenance-track Issue

- `kind:regression`
  - an established capability/rule/path is failing or has regressed in real use.
- `kind:enhancement`
  - improve an existing capability's quality, usability, maintainability or
    completeness without creating a fundamentally new user capability.
- `kind:new-capability`
  - introduce a user-visible capability that the current system does not
    materially provide.
- `kind:governance`
  - repository/workflow/maintenance policy, handoff, lifecycle, release or
    governance mechanics.

Do not add priority labels in v7. There is no approved priority process yet.

### 5.3 Scope — exactly one on every maintenance-track Issue

- `scope:plugin`
- `scope:standalone-skill`
- `scope:repo-workflow`
- `scope:cross-repo`

`scope:cross-repo` means the AI_Skills-owned tracked item genuinely spans repo
boundaries. It does not transfer ownership of another repo's bug into
AI_Skills.

### 5.4 Area — exactly one on every maintenance-track Issue

Mirror the existing Project `Area` values:

- `area:workflow-core`
- `area:ai-skills-core`
- `area:writing-style`
- `area:research-writing`
- `area:presentations`
- `area:scientific-visualization`
- `area:web-development`
- `area:statistical-modeling`
- `area:bioinformatics`
- `area:medical-imaging`
- `area:standalone-skill`
- `area:repo`
- `area:cross-plugin`

Project `Area` is authoritative. The matching Issue label exists for normal
GitHub search and triage.

Do not create a second per-skill Project Area taxonomy in v7. Specific
standalone-skill identity remains visible through its canonical source path and
Issue title/body.

### 5.5 Optional integration metadata

- `integration:bridge-kit`

Use only when the AI_Skills-owned issue truly has a Bridge Kit integration /
dependency dimension.

Do **not** create `area:bridge-kit`.

A Bridge Kit runtime/product bug belongs to the Bridge canonical repository.
An AI_Skills issue may reference that external Issue through a native dependency
or ordinary locator while retaining the correct AI_Skills Area.

## 6. Intake design

v7 should add only two human-facing Issue Forms.

Forms are an intake surface, not the canonical TODO source and not automatic
Project admission.

### 6.1 Existing plugin / skill real failure

Proposed file:

`.github/ISSUE_TEMPLATE/existing_capability_failure.yml`

Purpose:

- report a real failure from an existing plugin or standalone skill.

Required fields should ask for:

- target plugin / skill;
- real task / project context;
- what was expected;
- what actually happened;
- evidence / reproduction locator;
- project-specific details that should not become generic rules.

Default label:

- `triage:needed`

Do **not** automatically add:

- `maintenance-track`;
- `kind:regression` — because some reported failures are actually enhancement
  gaps rather than true regressions;
- Area / scope guessed from free text.

Planner/maintainer triage assigns the real taxonomy.

### 6.2 New capability proposal

Proposed file:

`.github/ISSUE_TEMPLATE/new_capability.yml`

Ask for:

- user problem / desired capability;
- why existing plugin/skill/workflow is insufficient;
- expected normal entry;
- affected owner if known;
- real examples/evidence;
- explicit non-goal / project-local detail if known.

Default labels:

- `triage:needed`
- `kind:new-capability`

Do not automatically add `maintenance-track`.

### 6.3 Template chooser

Add:

`.github/ISSUE_TEMPLATE/config.yml`

Keep `blank_issues_enabled: true` in v7.

Reason:

- these two forms cover common human intake, not every governance/cross-repo
  maintenance case;
- internal Codex/maintainer-created Issues must remain able to use direct
  programmatic creation without an artificial form round-trip;
- unstructured blank Issues still enter bounded triage rather than the Project
  automatically.

The forms must not use the `projects:` key. Project admission remains
`maintenance-track`-gated after triage.

## 7. Intake-to-tracking contract

Human intake and canonical TODO admission remain distinct.

### 7.1 New form/blank Issue

Initial state:

- not `maintenance-track`;
- not in the lifecycle Project;
- `triage:needed` present;
- optional form-supplied kind label only where semantically safe.

### 7.2 Planner / maintainer triage

For an intake Issue:

1. compare with canonical TODO entries and existing Issues;
2. decide project-local / duplicate / rejected / central maintenance;
3. if central maintenance:
   - create/update the canonical TODO entry first;
   - reuse the intake Issue as the top-level tracking Issue when it is the right
     granularity;
   - write source `tracking: #N`;
   - assign exactly one `kind:*`, `scope:*`, and matching `area:*`;
   - add `maintenance-track`;
   - remove pre-admission triage labels;
   - set Project `Area` and lifecycle `TODO`.
4. if duplicate:
   - reference the existing canonical Issue;
   - close as duplicate / not-planned according to truthful GitHub reason;
   - do not add `maintenance-track`.
5. if project-local / rejected:
   - keep it out of the Maintenance Project;
   - close or redirect truthfully if appropriate.

This avoids making GitHub Issues a second raw TODO inbox.

## 8. Issue hierarchy and dependency design

Use GitHub-native relations only.

### 8.1 Dependencies — adopt

Use native `blocked by` / `blocking` when one tracked Issue genuinely cannot
progress until another Issue completes.

Examples:

- a plugin refinement blocked by a cross-plugin workflow fix;
- an AI_Skills integration issue blocked by a Bridge Kit Issue in its canonical
  repository.

Do not create `blocked` lifecycle states or duplicate blocked-by labels.

### 8.2 Sub-issues — adopt narrowly

Use native sub-issues only when there is a **real parent maintenance goal** and
children are independently meaningful Issues.

Good use:

- one genuine feature/refinement parent decomposed into multiple independently
  closeable regressions/components.

Do not create a parent Issue merely because several unrelated regressions happen
to be implemented in the same release round.

A release/refinement batch is execution evidence unless it is itself a real
top-level maintenance idea.

This preserves the current rule that execution rounds are not automatically
new lifecycle items.

## 9. Automation alternatives

### Option A — no automation

Use labels/forms but rely entirely on Planner/Codex manual updates.

Pros:

- minimal implementation.

Cons:

- with 60+ open maintenance Issues and growing intake, label drift becomes
  predictable;
- blank/programmatic intake can remain untriaged;
- metadata completeness is not observable.

Not selected as the target maturity level.

### Option B — GitHub-native forms + one small bounded intake Action

Selected.

Add one small Issue Action whose job is deliberately narrow:

On new Issue:

- if it already has `maintenance-track`, do nothing;
- otherwise ensure `triage:needed` exists;
- never add `maintenance-track`;
- never guess `kind:*`, `scope:*`, or `area:*`;
- never close an Issue;
- never mutate Project Status;
- never edit canonical TODO files.

This is bounded triage automation, not a bot state machine.

The Action can use repository-scoped `GITHUB_TOKEN` with minimum
`issues: write` permission.

### Option C — Rust-style custom triage bot

Rejected for v7.

A custom command bot would add:

- new deployment/runtime ownership;
- permission surface;
- command syntax;
- config state;
- maintenance burden.

The current repo does not need Rust's thousands-of-Issues / many-contributor
permission delegation.

## 10. Metadata consistency audit

Do not add a scheduled daemon or a long-lived database.

v7 should add a deterministic **bounded audit command** in the repository or
maintenance tooling, invoked by the existing Project-capable
Planner/Codex/maintainer path.

It must check every current `maintenance-track` Issue:

- exactly one `kind:*`;
- exactly one `scope:*`;
- exactly one `area:*`;
- no pre-admission `triage:needed` / `triage:needs-info`;
- `area:*` equals Project `Area`;
- canonical source backlink exists when the Issue came from a canonical TODO;
- Issue close state remains compatible with Project lifecycle / BOARD-01.

Why not make this a scheduled GitHub Action immediately:

- repository `GITHUB_TOKEN` is repo-scoped;
- GitHub's own Project-Actions documentation uses a separate token with
  `project` scope for Project v2 automation;
- adding a long-lived Project token secret solely for a periodic audit is not
  justified yet.

The initial v7 migration and acceptance can run the audit through the existing
Project-capable maintainer/Codex environment that already maintains the board.

If repeated drift later proves a scheduled audit is valuable, propose that
separately with its credential/permission contract.

## 11. Bounded auto-labeling

v7 permits automation only where classification is deterministic.

Allowed:

- Issue Forms add their fixed initial intake labels;
- intake Action ensures `triage:needed` on ordinary new Issues;
- explicit Planner/Codex triage writes kind/scope/area labels;
- one-time migration derives `area:*` from Project Area and `scope:*` from
  canonical source ownership where unambiguous.

Not allowed:

- keyword/LLM Action guessing kind/area;
- title regex that changes lifecycle;
- auto-adding `maintenance-track`;
- auto-closing Issue based on labels/activity;
- copying Project Status into labels.

## 12. PR path labeler

GitHub's official `actions/labeler` can apply PR labels from changed paths.

Decision for v7 core: **defer**.

Reason:

- the identified maturity gap is Issue intake/search/triage;
- PR path labeling does not solve Issue taxonomy;
- AI_Skills generated/source/shared paths make area mapping non-trivial;
- adding a path map before Issue taxonomy stabilizes creates another taxonomy
  mapping to maintain.

After v7 has operated for one or two real refinement rounds, evaluate a small
PR-only `area:*` path map as a separate enhancement.

This is not a blocker to v7.

## 13. Stale policy

Do **not** add `actions/stale` for v7 maintenance backlog.

GitHub's official stale Action can, by default, mark and later close Issues after
inactivity. That is incompatible with long-lived maintenance TODOs and can cause
false closure.

Normative rule:

- `maintenance-track` Issues are exempt from inactivity-based closure;
- inactivity alone is never evidence for DONE or not-planned;
- no stale automation may close a Project lifecycle Issue.

If a future repository wants stale handling for pre-admission
`triage:needs-info` Issues, it must be a separately reviewed rule that:

- targets only pre-admission intake;
- explicitly exempts `maintenance-track`;
- never uses `completed` as close reason;
- cannot trigger Project DONE;
- has a recovery/reopen path.

No such automation is needed now.

## 14. CODEOWNERS

Defer.

GitHub CODEOWNERS is valuable for PR review routing and branch protection when
there are multiple human/team owners.

Current Maintenance Board already has Project `Area` and the repository is not
currently suffering from human reviewer routing ambiguity.

Adding CODEOWNERS would not materially improve Issue intake or Board semantics
today and could create self-review/noisy review requests.

Revisit only when:

- multiple human maintainers/teams own distinct source areas; or
- branch rules need code-owner approval.

## 15. Dependabot

Defer from v7.

Dependabot is a dependency-update/security feature. It does not solve Issue
taxonomy, intake, hierarchy or Board metadata drift.

The repo does use GitHub Actions and dependencies, so Dependabot may be useful as
a separate supply-chain maintenance task, especially for GitHub Actions
references. But enabling it here would mix an unrelated PR-generation policy
into Issue maturity and create review noise.

Do not add it merely to appear mature.

## 16. Migration / backfill strategy

### 16.1 Freeze live state

Before mutation in a future implementation:

- snapshot current labels and Project Area for all `maintenance-track` Issues;
- snapshot open/closed state;
- save a migration report under task results.

Do not change lifecycle Status during taxonomy migration.

### 16.2 Create labels first

Create the approved label set and descriptions before changing Issues or adding
forms.

### 16.3 One-time classification

For every existing open **and closed** `maintenance-track` Issue:

- `area:*`: mirror current Project Area;
- `scope:*`:
  - plugin source -> `scope:plugin`;
  - standalone-skill source -> `scope:standalone-skill`;
  - repo-level board/workflow -> `scope:repo-workflow`;
  - real AI_Skills-owned cross-repo item -> `scope:cross-repo`;
- `kind:*`: Planner/maintainer semantic classification, not keyword automation.

Representative expected mappings:

- #5 Bridge-rule separation:
  `kind:governance`, `scope:cross-repo`,
  `area:workflow-core`, optional `integration:bridge-kit`;
- #35 presentation real-quality regression:
  `scope:plugin`, `area:presentations`; kind determined from evidence as
  regression vs enhancement;
- #63 UI presentation-boundary improvement:
  likely `kind:enhancement`, `scope:plugin`,
  `area:web-development`;
- #86 machine-update orchestration:
  `kind:new-capability`, `scope:plugin`, `area:ai-skills-core`.

If kind classification is genuinely ambiguous, do not guess merely to achieve
100% labels. Leave the Issue in an explicit migration exception report and
return Planner.

### 16.4 Bridge ownership rule

For any candidate `integration:bridge-kit` Issue:

- verify AI_Skills owns the problem being tracked;
- if the real bug is Bridge runtime/product behavior, the canonical Issue belongs
  in Bridge Kit's repo;
- AI_Skills may keep only its own integration/adaptation Issue and represent the
  Bridge dependency natively.

### 16.5 Forms last

Only after labels exist and backfill taxonomy is validated:

- add Issue Forms;
- add the tiny intake Action;
- verify newly opened human intake would not auto-enter the Project.

## 17. Acceptance

A future implementation cannot PASS from config files alone.

### A1 — taxonomy integrity

For every `maintenance-track` Issue:

- exactly one `kind:*`;
- exactly one `scope:*`;
- exactly one `area:*`;
- `area:*` equals Project `Area`;
- no lifecycle label;
- no pre-admission triage label.

### A2 — source/project separation

Verify:

- canonical TODO maturity unchanged by taxonomy migration;
- `tracking: #N` unchanged unless a real rebind occurs;
- Project Status unchanged by taxonomy migration;
- Project Area remains the owner source of truth.

### A3 — intake

Verify live template chooser contains exactly the intended minimal forms plus
blank Issue route.

Validate:

- failure form creates only pre-admission intake labels;
- new-capability form creates `triage:needed` +
  `kind:new-capability`;
- neither form adds `maintenance-track` or Project admission;
- internal Codex issue creation remains possible without using the form.

### A4 — bounded Action

Verify on representative event payloads:

- ordinary new Issue receives `triage:needed`;
- already-`maintenance-track` Issue is untouched;
- Action never closes, edits Project Status, or assigns kind/scope/area;
- permissions are minimum required.

### A5 — hierarchy

Verify native dependency/sub-issue use does not create a second lifecycle or
custom hierarchy store.

No requirement to backfill hierarchy onto every historical Issue.

### A6 — stale safety

There is no workflow capable of inactivity-closing `maintenance-track`
Issues.

### A7 — human usability

Sample open and closed Issues across at least:

- workflow-core;
- presentations;
- web-development;
- ai-skills-core / repo;

and confirm GitHub Issues search can answer:

- all regressions for presentations;
- all governance work;
- all cross-repo integration work;
- all items owned by workflow-core;

without opening the Project.

## 18. Rollback

Taxonomy migration must be reversible without touching lifecycle/source truth.

Rollback can:

- remove v7-only labels from Issues;
- remove Issue Forms / intake Action;
- remove native dependency/sub-issue relations added by the task.

Rollback must not:

- remove `maintenance-track`;
- alter Project Status;
- alter Project Area;
- alter source `tracking: #N`;
- reopen/close Issues solely to undo taxonomy;
- rewrite canonical TODO maturity/evidence.

Keep a pre-migration label snapshot in task results.

## 19. What mature practices are deliberately not copied

Not adopted in v7:

- Rust-scale triagebot command/control surface;
- Rust priority/team/status label families;
- VS Code/PyTorch-style automatic stale/needs-info closure for tracked backlog;
- PyTorch oncall labels;
- issue types requiring organization-level taxonomy;
- PR path labeler before Issue taxonomy stabilizes;
- CODEOWNERS before multiple human/team ownership exists;
- Dependabot as part of Issue maturity;
- custom hierarchy database;
- Project Status mirrored as labels;
- Bridge Kit as an AI_Skills Area.

These are mature practices in the right context, but not evidence-backed needs
for this repository now.

## 20. Relationship to v6.1

v6.1 is already independently approved and corrects a live required-consumer
semantic error for Issue #4.

v7 is a **new maturity enhancement**, not a prerequisite for fixing that error.

Recommendation:

```text
DO_NOT_COMBINE_IMPLEMENTATION_BY_DEFAULT
```

Reason:

- v6.1 is a small policy/current-truth correction on an existing ADAPTING item;
- v7 adds labels, intake configuration, migration, hierarchy policy and bounded
  automation;
- combining them would make the urgent #4 semantic correction wait behind a
  broader migration and would move #4's completion target;
- v7 should have its own tracking Issue / completion evidence after design PASS.

Recommended order:

1. keep v6.1 implementation minimal and close its policy/current-truth repair;
2. treat v7 as a separate Maintenance Board maturity tracking item;
3. only share mechanical helpers if they are already mature and do not merge
   lifecycle/accountability.

If a future execution-ready Critic finds one atomic implementation materially
safer, it may propose that explicitly, but the default plan is separation.

## 21. Minimal v7 scope

The minimum worthwhile v7 is:

1. exact label taxonomy above;
2. source-of-truth contract above;
3. two Issue Forms + chooser config;
4. one tiny pre-admission intake Action;
5. native dependency/sub-issue policy;
6. one-time taxonomy backfill of current maintenance Issues;
7. bounded metadata audit through existing Project-capable maintenance tooling;
8. stale prohibition for `maintenance-track`.

Deferred:

- PR path labeler;
- custom bot;
- scheduled Project audit requiring a new token;
- CODEOWNERS;
- Dependabot;
- priority/oncall labels.

## 22. External references and adoption state

Reviewed:

- GitHub Issues / sub-issues / dependencies / Project best practices;
- GitHub Issue Forms and form schema;
- `actions/labeler`;
- `actions/stale`;
- Rust triagebot / Rust triage label families;
- VS Code issue triage + automated triage;
- PyTorch AutoLabel Bot / issue labeling practice;
- GitHub CODEOWNERS;
- GitHub Dependabot version updates.

Adoption states:

- GitHub Issue Forms: `SELECTIVELY_PORTED` in proposal;
- GitHub native sub-issues/dependencies: `SELECTIVELY_PORTED`;
- GitHub small Issues Action: `SELECTIVELY_PORTED`;
- Rust label-family idea: `REFERENCE_ONLY -> SELECTIVE_TAXONOMY_PATTERN`;
- Rust custom triagebot: `REVIEWED_NOT_ADOPTED`;
- VS Code triage model: `REFERENCE_ONLY -> SELECTIVE_KIND_AREA_PATTERN`;
- PyTorch module labels: `REFERENCE_ONLY -> SELECTIVE_AREA_PATTERN`;
- actions/stale: `REVIEWED_NOT_ADOPTED`;
- actions/labeler: `DEFERRED`;
- CODEOWNERS: `DEFERRED`;
- Dependabot: `DEFERRED`.

## 23. Non-goals

This design round does not:

- create labels;
- modify Issues or Project;
- add `.github` files;
- create sub-issue/dependency links;
- run Actions;
- modify canonical board policy;
- implement v6.1;
- modify plugin production source;
- execute machine adaptation;
- create a bot/service/database;
- bump repository/plugin version.

## 24. Planner result

```text
RESULT = PROPOSAL_READY
PROPOSAL_VERSION = v7
CURRENT_GAP = ISSUE_TAXONOMY_INTAKE_HIERARCHY_BOUNDED_TRIAGE
SELECTED_AUTOMATION = GITHUB_NATIVE_FORMS_PLUS_SMALL_PRE_ADMISSION_ACTION
CUSTOM_TRIAGE_BOT = NO
MAINTENANCE_TRACK_STALE_CLOSE = FORBIDDEN
PROJECT_STATUS_LABELS = FORBIDDEN
PR_PATH_LABELER = DEFER
CODEOWNERS = DEFER
DEPENDABOT = DEFER
V6_1_REOPENED = NO
COMBINE_WITH_V6_1_IMPLEMENTATION = NO_BY_DEFAULT
CRITIC_REVIEW_REQUIRED = YES
NEXT_HANDOFF = CRITIC
```
