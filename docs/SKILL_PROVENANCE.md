# Skill Provenance Audit

This report records what can be proven from files currently in this repository. It does not infer an upstream skill origin from package documentation links, license URLs, or library names.

## Summary

- Scope: `active_and_non_archived`
- Skills audited: 150
- Skills with explicit source fields: 11
- User-authored skills: 18
- External adapted skills: 11
- External vendored skills: 0
- Generated skills: 0
- Local legacy skills: 6
- Unknown-origin historical skills: 115
- Skills containing URLs in the body: 67
- Skills containing local license files: 11

## Provenance Counts

| Provenance | Count |
| --- | --- |
| external-adapted | 11 |
| local | 6 |
| unknown | 115 |
| user-authored | 18 |

## User Authored

| Skill | Path | Provenance | Source |
| --- | --- | --- | --- |
| ai-skills-repository-maintainer | skills/core/codex-system/ai-skills-repository-maintainer | user-authored |  |
| codex-workflow-protocol | skills/core/codex-system/codex-workflow-protocol | user-authored |  |
| cardiac-mri | skills/domains/medical-imaging/cardiac-mri | user-authored |  |
| medical-imaging-terminology-measurement | skills/domains/medical-imaging/medical-imaging-terminology-measurement | user-authored |  |
| clinical-guideline-checking | skills/domains/medicine-clinical/clinical-guideline-checking | user-authored |  |
| medical-literature-evidence-review | skills/domains/medicine-clinical/medical-literature-evidence-review | user-authored |  |
| medical-safety-boundaries | skills/domains/medicine-clinical/medical-safety-boundaries | user-authored |  |
| publication-figure-palettes | skills/science/communication/publication-figure-palettes | user-authored |  |
| scientific-figure-qa | skills/science/communication/scientific-figure-qa | user-authored |  |
| business-presentations | skills/tools/documents-media/presentations/business-presentations | user-authored |  |
| research-presentations | skills/tools/documents-media/presentations/research-presentations | user-authored |  |
| render-chinese-math-pdf | skills/tools/documents-media/render-chinese-math-pdf | user-authored |  |
| frontend-reference-research | skills/tools/frontend/frontend-reference-research | user-authored |  |
| frontend-visual-systems | skills/tools/frontend/frontend-visual-systems | user-authored |  |
| research-product-frontend | skills/tools/frontend/research-product-frontend | user-authored |  |
| slurm-workflows | skills/tools/hpc/slurm-workflows | user-authored |  |
| writing-fidelity | skills/writing/core/writing-fidelity | user-authored |  |
| research-reporting | skills/writing/research/research-reporting | user-authored |  |

## External Adapted

| Skill | Path | Provenance | Source |
| --- | --- | --- | --- |
| skill-library-analysis | skills/core/codex-system/skill-library-analysis | external-adapted | {"source_imported_at": "2026-07-09", "source_license": "MIT", "source_note": "Distilled from graph-of-skills and local provenance audit work.", "source_path": ".", "source_ref": "69f2ab2f5e18681cb809e8e123da6b83ec50f5fc", "source_repo_url": "https://github.com/davidliuk/graph-of-skills"} |
| valyu-scientific-search | skills/science/discovery/valyu-scientific-search | external-adapted | {"source_imported_at": "2026-07-09", "source_license": "MIT", "source_note": "Distilled from scientific-skills search skills; kept optional because it depends on external semantic-search infrastructure.", "source_path": ".", "source_ref": "20b3d503700656f847e6de873753335bf90e63e3", "source_repo_url": "https://github.com/yorkeccak/scientific-skills"} |
| experiment-execution | skills/science/ideation/experiment-execution | external-adapted | {"source_imported_at": "2026-07-09", "source_license": "MIT", "source_note": "Distilled from experiment-agent and existing codex-workflow-protocol verification gates.", "source_path": ".", "source_ref": "e291e7dc7ca268b2de7e1a9cf23bc2eef5dc0651", "source_repo_url": "https://github.com/Imbad0202/experiment-agent"} |
| d2-diagrams | skills/tools/visualization/d2-diagrams | external-adapted | {"source_imported_at": "2026-07-09", "source_license": "MIT", "source_note": "Distilled from D2-Diagram-Skill and heathdutton/claude-d2-diagrams plugin notes; plugin-only repo recorded but not imported.", "source_path": ".", "source_ref": "5b30a5597f93876295b1ae9567c0e97e87543aa4", "source_repo_url": "https://github.com/RayanAhmed0/D2-Diagram-Skill"} |
| drawio-diagrams | skills/tools/visualization/drawio-diagrams | external-adapted | {"source_imported_at": "2026-07-09", "source_license": "Apache-2.0", "source_note": "Distilled from drawio-mcp, Agents365-ai/drawio-skill, and little-hands/claude-drawio-skill.", "source_path": ".", "source_ref": "883b34c8aea72ca7bc978a281061c411bc3e3745", "source_repo_url": "https://github.com/jgraph/drawio-mcp"} |
| excalidraw-diagrams | skills/tools/visualization/excalidraw-diagrams | external-adapted | {"source_imported_at": "2026-07-09", "source_license": "MIT", "source_note": "Distilled from excalidraw-diagram-skill and kept separate from publication-final diagram workflows.", "source_path": ".", "source_ref": "8646fcc9f74f38539c6cdb4c969723336a96ddcd", "source_repo_url": "https://github.com/coleam00/excalidraw-diagram-skill"} |
| plantuml-diagrams | skills/tools/visualization/plantuml-diagrams | external-adapted | {"source_imported_at": "2026-07-09", "source_license": "MIT", "source_note": "Distilled from Agents365-ai/plantuml-skill, SpillwaveSolutions/plantuml, and Kroki multi-engine diagram guidance.", "source_path": ".", "source_ref": "07fe0ade1fc9a0a1e2ae8d64f95aa45cd8882284", "source_repo_url": "https://github.com/Agents365-ai/plantuml-skill"} |
| citation-verification | skills/writing/research/citation-verification | external-adapted | {"source_imported_at": "2026-07-09", "source_license": "MIT", "source_note": "Distilled from citation-check-skill, Nature-Paper-Skills citation-verifier/reference-audit, claude-scholar citation-verification, and paperpipe verification workflows.", "source_path": ".", "source_ref": "b9deb7077099f56b05c9b6ecea744c2ca0a6d324", "source_repo_url": "https://github.com/serenakeyitan/citation-check-skill"} |
| latex-paper-authoring | skills/writing/research/latex-paper-authoring | external-adapted | {"source_imported_at": "2026-07-09", "source_license": "MIT", "source_note": "Distilled from latex-paper-skills, latex-document-skill, claude-scholar LaTeX template organizer, and existing render-chinese-math-pdf practice.", "source_path": ".", "source_ref": "d0f106108cb09e448604a56ce973d35b340cf497", "source_repo_url": "https://github.com/yunshenwuchuxun/latex-paper-skills"} |
| nature-manuscript-workflow | skills/writing/research/nature-manuscript-workflow | external-adapted | {"source_imported_at": "2026-07-09", "source_license": "MIT", "source_note": "Distilled from Nature-Paper-Skills, nature-skills, and claude-scholar Nature writing/response/data skills.", "source_path": ".", "source_ref": "44cff42ac22a5ac4dcfb7ba01b2e81c21d689ea6", "source_repo_url": "https://github.com/Boom5426/Nature-Paper-Skills"} |
| paper-workflow-orchestrator | skills/writing/research/paper-workflow-orchestrator | external-adapted | {"source_imported_at": "2026-07-09", "source_license": "MIT", "source_note": "Distilled from PaperSpine, academic-research-skills, Nature-Paper-Skills, paper-writing-skill, and Research-Paper-Writing-Skills; see docs/provenance/INTEGRATION_HISTORY.md.", "source_path": ".", "source_ref": "d4529208cda72aa075767611b0265b95b709b550", "source_repo_url": "https://github.com/WUBING2023/PaperSpine"} |

