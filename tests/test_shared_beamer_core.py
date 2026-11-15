from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "skills/tools/documents-media/presentations/shared"
PAYLOAD = ROOT / "plugins/codex/plugins/presentations/shared"
FIXTURE = ROOT / "tests/fixtures/presentations/shared_beamer_core"
EVIDENCE = ROOT / "results/presentations-shared-core-template-parity"
CORE_PATH = "templates/_shared/beamer-core-v1"
COURSE_PDF = SHARED / "templates/course-standard/reference.pdf"
CUHK_PDF = EVIDENCE / "cuhk-parity.pdf"

sys.path.insert(0, str(SHARED / "scripts"))
import build_beamer_template as builder
from validate_cuhk_scientific_layout_stage3 import audience_tex


class SharedBeamerSourceTests(unittest.TestCase):
    def test_frozen_contract_and_implementation_are_shared(self):
        contract = SHARED / CORE_PATH / "layout-contract.yaml"
        planner = ROOT / "docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_LAYOUT_CONTRACT_2026-11-14.yaml"
        self.assertEqual(contract.read_bytes(), planner.read_bytes())

        for entry in (
            "templates/course-standard/beamer/source/template.tex",
            "templates/cuhk/beamer/source/styles/beamerthemesintef.sty",
        ):
            opening = (SHARED / entry).read_text()
            self.assertIn(r"\input{\PresentationCoreDir/core.tex}", opening)
            self.assertNotRegex(opening, r"\\(?:setbeamertemplate|setbeamerfont|geometry|fontsize|setbeamersize)\b")

        for source in (SHARED / CORE_PATH).glob("*"):
            self.assertEqual(source.read_bytes(), (PAYLOAD / CORE_PATH / source.name).read_bytes())

    def test_skin_can_only_declare_colours_artwork_and_credit(self):
        allowed = {"PresentationCredit", "CUHKAssets", "PresentationHeaderBrandAsset",
                   "PresentationTitleBrandAsset", "CUHKSetBrandBackground"}
        for skin in ("course-standard", "cuhk"):
            source = SHARED / f"templates/{skin}/beamer/source/skin.tex"
            with self.subTest(skin=skin):
                for line in source.read_text().splitlines():
                    if not line or line.startswith("%"):
                        continue
                    self.assertRegex(line, r"^\\(?:definecolor|colorlet|newcommand|providecommand)\b")
                    if macro := re.match(r"\\(?:new|provide)command\\([a-zA-Z]+)", line):
                        self.assertIn(macro.group(1), allowed)
                    self.assertNotRegex(line, r"\\(?:input|include|fontsize|selectfont|setbeamerfont|setlength|setbeamersize|vspace|setbeamertemplate|geometry)\b")

    def test_all_cuhk_assets_keep_the_frozen_bytes(self):
        expected = {
            "background.png": "088792e2b9b51ebb3a0f0b99bf527005d0b8691fb440077b6fa7c429fa05d7aa",
            "background_negative.png": "cae1d6d7494c9d9600156dd4af60a31715229ddca200598b4435cd2d8a8eb9e8",
            "logo_RGB.png": "598cac8fcc5f5a1d5c78877651b51192b313049e5277a2862f7fff7f04fc102c",
            "logo_RGB_negative.png": "b243d1965fb604ea59f4653cc2f1eca27e54464838ac64291aacbddccd11a516",
        }
        for tree in (SHARED, PAYLOAD):
            assets = tree / "templates/cuhk/beamer/source/assets"
            for filename, digest in expected.items():
                self.assertEqual(hashlib.sha256((assets / filename).read_bytes()).hexdigest(), digest)

    def test_rebuilding_an_edited_source_rebinds_to_the_core(self):
        with tempfile.TemporaryDirectory() as temp:
            parent = Path(temp)
            editable = parent / "edited"
            editable.mkdir()
            (editable / "main.tex").write_text("Edited deck")
            (editable / "main.pdf").write_text("stale build")
            (editable / "beamer-font-root.tex").write_text("stale binding")
            (editable / "beamer-core-v1").mkdir()
            (editable / "beamer-core-v1/core.tex").write_text("stale core")
            (editable / "figures").mkdir()
            (editable / "figures/main.pdf").write_text("figure input")
            dest = parent / "rebuilt"
            builder.renderer.copy_beamer_source(editable, dest)
            self.assertEqual((dest / "main.tex").read_text(), "Edited deck")
            self.assertEqual((dest / "figures/main.pdf").read_text(), "figure input")
            self.assertFalse((dest / "main.pdf").exists())
            self.assertFalse((dest / "beamer-font-root.tex").exists())
            self.assertEqual((dest / "beamer-core-v1/core.tex").read_bytes(),
                             (SHARED / CORE_PATH / "core.tex").read_bytes())

    def test_routing_keeps_formats_and_explicit_template_precedence(self):
        routing = (SHARED / "template-routing.md").read_text()
        self.assertLess(routing.index("Honour the requested output format"),
                        routing.index("explicit user-supplied template"))
        self.assertLess(routing.index("explicit user-supplied template"), routing.index("built-in skins"))
        expected_rows = {
            "Course-standard Beamer": "templates/course-standard/beamer/source/",
            "CUHK research": "templates/cuhk/beamer/source/",
            "Explicit editable PPTX or Google Slides": "existing editable Presentation/Slides route",
        }
        for label, destination in expected_rows.items():
            row = next(line for line in routing.splitlines() if line.startswith(f"| {label}"))
            self.assertIn(destination, row)
        for name in ("course-standard", "cuhk"):
            self.assertTrue((SHARED / f"templates/{name}/beamer/source/main.tex").is_file())

    def test_audience_lint_ignores_graphic_filenames_and_keeps_visible_copy(self):
        tex = r"\includegraphics[width=\linewidth]{study_workflow.png}\CoreCaption{fixture label}"
        self.assertNotIn("workflow", audience_tex(tex))
        self.assertIn("fixture label", audience_tex(tex))


