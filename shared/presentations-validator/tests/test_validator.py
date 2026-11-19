"""Public regression fixtures are generated synthetic PDFs, never private decks."""

import json
import subprocess
import sys
from pathlib import Path

import pymupdf as pdf
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import validator as v

W, H = 160 * 72 / 25.4, 90 * 72 / 25.4


def put(page, text, x=25, y=70, size=10.959, font="helv"):
    page.insert_text((x, y), text, fontsize=size, fontname=font)


def center(page, text, y, size):
    put(
        page,
        text,
        (page.rect.width - pdf.get_text_length(text, fontsize=size)) / 2,
        y,
        size,
    )


def make_deck(
    path,
    *,
    author=True,
    date=True,
    title=True,
    body="A measured comparison supports the conclusion.",
    caption=None,
    question_size=16,
    question_fraction=0.78,
    question_dx=0,
    width=W,
    height=H,
    blank_body=False,
):
    d = pdf.open()
    p = d.new_page(width=width, height=height)
    if title:
        center(p, "Synthetic Study", 65, 24)
    if author:
        center(p, "Example Author", 101, 12.5)
    if date:
        center(p, "19 November 2026", 130, 12.5)
    p = d.new_page(width=width, height=height)
    if not blank_body:
        put(p, "Measured result", y=37, size=13)
        if caption is not None:
            p.draw_rect((40, 65, 300, 125), color=(0, 0, 0))
            put(p, caption, x=40, y=144, size=7.97)
        else:
            for i, line in enumerate(body.split("\n")):
                put(p, line, y=70 + i * 14)
    p = d.new_page(width=width, height=height)
    put(p, "Conclusion", y=37, size=13)
    put(p, "The measured effect supports further study.", y=75)
    top, bottom = 46 * height / 255.12, 245 * height / 255.12
    cy = top + question_fraction * (bottom - top)
    font = pdf.Font("helv")
    baseline = cy + (font.ascender + font.descender) * question_size / 2
    text = "Questions?"
    x = (width - pdf.get_text_length(text, fontsize=question_size)) / 2 + question_dx
    put(p, text, x, baseline, question_size)
    d.save(path)
    d.close()
    return path


# Every auto rule has a PDF positive and a PDF negative. Expected labels below
# are authored independently of detector output; no private label is loaded.
CASES = {
    "LAY-GEOMETRY": ({}, {"width": 500}),
    "CAP-NO-LABEL-CHAINS": (
        {"caption": "Figure 1 shows the measured trend."},
        {"caption": "Figure 1 shows A; B."},
    ),
    "CAP-NO-RUNTIME": (
        {"caption": "Figure 1 shows the measured trend."},
        {"caption": "Figure 1 runtime is 12 seconds."},
    ),
    "CAP-NO-DATA-VERSION": (
        {"caption": "Figure 1 shows the measured trend."},
        {"caption": "Figure 1 uses data version 3."},
    ),
    "TEXT-NO-CONTRAST": ({}, {"body": "It is not a result but a slogan."}),
    "TYPE-CLOSING-QUESTION": ({}, {"question_size": 12}),
    "LAY-CLOSING-QUESTION-Y": ({}, {"question_fraction": 0.4}),
    "TEXT-COVER-TITLE": ({}, {"title": False}),
    "TEXT-COVER-AUTHOR": ({}, {"author": False}),
    "TEXT-COVER-DATE": ({}, {"date": False}),
    "TEXT-NO-AUDIT-TOKENS": (
        {},
        {"body": "receipt PASS sha256: abcdef0123456789abcdef0123456789ab"},
    ),
    "TEXT-NO-FILE-PATHS": (
        {},
        {"body": "See /workspace/reports/result.json for details."},
    ),
    "TEXT-NO-INTERNAL-VERSIONS": ({}, {"body": "Internal revision v7 is ready."}),
    "TEXT-WORD-BUDGET": ({}, {"body": "\n".join(["word " * 20] * 10)}),
    "TEXT-EXTRACTION-COVERAGE": ({}, {"blank_body": True}),
    "CAP-SINGLE-SENTENCE": (
        {"caption": "Figure 1 shows the measured trend."},
        {"caption": "Figure 1 shows the trend. It rises."},
    ),
}


