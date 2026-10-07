# G3 Final Reviewer Rubric — MoSAIC CARE 2026 package

PASS requires all items below on the exact Research Authoring final candidate.

## Scientific and authority fidelity

1. Author/project truth files control claims; the candidate does not invent result provenance.
2. The author-approved active result boundary is preserved.
3. Unsupported ablation, controlled robustness, SOTA, cross-center robustness or unresolved provenance is not promoted into stronger manuscript claims.
4. The old unsupported/misattributed edema row is not reintroduced as a MoSAIC result.
5. Compression to the page limit does not delete necessary limitations or convert uncertainty into certainty.

## Document/package production

6. The paper remains double-blind.
7. LNCS class/style are consumed without unauthorized template modification.
8. Final PDF satisfies the frozen CARE page-limit contract (<=12 pages including references).
9. Data-origin/citation/acknowledgment requirement is represented in the manuscript according to frozen project authority.
10. All active citations resolve to `refs.bib`; no fabricated citation/key.
11. Active figure path exists and caption/figure identity match.
12. Equation/table/figure labels and cross-references compile without unresolved references.
13. No stale disabled/unsupported table is accidentally promoted into active text.
14. Main text, abstract, results, discussion, conclusion, tables and figure claims are mutually consistent.

## Package selection

15. Only the frozen package subset is generated. Missing a required file => FAIL; manufacturing unrelated sidecars does not help and is a package-selection defect.
16. `SUBMISSION_MANIFEST.md` truthfully records build/page/anonymization/data-origin/reference state and does not claim live submission.

## Artifact quality

17. `mosaic.tex` builds using the frozen source package.
18. Final `mosaic.pdf` is readable/searchable and not obviously broken by page-limit edits.
19. Compile success alone is not PASS; Reviewer reads the full manuscript/PDF and checks claim consistency against truth files.

Any material failure => `G3=FAIL`.

## Freshness

Task identity, source ref, package subset and this rubric are frozen before final execution. If product/rubric/task/source ref is changed after final output is seen, the final attempt terminates and the material becomes development regression only.
