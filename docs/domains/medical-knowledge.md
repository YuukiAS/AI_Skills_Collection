# medical-knowledge

Active skills: 9

## Install

Complete domain install:

```bash
ai-skills install --target repo --domain medicine-clinical --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
ai-skills install --target repo --skill domain/medicine-clinical/clinical-decision-support --skill domain/medicine-clinical/clinical-guideline-checking --skill domain/medicine-clinical/clinical-reports --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `clinical-decision-support` (`skills/domains/medicine-clinical/clinical-decision-support`): Produce group-level clinical decision support, cohort evidence summaries, biomarker-stratified analyses, and guideline-style recommendation documents. Use for research, pharmaceutical, or policy documents, not bedside individual care.
- `clinical-guideline-checking` (`skills/domains/medicine-clinical/clinical-guideline-checking`): Check clinical guideline claims against current authoritative sources, jurisdictions, population boundaries, recommendation strength, and update dates before using them in medical documents.
- `clinical-reports` (`skills/domains/medicine-clinical/clinical-reports`): Draft clinical case reports, diagnostic summaries, trial reports, SOAP/H&P/discharge-style documentation, and de-identified medical report templates with privacy, source, and guideline checks.
- `medical-literature-evidence-review` (`skills/domains/medicine-clinical/medical-literature-evidence-review`): Review medical literature evidence with dated source notes, evidence hierarchy, population applicability, uncertainty, and safety boundaries. Use for medical evidence summaries, not direct care advice.
- `medical-safety-boundaries` (`skills/domains/medicine-clinical/medical-safety-boundaries`): Apply safety boundaries for medical tasks: no autonomous diagnosis or prescribing, current-source verification, privacy checks, missing-data caveats, emergency escalation, and clinician-review language.
- `neurokit2` (`skills/domains/medicine-clinical/neurokit2`): Comprehensive biosignal processing toolkit for analyzing physiological data including ECG, EEG, EDA, RSP, PPG, EMG, and EOG signals.
- `pyhealth` (`skills/domains/medicine-clinical/pyhealth`): Comprehensive healthcare AI toolkit for developing, testing, and deploying machine learning models with clinical data.
- `scikit-survival` (`skills/domains/medicine-clinical/scikit-survival`): Comprehensive toolkit for survival analysis and time-to-event modeling in Python using scikit-survival.
- `treatment-plans` (`skills/domains/medicine-clinical/treatment-plans`): Draft concise, clinician-reviewed treatment plan documents with goals, interventions, monitoring, and follow-up. Use only as documentation support with current-source verification, not as autonomous medical advice.

## Main References

- `skills\domains\medicine-clinical\clinical-decision-support\references\evidence-checklist.md`
- `skills\domains\medicine-clinical\clinical-decision-support\references\legacy-full-skill.md`
- `skills\domains\medicine-clinical\clinical-decision-support\references\source-notes.md`
- `skills\domains\medicine-clinical\clinical-guideline-checking\references\guideline-checklist.md`
- `skills\domains\medicine-clinical\clinical-reports\references\clinical-report-checklist.md`
- `skills\domains\medicine-clinical\clinical-reports\references\legacy-full-skill.md`
- `skills\domains\medicine-clinical\clinical-reports\references\source-notes.md`
- `skills\domains\medicine-clinical\medical-literature-evidence-review\references\evidence-table-template.md`
- `skills\domains\medicine-clinical\medical-literature-evidence-review\references\source-notes.md`
- `skills\domains\medicine-clinical\medical-safety-boundaries\references\safety-checklist.md`
- `skills\domains\medicine-clinical\neurokit2\references\source-notes.md`
- `skills\domains\medicine-clinical\pyhealth\references\source-notes.md`
- `skills\domains\medicine-clinical\scikit-survival\references\source-notes.md`
- `skills\domains\medicine-clinical\treatment-plans\references\legacy-full-skill.md`
- `skills\domains\medicine-clinical\treatment-plans\references\source-notes.md`
- `skills\domains\medicine-clinical\treatment-plans\references\treatment-plan-checklist.md`

Alias for registry domain `medicine-clinical`.
