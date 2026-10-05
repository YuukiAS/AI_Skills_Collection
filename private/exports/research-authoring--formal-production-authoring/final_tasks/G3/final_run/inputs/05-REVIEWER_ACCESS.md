# G3 Reviewer Access Contract

## Direct source access

Reviewer must be able to read `YuukiAS/MoSAIC_Paper@590bfbac1450fbab5e4ca8ce77c877ece845f094` through the linked GitHub connector, including the exact authority/source files in `VENUE_PROJECT_AUTHORITY.md`.

If a required binary/source cannot be read through that surface, Executor must materialize the exact Git blob into the AI_Skills task private export before final execution and bind it by hash. No summary substitute is allowed.

## Task-local source and output

After pre-final Critic PASS:

- frozen source snapshot:
  `private/exports/research-authoring--formal-production-authoring/final_tasks/G3/runtime_input/`
- candidate output:
  `private/exports/research-authoring--formal-production-authoring/final_tasks/G3/final_run/`

The MoSAIC repository is read-only and must not be mutated.

## Reviewer must directly inspect

- project truth/authority files;
- complete input `mosaic.tex`;
- complete output `mosaic.tex`;
- `refs.bib`;
- active figure;
- final compiled PDF;
- submission manifest;
- source-to-output diff;
- compile/log/reference status.

Reviewer must not PASS from a summary, page count, or compile status alone.
