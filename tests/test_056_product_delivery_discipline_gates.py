from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = REPO_ROOT / "tests/fixtures/056_product_delivery_discipline_gates.json"


class ProductDeliveryDisciplineGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.gates = {entry["gate"]: entry for entry in cls.fixture["gates"]}
        cls.workflow = (REPO_ROOT / "skills/core/codex-system/codex-workflow-protocol/SKILL.md").read_text(
            encoding="utf-8"
        )
        cls.frontend = (REPO_ROOT / "skills/tools/frontend/frontend-visual-systems/SKILL.md").read_text(
            encoding="utf-8"
        )
        cls.maintainer = (
            REPO_ROOT / "skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md"
        ).read_text(encoding="utf-8")
        cls.marketplace_config = json.loads(
            (REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8")
        )

    def test_g2_incomplete_or_human_blocked_candidate_is_not_acceptance_ready(self) -> None:
        gate = self.gates["G2"]

        acceptance_ready = gate["producer_evidence_complete"] and not gate["human_blocked"]
        advisory_allowed = gate["advisory_review_requested"]

        self.assertFalse(acceptance_ready)
        self.assertEqual(acceptance_ready, gate["expected_acceptance_ready"])
        self.assertEqual(advisory_allowed, gate["expected_advisory_allowed"])
        self.assertIn("Advisory", self.workflow)
        self.assertIn("readiness or completion", self.workflow)
        self.assertIn("Human action", self.workflow)

    def test_g3_resume_requires_same_goal_exact_once_and_post_action_closure(self) -> None:
        gate = self.gates["G3"]

        resume_valid = gate["same_goal"] and gate["answer_consumed_count"] == 1
        complete_after_action_only = gate["human_action_only"] and not gate["post_action_closure_complete"]

        self.assertEqual(resume_valid, gate["expected_resume_valid"])
        self.assertEqual(complete_after_action_only, gate["expected_complete_after_action_only"])
        self.assertIn("exactly once", self.workflow)
        self.assertIn("post-action closure", self.workflow)

    def test_g4_faithful_regression_covers_old_bad_new_good_sequence(self) -> None:
        gate = self.gates["G4"]

        gate_passes = (
            gate["old_bad_caught"]
            and gate["new_candidate_passes_same_surface"]
            and gate["interaction_sequence_included"]
            and not gate["mock_only_claims_hosted"]
        )

        self.assertEqual(gate_passes, gate["expected_pass"])
        self.assertIn("old-bad/new-good", self.workflow)
        self.assertIn("Interaction controls", self.workflow)
        self.assertIn("Hosted/external-provider claims", self.workflow)

    def test_g5_claim_scope_stays_with_same_final_candidate_and_surface(self) -> None:
        gate = self.gates["G5"]

        claim_allowed = (
            gate["same_candidate"]
            and not gate["cross_candidate_stitching"]
            and gate["evidence_surface"] == gate["claim_surface"]
        )

        self.assertEqual(claim_allowed, gate["expected_claim_allowed"])
        self.assertIn("prove only their own surface", self.workflow)
        self.assertIn("Do not stitch PASS evidence", self.workflow)

    def test_g6_frontend_design_consumes_canonical_design_and_existing_capabilities(self) -> None:
        gate = self.gates["G6"]
        web = next(plugin for plugin in self.marketplace_config["plugins"] if plugin["name"] == "web-development")
        visual = next(skill for skill in web["skills"] if skill["artifact_id"] == "visual")
        sources = {entry["source"] for entry in visual["source_skills"]}

        self.assertTrue(gate["canonical_design_source_read_only"])
        self.assertFalse(gate["invent_missing_material_state_in_code"])
        self.assertIn("skills/tools/frontend/figma-design-to-code", sources)
        self.assertIn("skills/tools/frontend/motion-interaction", sources)
        self.assertIn("F-A Design Authority And State Coverage", self.frontend)
        self.assertIn("missing, close the design-source gap", self.frontend)

    def test_g7_non_overreach_negative_routes_do_not_trigger_heavy_gates(self) -> None:
        gate = self.gates["G7"]
        heavy_keys = [
            "requires_figma",
            "requires_locale_catalog",
            "requires_provider_probe",
            "requires_gpt_work",
            "requires_full_e2e",
            "requires_native_smoke",
        ]

        for route in gate["routes"]:
            self.assertFalse(any(route[key] for key in heavy_keys), route["task_type"])

        self.assertTrue(gate["expected_pass"])
        self.assertIn("risk-matched actual surface", self.workflow)
        self.assertIn("Do not force every project into Figma", self.frontend)

    def test_g8_consumption_regression_diagnoses_consumer_path_before_new_policy(self) -> None:
        gate = self.gates["G8"]

        gate_passes = (
            gate["active_rule_exists"]
            and gate["diagnoses_consumer_path"]
            and gate["failure_class"] == "stale_install"
            and not gate["adds_duplicate_policy"]
        )

        self.assertEqual(gate_passes, gate["expected_pass"])
        self.assertIn("Production Consumption Diagnosis", self.maintainer)
        self.assertIn("stale_install", self.maintainer)
        self.assertIn("before adding another synonymous rule", self.maintainer)

    def test_source_discovery_preserves_dirty_canonical_source_without_network_clone(self) -> None:
        fixture = self.fixture["source_discovery"]

        gate_passes = (
            fixture["local_canonical_repo_exists"]
            and fixture["unrelated_dirty_work_exists"]
            and fixture["identity_verified"]
            and fixture["freshness_checked"]
            and fixture["dirty_work_preserved"]
            and fixture["authorized_isolated_worktree"]
            and not fixture["network_clone_used"]
            and not fixture["remote_remapped"]
        )

        self.assertEqual(gate_passes, fixture["expected_pass"])
        self.assertIn("Protect unrelated dirty work", self.workflow)
        self.assertIn("Network clone only", self.workflow)


if __name__ == "__main__":
    unittest.main()
