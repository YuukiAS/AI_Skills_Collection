from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BRIDGE_KIT_COMMIT = "3d73572a6476f925745cfb873e48057c21be3502"


class PaidReviewWorkflowPolicyTests(unittest.TestCase):
    def paid_workflows(self) -> list[Path]:
        return [
            path
            for path in sorted((REPO_ROOT / ".github" / "workflows").glob("*.yml"))
            if "OPENAI_REVIEW_API_KEY" in path.read_text(encoding="utf-8")
            or "OPENAI_VISUAL_REVIEW_API_KEY" in path.read_text(encoding="utf-8")
        ]

    def test_all_paid_workflows_are_manual_only_and_pinned(self) -> None:
        workflows = self.paid_workflows()
        self.assertEqual(
            {path.name for path in workflows},
            {
                "ai-bridge-text-review.yml",
                "ai-bridge-visual-review.yml",
                "research-presentation-candidate-visual-finish-review.yml",
                "research-presentation-comparative-visual-review.yml",
            },
        )
        for path in workflows:
            text = path.read_text(encoding="utf-8")
            with self.subTest(workflow=path.name):
                self.assertIn("workflow_dispatch:", text)
                self.assertNotIn("\n  push:", text)
                self.assertIn(BRIDGE_KIT_COMMIT, text)
                self.assertIn('AI_BRIDGE_PAID_REVIEW_GIT_RESERVE: "1"', text)
                self.assertIn("group: ai-bridge-paid-review-${{ github.repository }}-${{ github.ref }}", text)
                self.assertNotIn("secrets.OPENAI_REVIEW_API_KEY || secrets.OPENAI_VISUAL_REVIEW_API_KEY", text)
                self.assertNotIn("secrets.OPENAI_VISUAL_REVIEW_API_KEY || secrets.OPENAI_REVIEW_API_KEY", text)
                self.assertNotIn("vars.OPENAI_TEXT_REVIEW_MODEL", text)
                self.assertNotIn("vars.OPENAI_VISUAL_REVIEW_MODEL", text)

    def test_text_and_visual_secrets_do_not_cross_fallback(self) -> None:
        text_workflow = (REPO_ROOT / ".github/workflows/ai-bridge-text-review.yml").read_text(encoding="utf-8")
        visual_workflow = (REPO_ROOT / ".github/workflows/ai-bridge-visual-review.yml").read_text(encoding="utf-8")
        self.assertIn("OPENAI_REVIEW_API_KEY: ${{ secrets.OPENAI_REVIEW_API_KEY }}", text_workflow)
        self.assertNotIn("OPENAI_VISUAL_REVIEW_API_KEY", text_workflow)
        self.assertIn("OPENAI_VISUAL_REVIEW_API_KEY: ${{ secrets.OPENAI_VISUAL_REVIEW_API_KEY }}", visual_workflow)
        self.assertNotIn("OPENAI_REVIEW_API_KEY", visual_workflow)
        self.assertNotIn("OPENAI_API_KEY: ${{ secrets.", text_workflow + visual_workflow)

    def test_paid_review_models_resolve_to_terra(self) -> None:
        for path in self.paid_workflows():
            text = path.read_text(encoding="utf-8")
            with self.subTest(workflow=path.name):
                if "text-review" in path.name:
                    self.assertIn("OPENAI_TEXT_REVIEW_MODEL: gpt-5.6-terra", text)
                if "visual" in path.name:
                    self.assertIn("OPENAI_VISUAL_REVIEW_MODEL: gpt-5.6-terra", text)
                self.assertNotRegex(text, re.compile(r"OPENAI_(TEXT|VISUAL)_REVIEW_MODEL: \\$\\{\\{ vars\\."))

    def test_input_tokens_permission_preflight_skips_paid_responses(self) -> None:
        for path in [
            REPO_ROOT / ".github/workflows/ai-bridge-text-review.yml",
            REPO_ROOT / ".github/workflows/ai-bridge-visual-review.yml",
        ]:
            text = path.read_text(encoding="utf-8")
            with self.subTest(workflow=path.name):
                self.assertIn("input_tokens_preflight_only:", text)
                self.assertIn("https://api.openai.com/v1/responses/input_tokens", text)
                self.assertIn("input_tokens_permission: FAIL_CLOSED HTTP", text)
                self.assertIn("openai_error_message:", text)
                self.assertIn("Verify input-token endpoint permission only", text)
                self.assertIn("do not call /v1/responses", text)
                self.assertIn("AI_BRIDGE_INPUT_TOKENS_PREFLIGHT_ONLY", text)
        text_workflow = (REPO_ROOT / ".github/workflows/ai-bridge-text-review.yml").read_text(encoding="utf-8")
        visual_workflow = (REPO_ROOT / ".github/workflows/ai-bridge-visual-review.yml").read_text(encoding="utf-8")
        self.assertIn(
            "if: env.AI_BRIDGE_TEXT_REVIEW_SKIP != '1' && env.AI_BRIDGE_INPUT_TOKENS_PREFLIGHT_ONLY != 'true'",
            text_workflow,
        )
        self.assertIn(
            "if: env.AI_BRIDGE_VISUAL_REVIEW_SKIP != '1' && env.AI_BRIDGE_INPUT_TOKENS_PREFLIGHT_ONLY != 'true'",
            visual_workflow,
        )

    def test_paid_review_contracts_document_budget_and_no_tools(self) -> None:
        policy = (REPO_ROOT / "docs/workflows/PAID_EXTERNAL_REVIEW_POLICY.md").read_text(encoding="utf-8")
        executor = (REPO_ROOT / "automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md").read_text(encoding="utf-8")
        planner = (REPO_ROOT / "automation/reviewed_handoff/prompts/PLANNER.md").read_text(encoding="utf-8")
        visual_doc = (REPO_ROOT / "docs/AI_BRIDGE_VISUAL_REVIEW.md").read_text(encoding="utf-8")
        combined = "\n".join([policy, executor, planner, visual_doc])
        for required in [
            "max paid calls per task campaign: 2",
            "campaign reserved-cost hard ceiling: USD 0.50",
            "per-call worst-case ceiling: USD 0.25",
            "automatic paid retries: 0",
            "persistent pre-request reservation",
            "only call input-token endpoint",
            "billing/quota zero-retry",
            "Visual Review sends image\ninputs",
            "must not enable image generation",
            "Full CI is a phase gate, not a per-commit ritual",
        ]:
            self.assertIn(required, combined)


if __name__ == "__main__":
    unittest.main()
