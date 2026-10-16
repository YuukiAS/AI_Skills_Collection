# Presentations Release Acceptance

## Review identity

- Review type: fresh independent, read-only artifact and rendered-output review
- Reviewer: `/root/presentations_release_acceptance_audit`
- Exact candidate: `e9737e483fa911a5b63f96cdd64d6c479a608913`
- Candidate subject: `Merge remote-tracking branch 'origin/main'`
- Candidate parents: `f717d28beef4dd1cbbb66cb491712769d1250aac`, `e0ce58cbed0d948845f9df6571ba054615cd75ab`
- Review scope: the normal-entry Presentations artifact under `results/repository--formal-release-5.5.0/presentations/normal-entry/`
- Product version under replay: `presentations 0.3`
- Proposed accepted release version: `presentations 0.4`

This review independently opened the five rendered page PNGs and the whole-deck contact sheet, then checked the PDF, editable TeX source, deck plan, compile record, deterministic QA record, rendered-review manifest, replay manifest, source fidelity, and candidate/plugin-consumption binding.

## Candidate and artifact binding

The replay manifest binds the run to candidate `e9737e483fa911a5b63f96cdd64d6c479a608913` and to the installed candidate plugin `presentations@ai-skills-candidate`, version `0.3`.

| Artifact | SHA-256 |
|---|---|
| `normal-entry/deck/main.pdf` | `902019a96971a383357228a51f12f2b5777d7c7542e6a0277cfa26aa859eb735` |
| `normal-entry/deck/main.tex` | `182741939a67e4a23e0ebb4e20df1e533175172f76495d2dfe4e307676bfbeaf` |
| `normal-entry/deck-plan.yaml` | `91ec1cfe581390109e9e5bf599c8694477f7b2e4d65f559a9256b35bc90809f4` |
| `normal-entry/deck_contact_sheet.png` | `99ceb1efe626b908278644ff0770e622e17708126f64073d331ff439af032c2a` |
| `normal-entry/deck/rendered/slide-1.png` | `df2ca0032f58d08a6514468405bc862e612104bbf5538a86dc27e5d0708cb977` |
| `normal-entry/deck/rendered/slide-2.png` | `b0b3f0785cc293f827d37739891779b50bac7a1ba2b3958f67be3b3658f10c80` |
| `normal-entry/deck/rendered/slide-3.png` | `d75b39b551901e38520030370a25d3d4e8a113d0cba644f5f862a6b7d85dad45` |
| `normal-entry/deck/rendered/slide-4.png` | `315db780596ebcc7315b0058fd83e5da543bd5e5fe5e5e7999559f4bad22e6d2` |
| `normal-entry/deck/rendered/slide-5.png` | `d6c0de10335a5357b090b09a4817dd8bb645d0105b6e85f5f53a2fb21a83c00a` |
| Public-safe source used by the replay | `fb36713b86f8a4e72fd5feb52439d389ff3bf47b9c7cd5771fde867297cfb016` |

The evidence records themselves were also re-hashed during this review:

| Evidence record | SHA-256 |
|---|---|
| `normal-entry/compile-status.json` | `d116ca7153d3286455dc2f133d1335c7e40729270ff6cea9c3d0d81719b0a421` |
| `normal-entry/deterministic-qa.json` | `b780119edeab95c8106f75794470335e9203cba0e17afb828ec178fc190f8dc5` |
| `normal-entry/rendered-review-input.json` | `1990a3cc483031a8829b2fcbbb04b41a0d5af3641d8db0d4460742ac382b3bd9` |
| `normal-entry/replay-run.json` | `18d1983a722b9f1744e8f045bf47f9799dfff9ffa00a03edc4be405a80a75ab9` |

All PDF, TeX, plan, contact-sheet, and page hashes recorded by the manifests match the reviewed files.

## Normal-entry and actual plugin consumption

`replay-run.json` records:

- candidate commit: `e9737e483fa911a5b63f96cdd64d6c479a608913`;
- plugin: `presentations@ai-skills-candidate`;
- installed candidate version: `0.3`;
- runtime: `codex-cli 0.153.4`;
- actual consumption: proven at child JSONL line index 5.

The corresponding event is an actual read of the installed candidate skill:

```text
cat /users/a/e/aereinh/.codex/plugins/cache/ai-skills-candidate/presentations/0.3/skills/research/SKILL.md
```

The replay used the skill's documented native exact-CUHK Beamer route and its production render/contact-sheet utilities. `deterministic-qa.json` records `production_entry_used=false` because the specialized one-call layout path was not suitable for this editable native table/prose/failure-case deck. This does not indicate plugin bypass: the installed candidate skill was consumed through the normal entry, and the selected native route is part of its documented production behavior.

**Normal-entry consumption: PASS.**

## Compile, structure, and deterministic QA

`main.pdf` is a five-page, 16:9, unencrypted Beamer PDF. Its text is extractable and retains the supplied numbers, study limits, uncertainty, and proposed-versus-completed distinction.

`main.tex` is editable source. It contains no page-local font shrinking, no fabricated evidence, no invented citations, no statistical-significance claim, no clinical claim, and no superiority claim.

`compile-status.json` records:

- status: `COMPILED`;
- engine: `/usr/bin/xelatex`;
- compile passes: `2`;
- font binding: `READY`;
- missing fonts: none;
- output PDF SHA-256: `902019a96971a383357228a51f12f2b5777d7c7542e6a0277cfa26aa859eb735`.

