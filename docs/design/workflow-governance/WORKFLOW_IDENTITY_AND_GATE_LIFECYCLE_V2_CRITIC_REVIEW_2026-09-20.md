# Workflow Identity & Capability Gate Lifecycle — Critic Review v2

- Date: 2026-09-20
- Review role: independent Critic
- Review stage: DESIGN_PROPOSAL_R2
- Reviewed proposal: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md`
- Reviewed proposal version: `v2`
- Reviewed proposal commit: `7a01c84c1c7f5a6419f62623cf8edc42199d33a4`
- Proposal blob SHA at reviewed commit/current main: `c28839ea78fb1b077da31460f6e7716886c0131b`
- AI_Skills current main checked: `3caeade8ca090e89ae289215a27b40008fc4139c`
- Bridge Kit current main checked: `afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Decision: **REVISE**
- Complexity verdict: **APPROPRIATE**
- Scope: design review only; no execution / production / paid / branch authorization

## 1. Bottom line

v2 closes all three original v1 blockers.

- `C-WIGL-01-SCOPE-PRECEDENCE`: **CLOSED**
- `C-WIGL-02-IMPACT-FALLBACK-BOUNDARY`: **CLOSED**
- `C-WIGL-03-IDENTITY-CUTOVER-COVERAGE`: **CLOSED**

The underlying architecture remains appropriate and has not regressed.

However, the user added one new requirement in this review turn: **human-facing workflow names must optimize for readability and low cognitive load, and must not force the user to mentally parse machine scope tokens or long governance contracts**. Because this review object is specifically about workflow identity, that requirement is central rather than cosmetic.

v2 currently defines a good machine-stable semantic `task_key`, but it still leaves that key too close to being the primary human-facing name. A minimal separation is therefore required before design PASS:

> technical `task_key` for branch/path/control identity; short human-readable workflow label for threads, Codex/Planner/Critic headings and ordinary discussion.

This does **not** justify a new schema, field, registry, database, display-name service, or state machine.

## 2. Source reviewed

