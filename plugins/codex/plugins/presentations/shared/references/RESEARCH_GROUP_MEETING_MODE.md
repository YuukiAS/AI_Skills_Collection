# Research Group Meeting Mode

Use `metadata.mode: research-group-meeting` for PhD group meetings, supervisor discussions, research progress updates, and short decision-oriented lab reports.

This mode starts from research state, not layout. Build these fields internally before writing slide text:

| Field | Planning meaning |
|---|---|
| `previous_question` | The real scientific question left from the previous discussion. |
| `prior_belief` | What explanation or route was more plausible before the new evidence. |
| `new_evidence` | New figures, images, plots, equations, logs, failures, or experiments. |
| `evidence_quality` | Scale, replication, center/site coverage, power, provenance, and caveats. |
| `belief_update` | How the new evidence changes the prior belief. |
| `successes` | What mechanism, result, or workflow is now supported. |
| `failures` | What experiment, model, assumption, or implementation failed. |
| `largest_uncertainty` | The highest-value unknown to reduce next. |
| `frozen_items` | Settings or claims that now have enough evidence to stop revisiting. |
| `stop_items` | Routes whose information value is now lower than continued cost. |
| `next_discriminating_experiment` | The next experiment that can distinguish the leading explanations. |
| `decision_needed` | The concrete supervisor decision needed today. |

Do not paste this table onto slides. Translate it into scientific pages such as result, hard case, negative result, experiment design, or supervisor decision.

## Evidence Board

Before creating a slide plan, inventory evidence in these categories:

- `available_figures`
- `medical_images`
- `qualitative_examples`
- `quantitative_plots`
- `model_diagrams`
- `equations`
- `experiment_logs`
- `failed_experiments`
- `literature_figures_to_redraw`
- `missing_evidence`

Each item should include an id, source path or URL, provenance, rights/privacy note, and the claim or question it can support. If a claim lacks evidence, do not fill the slide with icons, rounded cards, slogans, or an empty table. Use a missing-evidence note, convert it to `NEXT_EXPERIMENT`, move it to speaker notes, or delete the slide.

## Planning Sequence

```text
research state
-> scientific question or claim
-> required evidence
-> page archetype
-> scientific-object composition
-> editable file generation
-> rendered scientific QA
```

Common group-meeting rhythm:

```text
previous question -> new evidence -> result or failure -> interpretation -> uncertainty -> next experiment -> decision
```

This is not a fixed slide-count template. Delete any step without real content.

## Beamer Fallback

If the user has an urgent real group meeting and editable PPTX `research-group-meeting` output has not passed regression in the current environment, use mature Beamer or the user's existing template first. Plugin experimentation must not block real research delivery.
