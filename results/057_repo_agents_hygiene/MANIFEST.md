# 057 Manifest

Status: `EXECUTED_UNAUDITED`

AI_SKILLS_RESULT_COMMIT=`745281b70322b8508e43e59a5bdef70529749ea5`

BRIDGE_CANDIDATE_COMMIT=`e1d6b781ad7e56d567bed419001069baf439d0a5`
BRIDGE_VERSION=`0.8.3`

BOBBIO_CANDIDATE_COMMIT=`ab5dccb6b8b87c49671aa097233ce1bcc38be004`
LUCERNA_CANDIDATE_COMMIT=`41cd1297af6901531d3135593bc9806bffc38829`
MICA_CANDIDATE_COMMIT=`e49416f874f633aedc7521734ee5b0f441aae970`
ASTERIA_CANDIDATE_COMMIT=`0ce1d4daca1e410ce551570578dd563d4ef67e90`
SEMINARARC_CANDIDATE_COMMIT=`74caaa4ecec16f1bc90987979458d1a4e93f52be`
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
- Bridge real CLI normal/force byte-preservation smoke on a CRLF/trailing-space
  existing-root fixture.
- Product-repository `git diff --check` and cached-diff inspection before commit.

This manifest intentionally does not record its own containing commit SHA.
