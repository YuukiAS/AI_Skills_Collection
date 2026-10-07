# Post-render scientific QA

Artifact checked: `outputs/advisor_update.pdf`

Source authority: `stable_source.md` and protected scientific meaning in `production_handoff.md`.

Final file hashes:

- `outputs/advisor_update.md`: `3dbcf3c099b8613256534517833ed07be4dff9f2ce22226807495a62a1287a9a`
- `outputs/advisor_update.pdf`: `62b315575149ad98de0a988810528d3307114f7686beebf7ce9c60f96be9676c`

## Protected meaning check

- Dice values are preserved exactly: baseline Dice is 0.781 and clipped-window Dice is 0.806.
- The final text describes the observed change as a "small directional gain" and explicitly says it is "not enough to claim method superiority"; it does not make a conclusive claim.
- No new baselines, datasets, methods, figures, or external citations were added.
- The next action remains a three-seed rerun with the same train/validation split.
- The boundary-touching failure review is preserved as an error-review requirement.

## Render QA

- Local PDF render completed under `outputs/`.
- `pdfinfo` reports one letter-size page.
- `pdftotext` extraction preserves the title, Dice table values, non-conclusive interpretation, and next-action sentence.
