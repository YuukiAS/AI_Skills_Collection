from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE = REPO_ROOT / "tests/fixtures/056_product_delivery_discipline_gates.json"


class ProductDeliveryDisciplineGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_fixture_is_public_safe_and_covers_g2_through_g8(self) -> None:
        self.assertEqual(self.data["candidate_surface"], "non_host_source_unit_fixture")
        self.assertEqual({item["gate"] for item in self.data["gates"]}, {f"G{i}" for i in range(2, 9)})
        serialized = json.dumps(self.data, ensure_ascii=False)
        for forbidden in ["PRIVATE_ORG", "PRIVATE_PROJECT", "/home/", "/users/", "/nas/"]:
            self.assertNotIn(forbidden, serialized)

    def test_acceptance_and_resume_semantics_stay_explicit(self) -> None:
        by_gate = {item["gate"]: item for item in self.data["gates"]}
        self.assertFalse(by_gate["G2"]["expected_acceptance_ready"])
        self.assertTrue(by_gate["G2"]["expected_advisory_allowed"])
        self.assertTrue(by_gate["G3"]["expected_resume_valid"])
        self.assertFalse(by_gate["G3"]["expected_complete_after_action_only"])

    def test_evidence_and_frontend_gates_preserve_claim_boundaries(self) -> None:
        by_gate = {item["gate"]: item for item in self.data["gates"]}
        self.assertTrue(by_gate["G4"]["old_bad_caught"])
        self.assertTrue(by_gate["G4"]["new_candidate_passes_same_surface"])
        self.assertTrue(by_gate["G5"]["same_candidate"])
        self.assertFalse(by_gate["G5"]["cross_candidate_stitching"])
        self.assertTrue(by_gate["G6"]["canonical_design_source_read_only"])
        self.assertFalse(by_gate["G6"]["invent_missing_material_state_in_code"])

    def test_non_overreach_and_consumption_diagnosis_remain_covered(self) -> None:
        by_gate = {item["gate"]: item for item in self.data["gates"]}
        for route in by_gate["G7"]["routes"]:
            self.assertFalse(any(value for key, value in route.items() if key.startswith("requires_")))
        self.assertEqual(by_gate["G8"]["failure_class"], "stale_install")
        self.assertTrue(by_gate["G8"]["diagnoses_consumer_path"])
        self.assertFalse(by_gate["G8"]["adds_duplicate_policy"])


if __name__ == "__main__":
    unittest.main()