@pytest.mark.parametrize("rule_id", list(CASES))
@pytest.mark.parametrize("bad", [False, True], ids=["positive", "negative"])
def test_every_auto_rule_with_synthetic_pdf(tmp_path, rule_id, bad):
    path = make_deck(tmp_path / "synthetic.pdf", **CASES[rule_id][int(bad)])
    report = v.validate(path, tmp_path / "report", profile="v19")
    assert not report["errors"], report["errors"]
    hits = [
        f
        for f in report["findings"]
        if f["rule_id"] == rule_id and f["status"] == "FAIL"
    ]
    assert bool(hits) == bad, (rule_id, hits)


def test_registry_complete_and_detector_contracts():
    rows = v.rules()
    assert len(rows) == 117
    assert {r["id"] for r in rows if r["mode"] == "auto"} == set(CASES)
    assert len({r["id"] for r in rows}) == len(rows)
    assert all(r["thresholds"] is not None for r in rows)
    assert all(r["detector"] is None for r in rows if r["mode"] == "judged")


def test_pdf_only_non_beamer_and_never_semantic_pass(tmp_path):
    p = make_deck(tmp_path / "ordinary.pdf")
    r = v.validate(p, tmp_path / "report")
    assert r["auto_verdict"] == "PASS"
    assert r["verdict"] == "REVIEW"
    assert r["measured_pages"] == 3
    assert r["human_checklist"]
    assert all(
        c["status"] != "PASS" for c in r["coverage"] if c["rule_id"] == "COMP-REASONING"
    )
    assert (tmp_path / "report/report.md").read_text().startswith("总判定：")
    assert (
        json.loads((tmp_path / "report/report.json").read_text())["schema"]
        == "generic-deck-report-v1"
    )


def test_author_in_tex_must_be_visible(tmp_path):
    p = make_deck(tmp_path / "ordinary.pdf", author=False)
    tex = tmp_path / "source.tex"
    tex.write_text(r"\author{Example Author}")
    r = v.validate(p, tmp_path / "out", tex_path=tex)
    assert any(f["rule_id"] == "TEXT-COVER-AUTHOR" for f in r["findings"])


def test_later_definition_does_not_fix_first_use(tmp_path):
    p = make_deck(tmp_path / "ordinary.pdf", body="XYZ is measured here.")
    d = pdf.open(p)
    put(d[-1], "Xylophone yield zone (XYZ) is defined later.", y=100)
    d.save(tmp_path / "later.pdf")
    d.close()
    r = v.validate(tmp_path / "later.pdf", tmp_path / "out")
    assert any(
        f["rule_id"] == "COMP-TERMS"
        and f["page"] == 2
        and f["details"]["term"] == "XYZ"
        for f in r["findings"]
    )


def test_prior_expansion_is_recognized(tmp_path):
    p = make_deck(
        tmp_path / "ordinary.pdf",
        body="Xylophone yield zone (XYZ) is measured.\nXYZ remains stable.",
    )
    r = v.validate(p, tmp_path / "out")
    assert not any(
        f["rule_id"] == "COMP-TERMS" and f["details"].get("term") == "XYZ"
        for f in r["findings"]
    )


def test_filename_metadata_and_hash_independence(tmp_path):
    a = make_deck(tmp_path / "alpha.pdf")
    b = tmp_path / "different-v999.pdf"
    doc = pdf.open(a)
    doc.set_metadata(
        {"author": "Different Author", "title": "arbitrary", "subject": "PASS"}
    )
    doc.save(b)
    doc.close()
    x = v.validate(a, tmp_path / "a")
    y = v.validate(b, tmp_path / "b")
    assert x["findings"] == y["findings"]
    assert x["coverage"] == y["coverage"]


