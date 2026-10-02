from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/core/codex-system/codex-workflow-protocol/SKILL.md"
ESCALATION = ROOT / "skills/core/codex-system/codex-workflow-protocol/references/escalation-rules.md"
AGENT = ROOT / "skills/core/codex-system/codex-workflow-protocol/agents/openai.yaml"
EVALS = ROOT / "skills/core/codex-system/codex-workflow-protocol/evals/trigger_queries.json"


def compact(text: str) -> str:
    return " ".join(text.split())


class WorkflowCoreNormalEntryReliabilityTests(unittest.TestCase):
    def test_source_defines_least_privilege_normal_entry_order(self) -> None:
        text = compact(SKILL.read_text(encoding="utf-8"))

        self.assertIn("Normal Entry And Approval-Boundary Routing", text)
        for marker in [
            "current-user, frozen-task, or repository canonical route",
            "matched specialist probe, resource, wrapper, or runner",
            "project-declared environment or runtime",
            "current workspace normal capability",
            "authority path only when the required effect clearly exceeds every valid normal boundary",
            "Missing tools on the default `PATH`",
            "unavailable optional mode",
            "Repo-local build, check, render, QA, and deterministic validation",
        ]:
            self.assertIn(marker, text)

    def test_source_requires_privilege_non_increasing_recovery(self) -> None:
        text = compact(SKILL.read_text(encoding="utf-8"))

        for marker in [
            "privilege or authority surface does not increase",
            "frozen effect",
            "professional quality",
            "acceptance evidence strength",
            "safety/privacy",
            "artifact identity",
            "current authorization scope",
            "If any dimension is unknown or changed, fail closed",
            "Do not replace a bounded/canonical publisher",
        ]:
            self.assertIn(marker, text)

    def test_source_classifies_rejection_and_preserves_effect_scoped_truth(self) -> None:
        text = compact(SKILL.read_text(encoding="utf-8"))

        for marker in [
            "optional or non-required effect",
            "unnecessarily privileged selected route",
            "genuine authority or safety boundary",
            "canonical or normal entry unavailable or broken",
            "publication failure must not be reported as a build, render, QA, or local-commit failure",
            "Merely switching to `bash`, Python, a raw wrapper",
        ]:
            self.assertIn(marker, text)

    def test_escalation_rules_cover_known_regression_bank(self) -> None:
        text = compact(ESCALATION.read_text(encoding="utf-8"))

        for marker in [
            "Missing default `PATH` tools",
            "matched specialist probe/resource/wrapper",
            "project-declared runtime",
            "workspace normal entry",
            "Optional cleanup",
            "six-dimension-equivalent",
            "Repeated approval rejection",
            "Bounded/canonical publication or transport failure blocks only that effect",
        ]:
            self.assertIn(marker, text)

    def test_trigger_assets_include_positive_and_negative_boundary_cases(self) -> None:
        agent = AGENT.read_text(encoding="utf-8")
        evals = json.loads(EVALS.read_text(encoding="utf-8"))

        self.assertIn("approval-boundary recovery", agent)
        self.assertIn("normal-entry routing", agent)
        self.assertIn("specialist-contained render or PDF task", agent)
        self.assertTrue(any("raw push" in item for item in evals["positive"]))
        self.assertTrue(any("bounded publisher" in item for item in evals["positive"]))
        self.assertTrue(any("specialist runner" in item for item in evals["near_miss"]))
        self.assertTrue(any("cache" in item for item in evals["negative"]))


if __name__ == "__main__":
    unittest.main()
