# Presentations — STAT5060 V05 annotation and layout follow-up

Date: 2026-10-05
Status: TODO / real-use evidence
Source artifact: `tutorial-01/student-deck V04`, instructor-annotated PDF, 37 pages

## 1. Evidence summary

The annotated PDF contains exactly 47 Highlight objects:

- Yellow: 36 — deck/course-specific repairs;
- Orange: 11 — reusable presentation-system failures;
- Green: 0.

Orange issues cover:

- footer regression;
- Question-rule geometry;
- column-versus-vertical choice;
- false structure from `What changes / What stays the same` columns;
- excessive visible gutter between columns;
- meaningless boxes and broken/short arrows;
- peer formula baseline alignment;
- equal arrow length and row fill;
- punctuation/fragment labels;
- caption text being used as main explanation;
- semantic groups separated to satisfy whitespace thresholds.

## 2. Arrow/connector contract

Presentations needs a shared connector primitive and a release gate.

- Connect from source-node boundary to target-node boundary.
- Do not start/end inside a node.
- Do not overlay node text, formula, label, border or another connector.
- Avoid arbitrary positive `shorten >=` / `shorten <=` that makes an arrow look detached.
- Visible shaft at 1920×1080 should be at least about 36 px (approximately 8 mm on a 16:9 Beamer slide); 8–10 mm or longer is preferred for peer nodes.
- Connectors in one peer row use equal visible lengths unless asymmetry is semantically meaningful.
- Relation labels need at least 0.34 cm clearance from the shaft.
- If the available space cannot support the minimum shaft without shrinking text/nodes or causing collision, use a numbered vertical sequence rather than a tiny arrow.

QA must inspect rendered shaft length and collisions, not only TikZ/source styles.

## 3. Column-versus-vertical decision gate

Use columns only for genuinely peer-level objects that should be compared simultaneously and can share corresponding anchors.

Use vertical layout when:

- one object precedes or causes the next;
- later content depends on earlier content;
- one formula/denominator governs the whole explanation;
- one column is mostly a label while the other contains the explanation;
- the visible gutter becomes a large meaningless gap;
- peer alignment cannot be maintained.

CAT-TRACE evidence remains useful:

- peer catalogue/open-tail components can be columns;
- learn → prior → update was correctly changed from three columns to a vertical sequence;
- dataset Question blocks work better full-width than squeezed into side columns.

Final multi-column QA must record:

- semantic reason for columns;
- top/formula/code/table anchor deltas;
- actual nearest-object gutter, not only declared column separation;
- lower-edge balance;
- responsive fallback if one column becomes cramped.

## 4. Semantic proximity must complement whitespace QA

Bottom-gap metrics can be gamed by moving a conclusion to the bottom and separating it from the table/figure it interprets.

Add a semantic-proximity gate:

- define semantic groups before layout;
- measure evidence→interpretation gap;
- conclusion interpreting a figure/table normally begins within 0.35–0.75 cm of that object;
- no conclusion is moved to the bottom solely to satisfy a whitespace threshold;
- intra-group gap should not exceed the nearest inter-group gap;
- `vfill` is allowed only between independently meaningful groups.

A page can fail semantic proximity even when bottom-gap metrics pass.

## 5. Footer regression must be a shared-core test

Course-standard and CUHK should consume the same footer core. Only colour/branding/left identity should differ.

Final footer QA requires:

- left credit and page-counter text baseline;
- native action-button optical centre;
- horizontal gap between final action group and page counter;
- exact approved action set;
- page denominator;
- representative crops from title, code, figure, Bayesian and closing pages;
- whole-page inspection.

Do not accept a prior footer PASS after any theme/font/page-count change without rerunning footer regression.

## 6. Question primitive geometry

The Question vertical rule must bind to the rendered label+question text box.

- starts at the first line top;
- ends at the final line bottom;
- <=1 px optical overshoot at release scale;
- does not enter title/next object;
- question body remains readable and full-width when needed.

This is a geometry gate, not merely a macro-presence check.

## 7. Package/code slides require runnable-context QA

A slide with package names or incomplete fragments does not satisfy software teaching.

Required for code/reference slides:

- imports and data objects introduced before use;
- complete model call for the task;
- extraction/diagnostic/predictive call shown where needed;
- package-specific parameterisation differences explained;
- shared backend disclosed honestly;
- code copied from final PDF retains ASCII quotes/operators/underscores;
- syntax parse/smoke test;
- one page job and visible output/interpretation.

A final PDF with typographic smart quotes in code must fail even if source TeX is correct.

## 8. Captions versus main explanation

Caption font must not carry the primary teaching claim.

- put the main statement in body text before/next to the figure;
- reserve caption for object identity or visual encoding;
- short caption centred within figure width;
- multi-line explanatory caption left-aligned within figure width;
- source credit remains in footer.

## 9. Natural slide language

Flag:

- `What changes / What stays the same` narrator blocks when two sentences suffice;
- colon/comma fragments such as `Slope estimate, replicate 1:`;
- generic `Why do we need...` titles without a concrete decision/calculation;
- software-name matrices without useful syntax;
- unexplained closing claims;
- repeated `What/How...` structures.

Rendered spoken-language review remains necessary after layout repair.

## 10. Promotion tests

Add regression fixtures for:

1. four-node flow with equal minimum shafts;
2. insufficient-width flow that must fall back to numbered vertical layout;
3. peer two-column formulas/code with baseline alignment;
4. sequential content that columns must reject;
5. semantic-proximity failure despite passing bottom gap;
6. footer after page-count/font/theme change;
7. multi-line Question rule geometry;
8. PDF code-copyability with straight quotes;
9. caption/main-explanation role separation.

Project-specific STAT5060 wording/data must not enter the plugin. Only the general layout, language, connector, code and QA contracts should be promoted.