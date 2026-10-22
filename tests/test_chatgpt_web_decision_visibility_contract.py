"""Offline checks for the frozen Planner/Critic 1.8 handoff contract.

These assertions test local contract semantics, not natural-language Web quality.
"""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PLANNER = (ROOT / "docs/workflows/PLANNER_ROLE_CONTRACT.md").read_text(encoding="utf-8")
CRITIC = (ROOT / "docs/workflows/CRITIC_ROLE_CONTRACT.md").read_text(encoding="utf-8")


class DecisionVisibilityContractTest(unittest.TestCase):
    def test_both_contracts_are_same_1_8_candidate(self):
        for source in (PLANNER, CRITIC):
            self.assertIn("版本：1.8", source)
            self.assertIn("日期：2026-10-22", source)

    def test_task_prompt_conflict_blocks_pass(self):
        self.assertIn("缩窄中央最终审查", PLANNER)
        self.assertIn("本轮不得按冲突 prompt 给 `PASS`", CRITIC)

    def test_missing_user_architecture_explanation_is_not_complete_pass(self):
        self.assertIn("最终技术 `PASS` 解释获准架构", CRITIC)
        self.assertIn("不能靠机器字段代替这些判断", CRITIC)

    def test_missing_next_handoff_is_not_closed(self):
        self.assertIn("仅说“需要一个具备某能力的环境”不算交接完成", PLANNER)
        self.assertIn("NEXT_HANDOFF=PLANNER", CRITIC)
        self.assertIn("=== COPY TO PLANNER BEGIN ===", CRITIC)

    def test_full_kickoff_dump_is_rejected(self):
        self.assertIn("不得把 Proposal/Plan/Kickoff 全文", PLANNER)
        self.assertIn("不得在 execution-ready PASS 后机械复制", CRITIC)

    def test_old_blockers_do_not_replace_full_final_review(self):
        self.assertIn("不能把最终审查缩成旧 blocker closure", CRITIC)
        self.assertIn("完整稳定用户承诺", PLANNER)

    def test_explanation_after_pass_does_not_reopen_design(self):
        self.assertIn("纯解释就解释已批准机制，不重开设计", PLANNER)
        self.assertIn("不无故撤销原 PASS", CRITIC)

    def test_contradiction_after_pass_is_investigated(self):
        self.assertIn("新证据与批准结论矛盾就核实事实", PLANNER)
        self.assertIn("不能用“已经 PASS”挡回", CRITIC)

    def test_explicit_new_requirement_is_not_old_authority(self):
        self.assertIn("新增产品要求、范围或权限", PLANNER)
        self.assertIn("不能静默纳入旧批准", CRITIC)

    def test_future_pass_returns_to_planner_before_codex(self):
        self.assertIn("CRITIC_VERDICT=PASS\nREADY_FOR_CODEX=YES\nNEXT_HANDOFF=PLANNER", CRITIC)
        self.assertIn("Planner 在交付验收后", PLANNER)


if __name__ == "__main__":
    unittest.main()
