#!/usr/bin/env python3
"""Generate a four-slide research-group-meeting regression deck.

The generator creates only source artifacts and evidence. It never writes a
final scientific PASS; that decision belongs to the independent reviewer.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import shutil
import subprocess
from pathlib import Path
from zipfile import ZipFile

from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt


W, H = 13.333, 7.5
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
    "soft_teal": "E1F4F1",
    "soft_blue": "E5EEF8",
    "soft_gold": "FBF1D6",
    "soft_red": "F8E3E1",
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


def line(slide, x1: float, y1: float, x2: float, y2: float, color: str = "muted", width: float = 1.4):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, inch(x1), inch(y1), inch(x2), inch(y2))
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(width)
    return c


def header(slide, number: int, title: str, message: str):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = rgb("bg")
    band = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, inch(0), inch(0), inch(W), inch(0.16))
    band.fill.solid()
    band.fill.fore_color.rgb = rgb("purple")
    band.line.fill.background()
    add_text(slide, title, 0.55, 0.38, 9.5, 0.36, 21, "ink", True)
    add_text(slide, f"{number:02d}/04", 11.6, 0.42, 0.95, 0.22, 9, "muted", False, PP_ALIGN.RIGHT)
    add_text(slide, message, 0.65, 0.88, 11.7, 0.34, 12.4, "purple", True)


ENDPOINT_DATA = {
    "Dice": {"Baseline": (0.82, 0.03), "Calibrated": (0.79, 0.04), "Federated": (0.76, 0.05), "Local-only": (0.72, 0.06)},
    "Lesion recall": {"Baseline": (0.58, 0.07), "Calibrated": (0.74, 0.05), "Federated": (0.69, 0.06), "Local-only": (0.63, 0.07)},
    "Burden error": {"Baseline": (0.31, 0.05), "Calibrated": (0.18, 0.04), "Federated": (0.22, 0.05), "Local-only": (0.35, 0.06)},
}


def load_font(size: int):
    for path in ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/dejavu/DejaVuSans.ttf"]:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_endpoint_chart(path: Path) -> dict:
    img = Image.new("RGB", (1060, 520), "white")
    draw = ImageDraw.Draw(img)
    font = load_font(18)
    small = load_font(14)
    colors = {"Baseline": "#1F4E79", "Calibrated": "#0F766E", "Federated": "#9A6A16", "Local-only": "#A33A34"}
    x0, y0 = 90, 390
    draw.line((x0, 55, x0, y0), fill="#5F6772", width=2)
    draw.line((x0, y0, 1010, y0), fill="#5F6772", width=2)
    for tick in range(0, 101, 20):
        y = y0 - tick * 3
        draw.line((x0 - 5, y, x0, y), fill="#5F6772", width=1)
        draw.text((38, y - 8), f"{tick/100:.1f}", fill="#17202A", font=small)
        draw.line((x0, y, 1010, y), fill="#E2E6EC", width=1)
    endpoints = list(ENDPOINT_DATA)
    methods = list(next(iter(ENDPOINT_DATA.values())))
    bar_w = 34
    group_w = 270
    for i, endpoint in enumerate(endpoints):
        gx = x0 + 60 + i * group_w
        draw.text((gx + 30, 420), endpoint, fill="#17202A", font=font)
        for j, method in enumerate(methods):
            value, err = ENDPOINT_DATA[endpoint][method]
            score = 1 - value if endpoint == "Burden error" else value
            x = gx + j * (bar_w + 12)
            y = y0 - int(score * 300)
            draw.rectangle((x, y, x + bar_w, y0), fill=colors[method])
            err_px = int(err * 300)
            draw.line((x + bar_w // 2, y - err_px, x + bar_w // 2, y + err_px), fill="#17202A", width=2)
            draw.text((x - 3, y - 25), f"{value:.2f}", fill="#17202A", font=small)
    for j, method in enumerate(methods):
        lx = 690 + (j % 2) * 170
        ly = 35 + (j // 2) * 24
        draw.rectangle((lx, ly, lx + 18, ly + 18), fill=colors[method])
        draw.text((lx + 25, ly - 1), method, fill="#17202A", font=small)
    img.save(path)
    best_by_endpoint = {
        endpoint: min(values, key=lambda key: values[key][0]) if endpoint == "Burden error" else max(values, key=lambda key: values[key][0])
        for endpoint, values in ENDPOINT_DATA.items()
    }
    return {"data": ENDPOINT_DATA, "best_by_endpoint": best_by_endpoint}


def inside_ellipse(x: int, y: int, cx: int, cy: int, rx: int, ry: int) -> bool:
    return ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1


def draw_phantom(path: Path) -> dict:
    w, h = 1040, 430
    img = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(img)
    font = load_font(17)
    small = load_font(13)
    panel_w = 230
    labels = ["Synthetic image", "GT mask", "Prediction", "FP/FN overlay"]
    gt: set[tuple[int, int]] = set()
    pred: set[tuple[int, int]] = set()
    for y in range(120):
        for x in range(120):
            if inside_ellipse(x, y, 55, 54, 22, 15) or inside_ellipse(x, y, 78, 77, 14, 18):
                gt.add((x, y))
            if inside_ellipse(x, y, 59, 57, 24, 14) or inside_ellipse(x, y, 84, 77, 11, 15) or inside_ellipse(x, y, 34, 82, 9, 7):
                pred.add((x, y))
    tp = len(gt & pred)
    fp = len(pred - gt)
    fn = len(gt - pred)
    dice = 2 * tp / (len(gt) + len(pred))
    recall = tp / len(gt)
    burden_error = (len(pred) - len(gt)) / len(gt)
    for i, label in enumerate(labels):
        xoff = 35 + i * 250
        draw.text((xoff + 35, 24), label, fill="#17202A", font=font)
        draw.rectangle((xoff, 58, xoff + panel_w, 288), outline="#C6CCD6", width=2)
        for yy in range(120):
            for xx in range(120):
                px0 = xoff + 55 + xx
                py0 = 100 + yy
                base = int(210 - 75 * math.exp(-(((xx - 60) ** 2 + (yy - 64) ** 2) / 1900)))
                if i == 0:
                    img.putpixel((px0, py0), (base, base, base))
                elif i == 1:
                    img.putpixel((px0, py0), (15, 118, 110) if (xx, yy) in gt else (238, 242, 246))
                elif i == 2:
                    img.putpixel((px0, py0), (154, 106, 22) if (xx, yy) in pred else (238, 242, 246))
                else:
                    if (xx, yy) in gt & pred:
                        img.putpixel((px0, py0), (42, 124, 84))
                    elif (xx, yy) in pred - gt:
                        img.putpixel((px0, py0), (180, 58, 52))
                    elif (xx, yy) in gt - pred:
                        img.putpixel((px0, py0), (31, 78, 121))
                    else:
                        img.putpixel((px0, py0), (238, 242, 246))
    draw.text((55, 330), f"Dice={dice:.2f}    lesion recall={recall:.2f}    burden error={burden_error:+.1%}", fill="#17202A", font=font)
    draw.text((55, 365), f"TP pixels={tp}, FP={fp}, FN={fn}; failure mechanism: small false-positive island plus shifted lesion boundary.", fill="#606977", font=small)
    img.save(path)
    return {"dice": round(dice, 3), "lesion_recall": round(recall, 3), "burden_error": round(burden_error, 3), "tp": tp, "fp": fp, "fn": fn}


def draw_result_page(slide, assets: Path, manifest: dict):
    chart_path = assets / "endpoint_ranking_chart.png"
    manifest["synthetic_endpoint_data"] = draw_endpoint_chart(chart_path)
    slide.shapes.add_picture(str(chart_path), inch(0.78), inch(1.42), width=inch(7.8))
    rect(slide, "Interpretation\nCalibrated wins recall and burden error;\nBaseline wins Dice only.", 9.0, 1.75, 3.25, 1.3, "soft_teal", "teal", 12.2, True)
    rect(slide, "Meeting decision\nFreeze endpoint priority before ranking methods.", 9.0, 3.65, 3.25, 1.0, "soft_gold", "gold", 12.2, True)
    add_text(slide, "Reference pull: figure-dominant result pages from RRL-002/RRL-012; style not copied.", 0.95, 6.55, 11.2, 0.35, 8.8, "muted")


def draw_failure_page(slide, assets: Path, manifest: dict):
    phantom_path = assets / "synthetic_segmentation_phantom.png"
    manifest["synthetic_phantom_metrics"] = draw_phantom(phantom_path)
    slide.shapes.add_picture(str(phantom_path), inch(0.72), inch(1.38), width=inch(11.85))
    add_text(slide, "Scientific object: same synthetic case, aligned GT/prediction/error overlay, case metric next to visual.", 0.95, 6.35, 11.2, 0.32, 12.2, "ink", True)
    add_text(slide, "Reference pull: aligned comparison/failure pages from RRL-010/RRL-011/RRL-017; no clinical image or public slide copied.", 0.95, 6.72, 11.2, 0.25, 8.8, "muted")


def draw_experiment_page(slide, assets: Path, manifest: dict):
    for i, site in enumerate(["Center A", "Center B", "Center C"]):
        rect(slide, f"{site}\nlocal image + local label\nexperimental unit: lesion-case", 0.75, 1.45 + i * 1.05, 2.75, 0.78, "soft_teal", "teal", 10.6, True)
        rect(slide, "local estimator\ncalibration score", 3.85, 1.5 + i * 1.05, 1.65, 0.65, "soft_blue", "blue", 10.3, True)
        line(slide, 3.55, 1.84 + i * 1.05, 3.82, 1.84 + i * 1.05, "purple", 1.6)
        line(slide, 5.55, 1.84 + i * 1.05, 6.3, 3.0, "purple", 1.4)
    rect(slide, "Transmitted\nlikelihood / score / summary update\n(raw images stay local)", 6.25, 2.38, 2.4, 1.25, "soft_gold", "gold", 11.2, True)
    line(slide, 8.72, 3.0, 9.18, 3.0, "purple", 1.8)
    rect(slide, "Global estimator\ncompare local-only vs summary-sharing", 9.2, 2.08, 3.2, 0.95, "soft_blue", "blue", 11.4, True)
    rect(slide, "Success endpoint\nlesion recall + burden error\nworst-center gap < 5%", 9.2, 3.78, 3.2, 1.05, "soft_red", "red", 11.4, True)
    add_text(slide, "Comparator: local-only model. What moves: score summaries and likelihood updates. What stays local: images, labels, case identifiers.", 0.95, 5.75, 11.3, 0.42, 12.2, "ink", True)
    add_text(slide, "Reference pull: experiment-design topology from RRL-005/RRL-013; no roadmap/card substitute.", 0.95, 6.55, 11.2, 0.35, 8.8, "muted")


def draw_model_page(slide, assets: Path, manifest: dict):
    add_text(slide, "Target estimand", 0.95, 1.4, 2.5, 0.25, 12, "muted", True)
    rect(slide, "beta1: effect of true lesion burden T_i\non downstream outcome Y_i", 0.9, 1.75, 2.9, 1.0, "soft_teal", "teal", 11.2, True)
    rect(slide, "Observed AI phenotype\nM_i = T_i + U_i\nerror varies by center", 4.15, 1.75, 2.7, 1.0, "soft_gold", "gold", 11.2, True)
    rect(slide, "Validation subset\nobserve both T_i and M_i\nestimate calibration error", 7.25, 1.75, 2.7, 1.0, "soft_blue", "blue", 11.2, True)
    rect(slide, "Inference target\nY_i = beta0 + beta1 T_i + eps_i\nnaive M_i attenuates beta1", 10.05, 1.75, 2.55, 1.0, "soft_red", "red", 10.6, True)
    for x in [3.85, 6.9, 9.95]:
        line(slide, x, 2.25, x + 0.25, 2.25, "purple", 1.8)
    add_text(slide, "Toy calibration: E[T|M,center] = alpha_center + gamma_center M. Report beta1 after validation-calibrated correction, not a raw AI burden coefficient.", 1.0, 3.55, 11.0, 0.45, 13, "ink", True)
    rect(slide, "Evidence boundary\nThis page is a generated-variable inference mechanism,\nnot completed clinical validity evidence.", 2.5, 4.65, 8.3, 0.95, "soft_teal", "teal", 12.2, True)
    add_text(slide, "Reference pull: formula-with-variable-semantics pages from RRL-007/RRL-016 plus Bayesian workflow model-check pages; formula is editable text.", 0.95, 6.55, 11.2, 0.35, 8.8, "muted")


SLIDES = [
    ("Endpoint Choice Changes the Method Ranking", "The method story changes when the endpoint changes.", "RESULT_FIGURE", draw_result_page, ["RRL-002", "RRL-012"]),
    ("Average Dice Can Hide the Hard Case", "A case page binds image, GT, prediction, error overlay, and metric.", "FAILURE_CASE", draw_failure_page, ["RRL-010", "RRL-011", "RRL-017"]),
    ("Limited-Information Multi-Center Experiment", "Raw data stay local; shared summaries are judged by endpoint-level evidence.", "EXPERIMENT_DESIGN", draw_experiment_page, ["RRL-005", "RRL-013"]),
    ("AI Phenotype Error Changes Inference", "Segmentation output is a measured variable whose error can attenuate inference.", "STATISTICAL_MODEL", draw_model_page, ["RRL-007", "RRL-016", "RRL-025"]),
]


def build_pptx(path: Path, assets: Path, manifest: dict) -> None:
    prs = Presentation()
    prs.slide_width = inch(W)
    prs.slide_height = inch(H)
    blank = prs.slide_layouts[6]
    manifest["slides"] = []
    for index, (title, message, archetype, drawer, refs) in enumerate(SLIDES, start=1):
        slide = prs.slides.add_slide(blank)
        header(slide, index, title, message)
        drawer(slide, assets, manifest)
        manifest["slides"].append({
            "slide": index,
            "title": title,
            "archetype": archetype,
            "reference_ids": refs,
            "learned_organization": "Use the referenced page function to organize scientific objects and evidence adjacency.",
            "style_not_copied": "No whole-slide screenshot, public slide styling, private CARE figure, or clinical image is copied.",
            "expected_scientific_objects": {
                "RESULT_FIGURE": ["endpoint-wise data", "error intervals", "method ranking", "endpoint decision"],
                "FAILURE_CASE": ["synthetic image", "GT mask", "prediction mask", "FP/FN overlay", "case metrics"],
                "EXPERIMENT_DESIGN": ["centers", "local image/label", "local estimator", "transmitted summary", "global estimator", "endpoint evaluation"],
                "STATISTICAL_MODEL": ["estimand", "observed AI phenotype", "measurement error", "validation subset", "inference target"],
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
        for candidate in sorted(tools.glob("LibreOffice*.AppImage")):
            return str(candidate)
    return None


def render_pptx(pptx_path: Path, out_dir: Path) -> dict:
    renderer = find_renderer()
    render_dir = out_dir / "rendered"
    pdf_dir = out_dir / "pdf"
    profile_dir = out_dir / "lo-profile"
    render_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir.mkdir(parents=True, exist_ok=True)
    profile_dir.mkdir(parents=True, exist_ok=True)
    if not renderer:
        return {"status": "BLOCKED_REAL_PPTX_RENDER", "reason": "no soffice/libreoffice/RESEARCH_PPTX_RENDERER found", "png_count": 0}
    profile_uri = profile_dir.resolve().as_uri()
    cmd = [renderer, f"-env:UserInstallation={profile_uri}", "--headless", "--convert-to", "pdf", "--outdir", str(pdf_dir), str(pptx_path)]
    result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=120)
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
        "status": "ok" if ppm.returncode == 0 and pngs else "BLOCKED_REAL_PPTX_RENDER",
        "renderer": renderer,
        "pptx_to_pdf": str(pdf_candidates[0]),
        "png_count": len(pngs),
        "rendered_pngs": [str(path) for path in pngs],
        "returncode": ppm.returncode,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=Path(".cache/research-group-meeting-regression"))
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    assets = args.out_dir / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    pptx_path = args.out_dir / "research_group_meeting_regression.pptx"
    manifest_path = args.out_dir / "EVIDENCE_MANIFEST.json"
    render_status_path = args.out_dir / "RENDER_STATUS.json"
    manifest: dict = {
        "status": "GENERATED_SOURCE_ARTIFACTS_ONLY",
        "generator_may_pass": False,
        "rights_note": "No downloaded public deck, private CARE figure, whole-slide screenshot, or clinical image is copied.",
    }
    build_pptx(pptx_path, assets, manifest)
    manifest["pptx"] = str(pptx_path)
    manifest["editable_slide_count"] = editable_slide_count(pptx_path)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    render = render_pptx(pptx_path, args.out_dir)
    render_status_path.write_text(json.dumps(render, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"pptx": str(pptx_path), "evidence_manifest": str(manifest_path), "render_status": str(render_status_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
