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


if __name__ == "__main__":
    unittest.main()
