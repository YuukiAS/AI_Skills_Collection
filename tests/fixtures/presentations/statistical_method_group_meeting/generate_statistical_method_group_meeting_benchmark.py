#!/usr/bin/env python3
"""Generate a five-slide statistical method group-meeting benchmark deck."""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import random
import shutil
import subprocess
import sys
from pathlib import Path
from zipfile import ZipFile

from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Inches, Pt


W, H = 13.333, 7.5
REPO_ROOT = Path(__file__).resolve().parents[4]
REFERENCE_ROOT = REPO_ROOT / "skills" / "tools" / "documents-media" / "presentations" / "shared" / "references"
REFERENCE_INDEX = REFERENCE_ROOT / "research_slide_reference_index.csv"
REFERENCE_MANIFEST = REFERENCE_ROOT / "reference_sources_manifest.json"
SEED = 20260822
REPLICATES = 400
CENTER_GRID = [8, 20, 50]
ICC_GRID = [0.0, 0.1, 0.3, 0.5]
IMBALANCE_GRID = ["balanced", "imbalanced"]
BETA1 = 0.25
P = {
    "bg": "F7F7F9",
    "ink": "17202A",
    "muted": "606977",
    "line": "C6CCD6",
    "purple": "4F1F68",
    "teal": "0F766E",
    "blue": "1F4E79",
    "gold": "9A6A16",
    "red": "A33A34",
    "green": "2A7C54",
    "soft_teal": "E1F4F1",
    "soft_blue": "E5EEF8",
    "soft_gold": "FBF1D6",
    "soft_red": "F8E3E1",
}

REFERENCE_QUERIES = {
    "STATISTICAL_MODEL": {
        "intent": "Explain estimand, DGP, cluster correlation, and why unbiased point estimates can still have wrong interval coverage.",
        "page_functions": ["STATISTICAL_MODEL", "BAYESIAN_MODEL", "ASSUMPTION", "MODEL_CHECK"],
        "scientific_domain": ["statistics", "biostatistics"],
        "statistical_subdomain": ["Bayesian workflow", "Bayesian data analysis", "survey nonresponse / MRP", "Bayesian clinical research"],
        "evidence_types": ["model objective", "Bayesian model", "assumption / challenge", "modeling workflow", "confidence interval principle"],
        "organization_lesson": "Make the estimand and data-generating mechanism the main object before discussing results.",
    },
    "ESTIMATOR": {
        "intent": "Show how a variance estimator changes when score contributions are aggregated by center.",
        "page_functions": ["ESTIMATOR", "CONFIDENCE_INTERVAL", "STATISTICAL_MODEL", "ASSUMPTION"],
        "scientific_domain": ["statistics", "biostatistics"],
        "statistical_subdomain": ["hybrid resource-bound analysis", "survey nonresponse / MRP", "Bayesian clinical research", "Bayesian workflow"],
        "evidence_types": ["estimator formula", "estimator pipeline", "uncertainty interval", "confidence interval principle", "metric definition"],
        "organization_lesson": "Put the formula next to definitions of the grouped objects it operates on.",
    },
    "SIMULATION_DESIGN": {
        "intent": "Connect DGP knobs, generated centers, interval methods, replicates, and coverage endpoints in one experiment design.",
        "page_functions": ["EXPERIMENT_DESIGN", "METHOD_DIAGRAM", "SIMULATION", "NEXT_EXPERIMENT", "ESTIMATOR"],
        "scientific_domain": ["statistics", "biostatistics", "medical imaging"],
        "statistical_subdomain": ["Bayesian workflow", "hybrid resource-bound analysis", "survey nonresponse / MRP", "lesion segmentation"],
        "evidence_types": ["task overview", "method mechanism", "simulation comparison", "planned evidence", "estimator pipeline"],
        "organization_lesson": "Use one left-to-right experimental path with explicit endpoints and visible comparator branches.",
    },
    "RESULT_FIGURE": {
        "intent": "Show coverage against ICC with nominal target line, method comparison, and Monte Carlo uncertainty.",
        "page_functions": ["RESULT_FIGURE", "CONFIDENCE_INTERVAL", "SIMULATION", "REAL_DATA_APPLICATION", "SENSITIVITY_ANALYSIS"],
        "scientific_domain": ["statistics", "biostatistics"],
        "statistical_subdomain": ["Bayesian workflow", "survey nonresponse / MRP", "Bayesian inference design", "Bayesian clinical research"],
        "evidence_types": ["quantitative plot", "uncertainty interval", "simulation comparison", "time-series interval", "forest plot"],
        "organization_lesson": "Let the plot dominate and keep uncertainty and interpretation adjacent to the graph.",
    },
    "NEGATIVE_RESULT": {
        "intent": "Show the stress regime where the current interval still fails and define the next discriminating experiment.",
        "page_functions": ["NEGATIVE_RESULT", "FINITE_SAMPLE", "MODEL_CHECK", "NEXT_EXPERIMENT", "SENSITIVITY_ANALYSIS"],
        "scientific_domain": ["statistics", "biostatistics"],
        "statistical_subdomain": ["Bayesian workflow", "Bayesian clinical research", "hybrid resource-bound analysis", "Bayesian inference design"],
        "evidence_types": ["negative/fix title", "limitation analysis", "posterior predictive check", "planned evidence", "sensitivity analysis"],
        "organization_lesson": "Keep the failure visible and separate completed evidence from the next planned method.",
    },
}

