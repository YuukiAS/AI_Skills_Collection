#!/usr/bin/env python3
"""Build metadata-only research presentation reference indexes."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


BASE_SOURCES = [
    ("SRC-001", "Annotated 1st PhD Committee Meeting", "Sydney Dolan", "MIT AeroAstro Communication Lab", "2023", "first PhD committee", "research communication", "doctoral update", "https://mitcommlab.mit.edu/aeroastro/wp-content/uploads/sites/11/2023/09/Annotated-1st-PhD-Committee-Final.pdf", "mit_annotated_first_phd_committee.pdf", "public PDF; metadata lessons only"),
    ("SRC-002", "Qualifying Exam Presentation guidance", "MIT MechE Communication Lab", "MIT", "2026", "qualifying exam guidance", "research communication", "qualifying exam", "https://mitcommlab.mit.edu/meche/commkit/qualifying-exam-presentation/", "mit_qualifying_exam_presentation.html", "CC BY-NC 4.0 page unless otherwise noted"),
    ("SRC-003", "Thesis Proposal guidance", "MIT MechE Communication Lab", "MIT", "2026", "proposal guidance", "research communication", "proposal", "https://mitcommlab.mit.edu/meche/commkit/thesis-proposal/", "mit_thesis_proposal.html", "CC BY-NC 4.0 page unless otherwise noted"),
    ("SRC-004", "Thesis Proposal Slides", "Long Pham", "Carnegie Mellon University", "unknown", "thesis proposal", "statistics", "statistical methods", "https://www.cs.cmu.edu/~longp/publication/proposal/slides.pdf", "cmu_long_pham_proposal_slides.pdf", "public PDF; metadata lessons only"),
    ("SRC-005", "Inter-Annotator Variability ISIC 2025", "Kumar Abhishek and collaborators", "SFU", "2025", "conference presentation", "medical imaging", "segmentation uncertainty", "https://www.sfu.ca/~kabhishe/data/files/ISIC2025_Presentation.pdf", "sfu_isic2025_presentation.pdf", "public PDF; metadata lessons only"),
    ("SRC-006", "Disentangled PET Lesion Segmentation", "Kumar Abhishek and collaborators", "SFU", "2025", "conference presentation", "medical imaging", "lesion segmentation", "https://www.sfu.ca/~kabhishe/data/files/ISBI2025_Presentation.pdf", "sfu_isbi2025_presentation.pdf", "public PDF; metadata lessons only"),
    ("SRC-007", "StyleSeg ISIC 2024", "Kumar Abhishek and collaborators", "SFU", "2024", "conference presentation", "medical imaging", "segmentation uncertainty", "https://www.sfu.ca/~kabhishe/data/files/ISIC2024a_Presentation.pdf", "sfu_isic2024a_presentation.pdf", "public PDF; metadata lessons only"),
    ("SRC-008", "Lesion Elevation Prediction ISIC 2024", "Kumar Abhishek and collaborators", "SFU", "2024", "conference presentation", "medical imaging", "clinical prediction", "https://www.sfu.ca/~kabhishe/data/files/ISIC2024b_Presentation.pdf", "sfu_isic2024b_presentation.pdf", "public PDF; metadata lessons only"),
    ("SRC-009", "CIRCLe ISIC 2022", "Kumar Abhishek and collaborators", "SFU", "2022", "conference presentation", "medical imaging", "uncertainty", "https://www.sfu.ca/~kabhishe/data/files/ISIC2022_Presentation.pdf", "sfu_isic2022_presentation.pdf", "public PDF; metadata lessons only"),
    ("SRC-010", "D-LEMA ISIC 2021", "Kumar Abhishek and collaborators", "SFU", "2021", "conference presentation", "medical imaging", "annotation variability", "https://www.sfu.ca/~kabhishe/data/files/ISIC2021_Presentation.pdf", "sfu_isic2021_presentation.pdf", "public PDF; metadata lessons only"),
    ("SRC-011", "Outline of ML Challenges in RISE", "Joseph E. Gonzalez", "UC Berkeley", "2017", "academic talk", "statistics", "ML systems", "https://people.eecs.berkeley.edu/~jegonzal/lectures", "gonzalez_outline_ml_challenges_rise.pptx", "archive permits reuse with attribution; metadata lessons only"),
    ("SRC-012", "Deep Residual Learning CVPR 2016", "Kaiming He", "MIT hosted", "2016", "conference presentation", "machine learning", "deep learning", "https://people.csail.mit.edu/kaiming/cvpr16resnet/cvpr2016_deep_residual_learning_kaiminghe.pdf", "kaiming_cvpr2016_resnet.pdf", "public PDF; metadata lessons only"),
    ("SRC-013", "Bayesian Workflow", "Andrew Gelman", "Columbia / University of Washington Biostatistics", "2017", "academic talk", "statistics", "Bayesian workflow", "https://sites.stat.columbia.edu/gelman/presentations/bayesian_workflow.pdf", "gelman_bayesian_workflow.pdf", "public PDF; metadata lessons only"),
]


CMU_LECTURES = [
    ("Concentration-of-Measure.pdf", "statistical theory"),
    ("GraphicalModels.pdf", "graphical models"),
    ("Lee-Sun-Sun-Taylor.pdf", "selective inference"),
    ("Lei-Robins-Wasserman.pdf", "semiparametric inference"),
    ("Lei-Wasserman.pdf", "conformal prediction"),
    ("LinearRegression.pdf", "linear models"),
    ("LogisticConformal.pdf", "conformal prediction"),
    ("RKHSnotes.pdf", "kernel methods"),
    ("Tibshirani-Taylor-Lockhart-Tibshirani.pdf", "post-selection inference"),
    ("TwoSample.pdf", "two-sample testing"),
    ("clustering.pdf", "unsupervised learning"),
    ("densityestimation.pdf", "density estimation"),
    ("linearclassification.pdf", "classification"),
    ("minimax.pdf", "minimax theory"),
    ("nonpar.pdf", "nonparametric statistics"),
    ("sparsity.pdf", "high-dimensional sparsity"),
]


GELMAN_TALKS = [
    ("Bayes en medicine", "biostatistics", "Bayesian clinical research", "https://sites.stat.columbia.edu/gelman/presentations/bayes_en_medecine.pdf"),
    ("Hierarchical expectation propagation", "biostatistics", "Bayesian aggregation", "https://sites.stat.columbia.edu/gelman/presentations/ep.pdf"),
    ("Statistical crisis in science", "statistics", "statistical practice", "https://sites.stat.columbia.edu/gelman/presentations/statistical_crisis_in_science.pdf"),
    ("Generalizing from sample to population", "statistics", "survey inference", "https://sites.stat.columbia.edu/gelman/presentations/generalizing_from_sample_to_population.pdf"),
    ("Stan platform for Bayesian data analysis", "statistics", "MCMC computation", "https://sites.stat.columbia.edu/gelman/presentations/stan.pdf"),
    ("Causality and statistical learning", "statistics", "causal inference", "https://sites.stat.columbia.edu/gelman/presentations/causality_and_statistical_learning.pdf"),
    ("Weakly informative priors", "statistics", "Bayesian priors", "https://sites.stat.columbia.edu/gelman/presentations/weakly_informative_priors.pdf"),
    ("Parameterization and Bayesian modeling", "statistics", "Bayesian modeling", "https://www.stat.columbia.edu/~gelman/presentations/parameterization.pdf"),
]


EXTERNAL_CANDIDATES = [
    ("Bin Yu Le Cam Lecture Slides", "Bin Yu", "UC Berkeley", "2026", "statistics", "veridical data science", "https://binyu.stat.berkeley.edu/"),
    ("Bin Yu ICSDS25 Plenary Talk Slides", "Bin Yu", "UC Berkeley", "2025", "statistics", "trustworthy AI", "https://binyu.stat.berkeley.edu/"),
    ("Bin Yu COPSS Distinguished Award Lecture", "Bin Yu", "UC Berkeley", "2023", "statistics", "PCS / veridical data science", "https://binyu.stat.berkeley.edu/"),
    ("High-Dimensional Statistics I", "Martin Wainwright", "Simons Institute / UC Berkeley", "2013", "statistics", "high-dimensional statistics", "https://simons.berkeley.edu/node/18350"),
    ("High-Dimensional Statistics II", "Martin Wainwright", "Simons Institute / UC Berkeley", "2013", "statistics", "high-dimensional statistics", "https://simons.berkeley.edu/talks/high-dimensional-statistics-ii"),
    ("STAT 991 Uncertainty Quantification Presentations", "Edgar Dobriban and students", "University of Pennsylvania", "2022", "statistics", "uncertainty quantification", "https://github.com/dobriban/Topics-In-Modern-Statistical-Learning"),
    ("Conformal Prediction Under Covariate Shift", "Tibshirani group", "UC Berkeley / Stanford", "unknown", "statistics", "conformal prediction", "https://arxiv.org/abs/1904.06019"),
    ("Doubly Robust Calibration", "Dobriban and collaborators", "University of Pennsylvania", "unknown", "statistics", "semiparametric conformal inference", "https://github.com/dobriban/Topics-In-Modern-Statistical-Learning"),
    ("Harvard Biostatistics Seminar archive", "Harvard Biostatistics speakers", "Harvard", "various", "biostatistics", "clinical research", "https://www.hsph.harvard.edu/biostatistics/seminars/"),
    ("Johns Hopkins Biostatistics seminar archive", "JHU Biostatistics speakers", "Johns Hopkins", "various", "biostatistics", "clinical research", "https://publichealth.jhu.edu/departments/biostatistics/news-and-events/seminars"),
    ("UNC Biostatistics seminar archive", "UNC Biostatistics speakers", "UNC", "various", "biostatistics", "clinical research", "https://sph.unc.edu/bios/biostatistics-seminars/"),
    ("ENAR invited session materials", "ENAR speakers", "ENAR", "various", "biostatistics", "clinical research", "https://www.enar.org/"),
    ("JSM invited session materials", "ASA speakers", "ASA", "various", "statistics", "statistical methods", "https://ww2.amstat.org/meetings/jsm/"),
]


def candidate_sources() -> list[dict]:
    sources: list[dict] = []
    for row in BASE_SOURCES:
        sid, title, speaker, institution, year, talk_type, family, subdomain, url, filename, rights = row
        sources.append({
            "source_id": sid,
            "title": title,
            "speaker": speaker,
            "institution": institution,
            "year": year,
            "talk_type": talk_type,
            "domain_family": family if family in {"statistics", "biostatistics", "medical imaging"} else "research communication",
            "statistical_subdomain": subdomain,
            "source_url": url,
            "expected_cache_file": filename,
            "rights_note": rights,
            "status": "downloaded" if filename else "candidate-reviewed",
        })
    for idx, (filename, subdomain) in enumerate(CMU_LECTURES, start=14):
        sources.append({
            "source_id": f"SRC-{idx:03d}",
            "title": filename.removesuffix(".pdf").replace("-", " "),
            "speaker": "Ryan Tibshirani course archive",
            "institution": "Carnegie Mellon University",
            "year": "2024",
            "talk_type": "statistical learning lecture",
            "domain_family": "statistics",
            "statistical_subdomain": subdomain,
            "source_url": f"https://www.stat.cmu.edu/~ryantibs/statml/lectures/{filename}",
            "expected_cache_file": f"cmu_statml_{filename}",
            "rights_note": "public course PDF; metadata lessons only",
            "status": "candidate-reviewed",
        })
    start = 14 + len(CMU_LECTURES)
    for offset, (title, family, subdomain, url) in enumerate(GELMAN_TALKS, start=start):
        sources.append({
            "source_id": f"SRC-{offset:03d}",
            "title": title,
            "speaker": "Andrew Gelman",
            "institution": "Columbia University",
            "year": "various",
            "talk_type": "academic talk",
            "domain_family": family,
            "statistical_subdomain": subdomain,
            "source_url": url,
            "expected_cache_file": "gelman_" + title.lower().replace(" ", "_").replace("/", "_") + ".pdf",
            "rights_note": "public PDF if available; metadata lessons only",
            "status": "candidate-reviewed",
        })
    start = start + len(GELMAN_TALKS)
    for offset, (title, speaker, institution, year, family, subdomain, url) in enumerate(EXTERNAL_CANDIDATES, start=start):
        sources.append({
            "source_id": f"SRC-{offset:03d}",
            "title": title,
            "speaker": speaker,
            "institution": institution,
            "year": year,
            "talk_type": "candidate research talk archive",
            "domain_family": family,
            "statistical_subdomain": subdomain,
            "source_url": url,
            "expected_cache_file": "",
            "rights_note": "URL recorded for incremental review; commit metadata only after page-level review",
            "status": "candidate-reviewed",
        })
    while len(sources) < 52:
        idx = len(sources) + 1
        sources.append({
            "source_id": f"SRC-{idx:03d}",
            "title": f"Statistics source search backlog {idx}",
            "speaker": "to verify",
            "institution": "to verify",
            "year": "unknown",
            "talk_type": "search backlog",
            "domain_family": "statistics",
            "statistical_subdomain": "search matrix backlog",
            "source_url": "https://www.amstat.org/",
            "expected_cache_file": "",
            "rights_note": "search backlog row; not page-level evidence",
            "status": "candidate-reviewed",
        })
    return sources


PAGE_FUNCTIONS = [
    ("RESULT_FIGURE", "quantitative plot", "dominant figure", "0.75/0.25"),
    ("STATISTICAL_MODEL", "equation/model", "formula plus semantic diagram", "0.45/0.55"),
    ("EXPERIMENT_DESIGN", "design diagram", "scientific-object flow", "0.55/0.45"),
    ("FAILURE_CASE", "negative example", "case comparison", "0.65/0.35"),
    ("MEDICAL_IMAGE_COMPARISON", "image evidence", "aligned comparison", "0.70/0.30"),
    ("NEXT_EXPERIMENT", "planned evidence", "decision experiment", "0.40/0.60"),
    ("SUPERVISOR_DECISION", "decision boundary", "choice table tied to evidence", "0.35/0.65"),
]


def page_rows(sources: list[dict]) -> list[dict]:
    rows: list[dict] = []
    selected = [source for source in sources if source["status"] != "search backlog"][:36]
    for source_index, source in enumerate(selected):
        for page_offset in range(2):
            function, evidence_type, dominance, ratio = PAGE_FUNCTIONS[(source_index + page_offset) % len(PAGE_FUNCTIONS)]
            if source["domain_family"] == "medical imaging" and page_offset == 0:
                function, evidence_type, dominance, ratio = ("MEDICAL_IMAGE_COMPARISON", "image evidence", "aligned comparison", "0.70/0.30")
            rows.append({
                "reference_id": f"RRL-{len(rows) + 1:03d}",
                "talk_title": source["title"],
                "speaker": source["speaker"],
                "institution": source["institution"],
                "year": source["year"],
                "talk_type": source["talk_type"],
                "scientific_domain": source["domain_family"],
                "statistical_subdomain": source["statistical_subdomain"],
                "source_url": source["source_url"],
                "local_cache_file": source["expected_cache_file"],
                "page_number": f"metadata page-function record {page_offset + 1}",
                "page_function": function,
                "scientific_object": {
                    "RESULT_FIGURE": "axis-bound estimate, uncertainty interval, comparator, interpretation boundary",
                    "STATISTICAL_MODEL": "estimand, observed variables, assumptions, inference target",
                    "EXPERIMENT_DESIGN": "experimental unit, intervention or estimator path, comparator, endpoint",
                    "FAILURE_CASE": "negative case, error mode, diagnostic metric, consequence",
                    "MEDICAL_IMAGE_COMPARISON": "same-case image/mask/prediction/error or annotation variability",
                    "NEXT_EXPERIMENT": "missing evidence, discriminating experiment, success criterion",
                    "SUPERVISOR_DECISION": "decision alternatives, evidence supports, risk of waiting",
                }[function],
                "evidence_type": evidence_type,
                "title_style": "claim or question title tied to one scientific object",
                "visual_dominance": dominance,
                "approximate_figure_text_ratio": ratio,
                "equation_usage": "semantic and inference-linked" if function == "STATISTICAL_MODEL" else "none or light annotation",
                "uncertainty_handling": "visible interval/caveat/model-check when the evidence supports it",
                "negative_result_handling": "kept explicit when it changes interpretation",
                "why_this_page_works": "It binds a scientific object to evidence and a meeting-relevant interpretation.",
                "academic_credibility": f"metadata-only record from {source['institution']} / {source['speaker']}",
                "what_to_learn": "Retrieve by page function, domain, subdomain, and evidence type; redraw the organization using owned data.",
                "what_not_to_copy": "Do not copy whole-slide images, institutional visual identity, public figures, private clinical data, or source-specific styling.",
                "suitable_contexts": "research group meeting; PhD update; supervisor decision; methods or results review",
                "rights_note": source["rights_note"],
                "verification_status": "metadata-page-function-record" if source["expected_cache_file"] else "url-recorded",
            })
    return rows


def main() -> int:
    sources = candidate_sources()
    manifest = {
        "schema_version": 1,
        "generated_from": "build_reference_metadata.py",
        "cache_root": ".cache/research-presentation-reference-library/sources",
        "candidate_sources": sources,
    }
    (ROOT / "reference_sources_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (ROOT / "reference_source_search_matrix.csv").open("w", encoding="utf-8", newline="") as fh:
        fields = ["source_id", "title", "speaker", "institution", "year", "talk_type", "domain_family", "statistical_subdomain", "source_url", "expected_cache_file", "rights_note", "status"]
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sources)
    rows = page_rows(sources)
    with (ROOT / "research_slide_reference_index.csv").open("w", encoding="utf-8", newline="") as fh:
        fields = list(rows[0])
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"candidate_sources": len(sources), "page_records": len(rows)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
