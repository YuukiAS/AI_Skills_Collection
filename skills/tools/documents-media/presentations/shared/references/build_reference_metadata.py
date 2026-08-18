#!/usr/bin/env python3
"""Build metadata-only research presentation reference indexes.

The committed page library is intentionally small and inspection-backed. Source
registry rows can be candidate backlog, but page-level rows are emitted only from
INSPECTED_PAGE_SPECS after an actual cached page was opened/rendered during a
review round. Do not infer page functions from source order.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[5]
CACHE_ROOT = REPO_ROOT / ".cache" / "research-presentation-reference-library"
SOURCE_CACHE = CACHE_ROOT / "sources"
RENDER_CACHE = CACHE_ROOT / "inspection" / "rendered_pages"

SOURCE_FIELDS = [
    "source_id",
    "title",
    "speaker",
    "institution",
    "year",
    "talk_type",
    "domain_family",
    "statistical_subdomain",
    "source_url",
    "expected_cache_file",
    "source_tier",
    "verification_status",
    "rights_note",
]

PAGE_FIELDS = [
    "reference_id",
    "source_id",
    "talk_title",
    "speaker",
    "institution",
    "source_url",
    "local_cache_file",
    "actual_page_number",
    "page_function",
    "scientific_object",
    "evidence_type",
    "title_style",
    "visual_dominance",
    "approximate_figure_text_ratio",
    "equation_usage",
    "uncertainty_handling",
    "negative_result_handling",
    "why_this_specific_page_works",
    "what_to_learn",
    "what_not_to_copy",
    "suitable_contexts",
    "rights_note",
    "verification_status",
    "source_file_sha256",
    "rendered_page_sha256",
    "visible_page_title",
    "short_page_specific_observation",
]


def source(
    source_id: str,
    title: str,
    speaker: str,
    institution: str,
    year: str,
    talk_type: str,
    domain_family: str,
    subdomain: str,
    url: str,
    filename: str,
    tier: str,
    status: str,
    rights: str,
) -> dict[str, str]:
    return {
        "source_id": source_id,
        "title": title,
        "speaker": speaker,
        "institution": institution,
        "year": year,
        "talk_type": talk_type,
        "domain_family": domain_family,
        "statistical_subdomain": subdomain,
        "source_url": url,
        "expected_cache_file": filename,
        "source_tier": tier,
        "verification_status": status,
        "rights_note": rights,
    }


BASE_SOURCES = [
    source("SRC-001", "Annotated 1st PhD Committee Meeting", "Sydney Dolan", "MIT AeroAstro Communication Lab", "2023", "first PhD committee", "research communication", "doctoral update", "https://mitcommlab.mit.edu/aeroastro/wp-content/uploads/sites/11/2023/09/Annotated-1st-PhD-Committee-Final.pdf", "mit_annotated_first_phd_committee.pdf", "PRIMARY_RESEARCH_PRESENTATION", "downloaded_inspected", "public PDF; metadata lessons only"),
    source("SRC-002", "Qualifying Exam Presentation guidance", "MIT MechE Communication Lab", "MIT", "2026", "qualifying exam guidance", "research communication", "qualifying exam", "https://mitcommlab.mit.edu/meche/commkit/qualifying-exam-presentation/", "mit_qualifying_exam_presentation.html", "PRESENTATION_GUIDANCE", "downloaded_uninspected", "CC BY-NC 4.0 page unless otherwise noted"),
    source("SRC-003", "Thesis Proposal guidance", "MIT MechE Communication Lab", "MIT", "2026", "proposal guidance", "research communication", "proposal", "https://mitcommlab.mit.edu/meche/commkit/thesis-proposal/", "mit_thesis_proposal.html", "PRESENTATION_GUIDANCE", "downloaded_uninspected", "CC BY-NC 4.0 page unless otherwise noted"),
    source("SRC-004", "Thesis Proposal Slides", "Long Pham", "Carnegie Mellon University", "unknown", "thesis proposal", "statistics", "hybrid resource-bound analysis", "https://www.cs.cmu.edu/~longp/publication/proposal/slides.pdf", "cmu_long_pham_proposal_slides.pdf", "PRIMARY_RESEARCH_PRESENTATION", "downloaded_inspected", "public PDF; metadata lessons only"),
    source("SRC-005", "What Can We Learn from Inter-Annotator Variability in Skin Lesion Segmentation?", "Kumar Abhishek and collaborators", "SFU / MICCAI 2025", "2025", "conference research talk", "medical imaging", "annotation variability", "https://www.sfu.ca/~kabhishe/data/files/ISIC2025_Presentation.pdf", "sfu_isic2025_presentation.pdf", "PRIMARY_RESEARCH_PRESENTATION", "downloaded_inspected", "public PDF; metadata lessons only"),
    source("SRC-006", "Disentangled PET Lesion Segmentation", "Kumar Abhishek and collaborators", "SFU / ISBI 2025", "2025", "conference research talk", "medical imaging", "lesion segmentation", "https://www.sfu.ca/~kabhishe/data/files/ISBI2025_Presentation.pdf", "sfu_isbi2025_presentation.pdf", "PRIMARY_RESEARCH_PRESENTATION", "downloaded_inspected", "public PDF; metadata lessons only"),
    source("SRC-007", "StyleSeg ISIC 2024", "Kumar Abhishek and collaborators", "SFU", "2024", "conference research talk", "medical imaging", "segmentation uncertainty", "https://www.sfu.ca/~kabhishe/data/files/ISIC2024a_Presentation.pdf", "sfu_isic2024a_presentation.pdf", "PRIMARY_RESEARCH_PRESENTATION", "downloaded_uninspected", "public PDF; metadata lessons only"),
    source("SRC-008", "Lesion Elevation Prediction ISIC 2024", "Kumar Abhishek and collaborators", "SFU", "2024", "conference research talk", "medical imaging", "clinical prediction", "https://www.sfu.ca/~kabhishe/data/files/ISIC2024b_Presentation.pdf", "sfu_isic2024b_presentation.pdf", "PRIMARY_RESEARCH_PRESENTATION", "downloaded_uninspected", "public PDF; metadata lessons only"),
    source("SRC-009", "CIRCLe ISIC 2022", "Kumar Abhishek and collaborators", "SFU", "2022", "conference research talk", "medical imaging", "uncertainty", "https://www.sfu.ca/~kabhishe/data/files/ISIC2022_Presentation.pdf", "sfu_isic2022_presentation.pdf", "PRIMARY_RESEARCH_PRESENTATION", "downloaded_uninspected", "public PDF; metadata lessons only"),
    source("SRC-010", "D-LEMA ISIC 2021", "Kumar Abhishek and collaborators", "SFU", "2021", "conference research talk", "medical imaging", "annotation variability", "https://www.sfu.ca/~kabhishe/data/files/ISIC2021_Presentation.pdf", "sfu_isic2021_presentation.pdf", "PRIMARY_RESEARCH_PRESENTATION", "downloaded_uninspected", "public PDF; metadata lessons only"),
    source("SRC-011", "Outline of ML Challenges in RISE", "Joseph E. Gonzalez", "UC Berkeley", "2017", "academic talk", "machine learning", "ML systems", "https://people.eecs.berkeley.edu/~jegonzal/lectures", "gonzalez_outline_ml_challenges_rise.pptx", "PRIMARY_RESEARCH_PRESENTATION", "downloaded_uninspected", "archive permits reuse with attribution; metadata lessons only"),
    source("SRC-012", "Deep Residual Learning CVPR 2016", "Kaiming He", "MIT hosted / CVPR", "2016", "conference research talk", "machine learning", "deep learning", "https://people.csail.mit.edu/kaiming/cvpr16resnet/cvpr2016_deep_residual_learning_kaiminghe.pdf", "kaiming_cvpr2016_resnet.pdf", "PRIMARY_RESEARCH_PRESENTATION", "downloaded_uninspected", "public PDF; metadata lessons only"),
    source("SRC-013", "Bayesian Workflow", "Andrew Gelman", "Columbia / University of Washington Biostatistics", "2017", "invited academic talk", "statistics", "Bayesian workflow", "https://sites.stat.columbia.edu/gelman/presentations/bayesian_workflow.pdf", "gelman_actual_bayesian_workflow.pdf", "PRIMARY_RESEARCH_PRESENTATION", "downloaded_inspected", "public PDF; metadata lessons only"),
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

GELMAN_ACTUAL_TALKS = [
    ("SRC-054", "Should the problems with polls make us worry about the quality of health surveys?", "Centers for Disease Control and Prevention", "2017", "biostatistics", "survey nonresponse / MRP", "https://sites.stat.columbia.edu/gelman/presentations/mrp_talk_cdc.pdf", "gelman_actual_mrp_talk_cdc.pdf", "downloaded_inspected"),
    ("SRC-055", "Taking Bayesian inference seriously", "Harvard conference on Big Data", "2016", "statistics", "Bayesian inference", "https://sites.stat.columbia.edu/gelman/presentations/bayes_harvard_bigdata.pdf", "gelman_actual_bayes_harvard_bigdata.pdf", "downloaded_inspected"),
    ("SRC-056", "Toward Routine Use of Informative Priors", "ICML workshop on data-efficient machine learning", "2016", "statistics", "Bayesian priors", "https://sites.stat.columbia.edu/gelman/presentations/routine_priors.pdf", "gelman_actual_routine_priors.pdf", "downloaded_inspected"),
    ("SRC-057", "Bayes en médecine : Les possibilités et les risques", "Conférence EPICLIN", "2016", "biostatistics", "Bayesian clinical research", "https://sites.stat.columbia.edu/gelman/presentations/epiclin.pdf", "gelman_actual_epiclin.pdf", "downloaded_inspected"),
    ("SRC-058", "What is Bayesian data analysis? Some examples", "New School", "2016", "statistics", "Bayesian data analysis", "https://sites.stat.columbia.edu/gelman/presentations/bayes_lecture.pdf", "gelman_actual_bayes_lecture.pdf", "downloaded_inspected"),
    ("SRC-059", "Crimes against data", "ESRC Research Methods Festival", "2016", "statistics", "statistical practice", "https://sites.stat.columbia.edu/gelman/presentations/crimes_bath.pdf", "gelman_actual_crimes_bath.pdf", "downloaded_uninspected"),
    ("SRC-060", "The statistical crisis in science", "Bank of England", "2016", "statistics", "statistical crisis", "https://sites.stat.columbia.edu/gelman/presentations/bank_england.pdf", "gelman_actual_bank_england.pdf", "downloaded_uninspected"),
    ("SRC-061", "Changing everything at once", "Electronic Conference on Teaching Statistics", "2016", "statistics", "teaching statistics", "https://sites.stat.columbia.edu/gelman/presentations/teaching_lecture.pdf", "gelman_actual_teaching_lecture.pdf", "downloaded_uninspected"),
    ("SRC-062", "The crisis in science and the crisis in science journalism", "Swiss Association for Science Journalism", "2016", "statistics", "statistical communication", "https://sites.stat.columbia.edu/gelman/presentations/switz_science.pdf", "gelman_actual_switz_science.pdf", "downloaded_uninspected"),
    ("SRC-063", "Preferences in Political Mapping", "Conference on mapping political preferences", "2016", "statistics", "political mapping", "https://sites.stat.columbia.edu/gelman/presentations/toulouse.pdf", "gelman_actual_toulouse.pdf", "downloaded_uninspected"),
    ("SRC-064", "More than just a game", "Columbia University", "2016", "statistics", "sports analytics", "https://sites.stat.columbia.edu/gelman/presentations/sports_lecture.pdf", "gelman_actual_sports_lecture.pdf", "downloaded_uninspected"),
]

EXTERNAL_PRIMARY_CANDIDATES = [
    ("SRC-065", "Generalizing from sample to population", "Andrew Gelman", "University of Michigan / Mathematica Policy Research", "2014/2016", "statistics", "survey inference", "https://sites.stat.columbia.edu/gelman/presentations/sampletopopulation.pdf"),
    ("SRC-066", "Causality and statistical learning", "Andrew Gelman", "Annual Health Economics Workshop", "2012", "statistics", "causal inference", "https://sites.stat.columbia.edu/gelman/presentations/causality.pdf"),
    ("SRC-067", "Weakly informative priors", "Andrew Gelman", "AISTATS / Harvard", "2011/2014", "statistics", "Bayesian priors", "https://sites.stat.columbia.edu/gelman/presentations/weakly_informative_priors.pdf"),
    ("SRC-068", "High-Dimensional Statistics I", "Martin Wainwright", "Simons Institute / UC Berkeley", "2013", "statistics", "high-dimensional inference", "https://simons.berkeley.edu/node/18350"),
    ("SRC-069", "High-Dimensional Statistics II", "Martin Wainwright", "Simons Institute / UC Berkeley", "2013", "statistics", "high-dimensional inference", "https://simons.berkeley.edu/talks/high-dimensional-statistics-ii"),
    ("SRC-070", "Harvard Biostatistics Seminar archive", "Harvard Biostatistics speakers", "Harvard", "various", "biostatistics", "clinical research", "https://www.hsph.harvard.edu/biostatistics/seminars/"),
    ("SRC-071", "Johns Hopkins Biostatistics seminar archive", "JHU Biostatistics speakers", "Johns Hopkins", "various", "biostatistics", "clinical research", "https://publichealth.jhu.edu/departments/biostatistics/news-and-events/seminars"),
    ("SRC-072", "UNC Biostatistics seminar archive", "UNC Biostatistics speakers", "UNC", "various", "biostatistics", "clinical research", "https://sph.unc.edu/bios/biostatistics-seminars/"),
    ("SRC-073", "Bayesian Workflow talk archive", "Andrew Gelman and collaborators", "Columbia / multiple venues", "various", "statistics", "Bayesian workflow", "https://sites.stat.columbia.edu/gelman/presentations/"),
    ("SRC-074", "ENAR invited session materials", "ENAR speakers", "ENAR", "various", "biostatistics", "clinical methods", "https://www.enar.org/"),
]


def candidate_sources() -> list[dict[str, str]]:
    sources = list(BASE_SOURCES)
    for idx, (filename, subdomain) in enumerate(CMU_LECTURES, start=14):
        status = "downloaded_inspected" if filename == "Lei-Robins-Wasserman.pdf" else "downloaded_uninspected"
        sources.append(source(
            f"SRC-{idx:03d}",
            filename.removesuffix(".pdf").replace("-", " "),
            "Ryan Tibshirani course archive",
            "Carnegie Mellon University",
            "2024",
            "advanced lecture",
            "statistics",
            subdomain,
            f"https://www.stat.cmu.edu/~ryantibs/statml/lectures/{filename}",
            f"cmu_statml_{filename}",
            "SECONDARY_TEACHING_REFERENCE",
            status,
            "public course PDF; metadata lessons only",
        ))
    for sid, title, venue, year, family, subdomain, url, filename, status in GELMAN_ACTUAL_TALKS:
        tier = "SECONDARY_TEACHING_REFERENCE" if "Teaching" in title else "PRIMARY_RESEARCH_PRESENTATION"
        sources.append(source(sid, title, "Andrew Gelman", venue, year, "invited academic talk", family, subdomain, url, filename, tier, status, "public PDF linked from speaker presentation archive; metadata lessons only"))
    for sid, title, speaker, institution, year, family, subdomain, url in EXTERNAL_PRIMARY_CANDIDATES:
        sources.append(source(sid, title, speaker, institution, year, "candidate real seminar or invited talk", family, subdomain, url, "", "CANDIDATE_BACKLOG", "candidate_backlog", "candidate URL only; inspect and download before page-level use"))
    return sources


def sha256(path: Path) -> str:
    if not path.exists() or not path.is_file():
        return ""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def visible_title(pdf: Path, page: int, fallback: str) -> str:
    if not pdf.exists() or pdf.suffix.lower() != ".pdf":
        return fallback
    try:
        result = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), str(pdf), "-"], check=False, capture_output=True, text=True, timeout=30)
    except Exception:
        return fallback
    for line in result.stdout.splitlines():
        line = re.sub(r"\s+", " ", line).strip()
        if line and not line.isdigit():
            return line[:160]
    return fallback


def rendered_page_hash(pdf: Path, page: int) -> str:
    if not pdf.exists() or pdf.suffix.lower() != ".pdf":
        return ""
    RENDER_CACHE.mkdir(parents=True, exist_ok=True)
    prefix = RENDER_CACHE / f"{pdf.stem}_p{page:03d}"
    png = prefix.with_suffix(".png")
    if not png.exists():
        try:
            subprocess.run(["pdftoppm", "-png", "-r", "140", "-f", str(page), "-l", str(page), "-singlefile", str(pdf), str(prefix)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
        except Exception:
            return ""
    return sha256(png)


def spec(source_id: str, page: int, page_function: str, obj: str, evidence: str, title: str, dominance: str, ratio: str, equation: str, uncertainty: str, negative: str, why: str, learn: str, observation: str, contexts: str = "research group meeting; PhD update; supervisor decision; methods or results review") -> dict[str, str | int]:
    return {
        "source_id": source_id,
        "actual_page_number": page,
        "page_function": page_function,
        "scientific_object": obj,
        "evidence_type": evidence,
        "title_style": title,
        "visual_dominance": dominance,
        "approximate_figure_text_ratio": ratio,
        "equation_usage": equation,
        "uncertainty_handling": uncertainty,
        "negative_result_handling": negative,
        "why_this_specific_page_works": why,
        "what_to_learn": learn,
        "what_not_to_copy": "Do not copy whole-slide screenshots, institutional styling, public figures, private clinical data, or source-specific visual identity; redraw the organization with owned or synthetic evidence.",
        "suitable_contexts": contexts,
        "short_page_specific_observation": observation,
    }


INSPECTED_PAGE_SPECS = [
    spec("SRC-001", 6, "REAL_DATA_APPLICATION", "growth plot plus motivating astronomy image", "motivating data context", "context title", "figure plus short caption", "0.65/0.35", "none", "growth curve shown without over-interpreting", "none", "A committee slide anchors motivation in a visible dataset and domain image rather than a generic background paragraph.", "Open a doctoral update with evidence context before method detail.", "Growth plot and image are paired with the research context; useful as a motivation page."),
    spec("SRC-001", 8, "METHOD_DIAGRAM", "graph neural network concept diagram", "method mechanism", "method title", "diagram dominant", "0.70/0.30", "none", "not explicit", "none", "The page reduces a technical method to one graph abstraction and one communication channel.", "Use one mechanism diagram before algorithm details.", "Simple objects and arrows explain satellites/debris graph representation."),
    spec("SRC-001", 13, "RESULT_FIGURE", "training-step reward curve with baselines", "quantitative plot", "claim title", "dominant plot", "0.75/0.25", "none", "baseline comparison visible", "none", "The plot carries the result while the caption states what is being compared.", "For result pages, make the graph the main object and keep interpretation close to it.", "Learning curve compares local/global information methods."),
    spec("SRC-001", 14, "SENSITIVITY_ANALYSIS", "ranked sensitivity bars and interpretation note", "sensitivity analysis", "question title", "bar plot plus note", "0.65/0.35", "none", "sensitivity magnitude is visible", "in-progress status explicit", "The slide keeps an in-progress sensitivity study useful by showing ranked effects and uncertainty about interpretation.", "Mark in-progress sensitivity honestly; do not hide it behind a polished conclusion.", "Sensitivity bars and yellow reviewer notes expose the unresolved issue."),
    spec("SRC-001", 16, "NEXT_EXPERIMENT", "future work bullets tied to robustness and interpretability", "planned evidence", "planning title", "text with highlighted decision note", "0.25/0.75", "none", "uncertainty appears as future robustness checks", "none", "The future-work page separates next work from completed result and asks a committee-facing question.", "Use future-work pages to ask for decisions, not to claim completed evidence.", "Highlighted note asks how much uncertainty to present as future work."),
    spec("SRC-004", 5, "STATISTICAL_MODEL", "hybrid resource-bound analysis pipeline", "model schematic", "proposal claim", "diagram dominant", "0.70/0.30", "light formula", "not explicit", "none", "The proposal frames the core research idea as a merge of two analysis paths with a bound output.", "State the proposed model as a mechanism, not just a problem label.", "Two analysis paths combine into an overall cost bound."),
    spec("SRC-004", 18, "BAYESIAN_MODEL", "Bayesian data-driven analysis generative model", "Bayesian model", "method contribution", "formula plus bullets", "0.45/0.55", "central", "posterior distribution explicit", "none", "The slide maps latent parameter, observations, and posterior samples into a program-analysis use case.", "For Bayesian pages, show prior/likelihood/posterior roles and the object of inference.", "Bayesian formulation is introduced with model components and posterior samples."),
    spec("SRC-004", 23, "ASSUMPTION", "hybrid analysis goal/challenge with posterior samples", "assumption / challenge", "challenge title", "diagram and boxed questions", "0.55/0.45", "light formula", "uncertainty about combination is explicit", "none", "The slide states what must be assumed or designed before the hybrid method can work.", "Put assumptions and interface questions in the main method flow, not hidden backup.", "Hybrid challenge asks how constraints and posterior samples can be combined."),
    spec("SRC-004", 27, "ESTIMATOR", "hybrid AARA plus BayesPC algorithm flow", "estimator pipeline", "method title", "algorithm diagram", "0.70/0.30", "light formula", "posterior sample restriction shown", "none", "The estimator page uses data objects, constraints, and optimization steps as the visual structure.", "Show estimator inputs, restrictions, and outputs in one editable diagram.", "AARA and BayesPC are connected through posterior samples and cost constraints."),
    spec("SRC-004", 28, "SIMULATION", "quicksort evaluation curves", "simulation comparison", "evaluation title", "plot plus steps", "0.65/0.35", "none", "curve comparison visible", "none", "The evaluation page names the example program and compares methods with plotted curves.", "Simulation pages need DGP/example, comparator, and performance curve together.", "Quicksort resource metrics compare Bayesian analysis and hybrid analysis."),
    spec("SRC-004", 30, "FINITE_SAMPLE", "limitations of hybrid AARA", "limitation analysis", "limitation title", "counterexample diagram", "0.55/0.45", "none", "finite recursion/time limits shown", "limitation is explicit", "The slide makes a limitation visual and concrete instead of burying it in text.", "Use limitation pages to name failure conditions and show why they matter.", "Bounded sort and memoization examples reveal where hybrid assumptions break."),
    spec("SRC-004", 42, "SUPERVISOR_DECISION", "proposal conclusion and timeline endpoint", "conclusion synthesis", "conclusion title", "pipeline summary", "0.45/0.55", "none", "future deadline explicit", "none", "The conclusion reuses the core mechanism and ties it to proposal deliverables.", "End a proposal section by restating mechanism plus next milestone.", "Hybrid mechanism appears beside the two-part conclusion."),
    spec("SRC-005", 14, "MEDICAL_IMAGE_COMPARISON", "representative skin lesion samples", "image evidence", "sample title", "image grid", "0.85/0.15", "none", "sample variability visible", "none", "Representative samples show the visual unit before annotator-agreement metrics.", "Introduce medical-image datasets with actual sample diversity before statistics.", "Grid of lesion samples makes the annotation problem concrete."),
    spec("SRC-005", 18, "ESTIMATOR", "inter-annotator agreement formula with masks", "metric definition", "metric title", "formula plus masks", "0.45/0.55", "central", "agreement definition visible", "none", "The page binds the agreement estimator to example masks so the formula is not abstract.", "For metrics, place formula next to the exact visual object being scored.", "IAA formula is paired with two binary masks."),
    spec("SRC-005", 22, "CONFIDENCE_INTERVAL", "bootstrap confidence interval surface", "uncertainty interval", "metric title", "surface plot", "0.70/0.30", "light formula", "confidence interval shown and annotated", "none", "The uncertainty page moves from point agreement to interval evidence and highlights the distribution shape.", "Show interval behavior, not just a single metric, when annotation variability matters.", "Observed distribution and 95 percent CI are called out on a surface plot."),
    spec("SRC-005", 28, "REAL_DATA_APPLICATION", "malignancy affects IAA table", "subgroup comparison", "finding title", "table dominant", "0.60/0.40", "none", "p-values and coefficients visible", "none", "The table ties a clinical subgroup to annotator variability with effect estimates.", "Biostatistics pages should name the clinical unit and subgroup before giving coefficients.", "Malignant vs benign rows summarize IAA association estimates."),
    spec("SRC-005", 40, "REAL_DATA_APPLICATION", "IAA prediction from images regression results", "predictive model result", "question title", "forest/point plot", "0.65/0.35", "none", "model uncertainty shown by intervals", "none", "The result answers whether image-only prediction carries signal and shows model comparison.", "Put the question, model family, and effect-size plot on the same page.", "Regression and classification heads are compared for IAA prediction."),
    spec("SRC-005", 52, "NEGATIVE_RESULT", "multi-task models diagnose better than diagnosis-only models", "model comparison", "result title", "line plots", "0.70/0.30", "none", "performance curves visible", "diagnosis-only comparison is explicit", "The slide states a negative comparator and shows why the multi-task setup improves the endpoint.", "Keep the failing baseline visible when it is scientifically informative.", "Diagnosis-only baseline is shown against multi-task alternatives."),
    spec("SRC-006", 3, "EXPERIMENT_DESIGN", "automatic lesion segmentation applications", "task overview", "introduction title", "pipeline plus examples", "0.70/0.30", "none", "not explicit", "none", "The page links PET segmentation to concrete downstream tasks before the model architecture.", "Start method talks by connecting task, data, and application unit.", "PET applications and lesion examples appear before architecture details."),
    spec("SRC-006", 8, "STATISTICAL_MODEL", "PET-Disentangler loss with segmentation and reconstruction", "model objective", "method title", "architecture diagram", "0.65/0.35", "central", "loss components visible", "none", "The objective page connects architecture branches to the exact losses being optimized.", "For model pages, make the loss terms visibly correspond to diagram parts.", "Segmentation and image decoder branches are tied to their losses."),
    spec("SRC-006", 20, "RESULT_FIGURE", "lesion segmentation Dice table", "quantitative table", "result title", "table dominant", "0.60/0.40", "none", "standard deviations visible", "none", "The result table has disease subgroup columns and method rows, making the endpoint structure explicit.", "Medical-imaging result pages should keep subgroups and endpoints visible.", "Healthy/disease/overall Dice values are compared across methods."),
    spec("SRC-006", 21, "MEDICAL_IMAGE_COMPARISON", "PET input, GT, predictions, reconstruction panels", "image comparison", "result evidence", "image grid", "0.90/0.10", "none", "qualitative uncertainty implicit", "failure/success differences visible", "The same-case panel makes qualitative performance inspectable rather than relying only on Dice.", "Use aligned panels for image, GT, prediction, and reconstruction in failure/result pages.", "Rows show input, ground truth, baselines, model output, probability and reconstruction."),
    spec("SRC-013", 8, "RESULT_FIGURE", "team-quality estimate forest plot", "posterior interval plot", "graph title", "forest plot", "0.80/0.20", "none", "credible intervals visible", "none", "The forest plot ranks many groups while preserving uncertainty intervals.", "Use interval plots when ranking is uncertain.", "Team-quality estimates are shown with intervals and ordering."),
    spec("SRC-013", 10, "MODEL_CHECK", "prediction comparison against model", "posterior predictive check", "comparison title", "interval plot", "0.75/0.25", "none", "predictive intervals visible", "none", "The page compares fitted model expectations with observed case-score differences.", "Model-check pages should compare model output to real held-out structure.", "Predictions are compared with observed game-score differentials."),
    spec("SRC-013", 11, "NEGATIVE_RESULT", "after finding and fixing a bug comparison", "bug-fix model check", "negative/fix title", "interval plot", "0.75/0.25", "none", "post-fix uncertainty visible", "bug is explicit", "The slide shows model debugging as a legitimate scientific result, not an embarrassment.", "Keep bug/failure pages when they change interpretation and show the corrected evidence.", "A bug-fix comparison is shown with the same predictive-check structure."),
    spec("SRC-013", 29, "SIMULATION", "simulate fake data in R", "fake-data simulation", "simulation title", "code plus scatter", "0.45/0.55", "light code", "simulated variation visible", "none", "The slide shows fake-data generation as part of model checking before refitting.", "Simulation pages need visible data-generating mechanism and output.", "R code and simulated scatter expose the model-generated data."),
    spec("SRC-013", 36, "POSTERIOR_DIAGNOSTIC", "skewed posterior distribution", "posterior diagnostic", "diagnostic title", "scatter dominant", "0.75/0.25", "none", "skew and scale visible", "none", "The diagnostic page uses posterior scatterplots to reveal parameterization trouble.", "Use posterior diagnostic pages to show shape, not only convergence tables.", "Two posterior scatterplots reveal skewed posterior structure."),
    spec("SRC-054", 14, "ESTIMATOR", "poststratification identity", "estimator formula", "formula title", "formula dominant", "0.35/0.65", "central", "not explicit", "none", "The estimator is isolated before applying it, so the audience can read the target quantity.", "Put estimand/estimator formulas on sparse pages when they define the rest of the talk.", "Poststratification identity is shown as the sole object."),
    spec("SRC-054", 20, "REAL_DATA_APPLICATION", "survey support by demographic cells", "survey data plot", "application result", "small multiples", "0.75/0.25", "none", "variation across cells visible", "none", "The page shows the actual cell structure behind a hierarchical regression story.", "Biostat/survey pages should expose units and cell structure before model conclusions.", "Survey support is broken down by sex, race, age, and education."),
    spec("SRC-054", 21, "CONFIDENCE_INTERVAL", "XBox estimates adjusting for demographics", "time-series interval", "result title", "plot dominant", "0.75/0.25", "none", "interval band visible", "none", "The plot conveys temporal uncertainty and adjusted estimate movement.", "Show adjusted estimate and uncertainty together when discussing survey quality.", "Grey interval band and smoothed estimate show poll movement."),
    spec("SRC-054", 30, "REFERENCE_COVERAGE_GAP", "open problems in MRP", "coverage gap", "open-problem title", "text list", "0.20/0.80", "none", "uncertainty expressed as open problems", "none", "The page is useful as a coverage-gap record rather than as a visual template.", "Record unresolved statistical issues as acquisition priorities for later rounds.", "Deep interactions and non-census variables are explicit open MRP problems."),
    spec("SRC-055", 14, "SENSITIVITY_ANALYSIS", "p-value / power illustration", "design sensitivity", "interpretive title", "annotated distribution", "0.65/0.35", "none", "type S/M errors annotated", "none", "The slide turns an abstract statistical concept into an annotated distribution with thresholds.", "Sensitivity-analysis pages should annotate the error mechanism directly on the plot.", "Power and exaggeration error are marked on a normal curve."),
    spec("SRC-055", 16, "CONFIDENCE_INTERVAL", "design sensitivity in criminal justice experiments", "forest plot", "paper title", "interval figure", "0.70/0.30", "none", "confidence intervals dominate", "null effects noted", "The page uses a real policy paper and interval plot to show small/nonzero effects.", "Tie applied-study pages to the source paper and the interval evidence.", "Effect estimates across cities are shown with intervals and notes about null effects."),
    spec("SRC-055", 24, "STATISTICAL_MODEL", "Bayesian toy model construction", "model reveal", "example title", "formula plus image", "0.40/0.60", "central", "inference elements revealed stepwise", "none", "The model is built progressively so data, parameters, and inference roles become legible.", "For model teaching, reveal model components step by step.", "Toy model bullets expose y, theta, sigma, data and inference."),
    spec("SRC-056", 23, "ASSUMPTION", "limitations of existing solutions", "limitation list", "question title", "text dominant", "0.15/0.85", "none", "expert uncertainty explicit", "limitation is central", "The page makes why current solutions fail explicit before proposing a prior-based fix.", "Assumption pages can be text-heavy if they state why current approaches fail.", "Limits of eliciting priors from experts are listed."),
    spec("SRC-056", 24, "BAYESIAN_MODEL", "hierarchical model and informative priors", "Bayesian solution", "solution title", "equation bullets", "0.35/0.65", "central", "weak/informative priors named", "none", "The page turns the limitation into a hierarchical-model strategy.", "Bayesian workflow pages should connect prior choices to the problem they solve.", "Hierarchical model and weakly informative priors are named as the solution."),
    spec("SRC-056", 27, "SIMULATION", "simulate fake data in R", "fake-data simulation", "simulation title", "code plus scatter", "0.45/0.55", "light code", "simulated variation visible", "none", "The page checks model behavior by making fake data visible.", "Simulation pages need code, generated data, and the model purpose.", "R code and scatter appear together."),
    spec("SRC-056", 32, "BAYESIAN_MODEL", "informative prior distribution", "prior specification", "prior title", "formula dominant", "0.20/0.80", "central", "prior scale explicit", "none", "The slide states the prior distribution as a first-class modeling object.", "Prior pages should show distribution and scale, not just say 'regularize'.", "Normal priors for log_a and log_b are shown."),
    spec("SRC-057", 14, "REAL_DATA_APPLICATION", "data and regression figure", "clinical regression example", "data title", "plot dominant", "0.70/0.30", "none", "interval / trend visible", "none", "The page uses an applied regression figure before deriving clinical interpretation.", "Clinical stats pages should expose the observed trend and uncertainty before prose.", "Regression line and shaded uncertainty are visible."),
    spec("SRC-057", 21, "CONFIDENCE_INTERVAL", "confidence intervals do not respect prior information", "confidence interval principle", "principle title", "text principle", "0.15/0.85", "none", "prior-information limitation explicit", "none", "The principle page states a conceptual limitation that motivates Bayesian treatment.", "Use principle pages sparingly when they frame later evidence.", "Confidence-interval limitation is stated in one sentence."),
    spec("SRC-057", 28, "NEGATIVE_RESULT", "histogram of p-values for fertility relationship", "p-value distribution", "possibilities title", "histogram dominant", "0.65/0.35", "none", "distribution shape visible", "p-value weakness explicit", "The page shows the many-choices problem as a p-value distribution, not a slogan.", "Negative statistical-method pages should show the failure distribution.", "Histogram of p-values appears after possible analyses are enumerated."),
    spec("SRC-057", 29, "BAYESIAN_MODEL", "Bayesian solution to comparison multiplicity", "Bayesian workflow list", "solution title", "text recipe", "0.20/0.80", "none", "variation accepted explicitly", "none", "The solution page names comparison enumeration, population adjustment, and accepting variation.", "Pair negative-result pages with a concrete modeling response.", "Bayesian solution bullets follow the p-value problem."),
    spec("SRC-058", 15, "MODEL_CHECK", "Bayesian data analysis model checking", "model checking checklist", "workflow title", "text checklist", "0.20/0.80", "none", "questions about fit explicit", "none", "The checklist defines what model checking must answer before improving the model.", "Checklist pages can be useful when each question maps to a later diagnostic.", "Questions ask if inferences make sense and whether model predictions fit data."),
    spec("SRC-058", 25, "BAYESIAN_MODEL", "Bayesian inference workflow for a pharmacokinetic model", "modeling workflow", "inference title", "text plus equations", "0.30/0.70", "central", "posterior comparison named", "none", "The page distinguishes parameter estimation, posterior checking, and future prediction.", "Bayesian workflow pages should separate inference targets and checks.", "Inference bullets separate PK parameters, concentration predictions, and checks."),
    spec("SRC-058", 31, "REAL_DATA_APPLICATION", "inference for the population", "population inference curves", "population title", "curve plot", "0.75/0.25", "none", "population bands visible", "none", "The page moves from individual inference to population inference with curves.", "Show the inferential population target, not only the fitted individual cases.", "Multiple curves show population-level prediction."),
    spec("SRC-058", 57, "POSTERIOR_DIAGNOSTIC", "generated quantities probability calculation", "generated quantities", "computation title", "code dominant", "0.25/0.75", "central", "posterior probability computed", "none", "The page shows generated quantities as the bridge from model fit to decision probability.", "Generated-quantity pages should name the decision quantity being computed.", "Stan generated quantities code computes win probabilities."),
    spec("SRC-017", 4, "SECONDARY_STATISTICAL_INTUITION", "prediction set illustrations", "conformal prediction intuition", "paper page", "paper figures", "0.55/0.45", "central", "coverage intuition visible", "none", "This is a paper/lecture PDF, useful for conformal-intuition references but not a primary talk template.", "Use secondary sources for theorem/statistical intuition only.", "Distribution-free prediction sets paper page shows example prediction sets.", "theorem/equation explanation; statistics teaching backup"),
    spec("SRC-017", 10, "THEOREM", "semiparametric equations and assumptions", "theorem / proof", "paper page", "equation dominant", "0.20/0.80", "central", "asymptotic assumptions visible", "none", "The dense theorem page is useful to decide what belongs in backup rather than main slides.", "Keep proof-heavy theory pages as backup inspiration, not main deck layout.", "Equations and assumptions dominate the page.", "theorem/equation explanation; backup technical material"),
]


def page_rows(sources: list[dict[str, str]]) -> list[dict[str, Any]]:
    by_id = {item["source_id"]: item for item in sources}
    rows: list[dict[str, Any]] = []
    for idx, item in enumerate(INSPECTED_PAGE_SPECS, start=1):
        src = by_id[item["source_id"]]
        pdf = SOURCE_CACHE / src["expected_cache_file"]
        page = int(item["actual_page_number"])
        row = {
            "reference_id": f"RRL-{idx:03d}",
            "source_id": src["source_id"],
            "talk_title": src["title"],
            "speaker": src["speaker"],
            "institution": src["institution"],
            "source_url": src["source_url"],
            "local_cache_file": src["expected_cache_file"],
            "actual_page_number": page,
            "rights_note": src["rights_note"],
            "verification_status": "inspected",
            "source_file_sha256": sha256(pdf),
            "rendered_page_sha256": rendered_page_hash(pdf, page),
            "visible_page_title": visible_title(pdf, page, str(item["short_page_specific_observation"])),
        }
        row.update(item)
        rows.append(row)
    return rows


def synthesized_knowledge(rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    return [
        {
            "knowledge_id": "SYN-001",
            "basis": "inspected pages with RESULT_FIGURE, CONFIDENCE_INTERVAL, and MODEL_CHECK functions",
            "lesson": "Result pages must expose the scientific object and uncertainty, not just the final claim.",
        },
        {
            "knowledge_id": "SYN-002",
            "basis": "inspected Bayesian workflow and routine-priors pages",
            "lesson": "Statistical model pages should name estimand/target, observed variables, validation or checking mechanism, and downstream inference target.",
        },
        {
            "knowledge_id": "SYN-003",
            "basis": "inspected medical-imaging IAA and PET segmentation pages",
            "lesson": "Medical-imaging slides should keep patient/case/image units, GT/prediction/error evidence, and endpoint-specific metrics visible together.",
        },
    ]


def write_csv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    sources = candidate_sources()
    rows = page_rows(sources)
    manifest = {
        "schema_version": 2,
        "generated_from": "build_reference_metadata.py",
        "cache_root": ".cache/research-presentation-reference-library/sources",
        "layers": {
            "source_registry": "candidate_sources",
            "inspected_page_library": "research_slide_reference_index.csv",
            "synthesized_knowledge": "synthesized_knowledge",
        },
        "retrieval_priority": ["PRIMARY_RESEARCH_PRESENTATION", "SECONDARY_TEACHING_REFERENCE", "PRESENTATION_GUIDANCE", "CANDIDATE_BACKLOG"],
        "candidate_sources": sources,
        "synthesized_knowledge": synthesized_knowledge(rows),
    }
    (ROOT / "reference_sources_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_csv(ROOT / "reference_source_search_matrix.csv", SOURCE_FIELDS, sources)
    write_csv(ROOT / "research_slide_reference_index.csv", PAGE_FIELDS, rows)
    print(json.dumps({
        "candidate_sources": len(sources),
        "inspected_page_records": len(rows),
        "inspected_decks": len({row["source_id"] for row in rows}),
        "primary_sources": sum(1 for source in sources if source["source_tier"] == "PRIMARY_RESEARCH_PRESENTATION"),
        "inspected_records_without_render_hash": sum(1 for row in rows if not row["rendered_page_sha256"]),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
