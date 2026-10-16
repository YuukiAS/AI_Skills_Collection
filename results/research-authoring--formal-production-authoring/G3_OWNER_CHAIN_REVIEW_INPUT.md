# G3 Owner-Chain Slice Independent Review Input

## Decision requested

Independently decide whether the exact-candidate owner/handoff/renderer/post-render slice closes the only G3 behavior affected after historical `G3=PASS`.

## Binding

- Candidate: `9ed9140c7a131c1f8a5ba02b0262639a44af66eb`
- Existing scientific acceptance: `results/research-authoring--formal-production-authoring/G3_FINAL_REVIEW.md`
- Accepted source SHA-256: `04858c2d6677ed0563cbc5a3a975d7935c24aa3d64de87cef10aa5de47bbfce5`
- Accepted PDF SHA-256: `8dddea5921b08b95a0400b3057094f6d950506f34e2d17ca6abb5e985b2a9652`
- New handoff: `private/exports/research-authoring--formal-production-authoring/release_closure_9ed9140c_v2/g3_owner_chain/HANDOFF.md`
- New QA: `private/exports/research-authoring--formal-production-authoring/release_closure_9ed9140c_v2/g3_owner_chain/G3_OWNER_CHAIN_QA.json`
- New rebuilt PDF: `private/exports/research-authoring--formal-production-authoring/release_closure_9ed9140c_v2/g3_owner_chain/rebuild_output/mosaic.pdf`
- Wrapper archive: `private/exports/research-authoring--formal-production-authoring/release_closure_9ed9140c_v2/research-authoring-wrapper-0.3.1-release-9ed9140c-v2.tar.gz`
- Wrapper SHA-256: `70dc8b7ed9d81dba6e82dceda5fbeebd47feb3a65514d6f48cf571e852adea8d`

## Review questions

1. Does the handoff contain the current Research Authoring contract's audience, purpose, source authority, claim/evidence limits, object roles, citation authority, format, renderer route, and post-render checks?
2. Does `research-main` actually admit the named renderer after Research Authoring handoff?
3. Is the direct `pdflatex`/`bibtex` chain a legitimate project/venue override for this already accepted LNCS source?
4. Do source hash, 10-page result, citation/reference log, all-page rasterization, and byte-identical plain-text extraction show that the affected ownership slice preserved the accepted scientific artifact?
5. Is any G3-specific rerun still required, or may the historical scientific acceptance plus this slice remain `G3=PASS` for release?

Do not infer G1 or G4 PASS from this review.
