from copy import deepcopy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import pymupdf

from presentations_validator_v2.cli import parser, run
from presentations_validator_v2.io import canonical, read_contract, sha256
from presentations_validator_v2.layout import checks
from presentations_validator_v2.layout.model import MM, Page
from presentations_validator_v2.render import Drawing, Rect, Render, Text


def contract_path():
    for parent in Path(__file__).resolve().parents:
        path = Path(__file__).parent / "fixtures/shared_beamer_core_layout_contract.yaml"
        if path.is_file():
            return path
    raise FileNotFoundError("Frozen contract")


CONTRACT = read_contract(contract_path())
W, H = 384, 216
STROKE = (0.2, 0.4, 0.6)


def text(value, bbox, size=10.959, font="TeXGyreTermes-Regular", flags=0):
    return Text(Rect(*bbox), ({"text": value, "font": font, "size": size, "flags": flags},),
                bbox[3] - 2)


def path(a, b):
    return Drawing(Rect(min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])),
                   ((a, b),), 1, STROKE, None)


def page(objects, *, lines=(), drawings=(), images=(), links=(), **spec):
    return Page({"id": "generic-page", "objects": objects, "spacing": [], **spec},
                Render(Rect(0, 0, W, H), list(lines), list(drawings), list(images), list(links)))


def obj(id_, role, **kwargs):
    return {"id": id_, "role": role, **kwargs}


def statuses(rows):
    return [row.status for row in rows]


