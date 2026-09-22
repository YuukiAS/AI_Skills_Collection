The next step is to diagnose production consumption, not add another central rule. The scenario suggests an existing-rule production regression, but does not yet establish its cause. “No obvious missing payload” is weaker than verified parity.

Check, in order:

1. The failing task’s installed and enabled plugin identity, version, and payload hash; compare them with candidate `33c30bbe0dd528031a23d379905cd00d6b65bc1f`.
2. Source/generated/Marketplace parity for that plugin.
3. Evidence that the normal invocation actually loaded that installed payload.
4. The trigger and routing path into the expected skill or aggregate.
5. The task entrypoint, branch/ref, and session context, including older instructions still in context.
6. Whether the replay faithfully reproduces the original task and failure surface.
7. Whether the resulting evidence supports `not_loaded`, `stale_install`, `consumer_not_routed`, `unfaithful_test`, `execution_noncompliance`, `missing_rule`, or `capability_gap`.

Another synonymous rule is not warranted now. If installation, routing, or execution caused the failure, address that cause in its existing layer. Consider a source behavior change only after evidence establishes a distinct missing requirement or capability, or a defect in the current rule’s implementation.

Before changing source behavior, collect the original request and failing artifact, applicable rule and existing TODO, exact runtime identity, loading/routing evidence, and a faithful baseline replay. Freeze a bounded change with the domain owner, explicit acceptance criteria, and an unrelated regression case. After implementation, require source/generated parity and original-failure plus unrelated-regression evidence from the same final installed candidate. Artifact quality claims require direct artifact inspection by the appropriate domain reviewer; CI or an executor summary is insufficient.

Source-tree inspection can establish that rule text exists and identify intended coverage or static inconsistencies. Explicit comparisons can establish static generated parity. Neither proves that the real session installed, loaded, routed to, or followed that rule, nor that the artifact passes or the regression is fixed. This diagnosis uses the supplied scenario and the installed AI Skills Maintainer entrypoint; it does not independently verify the failing task’s runtime or claim a successful production replay.
