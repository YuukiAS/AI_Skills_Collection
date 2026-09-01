# bioinformatics — Long-Term TODO

Canonical maintenance inbox for the `bioinformatics` plugin.

## Open candidates

### Curriculum-driven capability refinement

status: BLOCKED_NEEDS_EVIDENCE
source: user-approved design direction, 2026-09-01
proposal: Expand capabilities primarily through official workflow documentation, mature repositories, benchmark/best-practice papers, reference-database guidance, and selected textbooks. Public posts and WeChat articles may discover useful candidates but are not integration truth; trace them to authoritative sources before adoption. See `docs/workflows/CURRICULUM_DRIVEN_DOMAIN_PLUGIN_REFINEMENT.md`.
review requirement: use real data formats/workflow boundaries where practical and verify reference/database provenance, tool-version assumptions, sample structure, and reproducibility.
promotion gate: prefer integrating or adapting mature ecosystem workflows over creating lower-quality local substitutes; synthetic fixtures may protect regression but cannot prove production readiness alone.

No production change is currently frozen from this candidate.

Record real bioinformatics workflow failures here after checking database/reference provenance, real data formats, reproducibility and whether the issue is actually owned by statistical modeling or external platform tooling.

## Watch boundaries

- Tool/database-specific facts should not become permanent active rules without version/provenance handling.
- Project-local biological assumptions remain in the project repo.
- Repeated workflow/data-format failures may be promoted with real fixtures and reference provenance.
