from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReviewedHandoffPromptContractTests(unittest.TestCase):
    def test_scheduled_reviewer_requires_plan_frozen_preflight(self) -> None:
        prompt = (ROOT / "automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md").read_text(encoding="utf-8")

        self.assertIn("automation/reviewed_handoff/templates/PLAN.md", prompt)
        self.assertIn("重新读取刚写出的 `PLAN.md`", prompt)
        self.assertIn("frontmatter 与全部 required sections", prompt)
        self.assertIn("`## Frozen decisions`", prompt)
        self.assertIn("`## Implementation scope`", prompt)
        self.assertIn("`## Acceptance and regression gates`", prompt)
        self.assertIn("`## Out of scope`", prompt)
        self.assertIn("只有 PLAN preflight PASS 后，才允许最后写 `CURRENT.json`", prompt)
        self.assertIn("CURRENT.state=PLAN_FROZEN", prompt)
        self.assertIn("不得 freeze", prompt)

    def test_scheduled_reviewer_requires_final_report_preflight(self) -> None:
        prompt = (ROOT / "automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md").read_text(encoding="utf-8")
        template = (ROOT / "automation/reviewed_handoff/templates/FINAL_REPORT.md").read_text(encoding="utf-8")
        template_headings = re.findall(r"^## .+$", template, flags=re.MULTILINE)

        self.assertIn("automation/reviewed_handoff/templates/FINAL_REPORT.md", prompt)
        self.assertIn("以运行时当前 template 为 source of truth", prompt)
        self.assertIn("不允许凭记忆猜 headings", prompt)
        self.assertIn("重新读取刚写出的 `FINAL_REPORT.md`", prompt)
        self.assertIn("全部 required H2 headings", prompt)
        self.assertIn("只有 FINAL_REPORT preflight 通过后，才允许最后写 `CURRENT.json`", prompt)
        self.assertIn("不得写 terminal CURRENT", prompt)
        for heading in template_headings:
            self.assertIn(f"`{heading}`", prompt)

    def test_planner_prompts_prevent_adaptive_holdout_chasing(self) -> None:
        planner = (ROOT / "automation/reviewed_handoff/prompts/PLANNER.md").read_text(encoding="utf-8")
        scheduled = (ROOT / "automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md").read_text(encoding="utf-8")

        for prompt in (planner, scheduled):
            self.assertIn("complete holdout batch freeze", prompt)
            self.assertIn("adaptive replacement/chasing", prompt)
            self.assertIn("non-holdout / synthetic / public-safe regression", prompt)
            self.assertIn("human gate", prompt)
            self.assertIn("完整 frozen batch", prompt)

    def test_program_goal_requires_frozen_four_paper_batch(self) -> None:
        goal = (ROOT / "automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Frozen Batch Real-Paper Generalization Acceptance + Human Closure", goal)
        self.assertIn("一次性冻结", goal)
        self.assertIn("两篇 statistics / biostatistics / methodology papers", goal)
        self.assertIn("两篇 medical-imaging papers", goal)
        self.assertIn("4/4 Terra + Planner PASS", goal)
        self.assertIn("四套真实 rendered decks", goal)


if __name__ == "__main__":
    unittest.main()
