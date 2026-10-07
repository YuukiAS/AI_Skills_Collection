import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

from plugins.codex.plugins.presentations.shared.validator_v1.aggregation import aggregate_page_result
from plugins.codex.plugins.presentations.shared.validator_v1.anti_fitting import scan_paths_for_answer_fitting
from plugins.codex.plugins.presentations.shared.validator_v1.detectors import (
    build_protected_object_check,
    detect_code_output_proximity,
    detect_evidence_interpretation_proximity,
    detect_internal_identifier_leak,
    detect_object_scale_whitespace,
    detect_peer_layout,
    detect_qa_geometry,
    detect_reading_path,
    detect_scientific_object_readability,
    detect_shell_integrity,
    detect_text_collision,
    detect_typography,
)
from plugins.codex.plugins.presentations.shared.validator_v1.review import build_review_packet, normalize_reviewer_row, review_rendered_page


def packet(**overrides):
    base = {
        "artifact_id": "A",
        "physical_page": 1,
        "page_png_sha256": "0" * 64,
        "page_job": "derive a sequential mechanism",
        "page_role": "ordinary",
        "guards": [],
        "protected_objects": [],
        "features": {
            "image": {
                "width": 1000,
                "height": 600,
                "body_bbox_area_ratio": 0.6,
                "top_void_ratio": 0.05,
                "bottom_void_ratio": 0.08,
                "center_occupancy": 0.02,
                "largest_component": {"x0": 100, "y0": 100, "x1": 800, "y1": 450, "area_px": 100000},
                "content_components": [{"x0": 100, "y0": 100, "x1": 800, "y1": 450, "area_px": 100000}],
            },
            "text": {
                "word_count": 80,
                "median_word_height_px": 24,
                "left_body_words": 30,
                "right_body_words": 28,
                "two_column_text_signal": False,
                "question_spans": [],
                "answer_spans": [],
                "spans": [],
                "text_excerpt": "plain student visible text",
            },
        },
    }
    base.update(overrides)
    return base


