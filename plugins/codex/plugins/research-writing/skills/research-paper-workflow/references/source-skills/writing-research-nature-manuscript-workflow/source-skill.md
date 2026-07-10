---
name: nature-manuscript-workflow
description: Plan, draft, revise, and audit Nature-style manuscripts, including claim framing, figure logic, data availability, submission readiness, and reviewer response. Use when the user targets Nature-family journals or asks for Nature-style scientific writing.
status: active
provenance: external-adapted
source_repo_url: https://github.com/Boom5426/Nature-Paper-Skills
source_path: .
source_ref: 44cff42ac22a5ac4dcfb7ba01b2e81c21d689ea6
source_imported_at: 2026-07-09
source_license: MIT
source_note: Distilled from Nature-Paper-Skills, nature-skills, and claude-scholar Nature writing/response/data skills.
trusted: false
requires_network: true
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-09
profile_tags:
  - research-writing
  - nature
recommended_scope: project
metadata:
  skill-author: AI Skills Collection maintainers with recorded upstream sources
---
# Nature Manuscript Workflow

Use this for Nature-family manuscript strategy. It complements general `scientific-writing`; it does not replace venue-specific author instructions.

## Workflow

1. Identify the Nature-family target, article type, field, current manuscript state, and submission deadline.
2. Build the claim map:
   - headline claim;
   - significance beyond technical performance;
   - main figures and their panel-level claims;
   - methods/results needed to support the scope of the claim.
3. Audit Nature-specific risks:
   - overclaiming relative to evidence;
   - figure panels that are descriptive but not argumentative;
   - missing source data or code availability;
   - vague data availability statements;
   - terminology drift between title, abstract, results, figures, and discussion.
4. Draft or revise in this order: title/abstract framing, figure logic, results narrative, discussion boundaries, methods/data availability, cover or rebuttal text.
5. Before delivery, list unresolved policy or evidence checks that require the journal's current instructions.

## Data Availability

Treat data availability as a submission artifact, not boilerplate. Include repository, accession, restricted-access reason, code availability, source-data coverage, and timing. If a dataset cannot be shared, name the restriction and access mechanism.

## Reviewer Response

For reviewer comments, classify each point as evidence request, clarity request, scope challenge, method challenge, or policy/format issue. Draft response text only after mapping the manuscript edit that answers the comment.

## Boundaries

- Do not promise Nature compliance without checking current journal instructions.
- Do not imitate a journal voice by adding hype.
- Preserve scientific uncertainty and limitations.
