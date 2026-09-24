from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SKILL = ROOT / "skills/core/codex-system/codex-workflow-protocol/SKILL.md"
GENERATED_SKILL = ROOT / "plugins/codex/plugins/workflow-core/skills/workflow/SKILL.md"
MARKETPLACE_CONFIG = ROOT / "scripts/codex_marketplace_config.json"


class WorkflowCoreReviewedHandoffRoutingTests(unittest.TestCase):
    def test_source_defines_bridge_owned_bootstrap_resume_routing(self) -> None:
        text = SOURCE_SKILL.read_text(encoding="utf-8")

        for marker in [
            "Reviewed Handoff Bootstrap And Resume Routing",
            "ai-bridge reviewed-handoff task bootstrap",
            "ai-bridge reviewed-handoff materialize-worktree --mode resume",
            "fail early before substantive implementation",
            "Bridge owns the repo-local Git mechanics",
            "remote-only metadata discovery",
        ]:
            self.assertIn(marker, text)

        for forbidden in [
            "fall back to `git worktree add`",
            "a `/tmp`",
            "replacement",
            "a second clone",
            "remote remapping",
            "locally generated task",
            "metadata",
        ]:
            self.assertIn(forbidden, text)

    def test_generated_workflow_payload_consumes_same_routing_and_version(self) -> None:
        config = json.loads(MARKETPLACE_CONFIG.read_text(encoding="utf-8"))
        workflow = next(plugin for plugin in config["plugins"] if plugin["name"] == "workflow-core")
        generated = GENERATED_SKILL.read_text(encoding="utf-8")

        self.assertEqual(workflow["version"], "0.4")
        self.assertIn("ai-bridge reviewed-handoff task bootstrap", generated)
        self.assertIn("ai-bridge reviewed-handoff materialize-worktree --mode resume", generated)
        self.assertIn("Bridge owns the repo-local Git mechanics", generated)


if __name__ == "__main__":
    unittest.main()
