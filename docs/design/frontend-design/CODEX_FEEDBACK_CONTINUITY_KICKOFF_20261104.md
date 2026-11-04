# Codex 执行入口：Frontend Design 反馈连续性与定向返修

你负责对 `YuukiAS/AI_Skills_Collection` 中**现有** Frontend Design / `web-development` 进行一次小而完整的可靠性改造。**这不是开发新的 UI 产品，也不是重写现有 P0–P4、S1/S2/S3 或 Design Assurance。**

必须首先读取：
- `AGENTS.md`，尤其生产插件维护、source/generated 分界、任务规模和 Reviewed Handoff 规则；
- 当前仓库 `skills/tools/frontend/frontend-visual-systems/SKILL.md`、`product-ux-planning`、`visual-direction` 的直接相关部分；
- 分支 `design/frontend-feedback-continuity-20261104` 上的 `docs/design/frontend-design/FEEDBACK_CONTINUITY_IMPLEMENTATION_CONTRACT_20261104.md`；
- 同分支 `docs/plugin-todos/web-development.md` 中“用户反馈误升级为整体重设计”这一个新案例。

**已有的生产机制必须先实测其当前表现**。若一个真实案例已经被现有规则稳妥处理，不再增加同义条款。修复的是使用中真正缺失的路由与可验证保护，不是文字合规性。

## 直接目标

当一个真实产品已存在、用户指出一处问题时，FrontEnd coordinator 要实际做到：

1. 检查精确候选和用户反馈，区分 S1 局部修复、S2 有界设计调整、S3 方向级重设。普通反馈默认不得自动升级 S3；用户明确要求全重设时不得机械阻止。
2. 尽量从现有 repo/设计 authority 和用户历史决定恢复已认可的局部，不要求用户重复解释，不将旧自评/旧审查 PASS 冒充用户接受。
3. 在局部修改中绑定 `KEEP/REPAIR/UNTOUCHED/VERIFY/ROLLBACK`，只对有实质未决产品选择的情况向用户提最小必要问题。小 CSS/bug fix 不产生冗长状态文档、不强制 Work/Pro。
4. 给 Codex 明确差异实现合同；Codex 发现真产品歧义应退回决策者，不再自行猜出新的布局/图形隐喻。
5. 对同一准确 commit / 宿主 / 视口 / 用户任务链验证本次修复和已认可邻近行为，不能用“构建成功/旧截图/静态图”宣称新产品合格。
6. 连续两轮同类反馈仍失败或新版丢失已认可项，停止自动“再开一轮”，输出最小下一实验。

把 Claude/GPT Astra/GPT 高/极高/Work 作为按需**可替换角色**，不在 plugin 里硬编码模型名、订阅价格或固定 Planner–Critic 链。Codex 保留执行者职责，Claude/GPT 可通过项目已有 canonical design / Git 提交接手设计判断。

## 实施与仓库安全

遵守 `AGENTS.md`：生产插件变更使用现有 `workflow-core + ai-skills-core + web-development` 维护路线。不要自己跳过必须冻结的任务合同；需要 Reviewed Handoff 时以一个有边界任务完成，不新增并行计划系统。优先单一 task key：`web-development--feedback-continuity-repair`，实施写入其 `reviewed/<task_key>` 分支，保护 `main`、`release` 与 `design/frontend-feedback-continuity-20261104` 设计参考。没有提交到当前会话的明确合并/发布授权，不合并、不更新稳定 release。

最小源码范围优先：
- `skills/tools/frontend/frontend-visual-systems/SKILL.md` 的“反馈入口/分类/最小变更合同/回归”；
- 若确实必要，再最小修改 `product-ux-planning` 与 `visual-direction` 的对应职责；
- 原有测试/回放夹具；
- generated payload **只能通过已有 generator 生成**，不得手改 `plugins/codex/plugins/**`。

不要改 unrelated plugins、Bridge Kit、Figma provider、安全/审批机制；不要另建独立状态机、数据库、新 Skill、常驻模型服务。

## 真实回归与验收

以设计合同第七节的八个案例为依据，实际完成“现有入口 baseline → 最小修复 → 回归”。尤其：

- Atlas V06→V07：把“去除无意义边”误成“删除全部关系并做分类目录”必须被识别为范围/产品语义错误；不能只测试最后按钮数和边数量。
- Blueprint Workbench：实现台局部认可后的局部密度调整，不得重建成普通 IDE。
- Obsidian：静态好看不能代替真实宿主；无真实宿主证据只报告未验证。
- 一个按钮 CSS/S1 小修：只做小修，不强制 Figma、独立 Pro、整站 QA。
- 用户明确全重设：S3 可以合法进入，但必须保存可复用旧资产与回滚。
- 跨会话、跨模型接力：新对话只读 canonical design/相关 screenshot 和最新差异，不要求重读全部历史 PDF。
- 旧 commit 的截图不能用于宣称新 commit 完成。

至少一次实际 candidate/plugin 消费回放，证明新规则**真实影响动作**；不能只搜索源文件包含 `KEEP` 或 `S1` 就宣布有效。

## 完成方式

严格按仓库正式维护标准测试、生成、回放、review 与版本策略执行。通过前不得声明插件新能力已发布。只有通过全部适用证据后，才能提出正式集成/release 申请，不能自行更新 `main`、`release`。

最终中文解释“用户现在遇到反馈后会得到什么不同的行为”而不是流水账。必须给：精确 implementation branch/commit、修改范围、真实回放的旧坏/新好证据、没有通过的测试、需要用户判断的唯一产品问题（若无则说明没有）、当前是否已经发布并在 Mac mini 真正可用。未真正发布时明确说明需正式集成与更新安装环境。

如果当前 session 只能做 bootstrap/Plan，则只输出**一个**符合当前仓库契约的下一动作，保留已取得的成果，不回头再设计整套插件。
