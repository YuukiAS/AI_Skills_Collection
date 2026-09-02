# 049 Private Style Smoke Manifest

The full private report must not be generated until these three representative samples pass human style acceptance.

Plaintext stays private. Public Git records only segment role, source/candidate hashes, implementation identity and user decision.

## SMOKE-A — opening and checkpoint interpretation

Purpose:
- test whether the report opens with the actual research decision rather than audit/process vocabulary;
- test whether checkpoint overlap is explained as a consequence for interpretation before paths/identifiers are shown;
- test whether ordinary terms such as evidence source / training overlap / what the experiment answers are written as natural Chinese rather than English conceptual scaffolding.

Required reader question:
> After reading this sample once, can a technically trained reader explain what the current CARE experiment actually answers and why the checkpoint history matters?

## SMOKE-B — ODAL vs FedFisher / FedLPA

Purpose:
- test whether the conceptual distinction is explained intuitively before formulas and formal terminology;
- preserve Fisher/Laplace/ODAL formal names and mathematical meaning;
- avoid noun-stack prose such as parameter/posterior/curvature labels carrying the whole sentence.

Required reader question:
> Can the reader explain in ordinary language what information FedFisher/FedLPA combine, what the proposed shared-anchor idea would combine instead, and why that difference may or may not matter?

## SMOKE-C — next experiment and GO/STOP decision

Purpose:
- test whether the reader can turn the report directly into an experimental plan;
- explain why FedFisher/FedLPA are the immediate baselines, why local drift is the main axis, and what result would justify or stop new-method development;
- preserve exact experimental conditions and decision boundaries.

Required reader question:
> Can the reader state what to run next, what should stay fixed, what changes, and what outcome means GO versus STOP?

## Acceptance

The user returns one of:

- `STYLE_ACCEPT` — all three samples are good enough to authorize full private generation;
- `STYLE_REJECT` — one or more samples still reflect the failed 048 prose regime.

`STYLE_REJECT` must route to a bounded generic repair. Do not add project-specific phrase blacklists and do not change the frozen private source to make the test easier.
