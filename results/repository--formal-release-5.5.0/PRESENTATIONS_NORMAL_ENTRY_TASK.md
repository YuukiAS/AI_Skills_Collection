# Presentations 0.4 release acceptance — normal entry

Create a complete five-slide research update from the supplied public-safe source notes.

Use the installed Presentations candidate through its ordinary natural route. Do not use a benchmark generator as the orchestration surface. The requested deliverables are:

- an exact-CUHK source-editable Beamer `.tex` deck;
- the rendered PDF;
- one PNG per page and a contact sheet;
- a validated `deck-plan.yaml`;
- a concise deterministic QA record;
- a page-by-page rendered review input that binds every PNG and the PDF by SHA-256.

Use the production entry documented by the candidate when applicable. Keep every scientific number and limitation from the input. Do not invent evidence, citations, experiments, or stronger conclusions. The deck must make the decision request clear: whether a larger replicated study is justified.

Release-acceptance declaration:

```text
RUNBOOK_READ = YES
CUMULATIVE_ACCEPTANCE_CONTRACT_READ = YES
RENDERED_ARTIFACT_CONTRACT_READ = YES
TASK_CLASSIFICATION = NEW_SMALL
CRITIC_REQUIRED = NO
INTERNAL_COMPONENT_PROOF_REQUIRED = NO
INTERNAL_HIGH_RISK_PAGE_PROOF_REQUIRED = NO
GPT_WORK_REQUIRED = NO
DELIVERABLE_FORMAT = CUHK_BEAMER_TEX_PLUS_PDF
AUDIENCE = research group and principal investigator
PURPOSE = decide whether to run a larger replicated study
EXACT_BASELINE = none; new public-safe deck
SOURCE_SET = supplied public-safe source notes only
HISTORY_SCOPE = no prior deck; current production regression bank applies
CURRENT_FREEZE_LEVEL = F0 through F3 declared in the task
ACTIVE_GLOBAL_GUARDS = no invented evidence; readable scientific objects; no cards-as-content; evidence adjacent to interpretation; complete artifact identity
RENDER_PENDING_GUARDS = every page requires exact-render review
LOCKED_PAGEIDS = none
LOCKED_COMPONENTS = canonical CUHK shell
POSITIVE_VISUAL_ANCESTRY_READY = YES; canonical CUHK shell and candidate production layouts
IN_SCOPE_PAGEIDS = P01 through P05
IN_SCOPE_COMPONENTS = canonical title/header/footer/body/table/closing components
ROUND_ALLOWLIST = one initial candidate and at most one source-faithful repair after independent findings
USER_IS_FIRST_QA = NO
```

Use these frozen page jobs:

1. P01 — title and decision context.
2. P02 — study design and evidence boundary.
3. P03 — quantitative comparison with a readable table or plot.
4. P04 — failure case, uncertainty, and interpretation limits.
5. P05 — next discriminating experiment and explicit decision request.

Write every output under the provided output directory. If a required renderer/resource is unavailable, stop truthfully with an exact dependency report; do not substitute an unreviewed format.