def test_invisible_text_does_not_supply_author(tmp_path):
    p = make_deck(tmp_path / "ordinary.pdf", author=False)
    d = pdf.open(p)
    d[0].insert_text((150, 101), "Example Author", fontsize=12.5, render_mode=3)
    d.save(tmp_path / "hidden.pdf")
    d.close()
    r = v.validate(tmp_path / "hidden.pdf", tmp_path / "out")
    assert any(f["rule_id"] == "TEXT-COVER-AUTHOR" for f in r["findings"])


def test_budget_is_configurable_and_boundary_inclusive(tmp_path):
    p = make_deck(tmp_path / "ordinary.pdf", body="one two three four five")
    r = v.validate(p, tmp_path / "out", word_budget=7)
    assert not any(
        f["rule_id"] == "TEXT-WORD-BUDGET" and f["page"] == 2 for f in r["findings"]
    )
    r = v.validate(p, tmp_path / "out2", word_budget=6)
    assert any(
        f["rule_id"] == "TEXT-WORD-BUDGET" and f["page"] == 2 for f in r["findings"]
    )


def test_cli_bad_pdf_emits_error_reports(tmp_path):
    p = tmp_path / "bad.pdf"
    p.write_text("not a PDF")
    cp = subprocess.run(
        [
            sys.executable,
            str(ROOT / "validator.py"),
            str(p),
            "--out",
            str(tmp_path / "out"),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    assert cp.returncode == 3
    assert json.loads((tmp_path / "out/report.json").read_text())["verdict"] == "ERROR"


def test_chinese_date_and_author(tmp_path):
    d = pdf.open()
    p = d.new_page(width=W, height=H)
    put(p, "Synthetic Study", y=65, size=24)
    put(p, "示例作者", x=160, y=101, size=12.5, font="china-s")
    put(p, "2026 年 11 月 19 日", x=150, y=130, size=12.5, font="china-s")
    path = tmp_path / "cjk.pdf"
    d.save(path)
    d.close()
    r = v.validate(path, tmp_path / "out")
    assert not any(
        f["rule_id"] in {"TEXT-COVER-AUTHOR", "TEXT-COVER-DATE"} for f in r["findings"]
    )


def test_tex_compression_is_reviewed_and_source_optional(tmp_path):
    p = make_deck(tmp_path / "ordinary.pdf")
    tex = tmp_path / "source.tex"
    tex.write_text("\\vspace{-2pt}\n\\nointerlineskip\n\\setlength{\\tabcolsep}{2pt}")
    r = v.validate(p, tmp_path / "out", tex_path=tex, profile="v19")
    hits = [f for f in r["findings"] if f["rule_id"] == "TYPE-NO-COMPRESSION"]
    assert len(hits) == 3
    assert all(f["status"] == "REVIEW" for f in hits)


def test_plain_pass_verb_is_not_audit_token(tmp_path):
    p = make_deck(
        tmp_path / "ordinary.pdf",
        body="The method must pass four scientific conditions.",
    )
    r = v.validate(p, tmp_path / "out")
    assert not any(f["rule_id"] == "TEXT-NO-AUDIT-TOKENS" for f in r["findings"])


def test_chinese_spacing_spans_remain_visible(tmp_path):
    d = pdf.open()
    p = d.new_page(width=W, height=H)
    put(p, "Synthetic Study", y=65, size=24)
    put(p, "Example Author", x=150, y=101, size=12.5)
    # Separate Latin and CJK spans, with leading spaces in the CJK spans.
    x = 130
    for text, font in [
        ("2026", "helv"),
        (" 年", "china-s"),
        ("11", "helv"),
        (" 月", "china-s"),
        ("19", "helv"),
        (" 日", "china-s"),
    ]:
        put(p, text, x=x, y=130, size=12.5, font=font)
        x += pdf.Font(font).text_length(text, fontsize=12.5)
    path = tmp_path / "mixed.pdf"
    d.save(path)
    d.close()
    r = v.validate(path, tmp_path / "out")
    assert not any(f["rule_id"] == "TEXT-COVER-DATE" for f in r["findings"])


@pytest.mark.parametrize(
    "rule_id,options",
    [
        ("CAP-NO-BARE-RESULTS", {"caption": "Figure 1: 0.812"}),
        ("TEXT-NO-META", {"body": "We checked this contract yesterday."}),
        (
            "TEXT-NO-LABEL-PHRASES",
            {"body": "Unlock the power of a revolutionary method."},
        ),
        ("TEXT-NO-ENDING-DISCLAIMER", {"body": "For reference only."}),
        ("CAP-REQUIRED", {"caption": "Unmarked label"}),
        ("ROLE-COVER-CONTENT", {}),
        ("FOOT-NATIVE-COMPONENTS", {}),
        ("TYPE-BODY", {"body": "The example uses a fixed large font."}),
        ("LAY-BODY-WHITESPACE", {}),
        ("ROLE-CLOSING-NO-EXTRAS", {}),
    ],
)
def test_partial_rules_have_real_screening_evidence(tmp_path, rule_id, options):
    p = make_deck(tmp_path / "ordinary.pdf", **options)
    d = pdf.open(p)
    if rule_id == "CAP-REQUIRED":
        # A visible object without any extracted explanation or caption.
        d[1].draw_rect((40, 160, 300, 200), color=(0, 0, 0))
    if rule_id == "ROLE-COVER-CONTENT":
        put(d[0], "An extra subtitle appears here.", y=155, size=10)
    if rule_id == "TYPE-BODY":
        put(d[1], "Oversized paragraph text.", y=105, size=18)
    if rule_id == "ROLE-CLOSING-NO-EXTRAS":
        put(d[-1], "contact@example.invalid", y=100, size=10)
    d.save(tmp_path / "screen.pdf")
    d.close()
    r = v.validate(tmp_path / "screen.pdf", tmp_path / "out", profile="v19")
    assert not r["errors"]
    assert any(
        f["rule_id"] == rule_id and f["status"] == "REVIEW" for f in r["findings"]
    )
    assert any(c["rule_id"] == rule_id for c in r["human_checklist"])


def test_bad_detector_fails_loudly_instead_of_passing(tmp_path, monkeypatch):
    def broken(*args):
        raise RuntimeError("synthetic detector failure")

    monkeypatch.setattr(v, "check_geometry", broken)
    p = make_deck(tmp_path / "ordinary.pdf")
    r = v.validate(p, tmp_path / "out", profile="v19")
    assert r["verdict"] == "ERROR"
    assert len(r["errors"]) == 3
    assert sum(c["status"] == "ERROR" for c in r["coverage"]) == 3


def test_caption_decimals_are_not_multiple_sentences(tmp_path):
    p = make_deck(tmp_path / "ordinary.pdf", caption="Fig. 1 shows an effect of 0.812.")
    r = v.validate(p, tmp_path / "out")
    assert not any(f["rule_id"] == "CAP-SINGLE-SENTENCE" for f in r["findings"])


def test_positioned_word_gaps_do_not_erase_author_or_date(tmp_path):
    # TeX-like output: words are separately positioned, with no literal space
    # glyphs. PDF text extraction reconstructs the visible word boundaries.
    d = pdf.open()
    p = d.new_page(width=W, height=H)
    put(p, "Synthetic Study", y=65, size=24)
    put(p, "Example", x=150, y=101, size=12.5)
    put(p, "Author", x=202, y=101, size=12.5)
    put(p, "19", x=130, y=130, size=12.5)
    put(p, "November", x=149, y=130, size=12.5)
    put(p, "2026", x=212, y=130, size=12.5)
    path = tmp_path / "positioned.pdf"
    d.save(path)
    d.close()
    r = v.validate(path, tmp_path / "out")
    assert not any(
        f["rule_id"] in {"TEXT-COVER-AUTHOR", "TEXT-COVER-DATE"} for f in r["findings"]
    )


@pytest.mark.parametrize("budget", [float("nan"), float("inf"), 0, -1])
def test_invalid_budget_cannot_silently_pass(tmp_path, budget):
    p = make_deck(tmp_path / "ordinary.pdf")
    with pytest.raises(ValueError, match="finite and positive"):
        v.validate(p, tmp_path / "out", word_budget=budget)


def test_effective_thresholds_are_recorded_for_clean_deck(tmp_path):
    p = make_deck(tmp_path / "ordinary.pdf")
    r = v.validate(p, tmp_path / "out", word_budget=160)
    assert r["effective_thresholds"]["TEXT-WORD-BUDGET"]["max_units"] == 160


def test_callable_attribute_is_not_a_log_file(tmp_path):
    p = make_deck(tmp_path / "ordinary.pdf", body="value = math.log(2)")
    r = v.validate(p, tmp_path / "out")
    assert not any(f["rule_id"] == "TEXT-NO-FILE-PATHS" for f in r["findings"])
    p = make_deck(
        tmp_path / "real.pdf", body="See results.log for the recorded output."
    )
    r = v.validate(p, tmp_path / "real-out")
    assert any(f["rule_id"] == "TEXT-NO-FILE-PATHS" for f in r["findings"])


def test_small_bullets_below_chart_remain_body(tmp_path):
    p = make_deck(tmp_path / "ordinary.pdf")
    d = pdf.open(p)
    page = d[1]
    page.draw_rect((25, 110, 410, 150), color=(0, 0, 0))
    # A bullet glyph from a built-in CJK font, followed by an ordinary prose
    # span at a small historical body size. A chart caption has no bullet list.
    put(page, "•", x=35, y=165, size=8, font="china-s")
    put(page, "A body observation; followed by another sentence.", x=48, y=165, size=8)
    d.save(tmp_path / "bullets.pdf")
    d.close()
    r = v.validate(tmp_path / "bullets.pdf", tmp_path / "out")
    assert not any(
        f["rule_id"] in {"CAP-NO-LABEL-CHAINS", "CAP-SINGLE-SENTENCE"}
        and f["page"] == 2
        for f in r["findings"]
    )


def test_tounicode_ligature_expansion_survives_visible_filter(tmp_path):
    # Standard font plus a synthetic ToUnicode map: one painted fi glyph maps
    # to two Unicode characters. No external fonts or private assets are used.
    d = pdf.open()
    page = d.new_page(width=W, height=H)
    put(page, "xx", x=40, y=80, size=20, font="tiro")
    font_xref = next(f[0] for f in d.get_page_fonts(0) if f[3] == "Times-Roman")
    cmap = d.get_new_xref()
    d.update_object(cmap, "<< >>")
    d.update_stream(
        cmap,
        b"/CIDInit /ProcSet findresource begin 12 dict begin begincmap /CIDSystemInfo << /Registry (Example) /Ordering (Example) /Supplement 0 >> def /CMapName /ExampleMap def /CMapType 2 def 1 begincodespacerange <00> <FF> endcodespacerange 1 beginbfchar <78> <00660069> endbfchar endcmap CMapName currentdict /CMap defineresource pop end end",
    )
    d.xref_set_key(
        font_xref,
        "Encoding",
        "<< /Type /Encoding /BaseEncoding /WinAnsiEncoding /Differences [120 /fi] >>",
    )
    d.xref_set_key(font_xref, "ToUnicode", f"{cmap} 0 R")
    path = tmp_path / "ligature.pdf"
    d.save(path)
    d.close()
    with pdf.open(path) as doc:
        raw = doc[0].get_text().strip()
        lines = v.measure.extract_lines(doc[0], v.measurement_config())
    assert raw == "fifi"
    assert v.text_of(lines) == "fifi"
