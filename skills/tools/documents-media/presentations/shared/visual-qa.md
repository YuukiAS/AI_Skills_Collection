# Visual QA

Render the deck before delivery.

- Export PPTX/Slides to PDF or slide images.
- Inspect title message, section navigation, page numbers, figures, equations, text wrapping, clipping, overflow, contrast, alignment, visual hierarchy, slide density, and narrative continuity.
- Check that the deck is editable when `.pptx` was requested.
- Confirm every figure, table, screenshot, or image supports the slide's main message; decorative visuals do not satisfy QA.
- Do not use PDF page images or whole-slide images as slide backgrounds unless explicitly delivering image/PDF slides.
- Re-render changed slides after fixes.
- Mark the deck `complete` only after render/visual QA passes; file existence alone is not completion.

## Scientific Slide QA

For `research-group-meeting` decks, mechanical checks are necessary but not sufficient. Inspect rendered slide images page by page and answer:

- Does this page contain a real scientific object?
- What evidence supports the page?
- Does the visual object encode data, mechanism, experimental unit, medical case, formula, comparison, or uncertainty?
- Can the main question or result be understood in 5-10 seconds?
- Are figures, axes, legends, case labels, and formulas readable at presentation distance?
- Does the page look like a management-consulting page, report page, or card dashboard?
- If decorative frames are removed, is any scientific content left?
- Is this page worth discussing for 30-90 seconds in a group meeting?
- Is the evidence boundary clear enough that missing, synthetic, preliminary, or validation-subset evidence cannot be mistaken for completed scientific proof?

If a page fails these questions, do not mark it `PASS` only because it has no overflow, no overlap, editable objects, or a visible shape.

An independent scientific visual reviewer must output `PASS`, `REVISE`, or `BLOCKED` per page. The reviewer checks ten criteria: real scientific object, real evidence or generated dataset, relationship correctness, archetype match, no fake visual, no consulting/card/dashboard substitute, main figure readability, formula/label readability, worth 30-90 seconds, and evidence boundary clarity.

For editable PPTX regression, rendered PNGs must be produced from the PPTX by a real presentation engine. If `soffice`, `libreoffice`, or an explicitly configured renderer is unavailable, the correct status is `BLOCKED_REAL_PPTX_RENDER`. A separately hand-built PDF is not evidence that the PPTX rendered correctly.

## Evidence Versus Concept QA

If the slide contract requires real plot, image, table, data, case, metric, or source evidence, fail substitutes such as fabricated proxy plots, decorative concept art, invented toy examples, or unlabeled schematic stand-ins. Conceptual illustrations may help define a model or term, but they must be labeled as conceptual and cannot close a real-evidence requirement. When real data are available for a newly introduced concept, check whether the slide gives a short audited example and states any availability boundary.

## Diagram Semantic QA

For diagram pages, first decide whether a diagram is needed at all. A valid diagram must encode a real scientific relationship, mechanism, computation, experimental path, or dependency. Boxes, bubbles, or cards that only contain prose are not scientific diagrams. Connectors must be real structural connectors with semantic anchors and a consistent lane/sequence direction; typed arrow characters, random diagonals, connector lines that imply the wrong relation, and arrows used for containment are QA failures.

## Rendered Scientific Object QA

For existing research-deck revisions, the final rendered scientific-object QA
batch must inspect the reviewer-seen baseline and the revised render. Cover node
width and awkward wrapping, connector endpoint clearance, arrow readability,
local crowding together with unused space, figure-internal axis/tick/legend/title
and annotation readability, caption/panel pairing, and the source/footer safe zone
defined by the active template. These are completion gates for the rendered
artifact, not prose reminders.

## Revision Scope QA

For targeted revision, compare the new render with the specific version that received feedback. The cited issue becomes a regression constraint, but accepted slides/components should remain stable unless the fix directly depends on changing them. A repair that deletes accepted content, reintroduces a rejected design, or changes unrelated page structure without evidence should be marked `REVISE` for scope creep.

## Research Anti-Pattern Gate

Fail or revise pages that use these patterns to replace missing evidence:

- title plus slogan plus giant empty table;
- rounded-card dashboard;
- consulting language;
- generic arrows without scientific objects;
- fake visualization;
- paragraph pasted onto slide;
- unreadably shrunk paper figure;
- same layout on every slide despite different scientific objects;
- decorative icons replacing evidence;
- vague next steps;
- internal planning language leaking onto slide;
- evidence-free roadmap.

When evidence is missing, the acceptable outcomes are missing-evidence page, `NEXT_EXPERIMENT`, speaker note, backup, or deletion.