TIER_PRIORITY = {
    "PRIMARY_RESEARCH_PRESENTATION": 0,
    "SECONDARY_TEACHING_REFERENCE": 1,
    "PRESENTATION_GUIDANCE": 2,
    "CANDIDATE_BACKLOG": 3,
}


def rgb(name: str) -> RGBColor:
    value = P[name]
    return RGBColor(int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16))


def hex_color(name: str) -> str:
    return "#" + P[name]


def inch(value: float):
    return Inches(value)


def add_text(slide, text: str, x: float, y: float, w: float, h: float, size: float = 13, color: str = "ink", bold: bool = False, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(inch(x), inch(y), inch(w), inch(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = inch(0.04)
    tf.margin_right = inch(0.04)
    tf.margin_top = inch(0.02)
    tf.margin_bottom = inch(0.02)
    p = tf.paragraphs[0]
    p.text = text
    p.font.name = "Aptos"
    p.font.size = Pt(size)
    p.font.bold = bold
    p.font.color.rgb = rgb(color)
    p.alignment = align
    return box


def rect(slide, text: str, x: float, y: float, w: float, h: float, fill: str = "soft_blue", color: str = "ink", size: float = 12, bold: bool = False):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, inch(x), inch(y), inch(w), inch(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(fill)
    shape.line.color.rgb = rgb("line")
    shape.line.width = Pt(1)
    add_text(slide, text, x + 0.06, y + 0.05, w - 0.12, h - 0.1, size, color, bold, PP_ALIGN.CENTER)
    return shape


def arrow(slide, x1: float, y1: float, x2: float, y2: float, color: str = "purple", width: float = 1.7):
    connector = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, inch(x1), inch(y1), inch(x2), inch(y2))
    connector.line.color.rgb = rgb(color)
    connector.line.width = Pt(width)
    ln = connector.line._get_or_add_ln()
    tail = OxmlElement("a:tailEnd")
    tail.set("type", "triangle")
    ln.append(tail)
    return connector


def header(slide, number: int, title: str, message: str):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = rgb("bg")
    band = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, inch(0), inch(0), inch(W), inch(0.16))
    band.fill.solid()
    band.fill.fore_color.rgb = rgb("purple")
    band.line.fill.background()
    add_text(slide, title, 0.55, 0.36, 9.9, 0.4, 20.5, "ink", True)
    add_text(slide, f"{number:02d}/05", 11.6, 0.42, 0.95, 0.22, 9, "muted", False, PP_ALIGN.RIGHT)
    add_text(slide, message, 0.65, 0.88, 11.7, 0.34, 12.2, "purple", True)


def load_font(size: int):
    for path in ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/dejavu/DejaVuSans.ttf"]:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def tokens(value: str) -> set[str]:
    return {part.lower() for part in value.replace("/", " ").replace("-", " ").replace("_", " ").split() if len(part) > 2}


def load_reference_rows() -> list[dict[str, str]]:
    manifest = json.loads(REFERENCE_MANIFEST.read_text(encoding="utf-8"))
    source_tiers = {item["source_id"]: item["source_tier"] for item in manifest["candidate_sources"]}
    source_domains = {item["source_id"]: item["domain_family"] for item in manifest["candidate_sources"]}
    source_subdomains = {item["source_id"]: item["statistical_subdomain"] for item in manifest["candidate_sources"]}
    rows = []
    with REFERENCE_INDEX.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            if row.get("verification_status") != "inspected":
                continue
            if not (row.get("source_file_sha256") and row.get("rendered_page_sha256")):
                continue
            row["source_tier"] = source_tiers.get(row["source_id"], "")
            row["domain_family"] = source_domains.get(row["source_id"], "")
            row["statistical_subdomain"] = source_subdomains.get(row["source_id"], "")
            rows.append(row)
    return rows


def score_reference(row: dict[str, str], query: dict[str, object]) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    if row["page_function"] in query["page_functions"]:
        score += 10
        reasons.append(f"page_function={row['page_function']} matches query")
    if row["evidence_type"] in query["evidence_types"]:
        score += 6
        reasons.append(f"evidence_type={row['evidence_type']} matches query")
    if row["domain_family"] in query["scientific_domain"]:
        score += 4
        reasons.append(f"domain={row['domain_family']} matches query")
    if row["statistical_subdomain"] in query["statistical_subdomain"]:
        score += 4
        reasons.append(f"subdomain={row['statistical_subdomain']} matches query")
    query_terms = tokens(" ".join([str(query["intent"]), " ".join(query["page_functions"]), " ".join(query["evidence_types"])]))
    row_terms = tokens(" ".join([row["scientific_object"], row["why_this_specific_page_works"], row["what_to_learn"], row["short_page_specific_observation"]]))
    overlap = sorted(query_terms & row_terms)
    if overlap:
        score += min(5, len(overlap))
        reasons.append("semantic tokens overlap: " + ", ".join(overlap[:6]))
    tier_bonus = max(0, 3 - TIER_PRIORITY.get(row["source_tier"], 3))
    score += tier_bonus
    reasons.append(f"source_tier={row['source_tier']} priority_bonus={tier_bonus}")
    return score, reasons


def retrieve_references(archetype: str) -> dict[str, object]:
    query = REFERENCE_QUERIES[archetype]
    scored = []
    for row in load_reference_rows():
        score, reasons = score_reference(row, query)
        if score > 0:
            scored.append((score, TIER_PRIORITY.get(row["source_tier"], 3), row["reference_id"], row, reasons))
    scored.sort(key=lambda item: (-item[0], item[1], item[2]))
    candidate_rows = scored[:8]
    selected_rows = candidate_rows[:5]
    if len(selected_rows) < 2:
        raise RuntimeError(f"reference retrieval for {archetype} found fewer than two inspected references")
    return {
        "query": query,
        "candidate_ids": [row["reference_id"] for _, _, _, row, _ in candidate_rows],
        "selected_ids": [row["reference_id"] for _, _, _, row, _ in selected_rows],
        "source_tiers": {row["reference_id"]: row["source_tier"] for _, _, _, row, _ in selected_rows},
        "ranking_relevance_reason": {row["reference_id"]: "; ".join(reasons) for _, _, _, row, reasons in selected_rows},
        "organization_lesson": query["organization_lesson"],
        "what_was_not_copied": "No full-slide screenshots, source images, institutional styling, public figures, private clinical data, or source-specific visual identity were copied.",
    }


def reference_footer(refs: list[str], purpose: str) -> str:
    return f"Reference retrieval: {purpose} selected inspected pages {', '.join(refs)}; trace in EVIDENCE_MANIFEST; style not copied."


def invert_2x2(a: float, b: float, c: float, d: float) -> tuple[tuple[float, float], tuple[float, float]]:
    det = a * d - b * c
    if abs(det) < 1e-12:
        raise RuntimeError("singular two-column OLS design")
    return ((d / det, -b / det), (-c / det, a / det))


def simulate_cell(g_count: int, rho: float, imbalance: str, replicates: int, seed: int) -> dict[str, object]:
    rng = random.Random(seed + g_count * 1000 + int(rho * 100) + (17 if imbalance == "imbalanced" else 0))
    tau2 = rho / (1 - rho) if rho > 0 else 0.0
    naive_hits = 0
    cluster_hits = 0
    bias_sum = 0.0
    naive_width_sum = 0.0
    cluster_width_sum = 0.0
    for _ in range(replicates):
        data: list[tuple[int, int, float]] = []
        clusters: list[list[tuple[int, float]]] = []
        for g in range(g_count):
            if imbalance == "imbalanced":
                n = [8, 10, 14, 22, 42, 55, 16, 30][g % 8]
                p_treat = [0.18, 0.30, 0.45, 0.65, 0.80][g % 5]
            else:
                n = 24
                p_treat = 0.5
            u_g = rng.gauss(0.0, math.sqrt(tau2)) if tau2 else 0.0
            cluster_rows: list[tuple[int, float]] = []
            for _i in range(n):
                treatment = 1 if rng.random() < p_treat else 0
                y = BETA1 * treatment + u_g + rng.gauss(0.0, 1.0)
                data.append((g, treatment, y))
                cluster_rows.append((treatment, y))
            clusters.append(cluster_rows)
        n_total = len(data)
        sx = sum(x for _, x, _ in data)
        sy = sum(y for _, _, y in data)
        sxy = sum(x * y for _, x, y in data)
        inv = invert_2x2(n_total, sx, sx, sx)
        b0 = inv[0][0] * sy + inv[0][1] * sxy
        b1 = inv[1][0] * sy + inv[1][1] * sxy
        residuals = [(g, x, y - b0 - b1 * x) for g, x, y in data]
        rss = sum(e * e for _, _, e in residuals)
        sigma2_hat = rss / (n_total - 2)
        naive_se = math.sqrt(max(0.0, sigma2_hat * inv[1][1]))
        middle00 = middle01 = middle11 = 0.0
        offset = 0
        for rows in clusters:
            score0 = score1 = 0.0
            for x, _y in rows:
                _g, _x, e = residuals[offset]
                offset += 1
                score0 += e
                score1 += x * e
            middle00 += score0 * score0
            middle01 += score0 * score1
            middle11 += score1 * score1
        v11 = inv[1][0] * (middle00 * inv[0][1] + middle01 * inv[1][1]) + inv[1][1] * (middle01 * inv[0][1] + middle11 * inv[1][1])
        correction = g_count / (g_count - 1) * (n_total - 1) / (n_total - 2)
        cluster_se = math.sqrt(max(0.0, v11 * correction))
        naive_lo, naive_hi = b1 - 1.96 * naive_se, b1 + 1.96 * naive_se
        cluster_lo, cluster_hi = b1 - 1.96 * cluster_se, b1 + 1.96 * cluster_se
        naive_hits += naive_lo <= BETA1 <= naive_hi
        cluster_hits += cluster_lo <= BETA1 <= cluster_hi
        bias_sum += b1 - BETA1
        naive_width_sum += naive_hi - naive_lo
        cluster_width_sum += cluster_hi - cluster_lo
    naive = naive_hits / replicates
    cluster = cluster_hits / replicates
    return {
        "G": g_count,
        "rho": rho,
        "imbalance": imbalance,
        "replicates": replicates,
        "methods": {
            "naive_iid_ols_z": {
                "coverage": round(naive, 4),
                "mc_se": round(math.sqrt(naive * (1 - naive) / replicates), 4),
                "mean_width": round(naive_width_sum / replicates, 4),
            },
            "cluster_robust_z": {
                "coverage": round(cluster, 4),
                "mc_se": round(math.sqrt(cluster * (1 - cluster) / replicates), 4),
                "mean_width": round(cluster_width_sum / replicates, 4),
            },
        },
        "bias": round(bias_sum / replicates, 4),
    }


def run_simulation(out_dir: Path) -> dict[str, object]:
    rows = []
    for imbalance in IMBALANCE_GRID:
        for g_count in CENTER_GRID:
            for rho in ICC_GRID:
                rows.append(simulate_cell(g_count, rho, imbalance, REPLICATES, SEED))
    stress = next(row for row in rows if row["G"] == 8 and row["rho"] == 0.5 and row["imbalance"] == "imbalanced")
    summary = {
        "seed": SEED,
        "replicates_per_cell": REPLICATES,
        "dgp": {
            "formula": "Y_ij = beta_0 + beta_1 T_ij + u_j + epsilon_ij",
            "beta_1": BETA1,
            "u_j": "N(0, tau^2)",
            "epsilon_ij": "N(0, sigma^2)",
            "icc": "rho = tau^2 / (tau^2 + sigma^2)",
        },
        "grid": {
            "center_count": CENTER_GRID,
            "icc": ICC_GRID,
            "imbalance": IMBALANCE_GRID,
        },
        "methods": ["naive_iid_ols_z", "cluster_robust_z"],
        "endpoints": ["95% interval coverage", "mean bias", "mean interval width"],
        "nominal_coverage": 0.95,
        "rows": rows,
        "negative_result": {
            "condition": "G=8, rho=0.5, imbalanced cluster sizes and treatment shares",
            "cluster_robust_coverage": stress["methods"]["cluster_robust_z"]["coverage"],
            "naive_iid_coverage": stress["methods"]["naive_iid_ols_z"]["coverage"],
            "claim": "small-G/high-ICC stress remains under nominal for cluster-robust z intervals",
            "next_experiment": "planned: compare CR2 small-sample correction and wild cluster bootstrap under the same DGP grid",
        },
    }
    sim_dir = out_dir / "simulation"
    sim_dir.mkdir(parents=True, exist_ok=True)
    (sim_dir / "simulation_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (sim_dir / "simulation_summary.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["G", "rho", "imbalance", "method", "coverage", "mc_se", "mean_width", "bias"])
        writer.writeheader()
        for row in rows:
            for method, values in row["methods"].items():
                writer.writerow({
                    "G": row["G"],
                    "rho": row["rho"],
                    "imbalance": row["imbalance"],
                    "method": method,
                    "coverage": values["coverage"],
                    "mc_se": values["mc_se"],
                    "mean_width": values["mean_width"],
                    "bias": row["bias"],
                })
    return summary


def draw_coverage_plot(path: Path, summary: dict[str, object]) -> None:
    img = Image.new("RGB", (1180, 610), "white")
    draw = ImageDraw.Draw(img)
    font = load_font(18)
    small = load_font(13)
    title = load_font(22)
    draw.text((48, 22), "Imbalanced clusters: 95% coverage by ICC", fill=hex_color("ink"), font=title)
    panels = [(8, 60), (20, 430), (50, 800)]
    rows = summary["rows"]
    method_colors = {"naive_iid_ols_z": hex_color("red"), "cluster_robust_z": hex_color("teal")}
    for g_count, x0 in panels:
        y0 = 505
        plot_w = 300
        plot_h = 355
        draw.rectangle((x0, 105, x0 + plot_w, y0), outline=hex_color("line"), width=2)
        draw.text((x0 + 105, 78), f"G={g_count}", fill=hex_color("ink"), font=font)
        nominal_y = y0 - int((0.95 - 0.45) / 0.55 * plot_h)
        draw.line((x0, nominal_y, x0 + plot_w, nominal_y), fill=hex_color("gold"), width=3)
        draw.text((x0 + 210, nominal_y - 18), "nominal 0.95", fill=hex_color("gold"), font=small)
        for tick in [0.5, 0.7, 0.9, 1.0]:
            y = y0 - int((tick - 0.45) / 0.55 * plot_h)
            draw.line((x0 - 4, y, x0, y), fill=hex_color("muted"), width=1)
            draw.text((x0 - 38, y - 8), f"{tick:.1f}", fill=hex_color("muted"), font=small)
        for i, rho in enumerate(ICC_GRID):
            x = x0 + 35 + i * 75
            draw.line((x, y0, x, y0 + 5), fill=hex_color("muted"), width=1)
            draw.text((x - 10, y0 + 12), f"{rho:.1f}", fill=hex_color("muted"), font=small)
        for method in ["naive_iid_ols_z", "cluster_robust_z"]:
            points = []
            for i, rho in enumerate(ICC_GRID):
                row = next(item for item in rows if item["G"] == g_count and item["rho"] == rho and item["imbalance"] == "imbalanced")
                value = row["methods"][method]["coverage"]
                mc = row["methods"][method]["mc_se"]
                x = x0 + 35 + i * 75
                y = y0 - int((value - 0.45) / 0.55 * plot_h)
                lo = y0 - int((value - 1.96 * mc - 0.45) / 0.55 * plot_h)
                hi = y0 - int((value + 1.96 * mc - 0.45) / 0.55 * plot_h)
                draw.line((x, hi, x, lo), fill=method_colors[method], width=2)
                draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=method_colors[method])
                points.append((x, y))
            draw.line(points, fill=method_colors[method], width=3)
    draw.rectangle((880, 24, 902, 42), fill=method_colors["naive_iid_ols_z"])
    draw.text((910, 22), "naive iid OLS z", fill=hex_color("ink"), font=small)
    draw.rectangle((880, 50, 902, 68), fill=method_colors["cluster_robust_z"])
    draw.text((910, 48), "cluster-robust z", fill=hex_color("ink"), font=small)
    draw.text((500, 565), "ICC rho; vertical bars = Monte Carlo +/- 1.96 SE", fill=hex_color("muted"), font=small)
    img.save(path)


def draw_negative_plot(path: Path, summary: dict[str, object]) -> None:
    img = Image.new("RGB", (980, 430), "white")
    draw = ImageDraw.Draw(img)
    font = load_font(18)
    small = load_font(13)
    title = load_font(22)
    draw.text((40, 24), "Stress regime: G=8, imbalanced clusters", fill=hex_color("ink"), font=title)
    x0, y0 = 95, 350
    draw.line((x0, 70, x0, y0), fill=hex_color("muted"), width=2)
    draw.line((x0, y0, 900, y0), fill=hex_color("muted"), width=2)
    nominal_y = y0 - int((0.95 - 0.45) / 0.55 * 260)
    draw.line((x0, nominal_y, 900, nominal_y), fill=hex_color("gold"), width=3)
    draw.text((760, nominal_y - 22), "target 0.95", fill=hex_color("gold"), font=small)
    rows = summary["rows"]
    colors = {"naive_iid_ols_z": hex_color("red"), "cluster_robust_z": hex_color("teal")}
    for i, rho in enumerate(ICC_GRID):
        row = next(item for item in rows if item["G"] == 8 and item["rho"] == rho and item["imbalance"] == "imbalanced")
        cx = x0 + 90 + i * 180
        for j, method in enumerate(["naive_iid_ols_z", "cluster_robust_z"]):
            value = row["methods"][method]["coverage"]
            bar_h = int((value - 0.45) / 0.55 * 260)
            x = cx + j * 38
            draw.rectangle((x, y0 - bar_h, x + 28, y0), fill=colors[method])
            draw.text((x - 4, y0 - bar_h - 22), f"{value:.2f}", fill=hex_color("ink"), font=small)
        draw.text((cx + 2, y0 + 16), f"rho={rho:.1f}", fill=hex_color("muted"), font=font)
    draw.rectangle((650, 26, 672, 44), fill=colors["naive_iid_ols_z"])
    draw.text((680, 24), "naive", fill=hex_color("ink"), font=small)
    draw.rectangle((650, 52, 672, 70), fill=colors["cluster_robust_z"])
    draw.text((680, 50), "cluster", fill=hex_color("ink"), font=small)
    img.save(path)


def draw_model_page(slide, assets: Path, manifest: dict, refs: list[str], summary: dict[str, object]):
    add_text(slide, "Synthetic benchmark evidence boundary: generated DGP only, not completed validation or clinical evidence.", 0.82, 1.18, 11.8, 0.26, 10.6, "gold", True)
    add_text(slide, "DGP", 0.92, 1.58, 1.3, 0.24, 13, "muted", True)
    rect(slide, "Y_ij = beta_0 + beta_1 T_ij + u_j + epsilon_ij\n\nEstimand: beta_1 = treatment effect", 0.9, 1.9, 5.1, 1.65, "soft_blue", "blue", 17, True)
    rect(slide, "u_j ~ N(0, tau^2)\ncenter-level random effect\nshared inside center j", 6.42, 1.65, 2.65, 1.25, "soft_teal", "teal", 12.6, True)
    rect(slide, "epsilon_ij ~ N(0, sigma^2)\nindividual residual noise", 9.55, 1.65, 2.55, 1.25, "soft_gold", "gold", 12.6, True)
    rect(slide, "ICC rho = tau^2 / (tau^2 + sigma^2)\ncenter is the correlation and inference unit", 6.65, 3.28, 5.25, 0.92, "soft_red", "red", 13, True)
    arrow(slide, 6.0, 2.7, 6.38, 2.28)
    arrow(slide, 9.08, 2.28, 9.5, 2.28)
    arrow(slide, 8.7, 3.05, 8.7, 3.25)
    add_text(slide, "Why this page matters: point estimates can remain centered near beta_1 while interval coverage fails when residuals are correlated within center.", 0.95, 4.8, 11.0, 0.48, 14.2, "ink", True)
    add_text(slide, f"Simulation grid: G={CENTER_GRID}, rho={ICC_GRID}, imbalance={IMBALANCE_GRID}, seed={summary['seed']}.", 0.95, 5.58, 11.0, 0.32, 11.2, "muted")
    add_text(slide, reference_footer(refs, "statistical-model query"), 0.95, 6.55, 11.2, 0.35, 8.4, "muted")


def draw_estimator_page(slide, assets: Path, manifest: dict, refs: list[str], summary: dict[str, object]):
    add_text(slide, "Naive iid variance treats rows as independent; cluster sandwich groups score contributions by center.", 0.85, 1.17, 11.5, 0.26, 11, "gold", True)
    rect(slide, "Naive iid OLS interval\nVar(beta_hat) = sigma_hat^2 (X'X)^(-1)\nrow residuals are pooled one by one", 0.9, 1.65, 3.1, 1.28, "soft_red", "red", 12.3, True)
    rect(slide, "V_CR = (X'X)^(-1) [ sum_g X_g' u_g u_g' X_g ] (X'X)^(-1)", 3.25, 2.7, 6.95, 0.78, "soft_blue", "blue", 16.5, True)
    rect(slide, "Center g block\nX_g rows + residual vector u_g\naggregated before variance", 10.45, 1.65, 2.05, 1.28, "soft_teal", "teal", 11.2, True)
    arrow(slide, 4.0, 2.28, 5.0, 2.65)
    arrow(slide, 10.4, 2.3, 9.45, 2.65)
    add_text(slide, "Key change: the middle term preserves within-center covariance in the score. The current benchmark uses cluster-robust z intervals; small-G correction is reserved for the planned next experiment.", 1.0, 4.18, 11.1, 0.56, 13.2, "ink", True)
    add_text(slide, "Synthetic method labels: naive_iid_ols_z versus cluster_robust_z. Both estimate the same beta_1; only the interval variance changes.", 1.0, 5.15, 11.1, 0.34, 11.3, "muted")
    add_text(slide, reference_footer(refs, "estimator/variance query"), 0.95, 6.55, 11.2, 0.35, 8.4, "muted")


def draw_design_page(slide, assets: Path, manifest: dict, refs: list[str], summary: dict[str, object]):
    rect(slide, "DGP knobs\nG: 8 / 20 / 50\nrho: 0 / .1 / .3 / .5\ncluster imbalance", 0.85, 2.28, 2.3, 1.25, "soft_gold", "gold", 11.3, True)
    rect(slide, f"Monte Carlo data\n{REPLICATES} replicates per cell\nY_ij, T_ij, center j", 3.7, 2.28, 2.25, 1.25, "soft_blue", "blue", 11.3, True)
    rect(slide, "naive iid OLS z interval", 6.65, 1.66, 2.2, 0.72, "soft_red", "red", 11.3, True)
    rect(slide, "cluster-robust z interval\ncenter scores aggregated", 6.65, 3.18, 2.2, 0.82, "soft_teal", "teal", 10.7, True)
    rect(slide, "Endpoint evaluation\ncoverage near 0.95\nbias and interval width", 9.7, 2.36, 2.35, 1.18, "soft_blue", "blue", 11.3, True)
    arrow(slide, 3.15, 2.9, 3.68, 2.9)
    arrow(slide, 5.95, 2.9, 6.62, 2.05)
    arrow(slide, 5.95, 2.9, 6.62, 3.58)
    arrow(slide, 8.86, 2.05, 9.68, 2.72)
    arrow(slide, 8.86, 3.58, 9.68, 3.1)
    add_text(slide, "Diagram contract: structural connectors, visible arrowheads, left-to-right reading, no edge crossing.", 0.95, 4.9, 11.1, 0.34, 12.6, "ink", True)
    add_text(slide, "Synthetic simulation evidence boundary: this experiment distinguishes interval behavior; it is not a general theorem.", 0.95, 5.45, 11.1, 0.3, 11.1, "gold", True)
    manifest["simulation_design_diagram"] = {
        "structural_connectors": ["dgp_to_data", "data_to_naive", "data_to_cluster", "naive_to_endpoint", "cluster_to_endpoint"],
        "arrowheads": "DrawingML a:tailEnd type=triangle on every connector",
        "edge_crossing": "none",
        "reading_direction": "left_to_right",
        "endpoint_semantics": ["95% interval coverage", "bias", "interval width"],
    }
    add_text(slide, reference_footer(refs, "simulation-design query"), 0.95, 6.55, 11.2, 0.35, 8.4, "muted")


def draw_result_page(slide, assets: Path, manifest: dict, refs: list[str], summary: dict[str, object]):
    plot = assets / "coverage_by_icc.png"
    draw_coverage_plot(plot, summary)
    slide.shapes.add_picture(str(plot), inch(0.55), inch(1.28), width=inch(8.65))
    rect(slide, "Reading target\nCoverage close to nominal 0.95 is the goal.\nAbove or below nominal is not automatically better.", 9.55, 1.45, 2.9, 1.18, "soft_gold", "gold", 11.4, True)
    stress = summary["negative_result"]
    rect(slide, f"Observed in this synthetic run\nG=8, rho=.5, imbalanced:\nnaive={stress['naive_iid_coverage']:.2f}\ncluster={stress['cluster_robust_coverage']:.2f}", 9.55, 3.05, 2.9, 1.38, "soft_teal", "teal", 11.4, True)
    add_text(slide, "Conclusion limited to this simulation: cluster-robust intervals repair much of the iid undercoverage, but finite-center stress remains visible.", 0.95, 5.77, 11.0, 0.38, 12.8, "ink", True)
    add_text(slide, "Synthetic simulation evidence boundary; error bars are Monte Carlo uncertainty from deterministic simulation output.", 0.95, 6.22, 11.0, 0.28, 10.6, "gold", True)
    add_text(slide, reference_footer(refs, "coverage-result query"), 0.95, 6.62, 11.2, 0.28, 8.4, "muted")


def draw_negative_page(slide, assets: Path, manifest: dict, refs: list[str], summary: dict[str, object]):
    plot = assets / "small_g_negative_result.png"
    draw_negative_plot(plot, summary)
    slide.shapes.add_picture(str(plot), inch(0.75), inch(1.38), width=inch(6.7))
    stress = summary["negative_result"]
    rect(slide, f"Negative result\n{stress['condition']}\ncluster-robust z coverage = {stress['cluster_robust_coverage']:.2f}", 8.0, 1.48, 3.55, 1.18, "soft_red", "red", 11.7, True)
    rect(slide, "Failure mechanism\nFew independent centers make the sandwich variance noisy; imbalance amplifies center-level leverage.", 8.0, 3.05, 3.55, 1.1, "soft_gold", "gold", 11.4, True)
    rect(slide, "Next experiment is planned, not completed\nCompare CR2 small-sample correction and wild cluster bootstrap on the same grid.", 8.0, 4.56, 3.55, 1.2, "soft_teal", "teal", 11.2, True)
    add_text(slide, "This page uses completed synthetic evidence only for the failure diagnosis; the proposed correction methods are explicitly future work.", 0.95, 6.1, 11.1, 0.35, 12.2, "ink", True)
    manifest["negative_result_claim"] = stress
    add_text(slide, reference_footer(refs, "negative-result query"), 0.95, 6.62, 11.2, 0.28, 8.4, "muted")


SLIDES = [
    ("Why iid intervals fail with center correlation", "The estimand is stable, but the uncertainty model changes.", "STATISTICAL_MODEL", draw_model_page),
    ("Cluster sandwich changes the variance object", "The center, not the row, becomes the covariance aggregation unit.", "ESTIMATOR", draw_estimator_page),
    ("Simulation design tests interval behavior", "DGP knobs flow into two interval methods and one endpoint gate.", "SIMULATION_DESIGN", draw_design_page),
    ("Coverage falls when ICC and imbalance rise", "Coverage near 0.95 is the target; uncertainty must be visible.", "RESULT_FIGURE", draw_result_page),
    ("Small-G stress remains the negative result", "The next experiment must test finite-center corrections.", "NEGATIVE_RESULT", draw_negative_page),
]


def build_pptx(path: Path, assets: Path, manifest: dict, summary: dict[str, object]) -> None:
    prs = Presentation()
    prs.slide_width = inch(W)
    prs.slide_height = inch(H)
    blank = prs.slide_layouts[6]
    manifest["slides"] = []
    for index, (title, message, archetype, drawer) in enumerate(SLIDES, start=1):
        retrieval = retrieve_references(archetype)
        refs = list(retrieval["selected_ids"])
        slide = prs.slides.add_slide(blank)
        header(slide, index, title, message)
        drawer(slide, assets, manifest, refs, summary)
        manifest["slides"].append({
            "slide": index,
            "title": title,
            "archetype": archetype,
            "reference_ids": refs,
            "reference_retrieval": retrieval,
            "learned_organization": retrieval["organization_lesson"],
            "reference_rationale": "References are selected by auditable semantic query over inspected page records with rendered-page checksums; they inform organization only.",
            "style_not_copied": "No whole-slide screenshot, public slide styling, private CARE figure, or clinical/patient image is copied.",
            "what_not_copied": retrieval["what_was_not_copied"],
            "evidence_status": "synthetic_simulation_generated" if archetype in {"RESULT_FIGURE", "NEGATIVE_RESULT"} else "synthetic_model_or_simulation_context",
            "expected_scientific_objects": {
                "STATISTICAL_MODEL": ["beta_1 estimand", "DGP formula", "u_j random effect", "epsilon_ij residual", "ICC rho", "center inference unit"],
                "ESTIMATOR": ["naive variance formula", "cluster sandwich formula", "X_g block", "u_g residual vector", "center aggregation"],
                "SIMULATION_DESIGN": ["DGP knobs", "replicates", "naive interval branch", "cluster-robust interval branch", "coverage endpoint gate"],
                "RESULT_FIGURE": ["coverage plot", "nominal 95% line", "method comparison", "Monte Carlo uncertainty", "synthetic boundary"],
                "NEGATIVE_RESULT": ["small-G stress evidence", "coverage shortfall", "failure mechanism", "planned CR2/wild bootstrap experiment"],
            }[archetype],
        })
    prs.save(path)


def editable_slide_count(pptx_path: Path) -> int:
    with ZipFile(pptx_path) as zf:
        return len([name for name in zf.namelist() if name.startswith("ppt/slides/slide") and name.endswith(".xml")])


def find_renderer() -> str | None:
    explicit = os.environ.get("RESEARCH_PPTX_RENDERER")
    if explicit and Path(explicit).exists():
        return explicit
    for name in ("soffice", "libreoffice"):
        found = shutil.which(name)
        if found:
            return found
    tools = Path(".cache/tools")
    if tools.exists():
        for extracted_soffice in sorted(tools.glob("squashfs-root/opt/libreoffice*/program/soffice")):
            return str(extracted_soffice)
        extracted = tools / "squashfs-root" / "AppRun"
        if extracted.exists():
            return str(extracted)
        for candidate in sorted(tools.glob("LibreOffice*.AppImage")):
            return str(candidate)
    return None


def render_pptx(pptx_path: Path, out_dir: Path) -> dict:
    renderer = find_renderer()
    render_dir = out_dir / "rendered"
    pdf_dir = out_dir / "pdf"
    profile_dir = out_dir / "lo-profile"
    home_dir = out_dir / "lo-home"
    cache_dir = out_dir / "fontconfig-cache"
    render_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir.mkdir(parents=True, exist_ok=True)
    profile_dir.mkdir(parents=True, exist_ok=True)
    home_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)
    if not renderer:
        return {"status": "BLOCKED_REAL_PPTX_RENDER", "reason": "no soffice/libreoffice/RESEARCH_PPTX_RENDERER found", "png_count": 0}
    profile_uri = profile_dir.resolve().as_uri()
    env = os.environ.copy()
    env["HOME"] = str(home_dir.resolve())
    env["XDG_CACHE_HOME"] = str(cache_dir.resolve())
    cmd = [
        renderer,
        f"-env:UserInstallation={profile_uri}",
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        str(pdf_dir.resolve()),
        str(pptx_path.resolve()),
    ]
    result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=120, env=env)
    pdf_candidates = sorted(pdf_dir.glob("*.pdf"))
    if result.returncode != 0 or not pdf_candidates:
        return {"status": "BLOCKED_REAL_PPTX_RENDER", "renderer": renderer, "returncode": result.returncode, "stderr": result.stderr[-1000:], "png_count": 0}
    pdftoppm = shutil.which("pdftoppm")
    if not pdftoppm:
        return {"status": "BLOCKED_REAL_PPTX_RENDER", "renderer": renderer, "reason": "pdftoppm not found after real PPTX-to-PDF conversion", "png_count": 0}
    prefix = render_dir / "slide"
    ppm = subprocess.run([pdftoppm, "-png", "-r", "160", str(pdf_candidates[0]), str(prefix)], check=False, capture_output=True, text=True, timeout=120)
    pngs = sorted(render_dir.glob("slide-*.png"))
    return {
        "status": "ok" if ppm.returncode == 0 and len(pngs) == 5 else "BLOCKED_REAL_PPTX_RENDER",
        "renderer": renderer,
        "pptx_to_pdf": str(pdf_candidates[0]),
        "png_count": len(pngs),
        "rendered_pngs": [str(path) for path in pngs],
        "returncode": ppm.returncode,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=Path(".cache/statistical-method-group-meeting-benchmark"))
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    assets = args.out_dir / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    summary = run_simulation(args.out_dir)
    pptx_path = args.out_dir / "statistical_method_group_meeting_benchmark.pptx"
    manifest_path = args.out_dir / "EVIDENCE_MANIFEST.json"
    render_status_path = args.out_dir / "RENDER_STATUS.json"
    manifest: dict = {
        "status": "GENERATED_SOURCE_ARTIFACTS_ONLY",
        "generator_may_pass": False,
        "task_key": "016_statistical_method_group_meeting_benchmark",
        "rights_note": "Synthetic data only; no downloaded public deck image, private CARE figure, whole-slide screenshot, or patient image is copied.",
        "benchmark_story": "Multi-center correlation can leave beta_1 estimates nearly unbiased while interval coverage fails; cluster-robust z intervals repair much of the issue but small-G/high-ICC stress remains a negative result.",
        "simulation_summary": summary,
    }
    build_pptx(pptx_path, assets, manifest, summary)
    manifest["pptx"] = str(pptx_path)
    manifest["editable_slide_count"] = editable_slide_count(pptx_path)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    render = render_pptx(pptx_path, args.out_dir)
    render_status_path.write_text(json.dumps(render, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"pptx": str(pptx_path), "evidence_manifest": str(manifest_path), "render_status": str(render_status_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