class GeometryBoundaries(unittest.TestCase):
    def test_font_tolerance_and_compression(self):
        for delta, wanted in ((-0.101, "FAIL"), (-0.1, "PASS"), (0.1, "PASS"), (0.101, "FAIL")):
            with self.subTest(delta=delta):
                p = page([obj("copy", "body", lines=[0])],
                         lines=[text("A", (29, 40, 40, 50), 10.959 + delta)])
                self.assertEqual(statuses(checks.typography(p, CONTRACT)), [wanted])
        p = page([obj("copy", "body", lines=[0, 1])],
                 lines=[text("A", (29, 30, 40, 40)), text("B", (29, 40, 40, 50))])
        self.assertIn("FAIL", statuses(checks.typography(p, CONTRACT)))
        unrelated = page([obj("copy", "body", lines=[0])],
                         lines=[text("A", (29, 40, 40, 50), font="Helvetica")])
        self.assertEqual(statuses(checks.typography(unrelated, CONTRACT)), ["FAIL"])

    def test_spacing_relation_classification(self):
        for relation, rule in CONTRACT["spacing_pdf_pt"].items():
            for gap, wanted in ((rule["fail_below"] - 0.01, "FAIL"),
                                (rule["fail_below"], "REVIEW"),
                                (rule["target"][0], "PASS"),
                                (rule["target"][1] + 0.01, "REVIEW")):
                with self.subTest(relation=relation, gap=gap):
                    p = page([obj("a", "paragraph", lines=[0]), obj("b", "body", lines=[1])],
                             lines=[text("A", (30, 30, 50, 40)),
                                    text("B", (30, 40 + gap, 50, 50 + gap))],
                             spacing=[{"id": "edge", "from": "a", "to": "b",
                                       "relation": relation}])
                    self.assertEqual(statuses(checks.spacing(p, CONTRACT)), [wanted])

    def test_body_rail(self):
        for offset, wanted in ((0, "PASS"), (0.39, "PASS"), (0.41, "FAIL")):
            p = page([obj("body", "body", lines=[0])],
                     lines=[text("Body", (8 * MM - offset, 80, 190, 90))])
            self.assertEqual(statuses(checks.rail(p, CONTRACT)), ["PASS", wanted])

    def test_caption_role_and_multiline_left_anchor(self):
        for x, y, role, wanted in ((30, 90, "caption", "PASS"), (35, 90, "caption", "FAIL"),
                                     (30, 75, "caption", "FAIL"), (30, 90, "source_credit", "FAIL")):
            p = page([obj("figure", "figure", images=[0], caption_required=True),
                      obj("caption", role, lines=[0, 1], owner="figure")],
                     images=[Rect(30, 45, 190, 83)],
                     lines=[text("First", (30, y, 111, y + 8)),
                            text("Second", (x, y + 11, 128, y + 19))])
            self.assertEqual("FAIL" if "FAIL" in statuses(checks.captions(p, CONTRACT))
                             else "PASS", wanted)

    def test_answer_rule_endpoints_and_label(self):
        for delta, label_y, wanted in ((0, 53, "PASS"), (0.39, 53, "PASS"),
                                        (0.41, 53, "FAIL"), (0, 72, "FAIL")):
            p = page([obj("label", "answer_label", lines=[0]),
                      obj("body", "answer_body", lines=[1]),
                      obj("rule", "answer_rule", drawings=[0])],
                     lines=[text("Answer", (32, label_y, 76, label_y + 10), flags=16),
                            text("A result", (34, 70, 190, 81))],
                     drawings=[path((30, 70), (30, 81 + delta))],
                     qa=[{"id": "qa", "kind": "answer", "label": "label", "body": "body",
                          "rule": "rule", "accent_rgb": STROKE}])
            self.assertEqual(statuses(checks.qa(p, CONTRACT)), [wanted])

    def test_footer_link_and_credit_center(self):
        for shift, clickable, wanted in ((0, True, "PASS"), (0.101, True, "FAIL"),
                                          (0, False, "FAIL")):
            p = page([obj("credit", "source_credit", lines=[0]),
                      obj("num", "slide_number", lines=[1]), obj("nav", "slide_nav", lines=[2]),
                      obj("divider", "footer_divider", drawings=[0])],
                     lines=[text("Source", (12, 201 + shift, 49, 209 + shift)),
                            text("1/2", (355, 201, 372, 209)),
                            text("next", (300, 201, 322, 209))],
                     links=[Rect(300, 201, 322, 209)] if clickable else [],
                     drawings=[path((0, 195), (384, 195))],
                     footer={"band": (0, 195, 384, 215), "credit_role": "source_credit",
                             "page_label": "1/2", "inset_pdf_pt": 12})
            self.assertEqual(statuses(checks.footer(p, CONTRACT)), [wanted])

    def test_section_nav_frame_budget(self):
        for width, wanted in ((64.79, "PASS"), (64.8, "REVIEW"), (72, "REVIEW"), (72.01, "FAIL")):
            p = page([obj("nav", "section_label", lines=[0], section="alpha")],
                     lines=[text("label", (100, 10, 100 + width, 18))])
            self.assertEqual(statuses(checks.section_nav(p, CONTRACT, {"alpha": 2})), [wanted])

    def test_table_semantic_atom_wrap(self):
        for lines, wanted in ((["n = 30"], "PASS"), (["n =", "30"], "FAIL")):
            p = page([obj("table", "table", drawings=[0, 1]),
                      obj("cell", "table_cell", lines=list(range(len(lines))), owner="table",
                          region=(35, 53, 110, 78), atoms=["n = 30"])],
                     lines=[text(s, (40, 55 + i * 11, 90, 65 + i * 11))
                            for i, s in enumerate(lines)],
                     drawings=[path((30, 51), (150, 51)), path((30, 80), (150, 80))])
            self.assertEqual(statuses(checks.tables(p, CONTRACT)), [wanted])

    def test_column_anchors_and_custom_review(self):
        for preset, right_top, right_x, wanted in (
            ("equal", 60, 190, "PASS"), ("equal", 61, 190, "FAIL"),
            ("equal", 60, 130, "FAIL"), ("custom", 60, 190, "REVIEW"),
        ):
            p = page([obj("left", "body", lines=[0]), obj("right", "body", lines=[1])],
                     lines=[text("Left", (30, 60, 160, 70)),
                            text("Right", (right_x, right_top, 340, right_top + 10))],
                     columns=[{"id": "pair", "groups": [["left"], ["right"]],
                               "preset": preset, "anchor": "top"}])
            got = statuses(checks.columns(p, CONTRACT))
            self.assertEqual("FAIL" if "FAIL" in got else "REVIEW" if "REVIEW" in got
                             else "PASS", wanted)

    def test_arrow_thresholds_and_collision(self):
        for length, wanted in ((5.99, "FAIL"), (6, "REVIEW"), (7.99, "REVIEW"), (8, "PASS")):
            with self.subTest(length=length):
                x = 100 + length * MM
                p = page([obj("a", "node", drawings=[0], label="la",
                              style={"min_padding_pdf_pt": 1, "stroke_rgb": STROKE,
                                     "stroke_pdf_pt": 1}),
                          obj("b", "node", drawings=[1], label="lb",
                              style={"min_padding_pdf_pt": 1, "stroke_rgb": STROKE,
                                     "stroke_pdf_pt": 1}),
                          obj("la", "diagram_label", lines=[0]),
                          obj("lb", "diagram_label", lines=[1]),
                          obj("arrow", "connector", drawings=[2],
                              **{"from": "a", "to": "b"})],
                         drawings=[path((40, 45), (100, 78)), path((x, 45), (x + 50, 78)),
                                   path((100, 60), (x, 60))],
                         lines=[text("a", (50, 57, 62, 67)), text("b", (x + 10, 57, x + 22, 67))])
                self.assertEqual(statuses(checks.diagram(p, CONTRACT)),
                                 ["PASS", wanted, "PASS", "PASS"])

    def test_closing_center_and_body_rail(self):
        body = (8 * MM, 30, W - 8 * MM, 180)
        for fraction, x, wanted in ((0.78, W / 2, "PASS"), (0.82, W / 2, "PASS"),
                                     (0.825, W / 2, "FAIL"), (0.78, W / 2 + 2, "FAIL")):
            y = 30 + 150 * fraction
            p = page([obj("headline", "closing_headline", lines=[0]),
                      obj("cue", "closing_question", lines=[1])],
                     lines=[text("Takeaways", (30, 50, 100, 62)),
                            text("Questions", (x - 35, y - 7, x + 35, y + 7), 16)],
                     closing="substantive", body_region=body)
            self.assertEqual(statuses(checks.closing(p, CONTRACT)), [wanted])

    def test_whitespace_review_and_objective_contradiction(self):
        for x, size, wanted in ((110, None, ["REVIEW"]), (60, None, ["FAIL", "REVIEW"]),
                                 (110, (90, 20), ["FAIL", "REVIEW"])):
            p = page([obj("a", "body", lines=[0], primary=True), obj("b", "body", lines=[1])],
                     lines=[text("A", (29, 40, 80, 55)), text("B", (x, 40, 170, 55))],
                     primary_min_size_pdf_pt=size)
            self.assertEqual(statuses(checks.density(p, CONTRACT)), wanted)


