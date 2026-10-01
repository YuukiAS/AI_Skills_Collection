# AI Research Stack Project Instructions — Independent Review Package v0.1

Date: 2026-10-01  
Status: READY_FOR_INDEPENDENT_CRITIC_REVIEW  
Tracking: #93  
Architecture authority: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_V4_1_PLANNER_PROPOSAL_2026-10-01.md`  
Architecture Critic PASS: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_V4_1_CRITIC_REVIEW_2026-10-01.md`

## Review object

Candidate Project instructions:

`docs/design/project-instructions-editor/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_CANDIDATE_V0_1_2026-10-01.md`

Planner semantic-preservation audit:

`docs/design/project-instructions-editor/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_SEMANTIC_PRESERVATION_V0_1_2026-10-01.md`

Governance baseline:

`docs/skill-todos/project-instructions-editor.md` → “Reference B — revised AI Research Stack Project instructions”

Design history:

`docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_READABILITY_DESIGN_HISTORY_2026-10-01.md`

## Candidate size

The candidate Project-instruction body is 7,010 Unicode code points / characters and 134 lines.

The earlier real Project-instruction work used an approximately 8,000-character practical budget, so this candidate retains roughly 990 characters of headroom relative to that empirical limit. This is a planning check, not a claim about a universal/current product limit.

## Planner gate result

```text
STRUCTURAL_PRESERVATION=PASS
ROLE_BOUNDARIES=PASS
TRIGGER_ESCALATION=PASS
PERMISSION_AUTHORIZATION=PASS
SAFETY_EVIDENCE=PASS
BRIDGE_HANDOFF=PASS
CAPABILITY_GATE=PASS
RELEASE_RESOURCE=PASS
RESEARCH_INTEGRITY=PASS
EXACT_IDENTIFIER_PRESERVATION=PASS
FINAL_REWRITE_SEMANTIC_INVARIANT=PASS

PLANNER_SEMANTIC_PRESERVATION=PASS
READY_FOR_INDEPENDENT_CRITIC_REVIEW=YES
READY_FOR_REAL_PROJECT_REGRESSION=NO
READY_FOR_SKILL_IMPLEMENTATION=NO
```

## Independent Critic scope

The next Critic should verify:

1. Sections 1–18 preserve governance semantics rather than merely sounding similar.
2. Section 0's final user-reading rewrite preserves conclusion strength, conditions, authorization/safety state, evidence strength, uncertainty, and scope.
3. Exact identifiers remain exact while ordinary English is normalized only when safe.
4. The candidate has not silently redesigned Planner–Critic, Bridge / Reviewed Handoff, Capability Gate, release/deployment, resource/cost, or research-integrity rules.
5. If PASS, the candidate may be applied to the real AI Research Stack Project for Cases A–E. PASS does not authorize standalone Skill implementation.

## Explicit non-goals

This package does not create or authorize:

- a `project-instructions-editor` Skill directory;
- `SKILL.md`;
- `agents/openai.yaml`;
- trigger evals;
- Plugin wrapper;
- README standalone card;
- VERSION / registry / catalog / Marketplace / profile / release changes;
- publication or installation.
