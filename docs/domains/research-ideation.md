# research-ideation

Active skills: 6

## Install

Complete domain install:

```bash
python3 scripts/skills.py install --target repo --domain research-ideation --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
python3 scripts/skills.py install --target repo --skill consciousness-council --skill hypogenic --skill hypothesis-generation --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `consciousness-council` (`skills/research/ideation/consciousness-council`): Run a multi-perspective Mind Council deliberation on any question, decision, or creative challenge. Also trigger when the user faces a dilemma, trade-off, or complex choice with no obvious answer.
- `hypogenic` (`skills/research/ideation/hypogenic`): Automated LLM-driven hypothesis generation and testing on tabular datasets. Use when you want to systematically explore hypotheses about patterns in empirical data (e.g., deception detection, content analysis).
- `hypothesis-generation` (`skills/research/ideation/hypothesis-generation`): Structured hypothesis formulation from observations. Use when you have experimental observations or data and need to formulate testable hypotheses with predictions, propose mechanisms, and design experiments to test them.
- `scientific-brainstorming` (`skills/research/ideation/scientific-brainstorming`): Creative research ideation and exploration. Use for open-ended brainstorming sessions, exploring interdisciplinary connections, challenging assumptions, or identifying research gaps.
- `scientific-critical-thinking` (`skills/research/ideation/scientific-critical-thinking`): Evaluate scientific claims and evidence quality. Use for assessing experimental design validity, identifying biases and confounders, applying evidence grading frameworks (GRADE, Cochrane Risk of Bias), or teaching critical analysis. Best for understanding evidence quality, identifying flaws. For formal peer review writing use peer-review.
- `what-if-oracle` (`skills/research/ideation/what-if-oracle`): Run structured What-If scenario analysis with multi-branch possibility exploration. Also trigger when the user faces a fork-in-the-road decision, wants to stress-test an idea, or needs to think through consequences before committing.

## Main References

- No domain references discovered yet. Add `references/source-notes.md`, checklists, or overview notes when the skill carries long-lived domain knowledge.