## External Vendored

None.

## Generated

None.

## Local Legacy

| Skill | Path | Provenance | Source |
| --- | --- | --- | --- |
| project-skill-installer | skills/core/codex-system/project-skill-installer | local |  |
| bioinformatics-database-retrieval | skills/domains/bioinformatics/databases/bioinformatics-database-retrieval | local |  |
| figma-design-to-code | skills/tools/frontend/figma-design-to-code | local |  |
| motion-interaction | skills/tools/frontend/motion-interaction | local |  |
| chinese-prose | skills/writing/core/chinese-prose | local |  |
| scientific-prose | skills/writing/core/scientific-prose | local |  |

## Unknown Historical

| Skill | Path | Provenance | Source |
| --- | --- | --- | --- |
| mcp-builder | skills/core/codex-system/mcp-builder | unknown |  |
| imagegen | skills/core/codex-system/system-skills/imagegen | unknown |  |
| openai-docs | skills/core/codex-system/system-skills/openai-docs | unknown |  |
| plugin-creator | skills/core/codex-system/system-skills/plugin-creator | unknown |  |
| skill-creator | skills/core/codex-system/system-skills/skill-creator | unknown |  |
| skill-installer | skills/core/codex-system/system-skills/skill-installer | unknown |  |
| bayesian-ppl-diagnostics | skills/domains/bayesian/bayesian-ppl-diagnostics | unknown |  |
| pymc | skills/domains/bayesian/pymc | unknown |  |
| simpy | skills/domains/bayesian/simpy | unknown |  |
| statistical-analysis | skills/domains/bayesian/statistical-analysis | unknown |  |
| statsmodels | skills/domains/bayesian/statsmodels | unknown |  |
| biopython | skills/domains/bioinformatics/biology-toolkits/biopython | unknown |  |
| esm | skills/domains/bioinformatics/biology-toolkits/esm | unknown |  |
| etetoolkit | skills/domains/bioinformatics/biology-toolkits/etetoolkit | unknown |  |
| phylogenetics | skills/domains/bioinformatics/biology-toolkits/phylogenetics | unknown |  |
| scikit-bio | skills/domains/bioinformatics/biology-toolkits/scikit-bio | unknown |  |
| pysam | skills/domains/bioinformatics/genomics-io/pysam | unknown |  |
| tiledbvcf | skills/domains/bioinformatics/genomics-io/tiledbvcf | unknown |  |
| zarr-python | skills/domains/bioinformatics/genomics-io/zarr-python | unknown |  |
| arboreto | skills/domains/bioinformatics/omics-analysis/arboreto | unknown |  |
| deeptools | skills/domains/bioinformatics/omics-analysis/deeptools | unknown |  |
| flowio | skills/domains/bioinformatics/omics-analysis/flowio | unknown |  |
| geniml | skills/domains/bioinformatics/omics-analysis/geniml | unknown |  |
| gtars | skills/domains/bioinformatics/omics-analysis/gtars | unknown |  |
| polars-bio | skills/domains/bioinformatics/omics-analysis/polars-bio | unknown |  |
| pydeseq2 | skills/domains/bioinformatics/omics-analysis/pydeseq2 | unknown |  |
| dnanexus-integration | skills/domains/bioinformatics/platforms/dnanexus-integration | unknown |  |
| lamindb | skills/domains/bioinformatics/platforms/lamindb | unknown |  |
| latchbio-integration | skills/domains/bioinformatics/platforms/latchbio-integration | unknown |  |
| anndata | skills/domains/bioinformatics/single-cell/anndata | unknown |  |
| scanpy | skills/domains/bioinformatics/single-cell/scanpy | unknown |  |
| scvelo | skills/domains/bioinformatics/single-cell/scvelo | unknown |  |
| scvi-tools | skills/domains/bioinformatics/single-cell/scvi-tools | unknown |  |
| neuropixels-analysis | skills/domains/bioinformatics/specialized/neuropixels-analysis | unknown |  |
| medical-imaging-classical-features | skills/domains/medical-imaging/medical-imaging-classical-features | unknown |  |
| medical-imaging-deep-learning | skills/domains/medical-imaging/medical-imaging-deep-learning | unknown |  |
| pathml | skills/domains/medical-imaging/pathml | unknown |  |
| pydicom | skills/domains/medical-imaging/pydicom | unknown |  |
| clinical-decision-support | skills/domains/medicine-clinical/clinical-decision-support | unknown |  |
| clinical-reports | skills/domains/medicine-clinical/clinical-reports | unknown |  |
| neurokit2 | skills/domains/medicine-clinical/neurokit2 | unknown |  |
| pyhealth | skills/domains/medicine-clinical/pyhealth | unknown |  |
| scikit-survival | skills/domains/medicine-clinical/scikit-survival | unknown |  |
| treatment-plans | skills/domains/medicine-clinical/treatment-plans | unknown |  |
| latex-posters | skills/science/communication/latex-posters | unknown |  |
| paper-2-web | skills/science/communication/paper-2-web | unknown |  |
| pptx-posters | skills/science/communication/pptx-posters | unknown |  |
| scientific-schematics | skills/science/communication/scientific-schematics | unknown |  |
| scientific-visualization | skills/science/communication/scientific-visualization | unknown |  |
| arxiv-database | skills/science/discovery/arxiv-database | unknown |  |
| bgpt-paper-search | skills/science/discovery/bgpt-paper-search | unknown |  |
| biorxiv-database | skills/science/discovery/biorxiv-database | unknown |  |
| citation-management | skills/science/discovery/citation-management | unknown |  |
| openalex-database | skills/science/discovery/openalex-database | unknown |  |
| pubmed-database | skills/science/discovery/pubmed-database | unknown |  |
| pyzotero | skills/science/discovery/pyzotero | unknown |  |
| research-lookup | skills/science/discovery/research-lookup | unknown |  |
| consciousness-council | skills/science/ideation/consciousness-council | unknown |  |
| hypogenic | skills/science/ideation/hypogenic | unknown |  |
| hypothesis-generation | skills/science/ideation/hypothesis-generation | unknown |  |
| scientific-brainstorming | skills/science/ideation/scientific-brainstorming | unknown |  |
| scientific-critical-thinking | skills/science/ideation/scientific-critical-thinking | unknown |  |
| what-if-oracle | skills/science/ideation/what-if-oracle | unknown |  |
| modal | skills/tools/ai-ml/modal | unknown |  |
| pufferlib | skills/tools/ai-ml/pufferlib | unknown |  |
| pytorch-lightning | skills/tools/ai-ml/pytorch-lightning | unknown |  |
| stable-baselines3 | skills/tools/ai-ml/stable-baselines3 | unknown |  |
| timesfm-forecasting | skills/tools/ai-ml/timesfm-forecasting | unknown |  |
| torch-geometric | skills/tools/ai-ml/torch-geometric | unknown |  |
| transformers | skills/tools/ai-ml/transformers | unknown |  |
| aeon | skills/tools/data-science/aeon | unknown |  |
| dask | skills/tools/data-science/dask | unknown |  |
| exploratory-data-analysis | skills/tools/data-science/exploratory-data-analysis | unknown |  |
| geopandas | skills/tools/data-science/geopandas | unknown |  |
| matlab | skills/tools/data-science/matlab | unknown |  |
| networkx | skills/tools/data-science/networkx | unknown |  |
| polars | skills/tools/data-science/polars | unknown |  |
| pymoo | skills/tools/data-science/pymoo | unknown |  |
| scikit-learn | skills/tools/data-science/scikit-learn | unknown |  |
| shap | skills/tools/data-science/shap | unknown |  |
| sympy | skills/tools/data-science/sympy | unknown |  |
| umap-learn | skills/tools/data-science/umap-learn | unknown |  |
| vaex | skills/tools/data-science/vaex | unknown |  |
| docx | skills/tools/documents-media/docx | unknown |  |
| get-available-resources | skills/tools/documents-media/get-available-resources | unknown |  |
| markitdown | skills/tools/documents-media/markitdown | unknown |  |
| open-notebook | skills/tools/documents-media/open-notebook | unknown |  |
| parallel-web | skills/tools/documents-media/parallel-web | unknown |  |
| pdf | skills/tools/documents-media/pdf | unknown |  |
| perplexity-search | skills/tools/documents-media/perplexity-search | unknown |  |
| xlsx | skills/tools/documents-media/xlsx | unknown |  |
| brand-creative-assets | skills/tools/frontend/brand-creative-assets | unknown |  |
| design-system-tokens | skills/tools/frontend/design-system-tokens | unknown |  |
| implementation-react-tailwind | skills/tools/frontend/implementation-react-tailwind | unknown |  |
| product-ux-planning | skills/tools/frontend/product-ux-planning | unknown |  |
| responsive-accessibility-review | skills/tools/frontend/responsive-accessibility-review | unknown |  |
| visual-direction | skills/tools/frontend/visual-direction | unknown |  |
| webapp-testing | skills/tools/frontend/webapp-testing | unknown |  |
| canvas-design | skills/tools/visualization/canvas-design | unknown |  |
| generate-image | skills/tools/visualization/generate-image | unknown |  |
| infographics | skills/tools/visualization/infographics | unknown |  |
| markdown-mermaid-writing | skills/tools/visualization/markdown-mermaid-writing | unknown |  |
| matplotlib | skills/tools/visualization/matplotlib | unknown |  |
| plotly | skills/tools/visualization/plotly | unknown |  |
| seaborn | skills/tools/visualization/seaborn | unknown |  |
| theme-factory | skills/tools/visualization/theme-factory | unknown |  |
| academic-paper-writer-pro | skills/writing/research/academic-paper-writer-pro | unknown |  |
| content-generation | skills/writing/research/content-generation | unknown |  |
| literature-review | skills/writing/research/literature-review | unknown |  |
| ocr-kb | skills/writing/research/ocr-kb | unknown |  |
| peer-review | skills/writing/research/peer-review | unknown |  |
| research-grants | skills/writing/research/research-grants | unknown |  |
| scholar-evaluation | skills/writing/research/scholar-evaluation | unknown |  |
| scientific-writing | skills/writing/research/scientific-writing | unknown |  |
| venue-templates | skills/writing/research/venue-templates | unknown |  |

