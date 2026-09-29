# Template Routing

Use the most specific trustworthy template available.

1. Company, client, course, conference, or project template supplied by the user.
2. Repo-local project template.
3. Built-in template route selected by Stage 1 front-door routing:
   `cuhk-research` for research no-format requests, or `course-standard` for
   teaching/generic non-branded Beamer requests.
4. Plain editable deck with the same design tokens when official Presentation/Slides tooling cannot load a template.

Default routing:

- Explicit PPT, PowerPoint, `.pptx`, editable, Slides, Google Slides, or "I will edit it later" -> editable Presentation/Slides route.
- Group meeting, research update, paper talk, seminar, journal club, defense, QE/oral, method/result update, or "research slides" in the `presentation-desktop` context without a specified format -> `cuhk-research` exact CUHK Beamer route by default, producing source-editable `.tex` from `templates/cuhk/beamer/source/` plus rendered PDF.
- Tutorial, lecture, teaching, courseware, or generic classroom deck with no explicit ratio -> `course-standard` Beamer route, 4:3 by default, once canonical standard-Beamer source is available.
- Teaching with explicit 16:9 -> same `course-standard` template identity with the 16:9 variant, once canonical standard-Beamer source is available.
- Explicit "Beamer", "Overleaf", "LaTeX slides", ".tex", academic PDF, or a non-branded Beamer request without stronger context -> `course-standard` `.tex` plus PDF unless a project/venue locked template is supplied; do not invent a task-local canonical source.
- Business, operations, marketing, product, strategy, client, or executive decision decks -> editable `.pptx` through official Presentation/Slides or ChatGPT for PowerPoint unless the user asks for another format.
- Existing PPTX/Google Slides/local minor edit -> official Presentation/Slides only; preserve current format/template/ratio.
- External locked template -> pass-through locked input; do not add it to the built-in template set.
- Plan-only/storyline-only -> plan/notes only; do not claim a generated artifact.

When a request explicitly asks for plan/storyline only and no generated deck,
the plan-only route takes precedence even if the prompt also mentions an
existing deck or an external locked template.

Do not route explicitly requested editable PPTX/Slides work to Beamer only because the content is academic. Do not use `python-pptx`, python-ppt, rendered PDF pages, or whole-slide images to fake an editable PPTX when official Presentation/Slides should create editable objects.

CUHK exact mode:

- Use `templates/cuhk/beamer/source/` as the canonical template source.
- The first/title slide layout must match the CUHK template. Only metadata/content fields such as title, subtitle, author, institute, date, and similar text placeholders may change.
- Do not use `templates/cuhk/design-tokens.json`, `templates/cuhk/beamer/main.tex`, `templates/cuhk/pptx/build_reference_deck.py`, or `templates/cuhk/pptx/cuhk-reference-deck.pptx` for exact CUHK reproduction; those files are derived convenience scaffolds for non-exact/test workflows.

Course-standard mode:

- Stage 1 may route to the `course-standard` identity, but canonical template
  source consumption is currently waiting on the independent standard-Beamer
  task: `WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE`.
- Do not treat task-local temporary course-standard files as canonical source.
  After that task provides an exact source path and candidate commit, Planner
  must confirm how this Stage 1 task consumes it.
- Default/reference ratio is 4:3.
- Explicit 16:9 is the same `course-standard` identity, not a third built-in template.
- Stage 1 owns only template-level opening/navigation/bookmark/footline/closing primitives; semantic closing choice remains deferred.
- Machine-local TeX/font/resource discovery belongs to `render-chinese-math-pdf`, not this routing layer.