@unittest.skipUnless(importlib.util.find_spec("pymupdf"), "PDF object QA requires PyMuPDF")
class SharedBeamerRenderedTests(unittest.TestCase):
    def setUp(self):
        import pymupdf
        import compare_beamer_template_parity
        self.pdf = pymupdf
        self.parity = compare_beamer_template_parity

    def test_reference_pdfs_match_with_only_the_approved_brand_images_masked(self):
        report = self.parity.compare(COURSE_PDF, CUHK_PDF, FIXTURE / "brand-masks.json")
        self.assertEqual(report["errors"], [])
        self.assertEqual(len(report["pages"]), 11)
        self.assertEqual([row["matched_brand_images"] for row in report["pages"]], [2] + [1] * 10)
        self.assertTrue(all(row["links"] >= 19 for row in report["pages"]))

    def test_comparator_rejects_extra_generated_objects_and_a_mask_covering_text(self):
        with tempfile.TemporaryDirectory() as temp:
            scratch = Path(temp)
            pdf = scratch / "mutated.pdf"
            with self.pdf.open(CUHK_PDF) as source:
                page = source[1]
                page.insert_text((30, 206), "Changed generated copy")
                page.draw_rect(self.pdf.Rect(30, 212, 92, 218), color=(0, 0, 0))
                source.save(pdf)
            report = self.parity.compare(COURSE_PDF, pdf, FIXTURE / "brand-masks.json")
            self.assertEqual(report["status"], "FAIL")
            self.assertTrue(any("text and line breaks" in error for error in report["errors"]))
            self.assertTrue(any("vector objects" in error for error in report["errors"]))

            config = json.loads((FIXTURE / "brand-masks.json").read_text())
            config["cuhk"][0]["rect"][0] = 0
            masks = scratch / "unsafe-mask.json"
            masks.write_text(json.dumps(config))
            report = self.parity.compare(COURSE_PDF, CUHK_PDF, masks)
            self.assertEqual(report["status"], "FAIL")
            self.assertTrue(any("intersects generated text" in error for error in report["errors"]))
            self.assertTrue(any("intersects navigation" in error for error in report["errors"]))

    def test_real_cuhk_regression_uses_source_figures_and_shared_generated_fonts(self):
        pdf = EVIDENCE / "cuhk-research.pdf"
        with self.pdf.open(pdf) as deck:
            self.assertEqual(deck.page_count, 6)
            self.assertTrue(all(len(page.get_links()) >= 11 for page in deck))
            embedded = {font[3].split("+")[-1] for page in deck for font in page.get_fonts()}
            self.assertTrue(any(name.startswith("TeXGyreTermesMath") for name in embedded))
            self.assertTrue(all(name.startswith("TeXGyreTermes") for name in embedded))
            images = [i for page in deck for i in page.get_image_info(hashes=True)]
            self.assertEqual(sum(i["digest"].hex() == "359407a08e058b1ccd3c360df195d4d8" for i in images), 6)
            self.assertEqual(sum(i["digest"].hex() == "d0cbf2e6d3284c73d0f757d262367183" for i in images), 1)
            self.assertEqual(len(images), 10)
            self.assertIn("Stan-ready", deck[1].get_text())
            self.assertIn("LKJ", deck[1].get_text())


if __name__ == "__main__":
    unittest.main()