## URL Evidence

URLs below are evidence of related projects or references found in skill bodies. They are not treated as confirmed skill origins unless also recorded in an explicit source field.

| Skill | Path | URL count | First URLs |
| --- | --- | --- | --- |
| mcp-builder | skills/core/codex-system/mcp-builder | 4 | https://modelcontextprotocol.io/sitemap.xml, https://modelcontextprotocol.io/specification/draft.md, https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md |
| imagegen | skills/core/codex-system/system-skills/imagegen | 1 | https://platform.openai.com/api-keys |
| openai-docs | skills/core/codex-system/system-skills/openai-docs | 2 | https://developers.openai.com/api/docs/guides/latest-model.md, https://developers.openai.com/mcp |
| skill-installer | skills/core/codex-system/system-skills/skill-installer | 4 | https://github.com/<owner, https://github.com/openai/skills/tree/main/skills/.curated, https://github.com/openai/skills/tree/main/skills/.experimental |
| biopython | skills/domains/bioinformatics/biology-toolkits/biopython | 3 | https://biopython.org/docs/latest/, https://biopython.org/docs/latest/Tutorial/, https://github.com/biopython/biopython |
| esm | skills/domains/bioinformatics/biology-toolkits/esm | 7 | https://bit.ly/3FKwcWd, https://forge.evolutionaryscale.ai, https://github.com/evolutionaryscale/esm |
| phylogenetics | skills/domains/bioinformatics/biology-toolkits/phylogenetics | 9 | http://etetoolkit.org/, http://www.iqtree.org/, http://www.microbesonline.org/fasttree/ |
| scikit-bio | skills/domains/bioinformatics/biology-toolkits/scikit-bio | 3 | https://forum.qiime2.org, https://github.com/scikit-bio/scikit-bio, https://scikit.bio/docs/latest/ |
| pysam | skills/domains/bioinformatics/genomics-io/pysam | 1 | https://pysam.readthedocs.io/ |
| tiledbvcf | skills/domains/bioinformatics/genomics-io/tiledbvcf | 4 | https://cloud.tiledb.com, https://cloud.tiledb.com/academy/, https://cloud.tiledb.com/academy/structure/life-sciences/population-genomics/ |
| zarr-python | skills/domains/bioinformatics/genomics-io/zarr-python | 7 | https://docs.dask.org/, https://docs.xarray.dev/, https://github.com/zarr-developers/zarr-python |
| geniml | skills/domains/bioinformatics/omics-analysis/geniml | 4 | https://docs.bedbase.org/geniml/, https://github.com/databio/geniml, https://github.com/databio/geniml.git |
| pydeseq2 | skills/domains/bioinformatics/omics-analysis/pydeseq2 | 2 | https://github.com/owkin/PyDESeq2, https://pydeseq2.readthedocs.io |
| dnanexus-integration | skills/domains/bioinformatics/platforms/dnanexus-integration | 3 | http://autodoc.dnanexus.com/, https://documentation.dnanexus.com/, https://github.com/dnanexus/dx-toolkit |
| lamindb | skills/domains/bioinformatics/platforms/lamindb | 5 | https://docs.lamin.ai, https://docs.lamin.ai/api, https://docs.lamin.ai/faq |
| latchbio-integration | skills/domains/bioinformatics/platforms/latchbio-integration | 4 | https://blog.latch.bio, https://docs.latch.bio, https://docs.latch.bio/api/latch.html |
| anndata | skills/domains/bioinformatics/single-cell/anndata | 4 | https://anndata.readthedocs.io/, https://github.com/scverse/anndata, https://scanpy.readthedocs.io/ |
| scanpy | skills/domains/bioinformatics/single-cell/scanpy | 3 | https://scanpy-tutorials.readthedocs.io/, https://scanpy.readthedocs.io/, https://scverse.org/ |
| scvelo | skills/domains/bioinformatics/single-cell/scvelo | 6 | http://velocyto.org/, https://cellrank.readthedocs.io/, https://dynamo-release.readthedocs.io/ |
| scvi-tools | skills/domains/bioinformatics/single-cell/scvi-tools | 3 | https://docs.scvi-tools.org/en/stable/, https://docs.scvi-tools.org/en/stable/api/index.html, https://docs.scvi-tools.org/en/stable/tutorials/index.html |
| neuropixels-analysis | skills/domains/bioinformatics/specialized/neuropixels-analysis | 7 | https://github.com/AllenInstitute/ecephys_spike_sorting, https://github.com/Julie-Fabre/bombcell, https://github.com/MouseLand/Kilosort |
| medical-imaging-classical-features | skills/domains/medical-imaging/medical-imaging-classical-features | 1 | https://theibsi.github.io/ |
| pydicom | skills/domains/medical-imaging/pydicom | 5 | https://pydicom.github.io/pydicom/dev/, https://pydicom.github.io/pydicom/dev/auto_examples/index.html, https://pydicom.github.io/pydicom/dev/guides/user/index.html |
| neurokit2 | skills/domains/medicine-clinical/neurokit2 | 4 | https://doi.org/10.3758/s13428-020-01516-y, https://github.com/neuropsychology/NeuroKit, https://github.com/neuropsychology/NeuroKit/zipball/dev |
| pyhealth | skills/domains/medicine-clinical/pyhealth | 2 | https://github.com/sunlabuiuc/PyHealth/issues, https://pyhealth.readthedocs.io/ |
| scikit-survival | skills/domains/medicine-clinical/scikit-survival | 3 | https://github.com/sebp/scikit-survival, https://scikit-survival.readthedocs.io/, https://scikit-survival.readthedocs.io/en/stable/api/index.html |
| latex-posters | skills/science/communication/latex-posters | 3 | https://doi.org/10.1234/paper}\\, https://github.com/username/project}, https://webaim.org/resources/contrastchecker/ |
| paper-2-web | skills/science/communication/paper-2-web | 2 | https://github.com/YuhangChen1/Paper2All, https://github.com/YuhangChen1/Paper2All.git |
| scientific-schematics | skills/science/communication/scientific-schematics | 7 | http://www.consort-statement.org/consort-statement/flow-diagram, https://matplotlib.org/, https://networkx.org/documentation/ |
| arxiv-database | skills/science/discovery/arxiv-database | 3 | http://arxiv.org/abs/2309.10668v1, http://arxiv.org/pdf/2309.10668v1, https://arxiv.org/abs/2309.10668 |
| bgpt-paper-search | skills/science/discovery/bgpt-paper-search | 2 | https://bgpt.pro/mcp, https://bgpt.pro/mcp/sse |
| biorxiv-database | skills/science/discovery/biorxiv-database | 4 | https://doi.org/10.1101/2024.01.15.123456, https://www.biorxiv.org/content/, https://www.biorxiv.org/content/10.1101/2024.01.15.123456v1 |
| citation-management | skills/science/discovery/citation-management | 13 | http://www.bibtex.org/, http://www.bibtex.org/Format/, https://api.crossref.org/ |
| openalex-database | skills/science/discovery/openalex-database | 5 | https://doi.org/10.1038/s41586-021-03819-2, https://doi.org/10.1126/science.abc1234, https://doi.org/10.7717/peerj.4375 |
| pubmed-database | skills/science/discovery/pubmed-database | 3 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/, https://pubmed.ncbi.nlm.nih.gov/help/, https://www.ncbi.nlm.nih.gov/books/NBK25501/ |
| pyzotero | skills/science/discovery/pyzotero | 3 | https://www.zotero.org/settings/keys, https://www.zotero.org/settings/keys/new, https://www.zotero.org/support/dev/web_api/v3/start |
| research-lookup | skills/science/discovery/research-lookup | 1 | https://api.parallel.ai |
| consciousness-council | skills/science/ideation/consciousness-council | 2 | https://ahkstrategies.net, https://themindbook.app |
| hypogenic | skills/science/ideation/hypogenic | 11 | https://aclanthology.org/2024.nlp4science-1.10/, https://aclanthology.org/2024.nlp4science-1.10/}, https://arxiv.org/abs/2410.17309 |
| what-if-oracle | skills/science/ideation/what-if-oracle | 4 | https://ahkstrategies.net, https://doi.org/10.5281/zenodo.18736841, https://doi.org/10.5281/zenodo.18807387 |
| modal | skills/tools/ai-ml/modal | 2 | https://modal.com, https://modal.com/docs |
| pufferlib | skills/tools/ai-ml/pufferlib | 2 | https://github.com/PufferAI/PufferLib, https://puffer.ai/docs.html |
| timesfm-forecasting | skills/tools/ai-ml/timesfm-forecasting | 7 | https://arxiv.org/abs/2310.10688, https://cloud.google.com/bigquery/docs/timesfm-model, https://download.pytorch.org/whl/cpu |
| torch-geometric | skills/tools/ai-ml/torch-geometric | 5 | https://data.pyg.org/whl/torch-${TORCH}+${CUDA}.html, https://github.com/pyg-team/pytorch_geometric, https://github.com/pyg-team/pytorch_geometric/tree/master/examples |
| transformers | skills/tools/ai-ml/transformers | 1 | https://huggingface.co/settings/tokens |
| aeon | skills/tools/data-science/aeon | 4 | https://github.com/aeon-toolkit/aeon, https://www.aeon-toolkit.org/, https://www.aeon-toolkit.org/en/stable/api_reference.html |
| matlab | skills/tools/data-science/matlab | 5 | https://docs.octave.org/latest/, https://octave.org/download, https://www.mathworks.com/help/matlab/ |
| networkx | skills/tools/data-science/networkx | 4 | https://github.com/networkx/networkx, https://networkx.org/documentation/latest/, https://networkx.org/documentation/latest/auto_examples/index.html |
| pymoo | skills/tools/data-science/pymoo | 1 | https://pymoo.org/ |
| scikit-learn | skills/tools/data-science/scikit-learn | 4 | https://scikit-learn.org/stable/, https://scikit-learn.org/stable/api/index.html, https://scikit-learn.org/stable/auto_examples/index.html |
| shap | skills/tools/data-science/shap | 2 | https://github.com/slundberg/shap, https://shap.readthedocs.io/ |
| sympy | skills/tools/data-science/sympy | 4 | https://docs.sympy.org/, https://docs.sympy.org/latest/reference/index.html, https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html |
| docx | skills/tools/documents-media/docx | 1 | https://example.com |
| markitdown | skills/tools/documents-media/markitdown | 8 | https://github.com/microsoft/markitdown, https://github.com/microsoft/markitdown.git, https://openrouter.ai |
| open-notebook | skills/tools/documents-media/open-notebook | 7 | http://localhost:5055, http://localhost:5055/api, http://localhost:5055/docs |
| parallel-web | skills/tools/documents-media/parallel-web | 6 | https://docs.example.com/api, https://docs.example.com/api-reference, https://docs.parallel.ai |
| perplexity-search | skills/tools/documents-media/perplexity-search | 9 | https://docs.litellm.ai/, https://docs.litellm.ai/docs/providers/openrouter, https://docs.perplexity.ai/ |
| webapp-testing | skills/tools/frontend/webapp-testing | 1 | http://localhost:5173 |
| generate-image | skills/tools/visualization/generate-image | 2 | https://openrouter.ai/keys, https://openrouter.ai/models |
| infographics | skills/tools/visualization/infographics | 1 | https://openrouter.ai/keys |
| markdown-mermaid-writing | skills/tools/visualization/markdown-mermaid-writing | 3 | https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/, https://github.com/SuperiorByteWorks-LLC/agent-project, https://mermaid.js.org/ |
| matplotlib | skills/tools/visualization/matplotlib | 4 | https://matplotlib.org/, https://matplotlib.org/cheatsheets/, https://matplotlib.org/stable/gallery/index.html |
| plotly | skills/tools/visualization/plotly | 3 | https://community.plotly.com/, https://plotly.com/python-api-reference/, https://plotly.com/python/ |
| academic-paper-writer-pro | skills/writing/research/academic-paper-writer-pro | 1 | https://github.com/tfboy1/academic-paper-writer |
| literature-review | skills/writing/research/literature-review | 10 | http://www.prisma-statement.org/, https://amstar.ca/, https://apastyle.apa.org/ |
| scholar-evaluation | skills/writing/research/scholar-evaluation | 1 | https://arxiv.org/abs/2510.16234 |
| venue-templates | skills/writing/research/venue-templates | 10 | https://cvpr.thecvf.com/Conferences/2024/AuthorGuidelines, https://grants.nih.gov/grants/how-to-apply-application-guide.html, https://icml.cc/Conferences/2024/StyleAuthorInstructions |

