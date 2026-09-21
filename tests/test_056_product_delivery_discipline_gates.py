from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RESULT_ROOT = REPO_ROOT / "results/056_product_delivery_discipline"
REPLAY_ROOT = RESULT_ROOT / "replay_evidence"
PRODUCTION_CANDIDATE_COMMIT = "33c30bbe0dd528031a23d379905cd00d6b65bc1f"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class ProductDeliveryDisciplineReplayEvidenceTests(unittest.TestCase):
    def assert_candidate_replay_consumed(self, plugin: str, version: str) -> dict:
        run = read_json(REPLAY_ROOT / plugin.replace("-", "_") / "candidate_replay_run.json")
        add = read_json(REPLAY_ROOT / plugin.replace("-", "_") / "plugin-add.json")

        self.assertEqual(run["candidate_commit"], PRODUCTION_CANDIDATE_COMMIT)
        self.assertEqual(run["plugin_id"], f"{plugin}@ai-skills-candidate")
        self.assertEqual(run["runtime_version"], "codex-cli 0.153.4")
        self.assertTrue(run["actual_consumption"]["proven"])
        self.assertGreaterEqual(run["actual_consumption"]["line_index"], 1)
        self.assertIn("item.", run["actual_consumption"]["event_type"])
        self.assertEqual(add["pluginId"], f"{plugin}@ai-skills-candidate")
        self.assertEqual(add["marketplaceName"], "ai-skills-candidate")
        self.assertEqual(add["version"], version)
        self.assertEqual(add["installedPath"], run["installed_path"])
        self.assertIn(f"/plugins/cache/ai-skills-candidate/{plugin}/{version}", run["installed_path"])
        return run

    def test_workflow_core_replay_proves_g2_g3_g4_g5_g7_and_source_discovery_behavior(self) -> None:
        self.assert_candidate_replay_consumed("workflow-core", "0.3")
        output = read_json(REPLAY_ROOT / "workflow_core/workflow_core_gate_replay.json")

        self.assertEqual(output["plugin"], "workflow-core")
        self.assertEqual(output["normal_entry"], "Verified Workflow candidate")
        self.assertEqual(output["fixture_candidate_commit"], PRODUCTION_CANDIDATE_COMMIT)
        for gate in ["G2", "G3", "G4", "G5", "G7", "Source Discovery"]:
            self.assertTrue(output["gates"][gate]["pass"], gate)
            self.assertTrue(output["gates"][gate]["observed_behavior"])
            self.assertTrue(output["gates"][gate]["reason"])

        self.assertIn("不代表真实主机", output["evidence_scope"])
        self.assertIn("不声称 overall 056 achieved", "\n".join(output["should_not_change"]))
        self.assertIn("不重复网络 clone", output["gates"]["Source Discovery"]["observed_behavior"])
        self.assertIn("不重映射 remote", output["gates"]["Source Discovery"]["observed_behavior"])
        self.assertIn("禁止跨 implementation candidate 拼接 PASS", output["gates"]["G5"]["reason"])

    def test_web_development_replay_proves_g6_payload_consumption_and_non_host_limitations(self) -> None:
        self.assert_candidate_replay_consumed("web-development", "0.2")
        output = read_json(REPLAY_ROOT / "web_development/web_development_gate_replay.json")

        self.assertEqual(output["plugin"], "web-development")
        self.assertEqual(output["normal_entry"], "Frontend Design candidate")
        self.assertTrue(output["G6"]["pass"])
        behavior = output["G6"]["observed_behavior"]
        self.assertIn("只读设计权威", behavior["canonical_design_authority"])
        self.assertIn("Figma", behavior["figma_handoff_consumed"])
        self.assertIn("motion-interaction", behavior["motion_production_wiring_consumed"])
        self.assertIn("不得静默在代码中发明状态", behavior["missing_material_state_disposition"])
        self.assertFalse(output["limitations"]["product_repository_modified"])
        self.assertFalse(output["limitations"]["real_host_G1_final_pass_claimed"])
        self.assertFalse(output["limitations"]["release_ready_claimed"])

    def test_ai_skills_core_replay_proves_g8_consumption_diagnosis_behavior(self) -> None:
        self.assert_candidate_replay_consumed("ai-skills-core", "0.4")
        output = read_json(REPLAY_ROOT / "ai_skills_core/ai_skills_core_gate_replay.json")

        self.assertEqual(output["plugin"], "ai-skills-core")
        self.assertEqual(output["normal_entry"], "AI Skills Maintainer candidate")
        self.assertTrue(output["G8"]["pass"])
        self.assertEqual(output["classification"], "stale_install")
        self.assertTrue(output["consumer_path_checked"])
        self.assertFalse(output["adds_duplicate_policy"])
        self.assertIn("不能单独证明", output["G8"]["reason"])

    def test_fixture_files_are_inputs_not_gate_pass_authority(self) -> None:
        fixture = read_json(REPO_ROOT / "tests/fixtures/056_product_delivery_discipline_gates.json")

        self.assertEqual(fixture["task_key"], "056_product_delivery_discipline")
        self.assertNotIn("G1", {entry["gate"] for entry in fixture["gates"]})
        self.assertTrue((RESULT_ROOT / "replay_inputs/workflow_core_fixture.json").is_file())
        self.assertTrue((RESULT_ROOT / "replay_inputs/web_development_fixture.json").is_file())
        self.assertTrue((RESULT_ROOT / "replay_inputs/ai_skills_core_fixture.json").is_file())


if __name__ == "__main__":
    unittest.main()
