# Public Input: Workflow Identity And Gate Lifecycle

New Bridge / Reviewed Handoff tasks use semantic machine keys in the form `<scope-token>--<goal-token>`. Historical numeric keys can still be read and validated for existing tasks, but new creation must not teach numbered task IDs.

Human labels are separate from technical locators. A label such as "工作流命名与插件回归机制完善（AI_Skills + Bridge）" helps people recognize the work, but it must not generate branch names, results directories, replay bindings, or scheduled-review identities.

Capability gate lifecycle starts from existing gates. A new real failure first maps to the regression bank for an existing gate. A split or new gate is justified only by a distinct user capability, evidence type, failure semantics, normal entry, or owner boundary.

Release checks run cheap deterministic regression-bank cases first. Narrow gates need an isolation argument. Shared runtime, schema, generator, routing, Marketplace/profile exposure, artifact-review, credential/paid path, or cross-plugin user-visible behavior requires broad/full fallback. Final release claims must bind to the same final candidate.
