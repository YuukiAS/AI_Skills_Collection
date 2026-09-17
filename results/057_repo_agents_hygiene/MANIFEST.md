# 057 Manifest

Status: `EXECUTED_UNAUDITED`

AI_SKILLS_RESULT_COMMIT=`519c7da37979c8aa23aa98069c146b5cea1dd81c`

BRIDGE_CANDIDATE_COMMIT=`a5c4fe61dc9ab0e228822e854ace5c7e50a4d967`
BRIDGE_VERSION=`0.8.3`

BOBBIO_CANDIDATE_COMMIT=`dd977705a2cdfecaa2d4e09127ab4464ae898b32`
LUCERNA_CANDIDATE_COMMIT=`41cd1297af6901531d3135593bc9806bffc38829`
MICA_CANDIDATE_COMMIT=`7afb2277cd1001204e77e4987d9fcaa447e7c675`
ASTERIA_CANDIDATE_COMMIT=`b34f6c5d27dd9ac7b1193826ac878fca4a953fb5`
SEMINARARC_CANDIDATE_COMMIT=`c3fc5a64a3abaec7860808fbcb4082b95d2a0302`
CUHK_DATE_INSPECTED_REF=`711fab75f044b7ad31e5ff8610c076f902ccc949`

## Evidence Locators

- H1 semantic preservation: `results/057_repo_agents_hygiene/SEMANTIC_PRESERVATION.md`
- H2 no internal contradiction: `results/057_repo_agents_hygiene/RESULT.md`
- H3 discoverability: `results/057_repo_agents_hygiene/RESULT.md`
- H4 managed-block integrity: `results/057_repo_agents_hygiene/RESULT.md`
- H5 context quality: `results/057_repo_agents_hygiene/SIZE_REPORT.md`
- H6 repo-specific regression protections: `results/057_repo_agents_hygiene/RESULT.md`
- H7 fresh Bridge normal entry: `results/057_repo_agents_hygiene/RESULT.md`
- H8 existing-root preservation: `results/057_repo_agents_hygiene/RESULT.md`
- H9 no Lite/versioning duplication in root: `results/057_repo_agents_hygiene/RESULT.md`

## Verification Summary

- Bridge targeted tests: `python -m unittest tests.test_bridge_cli_router`
- Bridge full tests: `python -m unittest discover -s tests`
- Bridge real fresh init/validate fixture:
  `/tmp/057_repo_agents_hygiene/h7_fresh_cli`
- Bridge real existing-root normal/force fixture:
  `/tmp/057_repo_agents_hygiene/h8_existing_project`

This manifest intentionally does not record its own containing commit SHA.
