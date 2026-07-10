---
name: skill-library-analysis
description: Analyze, deduplicate, cluster, and select skills from a large skill library or cloned upstream sources. Use when maintaining AI_Skills_Collection, comparing external skill repos, or deciding whether to merge, add, archive, or ignore skills.
status: active
provenance: adapted
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-07-09
profile_tags:
  - maintenance
  - skills
recommended_scope: project
source_url: https://github.com/davidliuk/graph-of-skills
source_commit: 69f2ab2f5e18681cb809e8e123da6b83ec50f5fc
source_license: MIT
adaptation_notes: Distilled from graph-of-skills and local provenance audit work.
metadata:
  skill-author: AI Skills Collection maintainers with recorded upstream sources
---
# Skill Library Analysis

Use this to keep a large skill collection coherent. The goal is to reduce duplicates and preserve provenance, not to maximize skill count.

## Workflow

1. Inventory candidate skills with path, name, description, provenance, license, and upstream commit.
2. Group by user task, not by repository.
3. Compare each group against existing local skills:
   - exact duplicate;
   - same trigger with stronger references;
   - complementary capability;
   - plugin-only or software-only source;
   - unclear license or provenance.
4. Choose one action:
   - merge into existing skill;
   - create one new local skill;
   - record only;
   - reject as software/non-skill;
   - defer because of conflict.
5. Record decisions in a tracked source log before deleting scratch clones.

## Quality Rules

- Do not bulk-import a repository when a distilled local skill is enough.
- Do not keep multiple active skills with the same trigger boundary.
- Do not hide conflicts; record them for user decision.
- Prefer profile and marketplace aggregation over many near-duplicate installable skills.