class RenderedControls(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source.tex"

    def pdf(self, title, shift=0, outside=False):
        with pymupdf.open() as doc:
            p = doc.new_page(width=W, height=H)
            p.insert_text((28, 51), title, fontsize=10.959)
            p.draw_rect(pymupdf.Rect(30 + shift, 80, 70 + shift, 101), fill=(0.2, 0.4, 0.8))
            if outside:
                p.draw_rect(pymupdf.Rect(90, 88, 101, 110), fill=(0.2, 0.4, 0.8))
            return doc.tobytes()

    def layout(self, data, source, changes=None, mutate=None):
        self.source.write_text(source)
        manifest = {"pdf_sha256": sha256(data), "entry_source": "src",
                    "sources": [{"id": "src", "path": self.source.name, "role": "authored",
                                 "sha256": sha256(self.source.read_bytes())}]}
        mapping = {"pdf_sha256": sha256(data), "source_manifest_sha256": sha256(canonical(manifest)),
                   "pages": [{"id": "content", "index": 0, "section": "one", "spacing": [],
                              "footer_exempt": True,
                              "objects": [obj("body", "body", lines=[0]),
                                          obj("box", "figure", drawings=[0])]}]}
        contract = deepcopy(CONTRACT)
        contract["fonts"]["latin"] = "Helvetica"  # unrelated artificial render, not core oracle
        args = ["layout", "--contract", str(self.root / "contract.json"), "--pdf",
                str(self.root / "deck.pdf"), "--source-manifest", str(self.root / "source.json"),
                "--object-map", str(self.root / "map.json"), "--source-root", str(self.root)]
        if changes is not None:
            old, masks = changes
            (self.root / "baseline.pdf").write_bytes(old)
            args.extend(["--baseline-pdf", str(self.root / "baseline.pdf")])
            mapping["protection"] = {"baseline_pdf_sha256": sha256(old), "pages": [
                {"id": "content", "baseline_index": 0, "masks": masks}
            ]}
        if mutate:
            mutate(mapping)
        (self.root / "deck.pdf").write_bytes(data)
        for name, record in (("source", manifest), ("map", mapping), ("contract", contract)):
            (self.root / f"{name}.json").write_text(json.dumps(record))
        return run(parser().parse_args(args))

    def test_pdf_binding_and_review_preservation(self):
        for text_value in ("Try the complementary probability rule",
                           "Sensitivity to the missingness assumption"):
            data = self.pdf(text_value)
            result, code = self.layout(data, text_value)
            self.assertEqual(result["state"], "DETERMINISTIC_NO_FAIL_REVIEW_REQUIRED", result)
            self.assertEqual(code, 0)
        data = self.pdf("Unmapped content")
        result, code = self.layout(data, "Unmapped content",
                                   mutate=lambda m: m["pages"][0]["objects"].pop(0))
        self.assertEqual(code, 2)
        self.assertEqual(result["state"], "DETERMINISTIC_INCOMPLETE")

    def test_source_scan_ignores_comments(self):
        data = self.pdf("Source compression")
        for source, wanted in ((r"% \tiny", 0), (r"\tiny", 1), (r"\vspace{-2pt}", 1)):
            result, code = self.layout(data, source)
            self.assertEqual(code, wanted, result)

    def test_protection_masks(self):
        baseline = self.pdf("Protection")
        mask = {"kind": "change", "rect": [28, 78, 74, 104]}
        for outside, wanted in ((False, "PASS"), (True, "FAIL")):
            result, _ = self.layout(self.pdf("Protection", 2, outside), "Protection",
                                    changes=(baseline, [mask]))
            proof = [row["status"] for row in result["rows"] if row["detector"] == "PROTECTION"]
            self.assertEqual(proof, [wanted], result)
        brand = {"kind": "brand", "rect": [26, 40, 98, 54]}
        result, code = self.layout(baseline, "Protection", changes=(baseline, [brand]))
        self.assertEqual(code, 1, result)
