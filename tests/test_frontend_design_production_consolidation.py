from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RESULT_ROOT = REPO_ROOT / "results/web-development--frontend-design-production-consolidation"
SCENARIO_PATH = RESULT_ROOT / "candidate_visible_regressions/scenarios.json"
RUBRIC_PATH = RESULT_ROOT / "candidate_visible_regressions/adjudication_rubric.md"

ANSWER_SHAPED_PATTERN = re.compile(
    r"\bP[0-4]\b|\bF-[A-D]\b|\bS[1-3]\b|coordinator-first|EXPECTED|PASS|FAIL|rubric|adjudication",
    re.IGNORECASE,
)


class FrontendDesignProductionConsolidationTests(unittest.TestCase):
    def test_candidate_visible_regression_inputs_are_frozen_and_not_answer_shaped(self) -> None:
        data = json.loads(SCENARIO_PATH.read_text(encoding="utf-8"))
        self.assertEqual(data["schema"], "FRONTEND_DESIGN_COORDINATOR_REGRESSION_SCENARIOS_V1")
        self.assertTrue(data["candidate_visible"])
        scenario_ids = {scenario["id"] for scenario in data["scenarios"]}
        self.assertEqual(
            scenario_ids,
            {
                "s1_browser_tiny_spacing_fix",
                "s2_durable_authority_settings_panel",
                "s3_no_figma_product_redesign",
                "canonical_figma_material_change",
                "native_handoff_action_reachability",
                "competing_route_interaction_claim",
                "unsupported_metric_ranking_semantic_claim",
                "implementation_drift_should_not_change_design",
            },
        )
        for scenario in data["scenarios"]:
            visible_text = "\n".join(
                str(scenario[key]) for key in ["prompt", "project_context", "surface"] if key in scenario
            )
            self.assertIsNone(ANSWER_SHAPED_PATTERN.search(visible_text), scenario["id"])

    def test_regression_rubric_is_separate_from_candidate_visible_inputs(self) -> None:
        data = json.loads(SCENARIO_PATH.read_text(encoding="utf-8"))
        rubric = RUBRIC_PATH.read_text(encoding="utf-8")
        for scenario in data["scenarios"]:
            self.assertIn(scenario["id"], rubric)
        self.assertIn("This rubric is not included in candidate-visible prompts.", rubric)
        self.assertIn("generated Frontend Design coordinator first", rubric)

    def test_generated_frontend_design_payload_is_coordinator_first(self) -> None:
        skill = (REPO_ROOT / "plugins/codex/plugins/web-development/skills/visual/SKILL.md").read_text(
            encoding="utf-8"
        )
        plugin_skill_dirs = {
            path.parent.name
            for path in (REPO_ROOT / "plugins/codex/plugins/web-development/skills").glob("*/SKILL.md")
        }
        self.assertEqual(plugin_skill_dirs, {"refs", "visual"})
        self.assertIn('routing_mode: "coordinator-first"', skill)
        self.assertIn('coordinator_artifact_id: "system"', skill)
        self.assertIn("Read the coordinator source `_src/system/source.md` first.", skill)
        self.assertIn("_src/ux/source.md", skill)
        self.assertIn("_src/webapp-testing/source.md", skill)
        self.assertIn("_src/research/source.md", skill)
        self.assertNotIn("Choose the source workflow whose trigger boundary best matches", skill)


if __name__ == "__main__":
    unittest.main()
