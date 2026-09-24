---
name: codex-workflow-protocol
description: Use for complex or risky Codex tasks that require source-of-truth discovery, phased planning, specialist routing, gate-driven verification, live-state supervision, integration ownership, or honest final status reporting.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-09-20
profile_tags:
  - global
  - workflow
  - codex
recommended_scope: global
display_name: Verified Workflow
short_description: Process layer for complex Codex work.
icon_small: assets/workflow-core.svg
icon_large: assets/workflow-core.svg
default_prompt:
  - Run the full source-of-truth, implementation, verification, and reporting workflow.
---
# Codex Workflow Protocol

## Trigger Boundary

Use this skill when the task is complex or risky because it has one or more of these properties:

- multi-phase implementation or execution;
- cross-file, cross-system, generated-layer, deployment, or repository-wide changes;
- explicit acceptance gates, metrics, rendered artifacts, live state, or release/commit boundaries;
- delegation to sub-agents, long-running work, external services, or repeated verification;
- failure could corrupt code, data, research conclusions, publication artifacts, or user-visible releases;
- the user asks for end-to-end execution with evidence rather than a single explanation.

Do not trigger this skill only because the prompt mentions a specific tool, format, or platform. Simple compilation, one-command help, a short wording pass, a single scheduler header, or a casual explanation should route directly to the relevant specialist skill or ordinary answer.

## Non-Negotiable Rule

Do not claim completion without evidence from the current source of truth and the task's real acceptance gates.

Smoke tests, dry runs, preflights, successful compilation, file existence, job submission, HTTP 200, child-agent launch, or old status files are intermediate evidence. They are final only when the user explicitly asked for that intermediate check.

## Specialist Routing Contract

This skill owns process only:

1. discover source-of-truth files and live state;
2. protect existing user work and dirty-tree boundaries;
3. define phases, owners, and acceptance gates;
4. route domain work to the right specialist skill;
5. monitor execution and delegation;
6. integrate results and verify the final state;
7. report precise completion, partial completion, failure, or blocking state.

Specialist skills own technical rules for their domain. They may add stricter checks, commands, schemas, or quality gates. They must not weaken the global completion boundary. Verified Workflow must not override a specialist's technical instructions.

## Task Identity And Labels

Treat task keys as machine locators for branches, results paths, scheduled review bindings, and replay evidence. When Bridge Kit or Reviewed Handoff owns task creation, use its canonical task-key contract; new tasks use semantic `<scope-token>--<goal-token>` keys, while legacy numbered keys remain read/validate-only compatibility. Do not implement a local parser in this skill.

Pick scope from the real owner of the work before choosing a key. Cross-repo or cross-plugin work should use a scope that names the boundary being coordinated, not a client title. Human-readable labels, sidebar titles, thread names, and plugin `display_name` values are presentation metadata; they must not generate, rewrite, or override the technical task key.

## Release Gate Selection

For plugin or workflow releases, identify gates from the frozen Plan and the repository policy rather than inventing a fixed count. Known regressions first map to existing gates and the cheap deterministic regression bank. Split or create a gate only when capability, evidence type, failure semantics, normal entry, or owner boundary genuinely differs.

Run narrow gates only when the changed source area is explainably isolated and should-not-change evidence covers adjacent behavior. Escalate to broad/full gates when shared runtime/schema/generator, routing, marketplace/profile exposure, artifact review, credential/paid paths, or cross-plugin user-visible behavior changed. All release claims must be backed by the same final candidate, with grader/eval changes separated from product behavior changes.

## Workflow

1. Read source-of-truth instructions, repository state, relevant skills, configs, tests, and current artifacts before acting.
2. Separate discoverable facts from preferences; ask only for decisions that cannot be derived safely.
3. Define task-owned files, generated files, pre-existing dirty files, and forbidden changes.
4. Route specialist work explicitly, then follow the specialist's gates.
5. Verify with the strongest practical evidence for the requested outcome.
6. Report status honestly, including skipped checks, residual risk, and required user decisions.

## Product Delivery Discipline

For acceptance, release, user-ready, or other high-risk delivery claims, apply
these five capabilities before asking for external acceptance. Advisory,
diagnostic, design, and architecture reviews may happen earlier, but they must
not claim readiness or completion.

### W1 Acceptance Review Admission

Acceptance/release/user-ready review is allowed only after the applicable
vertical chain is closed for the current frozen feature or milestone:

```text
source/contract -> runtime/backend -> state/persistence when applicable
-> normal entry -> real target behavior -> failure/recovery
-> targeted regression -> risk-matched actual surface
```

UI shells, handlers, placeholder setup surfaces, schema fields, broad green
suites, or `IMPLEMENTED_WHEN_*` conditions do not by themselves prove
capability completion. Human action such as login, credential entry, OS
permission, or physical-device confirmation is an execution checkpoint, not
acceptance. After that action, resume the same Goal and complete the relevant
post-action closure before reconsidering readiness.

