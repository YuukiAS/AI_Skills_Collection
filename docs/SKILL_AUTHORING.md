# Skill Authoring

Author skills in this central repository first. Install them later with `scripts/skills.py install`.

## Create A Skill

```bash
python3 scripts/skills.py new --scope domain --domain bayesian --name mcmc-diagnostics --description "Diagnose MCMC sampling pathologies and report Bayesian fit quality."
```

This creates `skills/domains/bayesian/mcmc-diagnostics/` with `SKILL.md`, optional `references/`, and trigger eval scaffold.

## What Belongs Where

- `SKILL.md`: trigger boundary, workflow, default tools, traps, validation, and when to read references/scripts.
- `references/`: long-lived domain knowledge, dated source notes, checklists, formulas, terminology, evidence rules, migration notes, and legacy long-form content.
- `scripts/`: deterministic utilities the agent should run instead of rewriting.
- `assets/`: output resources or templates.
- `evals/trigger_queries.json`: positive, negative, and near-miss trigger examples.
- `docs/`: user-facing repository documentation and generated catalogs.
- `profiles/`: curated cross-domain install sets.
- `skills/archive/` or `status: archived`: obsolete or provider-specific skills that should not be active by default.

## Directory Scheme

- `skills/domains/`: installable complete domains. Subdirectories are allowed for browsing, but `--domain <name>` must still install the whole domain.
- `skills/tools/`: reusable tool families.
- `skills/writing/core/`: globally useful writing guardrails and prose polishers.
- `skills/writing/research/`: manuscript, citation, venue, OCR, and peer-review workflows.
- `skills/science/`: research discovery, communication, and ideation workflows.
- `skills/projects/`: project-specific skills.
- `skills/core/`: repository maintenance and system skills.
- `skills/archive/`: inactive external/plugin material.

## Description Guidance

Descriptions are the trigger surface. Keep them specific and under the official 1024 character limit; this repo warns above 350 characters. Include when to use the skill, not encyclopedia background. Avoid descriptions that overlap heavily with neighboring skills.

## Domain Knowledge

Do not delete valuable long knowledge just to shrink a skill. Move it into `references/` and link to it from `SKILL.md` with clear conditions.

For high-risk domains such as medicine, finance, legal, and system operations, source notes must include source dates, applicability, and boundaries. Do not treat stale model memory as current fact.

## Profiles Vs Domains

Domains are complete collections. Profiles are curated selections. Single skills are exact installs. Do not make a profile just to represent a full domain; use `--domain`.

## Validation

```bash
python3 scripts/skills.py validate
python3 scripts/skills.py audit --domain bayesian
python3 scripts/skills.py registry --write
python3 scripts/skills.py catalog --write
```
