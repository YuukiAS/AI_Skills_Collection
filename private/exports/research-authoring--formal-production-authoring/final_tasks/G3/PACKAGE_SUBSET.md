# G3 Frozen Package Subset

The final task uses a minimal real submission package. It must not create every possible Research Authoring sidecar.

## Required product package

Under the task-local output directory:

1. `mosaic.tex` — revised canonical manuscript source;
2. `refs.bib` — bibliography required by the manuscript;
3. `figures/fig1_original_redraw.pdf` — active figure referenced by the manuscript;
4. `llncs.cls` — frozen LNCS class;
5. `splncs04.bst` — frozen bibliography style;
6. `mosaic.pdf` — compiled final manuscript;
7. `SUBMISSION_MANIFEST.md` — concise package manifest with:
   - source ref and output identity;
   - build route;
   - page count;
   - double-blind check;
   - data-origin/declaration check;
   - bibliography/figure/cross-reference status;
   - known limitations that remain.

## Explicitly not required

Unless the frozen source itself makes them necessary:
- separate supplement;
- cover letter;
- reviewer response;
- separate author-contributions file;
- separate author-metadata file;
- standalone declarations file;
- reporting-guideline checklist;
- duplicate captions file;
- empty tables/placeholder sidecars.

The venue-specific data-origin statement belongs in the manuscript when required by the frozen project authority.

## Source snapshot

After pre-final Critic PASS, materialize the exact authority/source files from `YuukiAS/MoSAIC_Paper@590bfbac1450fbab5e4ca8ce77c877ece845f094` into:

`private/exports/research-authoring--formal-production-authoring/final_tasks/G3/runtime_input/`

The MoSAIC repository remains read-only. Candidate edits occur only in a separate task-local output directory.