## Unknown-Origin Inventory

| Skill | Path | License | License files |
| --- | --- | --- | --- |
| mcp-builder | skills/core/codex-system/mcp-builder | Complete terms in LICENSE.txt | LICENSE.txt, license.txt |
| imagegen | skills/core/codex-system/system-skills/imagegen |  | LICENSE.txt, license.txt |
| openai-docs | skills/core/codex-system/system-skills/openai-docs |  | LICENSE.txt, license.txt |
| plugin-creator | skills/core/codex-system/system-skills/plugin-creator |  |  |
| skill-creator | skills/core/codex-system/system-skills/skill-creator |  | LICENSE.txt, license.txt |
| skill-installer | skills/core/codex-system/system-skills/skill-installer |  | LICENSE.txt, license.txt |
| bayesian-ppl-diagnostics | skills/domains/bayesian/bayesian-ppl-diagnostics | Apache-2.0 |  |
| pymc | skills/domains/bayesian/pymc | Apache License, Version 2.0 |  |
| simpy | skills/domains/bayesian/simpy | MIT License |  |
| statistical-analysis | skills/domains/bayesian/statistical-analysis | MIT License |  |
| statsmodels | skills/domains/bayesian/statsmodels | BSD License |  |
| biopython | skills/domains/bioinformatics/biology-toolkits/biopython | Unknown |  |
| esm | skills/domains/bioinformatics/biology-toolkits/esm | MIT license |  |
| etetoolkit | skills/domains/bioinformatics/biology-toolkits/etetoolkit | GPL-3.0 license |  |
| phylogenetics | skills/domains/bioinformatics/biology-toolkits/phylogenetics | Unknown |  |
| scikit-bio | skills/domains/bioinformatics/biology-toolkits/scikit-bio | BSD-3-Clause license |  |
| pysam | skills/domains/bioinformatics/genomics-io/pysam | MIT license |  |
| tiledbvcf | skills/domains/bioinformatics/genomics-io/tiledbvcf | MIT license |  |
| zarr-python | skills/domains/bioinformatics/genomics-io/zarr-python | MIT license |  |
| arboreto | skills/domains/bioinformatics/omics-analysis/arboreto | BSD-3-Clause license |  |
| deeptools | skills/domains/bioinformatics/omics-analysis/deeptools | BSD license |  |
| flowio | skills/domains/bioinformatics/omics-analysis/flowio | BSD-3-Clause license |  |
| geniml | skills/domains/bioinformatics/omics-analysis/geniml | BSD-2-Clause license |  |
| gtars | skills/domains/bioinformatics/omics-analysis/gtars | Unknown |  |
| polars-bio | skills/domains/bioinformatics/omics-analysis/polars-bio | https://github.com/biodatageeks/polars-bio/blob/main/LICENSE |  |
| pydeseq2 | skills/domains/bioinformatics/omics-analysis/pydeseq2 | MIT license |  |
| dnanexus-integration | skills/domains/bioinformatics/platforms/dnanexus-integration | Unknown |  |
| lamindb | skills/domains/bioinformatics/platforms/lamindb | Apache-2.0 license |  |
| latchbio-integration | skills/domains/bioinformatics/platforms/latchbio-integration | Unknown |  |
| anndata | skills/domains/bioinformatics/single-cell/anndata | BSD-3-Clause license |  |
| scanpy | skills/domains/bioinformatics/single-cell/scanpy | SD-3-Clause license |  |
| scvelo | skills/domains/bioinformatics/single-cell/scvelo | BSD-3-Clause |  |
| scvi-tools | skills/domains/bioinformatics/single-cell/scvi-tools | BSD-3-Clause license |  |
| neuropixels-analysis | skills/domains/bioinformatics/specialized/neuropixels-analysis | MIT license |  |
| medical-imaging-classical-features | skills/domains/medical-imaging/medical-imaging-classical-features | Apache-2.0 |  |
| medical-imaging-deep-learning | skills/domains/medical-imaging/medical-imaging-deep-learning | Apache-2.0 |  |
| pathml | skills/domains/medical-imaging/pathml | GPL-2.0 license |  |
| pydicom | skills/domains/medical-imaging/pydicom | https://github.com/pydicom/pydicom/blob/main/LICENSE |  |
| clinical-decision-support | skills/domains/medicine-clinical/clinical-decision-support | MIT License |  |
| clinical-reports | skills/domains/medicine-clinical/clinical-reports | MIT License |  |
| neurokit2 | skills/domains/medicine-clinical/neurokit2 | MIT license |  |
| pyhealth | skills/domains/medicine-clinical/pyhealth | MIT license |  |
| scikit-survival | skills/domains/medicine-clinical/scikit-survival | GPL-3.0 license |  |
| treatment-plans | skills/domains/medicine-clinical/treatment-plans | MIT license |  |
| latex-posters | skills/science/communication/latex-posters |  |  |
| paper-2-web | skills/science/communication/paper-2-web | Unknown |  |
| pptx-posters | skills/science/communication/pptx-posters | MIT license |  |
| scientific-schematics | skills/science/communication/scientific-schematics | MIT license |  |
| scientific-visualization | skills/science/communication/scientific-visualization | MIT license |  |
| arxiv-database | skills/science/discovery/arxiv-database | MIT |  |
| bgpt-paper-search | skills/science/discovery/bgpt-paper-search | MIT |  |
| biorxiv-database | skills/science/discovery/biorxiv-database | Unknown |  |
| citation-management | skills/science/discovery/citation-management | MIT License |  |
| openalex-database | skills/science/discovery/openalex-database | Unknown |  |
| pubmed-database | skills/science/discovery/pubmed-database | Unknown |  |
| pyzotero | skills/science/discovery/pyzotero | MIT License |  |
| research-lookup | skills/science/discovery/research-lookup | MIT license |  |
| consciousness-council | skills/science/ideation/consciousness-council | MIT license |  |
| hypogenic | skills/science/ideation/hypogenic | MIT license |  |
| hypothesis-generation | skills/science/ideation/hypothesis-generation | MIT license |  |
| scientific-brainstorming | skills/science/ideation/scientific-brainstorming | MIT license |  |
| scientific-critical-thinking | skills/science/ideation/scientific-critical-thinking | MIT license |  |
| what-if-oracle | skills/science/ideation/what-if-oracle | MIT license |  |
| modal | skills/tools/ai-ml/modal | Apache-2.0 license |  |
| pufferlib | skills/tools/ai-ml/pufferlib | MIT license |  |
| pytorch-lightning | skills/tools/ai-ml/pytorch-lightning | Apache-2.0 license |  |
| stable-baselines3 | skills/tools/ai-ml/stable-baselines3 | MIT license |  |
| timesfm-forecasting | skills/tools/ai-ml/timesfm-forecasting | Apache-2.0 license |  |
| torch-geometric | skills/tools/ai-ml/torch-geometric | MIT license |  |
| transformers | skills/tools/ai-ml/transformers | Apache-2.0 license |  |
| aeon | skills/tools/data-science/aeon | BSD-3-Clause license |  |
| dask | skills/tools/data-science/dask | BSD-3-Clause license |  |
| exploratory-data-analysis | skills/tools/data-science/exploratory-data-analysis | MIT license |  |
| geopandas | skills/tools/data-science/geopandas | BSD-3-Clause license |  |
| matlab | skills/tools/data-science/matlab | For MATLAB (https://www.mathworks.com/pricing-licensing.html) and for Octave (GNU General Public License version 3) |  |
| networkx | skills/tools/data-science/networkx | 3-clause BSD license |  |
| polars | skills/tools/data-science/polars | https://github.com/pola-rs/polars/blob/main/LICENSE |  |
| pymoo | skills/tools/data-science/pymoo | Apache-2.0 license |  |
| scikit-learn | skills/tools/data-science/scikit-learn | BSD-3-Clause license |  |
| shap | skills/tools/data-science/shap | MIT license |  |
| sympy | skills/tools/data-science/sympy | https://github.com/sympy/sympy/blob/master/LICENSE |  |
| umap-learn | skills/tools/data-science/umap-learn | BSD-3-Clause license |  |
| vaex | skills/tools/data-science/vaex | MIT license |  |
| docx | skills/tools/documents-media/docx | Proprietary. LICENSE.txt has complete terms | LICENSE.txt, license.txt |
| get-available-resources | skills/tools/documents-media/get-available-resources | MIT license |  |
| markitdown | skills/tools/documents-media/markitdown | MIT license |  |
| open-notebook | skills/tools/documents-media/open-notebook | MIT |  |
| parallel-web | skills/tools/documents-media/parallel-web | MIT license |  |
| pdf | skills/tools/documents-media/pdf | Proprietary. LICENSE.txt has complete terms | LICENSE.txt, license.txt |
| perplexity-search | skills/tools/documents-media/perplexity-search | MIT license |  |
| xlsx | skills/tools/documents-media/xlsx | Proprietary. LICENSE.txt has complete terms | LICENSE.txt, license.txt |
| brand-creative-assets | skills/tools/frontend/brand-creative-assets |  |  |
| design-system-tokens | skills/tools/frontend/design-system-tokens |  |  |
| implementation-react-tailwind | skills/tools/frontend/implementation-react-tailwind |  |  |
| product-ux-planning | skills/tools/frontend/product-ux-planning |  |  |
| responsive-accessibility-review | skills/tools/frontend/responsive-accessibility-review |  |  |
| visual-direction | skills/tools/frontend/visual-direction |  |  |
| webapp-testing | skills/tools/frontend/webapp-testing | Complete terms in LICENSE.txt | LICENSE.txt, license.txt |
| canvas-design | skills/tools/visualization/canvas-design | Complete terms in LICENSE.txt | LICENSE.txt, license.txt |
| generate-image | skills/tools/visualization/generate-image | MIT license |  |
| infographics | skills/tools/visualization/infographics |  |  |
| markdown-mermaid-writing | skills/tools/visualization/markdown-mermaid-writing | Apache-2.0 |  |
| matplotlib | skills/tools/visualization/matplotlib | https://github.com/matplotlib/matplotlib/tree/main/LICENSE |  |
| plotly | skills/tools/visualization/plotly | MIT license |  |
| seaborn | skills/tools/visualization/seaborn | BSD-3-Clause license |  |
| theme-factory | skills/tools/visualization/theme-factory | Complete terms in LICENSE.txt | LICENSE.txt, license.txt |
| academic-paper-writer-pro | skills/writing/research/academic-paper-writer-pro |  |  |
| content-generation | skills/writing/research/content-generation |  |  |
| literature-review | skills/writing/research/literature-review | MIT license |  |
| ocr-kb | skills/writing/research/ocr-kb | Proprietary. LICENSE.txt has complete terms |  |
| peer-review | skills/writing/research/peer-review | MIT license |  |
| research-grants | skills/writing/research/research-grants | MIT license |  |
| scholar-evaluation | skills/writing/research/scholar-evaluation | MIT license |  |
| scientific-writing | skills/writing/research/scientific-writing | MIT license |  |
| venue-templates | skills/writing/research/venue-templates | MIT license |  |

## Going Forward

For every newly cloned or adapted skill, add provenance metadata before committing it:

```yaml
provenance: external-adapted
source_repo_url: https://github.com/<owner>/<repo>
source_path: path/to/original/skill
source_ref: <full commit sha or tag>
source_imported_at: YYYY-MM-DD
source_license: <license id or URL>
source_note: <short note on local changes>
metadata:
  skill-author: <upstream author or organization>
```

Use `provenance: user-authored` for original local work. Historical `unknown` is allowed only when the exact source was not recorded; do not guess URLs, refs, or licenses.

Machine-readable audit: `docs/skill_provenance_audit.json`