class ValidatorCoreTests(unittest.TestCase):
    def test_text_collision_detector(self):
        p = packet()
        p["features"]["text"]["spans"] = [
            {"text": "alpha", "x0": 10, "y0": 10, "x1": 80, "y1": 30},
            {"text": "beta", "x0": 15, "y0": 12, "x1": 78, "y1": 32},
        ]
        self.assertEqual(detect_text_collision(p).status, "REVISE")

    def test_typography_detector(self):
        p = packet()
        p["features"]["text"]["median_word_height_px"] = 12
        self.assertEqual(detect_typography(p).status, "REVISE")

    def test_object_scale_whitespace_detector(self):
        p = packet()
        p["features"]["image"]["body_bbox_area_ratio"] = 0.12
        p["features"]["image"]["bottom_void_ratio"] = 0.5
        self.assertEqual(detect_object_scale_whitespace(p).status, "REVISE")

    def test_peer_and_reading_path_detectors(self):
        p = packet()
        p["features"]["text"]["left_body_words"] = 90
        p["features"]["text"]["right_body_words"] = 20
        p["features"]["text"]["two_column_text_signal"] = True
        self.assertEqual(detect_peer_layout(p).status, "REVISE")
        self.assertEqual(detect_reading_path(p).status, "REVISE")

    def test_qa_geometry_detector(self):
        p = packet()
        p["features"]["text"]["question_spans"] = [{"text": "Question", "x0": 0, "y0": 100, "x1": 80, "y1": 120}]
        p["features"]["text"]["answer_spans"] = [{"text": "Answer", "x0": 0, "y0": 560, "x1": 80, "y1": 580}]
        self.assertEqual(detect_qa_geometry(p).status, "REVISE")

    def test_internal_readability_and_proximity_detectors(self):
        p = packet()
        p["features"]["text"]["spans"] = [{"text": f"tiny{i}", "x0": i, "y0": 150, "x1": i + 5, "y1": 160, "height": 10} for i in range(20)]
        self.assertEqual(detect_scientific_object_readability(p).status, "REVISE")
        p["features"]["text"]["spans"] = [
            {"text": "glm", "x0": 10, "y0": 10, "x1": 40, "y1": 30, "height": 20},
            {"text": "summary", "x0": 20, "y0": 40, "x1": 80, "y1": 60, "height": 20},
            {"text": "for", "x0": 20, "y0": 80, "x1": 80, "y1": 100, "height": 20},
            {"text": "fit", "x0": 20, "y0": 120, "x1": 80, "y1": 140, "height": 20},
            {"text": "estimate", "x0": 900, "y0": 500, "x1": 980, "y1": 520, "height": 20},
        ]
        self.assertEqual(detect_code_output_proximity(p).status, "REVISE")
        p["features"]["text"]["spans"] = [
            {"text": "plot", "x0": 10, "y0": 10, "x1": 50, "y1": 30, "height": 20},
            {"text": "therefore", "x0": 900, "y0": 500, "x1": 980, "y1": 520, "height": 20},
        ]
        self.assertEqual(detect_evidence_interpretation_proximity(p).status, "REVISE")

    def test_shell_and_internal_identifier_detectors(self):
        p = packet(page_role="title")
        p["features"]["text"]["text_excerpt"] = "Title workflow roadmap"
        self.assertEqual(detect_shell_integrity(p).status, "REVISE")
        p = packet()
        p["features"]["text"]["text_excerpt"] = "Visible PageID T99-SECRET"
        self.assertEqual(detect_internal_identifier_leak(p).status, "REVISE")

    def test_protected_packet_aggregation_and_review_packet(self):
        p = packet(protected_objects=[{"object_id": "diagram", "description": "must remain visible"}])
        self.assertEqual(build_protected_object_check(p).status, "N/A")
        review = normalize_reviewer_row(
            p,
            {
                "artifact_id": "A",
                "physical_page": 1,
                "page_png_sha256": "0" * 64,
                "reviewer_run_id": "unit",
                "fresh_context": "YES",
                "read_only_candidate": "YES",
                "image_inspection_runtime": "unit_visual_inspection",
                "overall_visual_verdict": "PASS",
                "checks": {
                    "shell": {"check_id": "shell", "status": "PASS", "positive_evidence": ["visible shell"]},
                    "typography": {"check_id": "typography", "status": "PASS", "positive_evidence": ["readable text"]},
                    "scientific_object_internal_readability": {"check_id": "scientific_object_internal_readability", "status": "N/A", "not_applicable_reason": "no object"},
                    "primary_object_scale": {"check_id": "primary_object_scale", "status": "PASS", "positive_evidence": ["object scale acceptable"]},
                    "whitespace": {"check_id": "whitespace", "status": "PASS", "positive_evidence": ["whitespace acceptable"]},
                    "reading_path": {"check_id": "reading_path", "status": "PASS", "positive_evidence": ["reading path clear"]},
                    "peer_layout": {"check_id": "peer_layout", "status": "N/A", "not_applicable_reason": "no peers"},
                    "q_a_geometry": {"check_id": "q_a_geometry", "status": "N/A", "not_applicable_reason": "no QA"},
                    "evidence_interpretation_proximity": {"check_id": "evidence_interpretation_proximity", "status": "N/A", "not_applicable_reason": "no evidence object"},
                    "code_output_proximity": {"check_id": "code_output_proximity", "status": "N/A", "not_applicable_reason": "no code"},
                    "protected_object": {"check_id": "protected_object", "status": "PASS", "positive_evidence": ["protected diagram visible"]},
                    "internal_identifier_or_markup_leak": {"check_id": "internal_identifier_or_markup_leak", "status": "PASS", "positive_evidence": ["no identifiers"]},
                    "audience_boundary": {"check_id": "audience_boundary", "status": "PASS", "positive_evidence": ["student-facing"]},
                    "historical_guard_closure": {"check_id": "historical_guard_closure", "status": "PASS", "positive_evidence": ["guards closed"]},
                },
                "substantive_observation": "Unit reviewer inspected the image and found the protected diagram visible.",
            },
        )
        result = aggregate_page_result(p, review, [])
        self.assertEqual(result["verdict"], "PASS")

    def test_png_opened_for_review_packet_and_anti_fitting(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "page.png"
            image = Image.new("RGB", (640, 360), "white")
            draw = ImageDraw.Draw(image)
            draw.rectangle((80, 60, 500, 260), outline="black", width=4)
            draw.text((100, 100), "Question", fill="black")
            image.save(path)
            packet_obj = build_review_packet(
                artifact_id="A",
                physical_page=1,
                page_png_path=path,
                pdf_text_page={"pdf_width": 640, "pdf_height": 360, "words": []},
                page_job="title",
                stable_targets=[],
                component_targets=[],
                guards=[],
            )
            self.assertEqual(packet_obj["features"]["image"]["png_sha256"], packet_obj["page_png_sha256"])
            blocked = review_rendered_page(packet_obj, reviewer_context_id="unit")
            self.assertEqual(blocked["overall_visual_verdict"], "BLOCKED")
        report = scan_paths_for_answer_fitting([Path("plugins/codex/plugins/presentations/shared/validator_v1")])
        self.assertEqual(report["AST_ANTI_FITTING"], "PASS")


if __name__ == "__main__":
    unittest.main()
