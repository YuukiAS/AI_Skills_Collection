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

    def test_plugin_refinement_requires_ai_skills_core_companion(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        maintainer = (ROOT / "skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md").read_text(
            encoding="utf-8"
        )
        planner = (ROOT / "automation/reviewed_handoff/prompts/PLANNER.md").read_text(encoding="utf-8")
        executor = (ROOT / "automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md").read_text(encoding="utf-8")
        scheduled = (ROOT / "automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md").read_text(
            encoding="utf-8"
        )

        for text in (agents, maintainer):
            self.assertIn("workflow-core", text)
            self.assertIn("ai-skills-core", text)
            self.assertIn("AI Skills Maintainer", text)
            self.assertIn("target domain plugin", text)
            self.assertIn("allow_implicit_invocation: false", text)
            self.assertIn("generated parity", text)
            self.assertIn("unrelated regression", text)
            self.assertIn("version/changelog", text)

        self.assertIn("## Plugin Refinement Companion Mode", maintainer)
        self.assertIn("Identify the target plugin", maintainer)
        self.assertIn("Identify the domain owner", maintainer)
        self.assertIn("Install or reload the real production plugin", maintainer)
        self.assertIn("Bump the affected plugin version exactly once", maintainer)
        self.assertIn("does not judge", maintainer)
        self.assertIn("PPT scientific quality", maintainer)
        self.assertIn("statistical correctness", maintainer)
        self.assertIn("medical imaging semantics", maintainer)
        self.assertIn("bioinformatics scientific workflow", maintainer)
        self.assertIn("prose scientific meaning", maintainer)

        for prompt in (planner, executor, scheduled):
            self.assertIn("Maintenance companion: ai-skills-core", prompt)
            self.assertIn("Domain owner: <target plugin>", prompt)
            self.assertIn("production behavior", prompt)
            self.assertIn("target domain plugin", prompt)
            self.assertIn("不得新增 schema", prompt)

        self.assertIn("codex plugin list", executor)
        self.assertIn("ai-bridge plugin-replay", executor)
        self.assertIn("只读取本仓库 source", executor)
        self.assertIn("不是 production plugin invocation proof", executor)
        self.assertIn("只读取 source `SKILL.md` 不能算 production plugin invocation", scheduled)

    def test_artifact_aware_review_blocks_044_regression(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        maintainer = (ROOT / "skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md").read_text(
            encoding="utf-8"
        )
        planner = (ROOT / "automation/reviewed_handoff/prompts/PLANNER.md").read_text(encoding="utf-8")
        executor = (ROOT / "automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md").read_text(encoding="utf-8")
        scheduled = (ROOT / "automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md").read_text(
            encoding="utf-8"
        )

        for text in (agents, maintainer, planner, executor, scheduled):
            self.assertIn("PROCESS PASS", text)
            self.assertIn("PRODUCT / ARTIFACT PASS", text)
            self.assertIn("Bridge Kit Text Review", text)
            self.assertIn("rewritten_report.md", text)
            self.assertIn("provenance", text)
            self.assertIn("estimand", text)
            self.assertIn("scientific gap", text)
            self.assertIn("resource contract", text)
            self.assertIn("state of the art", text)

        for text in (agents, planner, scheduled):
            self.assertIn("WAITING_FOR_EVIDENCE / NEEDS_REVIEW", text)
            self.assertIn("不自行实现另一套 artifact transport/reviewer", text)
            self.assertIn("明显机器腔", text)
            self.assertIn("明显 layout failure", text)
            self.assertIn("明显 artifact regression", text)
            self.assertIn("不得推给 `AWAIT_HUMAN_DECISION`", text)

        self.assertIn("不得把 Executor 摘要当作 artifact evidence", scheduled)
        self.assertIn("不要把缺 artifact 的任务交成可 PASS 状态", executor)
        self.assertIn("Private/text artifact review 的底层 owner 是 `GPT_Codex_AI_Bridge_Kit`", agents)
        self.assertIn("Private/text artifact review is owned by `GPT_Codex_AI_Bridge_Kit` Text Review", maintainer)

    def test_review_pass_defaults_to_integration_closure_without_human_gate(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        planner = (ROOT / "automation/reviewed_handoff/prompts/PLANNER.md").read_text(encoding="utf-8")
        scheduled = (ROOT / "automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md").read_text(
            encoding="utf-8"
        )

        for text in (agents, planner, scheduled):
            self.assertIn("integration preflight", text)
            self.assertIn("合回 `main`", text)
            self.assertIn("删除 task branch", text)
            self.assertIn("默认不要求 PR", text)
            self.assertIn("merge conflict", text)
            self.assertIn("branch protection", text)
            self.assertIn("Reviewer PASS 前不得自动 merge", text)

    def test_plugin_refinement_version_gate_is_hard_but_no_change_can_no_bump(self) -> None:
        version_policy = (ROOT / "docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md").read_text(
            encoding="utf-8"
        )
        planner = (ROOT / "automation/reviewed_handoff/prompts/PLANNER.md").read_text(encoding="utf-8")
        scheduled = (ROOT / "automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md").read_text(
            encoding="utf-8"
        )

        for text in (version_policy, planner, scheduled):
            self.assertIn("bump exactly once", text)
            self.assertIn("原 failure replay PASS", text)
            self.assertIn("unrelated regression PASS", text)
            self.assertIn("Unreleased", text)
            self.assertIn("NO_BUMP", text)

        self.assertIn("Baseline replay", version_policy)
        self.assertIn("docs-only", planner)
        self.assertIn("tests-only", scheduled)

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
