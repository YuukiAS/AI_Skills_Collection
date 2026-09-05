# 050 follow-up scope: what to import from the Distributed Imaging advisor-report rewrite

Status: source-of-truth repair note for task `050_writing_style_host_codex_runtime`.

This note records the bounded lessons from the successful Distributed Imaging advisor-facing report v2 that belong in the current `writing-style` repair, and the lessons that must remain owned by `research-writing`. It does not revise `PLAN.md`, create a new workflow state, or rename the plugin.

## Why this belongs before STYLE_ACCEPT

Round 4 is still rejected on language quality. The remaining failures are not limited to one private document: the Distributed Imaging report independently reproduced the same generic language problem and showed a better reader-facing solution.

The useful evidence is therefore strong enough to refine the current language-layer acceptance contract before `STYLE_ACCEPT`.

However, only the language-level lessons should enter 050. Importing report-planning behavior would blur the newly clarified plugin boundary and make `writing-style` absorb `research-writing` responsibilities.

## Promote into 050 now: generic language-layer lessons

### 1. Explain role and purpose, not merely terminology

When an unfamiliar technical term is necessary, the reader should learn what it does in the current argument and why it matters before the term is used as shorthand.

Acronym expansion, English retention, or a parenthetical translation alone is not sufficient.

### 2. Prefer reader-facing scientific relations over compressed labels

The final prose should express the actual relation directly: what is being compared, what changed, what limits the conclusion, and why the next step follows.

Ordinary English labels must not carry the sentence skeleton merely because they are common in papers or source notes.

### 3. Plain-language conclusion -> explanation -> exact technical detail -> evidence boundary

When the source supports it, the reader should encounter the bounded scientific point first, then the intuition or concrete explanation, then exact technical detail/formula/name, then the caveat or evidence boundary.

This is a language/explanation pattern, not authorization to change scientific content.

### 4. Positive scientific statements over meta/defensive framing

Prefer stating the scientific observation and limitation directly instead of narrating internal process, status, audit posture, or rhetorical `not X but Y` machinery when that machinery adds no scientific meaning.

### 5. Readability may require local expansion

A short explanatory bridge is preferable to a compressed noun stack when the reader would otherwise have to reconstruct the relation mentally.

`reader effort` is the objective; character-count reduction is not.

### 6. Existing captions, conclusions, table cells, figure annotations, slide copy, and statistical explanations are valid consumers

The generic language layer is not only for long reports. When another domain plugin has already fixed scientific meaning and information architecture, the same language/fidelity contract should be reusable for reader-facing captions, labels, conclusions, limitations, slide text, and result interpretation.

The language layer may improve expression and local explanation but must not alter domain semantics, comparison definitions, uncertainty, scientific claims, or visual/statistical encodings.

## Do NOT import into 050: research-writing responsibilities

The following successful Distributed Imaging v2 behaviors are important, but they do not belong in the current `writing-style` repair:

- choosing which experiments are decisive enough for the main narrative;
- deciding that secondary experiments belong in an appendix;
- deciding document-level section order for a newly authored advisor report;
- deciding report-level main-body vs appendix boundaries;
- designing rows/columns, comparison axes, units, precision, missing-value notation, and scientific comparability of large result tables;
- replacing internal project nicknames based on advisor/project context when doing so requires domain/project knowledge;
- deciding what scientific question or advisor decision a new report should foreground.

These belong to `research-writing` / `research-reporting`, which should later hand stable prose jobs to the generic language layer.

## Round-4 defect this repair must address

Round-4 public evidence shows that the terminal Chinese pass can classify a very large fraction of visible Latin-script occurrences as `useful_recognition` and still make zero textual change (`pre_chinese_candidate_sha256 == final_candidate_sha256`). This is not sufficient evidence of a real Chinese-first pass when the human reviewer still sees ordinary English reasoning such as `baseline discussion`, `anchor`, `exact estimand`, `resource contract`, or similar constructs.

The repair must close this generic escape route without using a banned-word list.

Required direction:

- `useful_recognition` is a narrow first-use recognition class, not a permanent license to retain convenient English;
- repeated non-identity English requires stronger justification than first use;
- a retained English technical identifier must be locally paired with natural Chinese meaning/context;
- ordinary reasoning relations must be expressed in Chinese in the final candidate;
- a Chinese pass that leaves the pre/post candidate unchanged is acceptable only when the classification evidence genuinely supports that no reader-facing repair is needed;
- human rejection overrides a mechanically valid classification receipt.

## Structural boundary for 050

Do not turn this repair into a new report planner.

For an existing source-faithful heavy rewrite, `writing-style` may regroup existing propositions by reader question when necessary to explain them clearly, but it may not silently drop experiments or redesign the project narrative the way `research-writing` may when authoring a new advisor report from repo evidence.

## Acceptance intent

The next A/B/C replay should show that a technically trained reader can read the Chinese directly without mentally translating ordinary English scaffolding, while all scientific content, formulas, exact identities, evidence boundaries, uncertainty, and conclusion strength remain intact.

If this bounded repair plus clean isolated production replay still fails human style review, return to Planner with the real artifacts and stage evidence. Do not add another project-specific phrase layer.