AI_Skills latest main was re-read for:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/PLUGIN_MATURITY.md`
- v1 Proposal
- v1 Critic Review
- v2 Proposal
- current 056 implementation Plan
- current 056 Goal

Bridge Kit latest main was re-read for task identity:

- `ai_bridge_kit/reviewed_handoff.py`
- `ai_bridge_kit/cli.py`
- `scripts/validate_handoff_workspace.py`
- `ai_bridge_kit/text_review.py`
- `ai_bridge_kit/visual_review.py`
- `tests/test_reviewed_handoff.py`
- task-bound Executor / Scheduled Reviewer prompt consumers
- `docs/design/reviewed_handoff_parallel_task_branches.md`

Current Bridge production source still has numeric task-key validation in exactly the three known validator surfaces. Text/visual review bind task identity by task-key equality/path propagation rather than defining a separate numeric grammar. This supports v2's “one canonical lexical authority + propagation” design.

## 3. Original blocker closure

### C-WIGL-01-SCOPE-PRECEDENCE — CLOSED

v2 now defines a mutually exclusive precedence:

1. more than one mutable canonical repo -> `cross-repo`;
2. one mutable AI_Skills repo + multiple central plugins whose production behavior changes -> `cross-plugin`;
3. one central plugin -> `plugin-<canonical-plugin-slug>`;
4. one repo, non-plugin-wide work -> `repo`.

Read-only reference repos do not count.

This closes the v1 ambiguity. Current 056 genuinely requires writes in both AI_Skills and Bridge Kit, while Bobbio/Lucerna/Mica/Asteria/SeminarArc/CUHK Date are read-only. Therefore if created under the new scheme, its technical task key is correctly in the `cross-repo` class.

The AI_Skills plugin owners workflow-core / web-development / ai-skills-core remain Plan-level ownership. Companion-plugin use, generated parity, repository release metadata and changelog work do not accidentally promote a one-plugin task to `cross-plugin` or `repo`.

Bridge remains lexical only and does not decide AI_Skills scope semantics.

### C-WIGL-02-IMPACT-FALLBACK-BOUNDARY — CLOSED

v2 turns the previous subjective “Planner thinks it is unaffected” rule into an executable narrow-vs-broad boundary.

Narrow selection is legal only when isolation is explainable, the applicable cheap deterministic known-regression bank passes, affected Gates are clear, no unresolved multi-Gate impact exists, no grader/eval-semantics change breaks comparability, and the release is not a maturity promotion.

v2 forces broad/full fallback for:

- shared generation / prompt assembly;
- model / runtime / provider / router;
- normal-entry / install / invocation;
- shared layers consumed by multiple release-critical Gates;
- impact that cannot be traced reliably;
- new failure with unresolved or multi-Gate attribution;
- material grader/rubric/eval-harness semantic changes;
- maturity promotion;
- concrete cross-Gate evidence.

The proposal also correctly preserves:

- same final candidate direct evidence for every release-critical Gate;
- canaries must observe actual capability, not file/schema existence;
- broad/full does not mean rerunning every historical qualitative/paid case;
- no fixed fresh/manual/paid sample count;
- no impact registry/dependency database/ledger;
- exposed or repair-used samples do not regain “fresh” status under a new grader.

This is a reasonable balance between regression strength and bounded cost. Anthropic's current eval guidance continues to distinguish capability and regression suites and recommends continuous regression maintenance; Microsoft TIA continues to use selective impact testing with an all-tests fallback when impact cannot be understood. Those external practices support the principle without implying their implementation should be copied.

### C-WIGL-03-IDENTITY-CUTOVER-COVERAGE — CLOSED

v2 strengthens G1/G2/G4 rather than adding G8.

The mandatory future acceptance surface now explicitly includes:

- canonical Reviewed Handoff creation;
- generic workspace validation;
- `automation/reviewed_handoff/tasks/<task_key>/`;
- `results/<task_key>/`;
- `reviewed/<task_key>`;
- CURRENT / PLAN / RESULT / REVIEW / FINAL_REPORT;
- text-review manifest/evidence;
- visual-review manifest/evidence;
- task-bound Planner/Reviewer/Executor consumers;
- legacy numeric + semantic coexistence;
- semantic-only canonical new creation after cutover;
- continued legacy numeric validation.

The boundary is also correct: generic validation does not guess from timestamps whether a numeric task was “old enough”. Canonical creation rejects new numeric keys; validator remains dual-format for historical compatibility. No creation ledger/timestamp registry/migration database is needed.

## 4. Capability Gate Matrix review

G1–G7 are sufficient.

- **G1** proves semantic creation through the canonical normal entry.
- **G2** proves complete identity propagation, including text/visual review and task-bound consumers.
- **G3** proves mutually exclusive scope classification.
- **G4** proves legacy coexistence and cutover behavior.
- **G5** proves stable Gate lifecycle with regression growth and obligation-preserving restructure.
- **G6** proves narrow selection, mandatory broad/full fallback and same-final-candidate evidence.
- **G7** proves no new governance machinery or expensive ceremony for ordinary small work.

No G8 is needed for this redesign.

## 5. Complexity review

The proposal remains **APPROPRIATE**.

Keep:

- stable Gate taxonomy;
- growing regression bank;
- same-final-candidate;
- narrow vs broad/full fallback;
- semantic technical task keys for new creation;
- legacy validation compatibility;
- stable task identity through repair/review/integration;
- minimal Bridge lexical support.

Do not add:

- controller;
- watcher;
- database;
- task registry;
- ACTIVE_WORK ledger;
- dependency database;
- state machine;
- GitHub Issues dependency;
- migration of 001–057;
- fixed paid/fresh sample counts;
- task-local docs directory migration.

## 6. New user requirement: human-facing workflow naming

### C-WIGL-04-HUMAN-READABLE-WORKFLOW-LABEL — OPEN

**Requirement**

The user explicitly requires thread/workflow/Codex-facing names to be simple, immediately understandable, and optimized for low cognitive load. A user should see what is being changed or delivered without decoding `cross-repo`, internal role names, long contract terminology, or old ordinal workflow numbers.

**Observed proposal**

v2 correctly defines `task_key` as a stable branch/path/evidence identity, but it does not explicitly separate that technical identity from the human-facing name used in thread titles, Planner/Critic/Codex headings and ordinary conversation.

For example, `cross-repo--product-delivery-discipline` is a valid technical key, but it is not the best normal user-facing title.

The user also clarified that a normal plugin-release workflow can often be named by the plugin display name plus the target version when that version is already frozen.

**Causal risk**

Without an explicit separation, the new semantic key can leak into every prompt/thread/report heading and recreate the same cognitive burden the redesign is supposed to remove—only with longer words instead of `056`.

This is especially likely for broad workflows such as current 056, whose technical scope token is useful for machine identity but not necessary in every human sentence.

**Minimum closure**

Add one small design rule, with no new machine field/schema:

1. `task_key` is the **technical locator** used where stable machine/path identity is needed: Reviewed Handoff task dir, result dir, branch, CURRENT/evidence and one compact locator block in Plan/Goal/Kickoff.
2. Normal user-facing naming uses a **short human label**, not the raw task key.
3. For a single-plugin release, prefer display name + frozen target version when that is the simplest useful label, e.g. `Clear Writing 0.4`. If no version is frozen, use a short outcome phrase such as `Clear Writing 发布收口`.
4. For broad/cross-repo work, use a short outcome phrase, optionally followed by a small scope hint only when needed, e.g. `开发交付流程完善（AI_Skills + Bridge）`; do not make `cross-repo--...` the thread title.
5. In Planner/Critic/Codex prose, show the technical key only when it helps locate branch/path/state, not repeatedly as the name of the work.
6. Do not create a new `display_name` schema field, registry, title service or state.
7. Clarify version handling: candidate/version is **not** a mandatory task-key dimension, but a frozen release target may be used as semantic disambiguation when that is genuinely the simplest way to distinguish two completed release objectives. Do not add opaque sequence/date suffixes.
8. This convention applies only where the workflow controls the wording. It does not claim the repository can force ChatGPT/Codex UI auto-generated conversation titles.

**Examples**

Technical identity:

`plugin-writing-style--release-0-4` (only if 0.4 is already a frozen stable release target and needed for identity)

Human-facing name:

`Clear Writing 0.4`

Technical identity:

`cross-repo--product-delivery-discipline` (or a shorter plain goal token chosen by Planner)

Human-facing name:

`开发交付流程完善（AI_Skills + Bridge）`

For current historical 056, no rename is performed. In user-facing discussion during transition, `开发交付流程完善（原 056）` is enough; the old number should not remain the long-term primary label.

**Owner**

Planner for the minimal v2.1 design clarification; AI Skills Maintainer/workflow policy for human-facing naming convention. Bridge remains unaware of human labels.

## 7. Decision

```text
REVIEWED_PROPOSAL_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
REVIEWED_PROPOSAL_VERSION=v2
REVIEWED_PROPOSAL_COMMIT=7a01c84c1c7f5a6419f62623cf8edc42199d33a4
DECISION=REVISE
COMPLEXITY=APPROPRIATE
C-WIGL-01=CLOSED
C-WIGL-02=CLOSED
C-WIGL-03=CLOSED
BLOCKERS=C-WIGL-04-HUMAN-READABLE-WORKFLOW-LABEL
NON_BLOCKING=NONE
READY_FOR_EXECUTION_PLAN=NO
NEXT_HANDOFF=PLANNER
```

## 8. Scope of next revision

The next Planner round should be a **minimal v2.1 clarification only**. Do not reopen the three closed blockers or redesign Gate lifecycle / scope precedence / Bridge compatibility.

The architecture is already acceptable. The only remaining design issue is making sure the technical semantic key does not become another user-facing contract burden.
