import json
from pathlib import Path
import unittest

from presentations_validator_v2.layout import checks
from presentations_validator_v2.layout.model import Page
from presentations_validator_v2.render import Rect, Render, Text

from test_layout import CONTRACT, obj, statuses


def semantic_page(sample, role, rows, frame_counts=()):
    bounds = Rect.from_value(sample["bounds"])
    lines = [Text(Rect.from_value(row["bbox"]),
                  ({"text": "x", **{key: row[key] for key in ("font", "size", "flags")}},),
                  row["baseline"]) for row in rows]
    objects = []
    for i, _ in enumerate(lines):
        extra = {"section": str(i)} if frame_counts else {}
        objects.append(obj(f"object-{i}", role, lines=[i], **extra))
    return Page({"id": "slice", "objects": objects}, Render(bounds, lines, [], [], []))


class ArchivedGeometry(unittest.TestCase):
    def test_exact_oracle_and_archived_body_rails(self):
        for key, wanted in (("oracle", "PASS"), ("archived", "FAIL")):
            with self.subTest(archive=key):
                sample = self.data[key]
                page = semantic_page(sample, "closing_takeaway", sample["body"])
                outcome = statuses(checks.rail(page, CONTRACT))
                self.assertEqual("FAIL" if "FAIL" in outcome else "PASS", wanted, outcome)
                self.assertNotIn("FAIL", statuses(checks.typography(page, CONTRACT)))

    def test_exact_archived_section_label_routes_fail(self):
        counts = self.data["section_frame_counts"]
        totals = {str(i): count for i, count in enumerate(counts)}
        for key, wanted in (("oracle", False), ("archived", True)):
            with self.subTest(archive=key):
                sample = self.data[key]
                page = semantic_page(sample, "section_label", sample["section"], counts)
                self.assertEqual("FAIL" in statuses(checks.section_nav(page, CONTRACT, totals)), wanted)
                self.assertNotIn("FAIL", statuses(checks.typography(page, CONTRACT)))

    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((Path(__file__).parent / "fixtures/archived_geometry.json").read_text())
