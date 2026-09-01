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
        self.assertIn("普通英文抽象标签不得承担中文句子的主要语义结构", text)

    def test_writing_fidelity_fails_unreadable_chinese_final_artifacts(self):
        text = (REPO_ROOT / "skills/writing/core/writing-fidelity/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("classify the deliverable as `qa_failed`", text)
        self.assertIn("Chinese Markdown/PDF/slide/report", text)
        self.assertIn("rewrite protects meaning, facts, equations, citations", text)
        self.assertIn("ordinary English abstraction labels", text)
        self.assertIn("text that must survive", text)

    def test_writing_style_phase_two_boundaries(self):
        fidelity = (REPO_ROOT / "skills/writing/core/writing-fidelity/SKILL.md").read_text(encoding="utf-8")
        chinese = (REPO_ROOT / "skills/writing/core/chinese-prose/SKILL.md").read_text(encoding="utf-8")
        scientific = (REPO_ROOT / "skills/writing/core/scientific-prose/SKILL.md").read_text(encoding="utf-8")

        self.assertIn("This is the preservation layer, not the style layer", fidelity)
        self.assertIn("Route Chinese natural-prose passes to chinese-prose", fidelity)
        self.assertIn("Hand off English scientific prose", fidelity)
        self.assertIn("detector evasion", fidelity)

        self.assertIn("正文优先用连贯段落", chinese)
        self.assertIn("不要为了显得结构化把每句话拆成 bullet", chinese)
        self.assertIn("是否保留英文靠语义判断，不靠禁词表", chinese)
        self.assertIn("不能为了自然而改掉证据边界", chinese)
        self.assertIn("普通英文抽象标签不得承担中文句子的主要语义结构", chinese)
        self.assertIn("这个 checkpoint 当初用过哪些病例，目前能确认到什么程度", chinese)
        self.assertIn("这个实验到底在估计什么、回答什么问题", chinese)
        self.assertIn("受保护的反向约束", chinese)
        self.assertIn("连字符英文复合名词", chinese)
        self.assertIn("local-mode posterior aggregation", chinese)
        self.assertIn("forensic-level exact proof", chinese)
        self.assertIn("数据使用与字段约束说明", chinese)
        self.assertIn("client", chinese)
        self.assertIn("参与方", chinese)
        self.assertIn("合并数据训练", chinese)
        self.assertIn("模型权重", chinese)

        self.assertIn("not the manuscript planner", scientific)
        self.assertIn("citation verifier", scientific)
        self.assertIn("Use `research-paper-workflow` for paper-level structure", scientific)
        self.assertIn("Do not erase real limitations", scientific)


if __name__ == "__main__":
    unittest.main()