`pdffonts` found only the expected embedded, subsetted, Unicode-capable fonts:

- `TeXGyreTermes-Regular-Identity-H`;
- `TeXGyreTermes-Bold-Identity-H`.

`deterministic-qa.json` records:

- page count: `5`;
- PNG count: `5`;
- numeric values preserved: `true`;
- limitations preserved: `true`;
- overfull boxes: `0`;
- missing characters: `0`;
- plan-validation errors: none;
- font QA: `PASS`.

`deck-plan.yaml` correctly binds P01-P05 to their source anchors, page jobs, scientific objects, evidence states, missing evidence, and forbidden fallbacks. P05 remains correctly marked `planned`; the proposed replication is not presented as completed work.

**Compile and deterministic QA: PASS.**

## Independent rendered review

The reviewer opened every full-resolution page PNG and the contact sheet rather than relying on deterministic QA or the producer's own assessment.

| Page | SHA-256 | Verdict | Independent observation |
|---|---|---|---|
| P01 | `df2ca0032f58d08a6514468405bc862e612104bbf5538a86dc27e5d0708cb977` | PASS | The research question and replication decision are immediately legible. The title, subtitle, public-safe synthetic boundary, CUHK branding, and page marker render completely. Typography is clear, with no overlap, clipping, or harmful line break. |
| P02 | `b0b3f0785cc293f827d37739891779b50bac7a1ba2b3958f67be3b3658f10c80` | PASS | The page clearly states 18 validation volumes, fixed split/model/training/post-processing, and the sole intended change of 1st/99th-percentile clipping. The small-validation and non-clinical limits remain adjacent and readable. The page is intentionally sparse but fulfills its study-boundary job without a projection-readability defect. |
| P03 | `d75b39b551901e38520030370a25d3d4e8a113d0cba644f5f862a6b7d85dad45` | PASS | The editable table is the clear primary object. All values and the HD95 unit are correct and readable: `0.742 -> 0.758`, `0.421 -> 0.469`, and `18.4 -> 17.9 mm`. The statements “supports replication, not superiority” and “no confidence interval or repeated-seed estimate” are visually adjacent to the result, preventing the descriptive title from becoming an unsupported superiority claim. |
| P04 | `315db780596ebcc7315b0058fd83e5da543bd5e5fe5e5e7999559f4bad22e6d2` | PASS | The unresolved motion-corrupted volume, disconnected false positives under both methods, missing confidence/repeated-seed evidence, small-split dependence, and interpretation boundary all remain visible. No case image was supplied, and the deck correctly avoids fabricating one. The page is sparse but contains no missing required evidence, clipping, or layout failure. |
| P05 | `d6c0de10335a5357b090b09a4817dd8bb645d0105b6e85f5f53a2fb21a83c00a` | PASS | The four next steps are legible: three fixed seeds, preregistered preprocessing/split policy, uncertainty reporting, and separate audit of the corrupted case. The approval request before architecture change is explicit. Proposed work is not represented as completed work. |

The contact sheet at SHA-256 `99ceb1efe626b908278644ff0770e622e17708126f64073d331ff439af032c2a` shows a coherent whole-deck sequence:

1. question and decision context;
2. controlled study design;
3. quantitative evidence;
4. failure and uncertainty;
5. next experiment and decision request.

The exact-CUHK shell, header/footer treatment, font family, hierarchy, and reading rhythm are consistent across all five pages. The deck has substantial whitespace on P02-P04, but for a five-minute public-safe decision deck this is a non-blocking aesthetic characteristic, not a release defect.

**Rendered artifact review: PASS.**

## Rejection of the producer's self-written review

The producer-created file `outputs/independent-review.json` is explicitly excluded from this acceptance decision.

The child execution log shows the same child process directly creating that file with a shell `cat > outputs/independent-review.json` command at JSONL events 64-65. No `spawn_agent`, fresh reviewer invocation, or separate independent-review execution is present. Therefore the file's self-description as a fresh independent review is unsupported and is not accepted as review evidence.

This release decision instead rests on the fresh, read-only review documented here, including direct inspection of every page image, the contact sheet, source, PDF, plan, compile evidence, QA evidence, replay binding, and hashes.

## Release decision

**Presentations release acceptance: PASS.**

The exact candidate `e9737e483fa911a5b63f96cdd64d6c479a608913` demonstrates a real normal-entry, user-facing Presentations result with:

- actual installed-plugin consumption;
- an editable exact-CUHK TeX source;
- a successfully compiled and font-validated PDF;
- complete per-page and whole-deck rendered artifacts;
- faithful preservation of all supplied values and limitations;
- no invented evidence or overclaim;
- deterministic QA PASS;
- fresh independent visual and source review PASS.

No release-blocking Presentations defect was found. The observed sparsity on two content pages is a non-blocking visual note and does not justify reopening product development or expanding the frozen release scope.

## Version decision

- Affected plugin: `presentations`
- Decision: `0.3 -> 0.4`
- Result: **APPROVED**

Reason: the current production runtime contains a user-facing improvement batch, and the exact candidate now has capability/regression evidence plus a successful normal-entry replay, complete final artifacts, deterministic QA, and independent rendered/source acceptance. This is sufficient for one Presentations plugin version increment under the repository version policy.
