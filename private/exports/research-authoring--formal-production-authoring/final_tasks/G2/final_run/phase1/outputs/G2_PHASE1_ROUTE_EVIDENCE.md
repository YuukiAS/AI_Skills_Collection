# G2 Phase 1 — Research Authoring route and evidence boundary

## Frozen document brief

- **Intent and family:** produce a new advisor-facing research update (`report`), not polish an existing report, answer a research question in chat, or reconstruct a run log.
- **Audience and purpose:** an advisor unfamiliar with execution history; explain site-conditioned measurement error, distinguish supported explanations from unresolved mechanisms, and identify the next discriminating scientific question.
- **Authority:** the four Phase 1 scope/manifest/rubric/materialization files and the six materialized raw evidence files in `inputs/`. The scope and rubric govern the task; contracts define experiments; decisions and CSV rows supply results. No external literature or prior reader-facing report is a source.
- **Claim spine:** clean CARE supplies the primary site-transfer evidence; H-ROBUST supports persistence under the reported checks; pooled-versus-local uncertainty limits a universal global-model claim; M&Ms offers a separate, less detailed supporting result; benefit from sharing followed by bounded site adaptation remains an untested question in this evidence set.
- **Section jobs:** orient the measurement question and clean design; distinguish the comparisons and their uncertainty; delimit excluded explanations; assess M&Ms separately; specify a falsifiable next question without predicting its answer.
- **Scientific objects:** one comparison table distinguishes global-model penalties from site-transfer penalties and separates decision-summary averages from seed-specific bootstrap estimates. No formula or figure is necessary.
- **Citation boundary:** short claim identifiers link to the separate claim-evidence map. Repository paths, hashes, decision tokens, and workflow evidence remain outside the advisor narrative. No bibliography is invented.
- **Edit scope and destination:** greenfield English Markdown, all deliverables under `outputs/`; no PDF requested; no accepted earlier report supplied or used.
- **Downstream route:** freeze scientific semantics and evidence map, draft through the report delegate, apply Clear Writing's English scientific-prose pass with fidelity protection, then return to Research Authoring for document-level checks.

## Route actually used

The installed candidate entry was read at:

`/users/a/e/aereinh/.codex/plugins/cache/ai-skills-candidate/research-writing/0.3/skills/report/SKILL.md`

Its coordinator-first route was followed in this order:

1. `skills/report/_src/core/source.md` — Research Authoring Core; document brief, authority, claim spine, section roles, and final QA.
2. `skills/report/_src/report/source.md` — Research Reporting delegate.
3. `skills/report/_src/report/references/group-meeting-advisor-reports.md` — advisor-facing structure and internal-detail filtering.

The candidate cache directory is an observed installation locator, not independent verification of a source commit. The rubric identifies pre-final C0 as `1c37c0715aca0096606f24e56192b7857e72bbd6`; this run did not inspect or modify plugin source to establish a separate build identity.

Fidelity support was loaded from `/users/a/e/aereinh/.codex/skills/writing-core-writing-fidelity/SKILL.md`. English scientific-prose guidance and its report checklist were also read. The installed Clear Writing pass was located at `/users/a/e/aereinh/.codex/plugins/cache/yuukias-ai-skills/writing-style/0.4/skills/sci/SKILL.md` and applied after the report's scientific content was fixed; pass details and final checks are recorded below.

## Input boundary and integrity

The complete scientific source universe used was:

| Local file | Role |
|---|---|
| `../inputs/01-PHASE1_RAW_SCOPE.md` | Task scope, audience, clean-design framing, and prohibition on withheld evidence |
| `../inputs/02-PHASE1_INPUT_MANIFEST.md` | Exact six-source allowlist and Git blob identities |
| `../inputs/03-G2_RUBRIC.md` | Frozen evaluation requirements; no scientific result authority |
| `../inputs/04-MATERIALIZED_PHASE1_INPUTS.json` | Materialized source mapping, byte counts, hashes, and source reference |
| `../inputs/05-experiment_contract.json` | CARE experiment definition |
| `../inputs/06-clean_replication_pattern_decision.json` | CARE comparison summaries |
| `../inputs/07-pattern_h_robustness_decision.json` | H-ROBUST summary |
| `../inputs/08-paired_bootstrap_ci.csv` | CARE paired estimates and intervals |
| `../inputs/09-mms_experiment_contract.json` | M&Ms experiment definition |
| `../inputs/10-mms_replication_decision.json` | M&Ms supporting decision |