When the frozen claim includes catalog breadth, multiple locales, material
branches, provider behavior, uploaded/persisted state, or similar breadth,
include representative coverage for those dimensions. Fallback and recovery
prove recoverability only; they prove the primary capability only when the
frozen Goal explicitly accepts the fallback as equivalent.

### W2 Human Decision Gate

Classify every potential user question first:

```text
HUMAN_ONLY / AGENT_RESOLVABLE / UNSUPPORTED_WITH_EVIDENCE /
OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE / SAFETY_OR_AUTHORITY_BLOCKER
```

Only genuine `HUMAN_ONLY` dependencies ask the user. Repository discovery,
clone/sync/worktree setup, diagnostics, test repair, config generation, and
other agent-resolvable work stays with Codex. Unsupported interfaces close
truthfully with evidence. Optional enhancements do not block the current frozen
objective. Safety or authority blockers use the existing Planner/STOP/approval
route.

In Default mode, required `HUMAN_ONLY` gates must use durable transcript
wait/resume: preserve the current Goal/resume point/prompt identity, ask one
concise plain-text question, and stop dependent execution. At the explicit
deadline or current run boundary with no answer, report recoverable human
blocked state with achieved/complete/user-ready all `NO`; do not continue by
default, poll, create a successor, or consume retry/review budget. A later
explicit in-scope answer resumes the same Goal exactly once after rereading the
current identity. Plan-mode native blocking question semantics remain separate.

### W3 Evidence Fidelity

Match verification to the exact failure and the claim surface. Prefer
old-bad/new-good evidence for deterministic bugs. Unit, mock, helper, browser,
screenshot, native, hosted, and live evidence each prove only their own surface.
Hosted/external-provider claims require bounded configured-target evidence when
safe and feasible. Interaction controls whose intermediate state matters need
sequence-level checks such as type, paste, replace/backspace, and blur/commit.
Do not stitch PASS evidence across different implementation candidates.

### W4 Repeat-Failure Circuit Breaker

When the same class of failure recurs, tests are green but the real path fails,
or a user/reviewer finds a violation of an active rule, stop the blind retry
loop. Before another broad suite, external review, or human retry, record new
information: candidate identity, consumer/loading path, fixture fidelity, root
cause, corrected hypothesis, or a concrete environment explanation.

### W5 Change Impact And Should-Not-Change

Before changing shared behavior, identify accepted behavior and adjacent
capabilities that must not regress. Refactors and rewrites must not silently
degrade mature structured interactions into generic or free-text fallbacks
without an explicit product decision. Domain quality remains owned by the
relevant specialist skill; workflow-core owns gates, routing, evidence, and
completion semantics.

### Source Discovery Enforcement

When a task points to a known repository, first locate the existing canonical
local checkout, worktree, or clone. Verify identity, branch/ref, origin,
freshness, and dirty ownership. Protect unrelated dirty work, but do not abandon
the canonical source merely because it is dirty; use an authorized clean
worktree or known-good local clone when isolation is needed. Network clone only
when no usable local source exists, and do not solve source confusion by
remapping remotes.

### Reviewed Handoff Bootstrap And Resume Routing

When an approved Reviewed Handoff task names an exact repository, task key,
reviewed branch, worktree, and base commit, use the canonical Bridge entry for
the observed lifecycle state. Do not assemble raw Git topology or invent an
alternate worktree.

Use this route:

```text
task missing locally and on the exact reviewed remote
-> ai-bridge reviewed-handoff task bootstrap

complete local task metadata exists, or the exact reviewed remote contains
valid REQUEST/CURRENT for the task
-> ai-bridge reviewed-handoff materialize-worktree --mode resume

required Bridge command, version, or policy support is unavailable
-> fail early before substantive implementation
```

The workflow layer owns only this decision and the early capability check.
Bridge owns the repo-local Git mechanics, canonical remote profile validation,
remote-only metadata discovery, branch/worktree creation, rollback, and
REQUEST/CURRENT validation. Never fall back to `git worktree add`, a `/tmp`
replacement, a second clone, remote remapping, or locally generated task
metadata to get past a missing Bridge capability.

## Final Status Vocabulary

- `complete`: all acceptance criteria met and verified.
- `partial_complete`: useful work exists, but some criteria remain unmet.
- `qa_failed`: an artifact exists but fails quality, validation, rendering, metric, fidelity, or live-state checks.
- `blocked`: external state, permission, dependency, secret, or user decision is required.
- `blocked_target_not_met`: the target cannot be met under current constraints without unacceptable compromise.

## References

- Read `references/task-template.md` when starting a large reusable Codex task or writing a handoff prompt.
- Read `references/verification-matrix.md` for completion gates, dirty-tree handling, and final evidence.
- Read `references/live-state-delegation.md` for long-running work, live state, or sub-agent supervision.
- Read `references/escalation-rules.md` when a baseline, smoke test, or simple method gives weak results.
