# GWAS Summary Statistics Databases

Reviewed on 2026-07-13 from private Notion `GWAS汇总数据库清单` images plus public official sources. Use official source pages and APIs for live retrieval.

## Routing Table

| Provider | Best for | Access pattern | Required checks |
|---|---|---|---|
| NHGRI-EBI GWAS Catalog Summary Statistics | Published GWAS studies, harmonized summary statistics where available, GCST-indexed study lookup, broad trait search | Web portal, REST APIs, and public FTP/download links | GCST accession, EFO trait mapping, genome build, harmonized vs submitted data, effect allele fields, citation of original study and Catalog |
| OpenGWAS | Mendelian randomization, rapid cross-study variant/trait lookup, TwoSampleMR/gwasglue workflows, large curated summary-stat collection | Web/API through OpenGWAS ecosystem and R/Python clients where appropriate | Dataset ID, API access policy, ancestry, sample overlap, harmonization assumptions, LD/reference panel assumptions |
| GWAS Atlas | Browseable public summary-stat atlas with plots, MAGMA, heritability, and genetic correlation outputs; useful as secondary exploration and UK Biobank-style broad scans | Web portal and downloads from original source links | Release date/version, whether the dataset is older than the project needs, original source terms, trait mapping, and whether full files are mirrored or linked |
| FinnGen public results | Finnish biobank endpoints, disease/clinical traits, large release-specific public summary statistics | Release-specific browser, endpoint pages, Google Cloud download after the project access form/email instructions | Release number/date, endpoint definition, sample size, variant count, allele-frequency convention, Finnish ancestry/context, and citation requirements |

## Selection Workflow

1. Define the trait, organism, population/ancestry, genome build, and downstream method.
2. If a GCST accession or publication is known, check GWAS Catalog first.
3. If the task is MR or cross-trait lookup, check OpenGWAS dataset IDs and access policy.
4. If the task is broad exploration or quick trait landscape, use GWAS Atlas as a secondary discovery aid and verify against original sources.
5. If the phenotype is likely covered by FinnGen endpoints or Finnish ancestry matters, check the latest FinnGen release and endpoint definitions.
6. Before analysis, write a manifest with provider, release, trait/endpoint ID, download URL/API query, genome build, sample size, ancestry, harmonization status, and access date.

## Caveats

- Summary statistics are not interchangeable across providers; allele orientation, genome build, imputation, harmonization, and trait definitions vary.
- Do not merge studies without checking sample overlap and ancestry compatibility.
- Prefer provider APIs or scripted downloads over manual browser-only steps for reproducibility.
- Cite both the database and original GWAS publication or release where applicable.