For all six evidence blobs, local byte counts, SHA-256 hashes, and Git blob SHA-1 identities were recomputed and matched the materialization JSON and manifest. Their source mapping is bound to `YuukiAS/Distributed_Imaging_Inference` at `c6ed0fb40c702936ec1f41454390ef188a5b4d97` as declared by those supplied files. This verifies the supplied bytes, not the underlying experiments.

No original DII checkout, prior advisor/group-meeting report, linked result report, patient-level manifest, checkpoint, or unlisted analysis was opened. Paths embedded in the raw contract were treated as provenance strings, not invitations to retrieve additional evidence. The only additional files read were installed skill instructions and writing references; these supplied procedure, not project evidence. No web search or external research was used.

Only Phase 1 task inputs were supplied to and consumed by this authoring run. No Phase 2 personalized partial-pooling file or result was opened, queried, inferred as an observed outcome, or used for structure or wording. The scope itself permits identifying sharing followed by bounded site-specific adaptation as a next question; that permission supplies no answer. The report preserves both possible benefit and failure as unresolved.

This is an account of the supplied input set and actual reads, not a claim of operating-system-level read isolation or proof that unrelated files could not exist elsewhere on the host.

## Clear Writing handoff and return to scientific QA

The installed `writing-style/0.4/skills/sci/SKILL.md` and its `references/scientific-report-checklist.md` were applied directly to the completed English report in this authoring session. This was a local skill-guided language pass, not a separate external reviewer call. The protected content comprised all numbers, comparison directions, endpoint definitions, uncertainty statements, claim anchors, Table 1, and the open outcome of the next test.

The pass made four local wording changes:

- “The contract specifies four matched local epochs” became “The adaptation budget is specified as four matched local epochs,” keeping the scientific budget while reducing operational phrasing.
- “The strongest uncertainty-resolved comparison” became “The reported intervals most consistently support,” avoiding wording that implied uncertainty had been resolved completely.
- The sentence about absence of replication was rewritten to name the repeated CARE seeds and adaptation scopes directly.
- “These results narrow the explanation more than they identify a cause” became a direct statement that comparisons narrow explanations without identifying the cause of site differences.

A programmatic before/after check confirmed unchanged numeric tokens and C-identifiers. Research Authoring then rechecked the final prose against the claim map: observational results remain separate from interpretation; causal mechanisms and prospective adaptation benefits remain uncertain; neither the language pass nor the supporting M&Ms summary strengthens the conclusion beyond CARE's evidence.

## Final author checks and artifact identity

- Six evidence blobs: byte counts, SHA-256, and Git blob hashes matched the supplied records.
- Table 1: all decision-summary values and bootstrap seed ranges recomputed from E2/E4 and matched at four-decimal precision.
- Interval statements: six own/off-site primary lower bounds above zero; three of six pooled/local primary intervals include zero; all six pooled/local scar-volume intervals include zero, with one negative point estimate.
- Evidence coverage: C1–C11 cover every substantive report paragraph and Table 1; proposals and missing evidence are explicitly classified in the map.
- Reader relevance: scientific questions organize the report; the table distinguishes comparisons; no decorative figure, invented reference, run chronology, or job/audit/provenance identifiers enter the main narrative.
- Phase boundary: no claim predicts or reveals the outcome of personalized partial pooling. Both benefit and failure remain possible in the proposed next test.
- Markdown artifact checks: the requested three files exist; source links in the claim map resolve locally. No rendered artifact was requested or claimed.

Final content identities:

| Artifact | SHA-256 |
|---|---|
| `G2_PHASE1_ADVISOR_UPDATE.md` | `ce7914b594d9723d9563fcaf26e1528913858c5eaf63475075ec354acdfc7139` |
| `G2_PHASE1_CLAIM_EVIDENCE.md` | `5d50ee8f0a1cda87edd53857aee6e65f6dc471afa003f0b2fe63eb347d667fe6` |

The requested Phase 1 authoring artifacts are complete. These are author checks, not the independent frozen-rubric Reviewer decision. No `PHASE1=PASS` or `G2=PASS` is asserted, and Phase 2 was not started.
