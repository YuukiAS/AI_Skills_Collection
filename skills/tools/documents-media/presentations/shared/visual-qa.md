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

If a page fails these questions, do not mark it `PASS` only because it has no overflow, no overlap, editable objects, or a visible shape.

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
