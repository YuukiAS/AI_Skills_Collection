import unittest
from pathlib import Path

from scripts.audit_skill_runtime_text import audit


REPO_ROOT = Path(__file__).resolve().parents[1]


class SkillRuntimeTextAuditTests(unittest.TestCase):
    def test_runtime_text_audit_passes(self):
        self.assertEqual(audit(), [])

    def test_chinese_prose_requires_automatic_final_pass(self):
        text = (REPO_ROOT / "skills/writing/core/chinese-prose/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("任何中文 Markdown/PDF/报告/README/面向用户或读者的中文内容都应自动触发", text)
        self.assertIn("用户不需要显式说“说人话”", text)
        self.assertIn("第一段必须先给人能读懂的判断", text)

    def test_generated_plugin_exposes_chinese_final_pass_trigger(self):
        text = (REPO_ROOT / "plugins/codex/plugins/writing-style/skills/zh/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("任何中文 Markdown/PDF/报告/README/面向用户或读者的中文内容都应自动触发", text)

    def test_writing_fidelity_fails_unreadable_chinese_final_artifacts(self):
        text = (REPO_ROOT / "skills/writing/core/writing-fidelity/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("classify the deliverable as `qa_failed`", text)
        self.assertIn("Chinese Markdown/PDF/slide/report", text)


if __name__ == "__main__":
    unittest.main()
