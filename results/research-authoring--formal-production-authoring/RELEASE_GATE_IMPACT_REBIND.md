# Research Authoring Release Gate Impact Rebind

## Candidate identity

- Exact current release candidate: `9ed9140c7a131c1f8a5ba02b0262639a44af66eb`
- Last C3 product candidate: `9e88d7eda1749c09bac0ed97562909a90810ccdb`
- Historical G1-G3 execution candidate: `1c37c0715aca0096606f24e56192b7857e72bbd6`
- Release baseline merged into the candidate: main `fc6baf61ea385fea6fae814864cc8c77c262a49a`

The G1-G3 evidence is not relabeled as if it had run on the new commit. This document records which gates remain semantically reusable, which exact ownership slice was affected, and which gates require fresh live evidence.

## Gate-impact analysis

The change from the historical G1-G3 candidate to C3 added the explicit artifact-owner and renderer-admission contract. It changes routing and handoff behavior around formal PDF work; it does not alter the accepted G2 scientific source data, claims, calculations, table contents, or final advisor document.

The change from C3 `9e88d7ed...` to exact candidate `9ed9140c...` leaves the following release-critical Research Authoring chain byte-identical:

| Surface | SHA-256 at exact candidate |
|---|---|
| `skills/writing/research/research-authoring-core/SKILL.md` | `a8bcd0c871336050ce3647ec8be0e3169deb1c840580a5c7eee84864cfdf25c5` |
| `skills/writing/research/research-reporting/SKILL.md` | `8f95d5de3785c96360db7da6655e88c73eef13a32b202ceb22a561a4414ea01f` |
| `profiles/research-main.json` | `c476b6dc9063046b45c8e1d91f5e6b5fabdc54edd026e25129520ef4876aa49d` |
| `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md` | `fe5000f39bb163efb636d237152beafe40e042808a5f7c4cab1aa6c40210e8f0` |
| generated Research Authoring report entry | `4ad8147f57214987e54e8ed80d1fef871c58d97a783b5e5a1c2d45f12d7f0a89` |

The later `student-assessment` additions are shared contract files. They do not change Research Authoring core/report/paper routing, `research-main`, the renderer, or the accepted G2/G3 scientific artifacts. Presentations, Project Instructions Editor, and release metadata changes are outside these gate semantics.

The only change from `c1da41a0...` to `9ed9140c...` resolves version-expectation tests to the already approved `research-writing 0.3` and `presentations 0.4`. The relevant production-tree diff is empty. The exact-candidate focused suite then passed all 91 tests.

## G2 rebind

G2 remains accepted without a mechanical rerun.

- Existing independent decision: `results/research-authoring--formal-production-authoring/G2_FINAL_REVIEW.md`, `G2=PASS`.
- Final advisor document SHA-256: `15bec572fc06948bce0f2f9419f332dea96b07bff4f00d838c26bfb933627149`.
- Baseline-to-updated diff SHA-256: `0c45c9ebe845482169254756161c80ed09ce5b19d42699054f9459ae1d2e7793`.
- Claim/evidence record SHA-256: `f2550b624c8df1e74543d5e380b1cbf8eaf5813c9076b391cdff684efe70bee4`.
- Route record SHA-256: `8a9d0d902d80b32fef315e3357ff1a75c3186da586d7fbf8e159eca8e4a9be13`.

The C3 change adds a stricter boundary after stable source/handoff. It does not weaken the accepted reader-first report, source provenance, claim/evidence limits, uncertainty language, or Phase 1/Phase 2 separation. Fresh live-wrapper routing remains a G1/G4 requirement and is not inferred from G2.

**G2 release rebind: PASS, subject to independent release reviewer confirmation.**

## G3 affected owner-chain slice

The accepted scientific source and package were reused without editing:

- `mosaic.tex` SHA-256: `04858c2d6677ed0563cbc5a3a975d7935c24aa3d64de87cef10aa5de47bbfce5`.
- accepted PDF SHA-256: `8dddea5921b08b95a0400b3057094f6d950506f34e2d17ca6abb5e985b2a9652`.
- existing independent decision: `results/research-authoring--formal-production-authoring/G3_FINAL_REVIEW.md`, `G3=PASS`.

Only the newly affected chain was rerun:

```text
accepted Research Authoring source/package
  -> exact-candidate downstream handoff
  -> research-main renderer admission
  -> venue-bound direct LaTeX compile
  -> renderer QA
  -> post-render Research Authoring identity/claim-boundary QA
```

Durable private evidence:

- `private/exports/research-authoring--formal-production-authoring/release_closure_9ed9140c_v2/g3_owner_chain/HANDOFF.md`
- `private/exports/research-authoring--formal-production-authoring/release_closure_9ed9140c_v2/g3_owner_chain/G3_OWNER_CHAIN_QA.json`

Observed result:

- copied source hash equals the accepted source hash;
- 10-page PDF produced under the existing LNCS venue/project route;
- no undefined citations or references;
- all 10 pages rasterized;
- plain `pdftotext` output is byte-identical to the accepted G3 baseline, SHA-256 `28225b0252db8203aebf75d30f9f50cf97e88d97e53ebab4f1f2ddbe45e7649c`;
- no scientific source, claim, figure, table, formula, citation, or limitation was revised.
- the immutable accepted package remains exactly seven files and matches its original `SUBMISSION_MANIFEST.md`; compiler auxiliary files and the rebuilt PDF are isolated under `rebuild_work/` and `rebuild_output/`.

The rebuilt PDF has SHA-256 `1fe3419d8a886f21d7302dde2dfc123e7ed9e97a5e9f15e4c95a9143452f3c5b`; binary identity is not expected because the new build uses a fixed source-date epoch. Text identity, page count, source identity, and compile evidence are the relevant affected-slice checks.

**G3 affected-slice result: PASS, subject to independent release reviewer confirmation.**

## Fresh live evidence still required

G1 and G4 are not closed by the rebind above.

The exact private skills-only wrapper prepared for both gates is:

- target live plugin: `plugins_6ac4471b735881918c17cd310f262429`;
- expected current live release: `pluginrel_6ac4471c7b90819189bc23af890135f3` (`0.3.0`);
- operation: `UPDATE`, not a second plugin create;
- wrapper version: `0.3.1`;
- archive: `private/exports/research-authoring--formal-production-authoring/release_closure_9ed9140c_v2/research-authoring-wrapper-0.3.1-release-9ed9140c-v2.tar.gz`;
- archive SHA-256: `70dc8b7ed9d81dba6e82dceda5fbeebd47feb3a65514d6f48cf571e852adea8d`;
- Research Authoring and Clear Writing payload commit: `9ed9140c7a131c1f8a5ba02b0262639a44af66eb`;
- scope/discoverability/capability: `USER` / `PRIVATE` / `Skills` only;
- excluded: renderer runtime, MCP, connector, database, watcher, state machine.
- manifest path: `./skills/`; discoverable skills are exactly `report`, `paper`, `litcite`, `writing-fidelity`, `chinese-prose`, and `scientific-prose`.

The earlier `release_closure_9ed9140c` archive is superseded and forbidden for live update because its three Research Authoring skills were outside the manifest-declared `./skills/` path. The v2 archive above is the only live-update candidate.

G1 requires fresh normal-entry and near-miss routing on that live wrapper. G4 requires the approved G2 semantic baseline to travel through the same live wrapper, exact-candidate Codex `research-main`, admitted renderer, final PDF, renderer QA, post-render scientific QA, artifact delivery, and independent review.

No Research Authoring release PASS or version increment is claimed until those live gates pass.
