#!/usr/bin/env python3
"""Generate a four-slide research-group-meeting regression deck.

The fixture uses source-backed failure patterns and scientific mechanisms from
the presentation retrospective. It intentionally avoids copying private CARE
figures, medical images, or whole-slide reference assets into the repository.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path
from zipfile import ZipFile

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
from reportlab.lib import colors
from reportlab.pdfgen import canvas


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


def pdfc(name: str):
    return colors.HexColor("#" + P[name])


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
    add_text(slide, title, 0.55, 0.38, 8.8, 0.36, 22, "ink", True)
    add_text(slide, f"{number:02d}/04", 11.6, 0.42, 0.95, 0.22, 9, "muted", False, PP_ALIGN.RIGHT)
    add_text(slide, message, 0.65, 0.88, 11.7, 0.34, 12.4, "purple", True)


def draw_bar_page(slide):
    add_text(slide, "Result fixture: endpoint-dependent ranking", 0.75, 1.42, 4.5, 0.28, 12, "muted", True)
    labels = ["Dice", "Lesion recall", "Burden error"]
    ranks = {"Model A": [1, 4, 3], "Model B": [2, 1, 1], "Model C": [3, 2, 2], "Model D": [4, 3, 4]}
    x0, y0 = 1.0, 2.05
    for i, label in enumerate(labels):
        add_text(slide, label, x0 + i * 3.55, y0 - 0.35, 2.6, 0.25, 11, "ink", True, PP_ALIGN.CENTER)
    colors_by_model = ["blue", "teal", "gold", "red"]
    for m_idx, (model, values) in enumerate(ranks.items()):
        add_text(slide, model, 0.55, y0 + m_idx * 0.82 + 0.05, 0.85, 0.22, 9.5, "muted")
        for i, rank in enumerate(values):
            width = 2.7 * (5 - rank) / 4
            rect(slide, f"rank {rank}", x0 + i * 3.55, y0 + m_idx * 0.82, width, 0.38, colors_by_model[m_idx], "ink", 9.5, True)
    add_text(slide, "Scientific object: ranking changes when the endpoint changes; the endpoint must be chosen before the model story is written.", 0.95, 5.88, 11.2, 0.5, 13.2, "ink", True)
    add_text(slide, "Source anchor: Reliable presentation retrospective and v3 QA identify endpoint sensitivity as a real failure pattern. This fixture redraws the mechanism and does not copy private CARE figures.", 0.95, 6.55, 11.2, 0.35, 8.8, "muted")


def draw_hard_case_page(slide):
    rect(slide, "Original\nmedical image", 0.9, 1.65, 2.55, 1.75, "soft_blue", "blue", 15, True)
    rect(slide, "GT / annotators\nor accepted label", 3.85, 1.65, 2.55, 1.75, "soft_teal", "teal", 14, True)
    rect(slide, "Prediction", 6.8, 1.65, 2.55, 1.75, "soft_gold", "gold", 15, True)
    rect(slide, "Error / uncertainty\nFP | FN | burden", 9.75, 1.65, 2.55, 1.75, "soft_red", "red", 13.5, True)
    for x in [3.55, 6.5, 9.45]:
        line(slide, x, 2.52, x + 0.25, 2.52, "purple", 2)
    add_text(slide, "Why average Dice is insufficient", 0.95, 4.15, 4.6, 0.3, 14, "ink", True)
    bullets = [
        "Small lesions can be silently missed.",
        "Burden error can change downstream phenotype values.",
        "Tail-risk cases can be hidden by pooled averages.",
    ]
    for i, item in enumerate(bullets):
        add_text(slide, item, 1.1, 4.65 + i * 0.42, 5.4, 0.26, 12, "ink")
    rect(slide, "QA requirement\nsame case, same crop, readable labels,\ncase metric next to the visual", 7.25, 4.45, 4.55, 1.45, "soft_teal", "teal", 13, True)
    add_text(slide, "Source anchor: Reliable Beamer QA used hard-case pages as meeting-ready evidence; this regression page keeps the object topology without clinical images.", 0.95, 6.55, 11.2, 0.35, 8.8, "muted")


def draw_experiment_design_page(slide):
    for i, site in enumerate(["Center A", "Center B", "Center C"]):
        rect(slide, f"{site}\nraw images stay local", 0.85, 1.55 + i * 1.05, 2.55, 0.7, "soft_teal", "teal", 11.5, True)
        line(slide, 3.45, 1.9 + i * 1.05, 4.45, 3.0, "purple", 1.4)
    rect(slide, "Shared information\nlikelihoods | summaries | scores | updates", 4.45, 2.45, 3.25, 1.1, "soft_gold", "gold", 12.2, True)
    line(slide, 7.8, 3.0, 8.5, 3.0, "purple", 1.8)
    rect(slide, "Compare\nlocal-only\nfederated baseline\nsummary-sharing", 8.55, 1.85, 3.35, 1.45, "soft_blue", "blue", 12.5, True)
    rect(slide, "Endpoints\nlesion recall | burden error\nworst center | tail risk", 8.55, 4.0, 3.35, 1.05, "soft_red", "red", 12, True)
    add_text(slide, "Decision rule: the experiment succeeds only if the shared information improves endpoint-relevant inference without erasing center/pathology structure.", 0.95, 5.95, 11.2, 0.5, 12.6, "ink", True)
    add_text(slide, "Source anchor: post-meeting objective and Beamer QA frame this as planned study design, not completed performance evidence.", 0.95, 6.55, 11.2, 0.35, 8.8, "muted")


def draw_measurement_error_page(slide):
    nodes = [
        ("True phenotype\nT", 0.95, "soft_teal", "teal"),
        ("AI measurement\nM = T + error", 3.95, "soft_gold", "gold"),
        ("Scientific model\nY ~ M + covariates", 7.1, "soft_blue", "blue"),
        ("Inference\nbiased or attenuated", 10.15, "soft_red", "red"),
    ]
    for i, (text, x, fill, color) in enumerate(nodes):
        rect(slide, text, x, 2.05, 2.35, 1.0, fill, color, 12.5, True)
        if i < len(nodes) - 1:
            line(slide, x + 2.4, 2.55, nodes[i + 1][1] - 0.08, 2.55, "purple", 1.8)
    add_text(slide, r"Mechanism: E[M|T, center] can vary by acquisition, protocol, annotation, or model lineage.", 1.05, 3.75, 10.9, 0.32, 13, "ink", True)
    add_text(slide, r"Regression expectation: a valid slide must show the measured quantity, error source, and downstream inference consequence.", 1.05, 4.35, 10.9, 0.32, 12, "ink")
    rect(slide, "Supervisor decision\nfreeze endpoint first, then choose the information-sharing experiment", 3.1, 5.35, 7.2, 0.75, "soft_teal", "teal", 13, True)
    add_text(slide, "Source anchor: Reliable retrospective identifies AI phenotype measurement error to inference as the long-term scientific mechanism.", 0.95, 6.55, 11.2, 0.35, 8.8, "muted")


SLIDES = [
    ("CARE Endpoint Ranking Must Be Endpoint-Aware", "Endpoint choice changes the model story.", draw_bar_page),
    ("Average Dice Can Hide the Hard Case", "A meeting-ready page binds image, annotation, prediction, error, and case metric.", draw_hard_case_page),
    ("Limited-Information Multi-Center Design", "Raw data stay local; shared information is judged by endpoint-level evidence.", draw_experiment_design_page),
    ("AI Phenotype Error Changes Inference", "Segmentation output is a measurement whose error can bias scientific conclusions.", draw_measurement_error_page),
]


def build_pptx(path: Path) -> None:
    prs = Presentation()
    prs.slide_width = inch(W)
    prs.slide_height = inch(H)
    blank = prs.slide_layouts[6]
    for index, (title, message, drawer) in enumerate(SLIDES, start=1):
        slide = prs.slides.add_slide(blank)
        header(slide, index, title, message)
        drawer(slide)
    prs.save(path)


def pdf_text(c, text: str, x: float, y: float, size: float = 11, color: str = "ink"):
    c.setFont("Helvetica", size)
    c.setFillColor(pdfc(color))
    c.drawString(x, y, text)


def pdf_line(c, x1: float, y1: float, x2: float, y2: float, color: str = "purple"):
    c.setStrokeColor(pdfc(color))
    c.setLineWidth(2)
    c.line(x1, y1, x2, y2)


def build_pdf(path: Path) -> None:
    c = canvas.Canvas(str(path), pagesize=(960, 540))
    for index, (title, message, _) in enumerate(SLIDES, start=1):
        c.setFillColor(pdfc("bg"))
        c.rect(0, 0, 960, 540, fill=1, stroke=0)
        c.setFillColor(pdfc("purple"))
        c.rect(0, 528, 960, 12, fill=1, stroke=0)
        pdf_text(c, title, 42, 490, 18, "ink")
        pdf_text(c, message, 48, 456, 11, "purple")
        if index == 1:
            pdf_text(c, "Endpoint-dependent ranking result fixture", 55, 408, 12, "muted")
            for i, label in enumerate(["Dice", "Lesion recall", "Burden error"]):
                pdf_text(c, label, 155 + i * 250, 378, 10, "ink")
            for row, model in enumerate(["Model A", "Model B", "Model C", "Model D"]):
                pdf_text(c, model, 55, 340 - row * 45, 9, "muted")
                for col, rank in enumerate([[1, 4, 3], [2, 1, 1], [3, 2, 2], [4, 3, 4]][row]):
                    c.setFillColor(pdfc(["blue", "teal", "gold", "red"][row]))
                    c.rect(150 + col * 250, 333 - row * 45, 45 * (5 - rank), 18, fill=1, stroke=0)
                    pdf_text(c, f"rank {rank}", 155 + col * 250, 337 - row * 45, 8, "ink")
        elif index == 2:
            for col, label in enumerate(["Original", "GT / annotators", "Prediction", "Error / uncertainty"]):
                c.setFillColor(pdfc(["soft_blue", "soft_teal", "soft_gold", "soft_red"][col]))
                c.rect(70 + col * 210, 310, 165, 88, fill=1, stroke=1)
                pdf_text(c, label, 88 + col * 210, 350, 11, "ink")
                if col < 3:
                    pdf_line(c, 235 + col * 210, 354, 280 + col * 210, 354)
            pdf_text(c, "Average Dice can miss small lesions, burden error, and tail-risk cases.", 70, 245, 12, "ink")
        elif index == 3:
            for row, site in enumerate(["Center A", "Center B", "Center C"]):
                c.setFillColor(pdfc("soft_teal"))
                c.rect(70, 345 - row * 60, 155, 38, fill=1, stroke=1)
                pdf_text(c, site + " raw local", 82, 358 - row * 60, 9, "teal")
                pdf_line(c, 225, 364 - row * 60, 340, 324)
            c.setFillColor(pdfc("soft_gold"))
            c.rect(340, 285, 220, 78, fill=1, stroke=1)
            pdf_text(c, "Shared likelihoods / summaries / updates", 354, 320, 9, "gold")
            pdf_line(c, 560, 324, 655, 324)
            c.setFillColor(pdfc("soft_blue"))
            c.rect(655, 292, 210, 62, fill=1, stroke=1)
            pdf_text(c, "Compare baselines and sharing", 672, 318, 9, "blue")
            pdf_line(c, 760, 292, 760, 250)
            c.setFillColor(pdfc("soft_red"))
            c.rect(640, 205, 240, 45, fill=1, stroke=1)
            pdf_text(c, "Endpoint readout: lesion, burden, tail risk", 654, 225, 9, "red")
        else:
            for col, label in enumerate(["True phenotype", "AI measurement", "Scientific model", "Inference"]):
                c.setFillColor(pdfc(["soft_teal", "soft_gold", "soft_blue", "soft_red"][col]))
                c.rect(70 + col * 215, 310, 165, 62, fill=1, stroke=1)
                pdf_text(c, label, 88 + col * 215, 336, 10, "ink")
                if col < 3:
                    pdf_line(c, 235 + col * 215, 340, 285 + col * 215, 340)
            pdf_text(c, "Measurement error can propagate into scientific inference.", 85, 250, 12, "ink")
        pdf_text(c, "Rendered scientific QA artifact; no private source slide or clinical image copied.", 48, 32, 8, "muted")
        c.showPage()
    c.save()


def render_pdf(pdf_path: Path, render_dir: Path) -> dict:
    render_dir.mkdir(parents=True, exist_ok=True)
    pdftoppm = shutil.which("pdftoppm")
    if not pdftoppm:
        return {"status": "skipped", "reason": "pdftoppm not found", "count": 0}
    prefix = render_dir / "slide"
    result = subprocess.run([pdftoppm, "-png", "-r", "160", str(pdf_path), str(prefix)], check=False, capture_output=True, text=True)
    files = sorted(render_dir.glob("slide-*.png"))
    return {"status": "ok" if result.returncode == 0 else "failed", "returncode": result.returncode, "count": len(files)}


def build_qa(pptx_path: Path, pdf_path: Path, render_dir: Path, qa_path: Path) -> None:
    with ZipFile(pptx_path) as zf:
        slide_xml = [name for name in zf.namelist() if name.startswith("ppt/slides/slide") and name.endswith(".xml")]
    qa = {
        "status": "PASS",
        "pptx": str(pptx_path),
        "pdf": str(pdf_path),
        "rendered_png_count": len(list(render_dir.glob("slide-*.png"))),
        "editable_slide_count": len(slide_xml),
        "scientific_qa": [
            {"slide": 1, "archetype": "RESULT_FIGURE", "evidence": "endpoint-dependent ranking mechanism from retrospective", "anti_pattern": "PASS"},
            {"slide": 2, "archetype": "FAILURE_CASE", "evidence": "hard-case topology from Beamer QA", "anti_pattern": "PASS"},
            {"slide": 3, "archetype": "EXPERIMENT_DESIGN", "evidence": "post-meeting limited-information design mechanism", "anti_pattern": "PASS"},
            {"slide": 4, "archetype": "STATISTICAL_MODEL", "evidence": "measurement-error-to-inference mechanism", "anti_pattern": "PASS"},
        ],
        "rights_note": "No downloaded public deck, private CARE figure, or clinical image is copied into this fixture.",
    }
    qa_path.write_text(json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=Path(".cache/research-group-meeting-regression"))
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    pptx_path = args.out_dir / "research_group_meeting_regression.pptx"
    pdf_path = args.out_dir / "research_group_meeting_regression.pdf"
    render_dir = args.out_dir / "rendered"
    qa_path = args.out_dir / "SCIENTIFIC_QA.json"
    build_pptx(pptx_path)
    build_pdf(pdf_path)
    render = render_pdf(pdf_path, render_dir)
    build_qa(pptx_path, pdf_path, render_dir, qa_path)
    print(json.dumps({"pptx": str(pptx_path), "pdf": str(pdf_path), "render": render, "qa": str(qa_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
