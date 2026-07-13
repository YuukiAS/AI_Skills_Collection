---
name: business-presentations
description: Plan business, executive, product, operations, market, client, strategy, pitch, and decision decks. Use when the audience is non-technical or the deck asks for a decision, resource, proposal, or business update.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-13
profile_tags:
  - presentations
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Business Presentations

Use this skill for decision-oriented decks. File creation, object editing, export, and rendering should be handled by the official Presentation/Slides capability when available.

## Boundary

- Use for executive summaries, company updates, product proposals, strategy, operations, market, client, and pitch decks.
- Do not use for technical research talks unless the user explicitly frames the audience as business or executive.
- Do not trigger for small edits to an existing PPTX/Google Slides file.
- Use `../../shared/deck-plan.schema.json` as the default intermediate representation.

## Narrative

Business decks should answer:

```text
answer/request -> problem or opportunity -> evidence and impact -> plan -> resources and risks -> decision and next step
```

## Workflow

1. Clarify the decision, audience, time limit, and required output format.
2. Produce `deck-plan.yaml` for non-trivial decks.
3. Keep each slide tied to one decision-relevant message.
4. Use the CUHK default visual system only when no company, client, course, or event template is specified.
5. Route editable deck creation to official Presentation/Slides and keep visual QA evidence.

## References

- `../../shared/deck-plan.schema.json`
- `../../shared/template-routing.md`
- `../../shared/ppt-skill-routing.md`
- `../../shared/source-fidelity.md`
- `../../shared/visual-qa.md`
