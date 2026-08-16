# 004 Current Library Acceptance — Planner Review

reviewed_commit: `109b333ed73a7ed2c304f45e4b294bc996b4eb48`
implementation_commit: `0e7939bcd914448e2dfef94ae2b98b25a213ce85`
review_round: 1
decision: REVISE

## 结论

004 目前非常接近通过，但还不能宣布 `ACHIEVED`。版本、十插件 Marketplace、CHANGELOG、最终用户报告、Marketplace 三个重点插件安装 smoke，以及当前 `main` 的 GitHub Actions 都已经满足最新总 Goal 的主要发布门槛。现在只剩 1 个明确阻断问题：`presentation-desktop` 的真实 Source CLI 安装没有把 profile 中声明的两个 `secondary_skills` 安装进目标环境，因此最终安装验收与冻结合同不一致。

这不是要求重新设计 profile 或安装系统，也不重新打开 001–003。只需要把 `presentation-desktop` 的实际安装结果与它自己的 profile 合同对齐，然后重跑相关生成、测试、真实安装 smoke 和远端 Action。

## 已确认通过的部分

- 001、002、003 均已有独立 Planner `PASS`，不重新打开。
- `setup.py` 当前为 `4.3.0`。
- 十个中央 Marketplace 插件拓扑保持不变，`marketplacePluginBudget=10`；发布实现把十个插件统一到 `4.3.0`，没有把 `scientific-visualization` 从 `4.2.0` 降级。
- `CHANGELOG.md` 已有 `4.3.0 - 2026-08-16` 发布记录，覆盖十插件恢复、科研写作/文献边界、writing-style、Presentation 路由与 render/visual QA，以及 server-local installation smoke。
- `docs/CURRENT_LIBRARY_REFINEMENT_REPORT.md` 已按用户能力说明本轮变化，包含 before → after、10 个自然语言 example usage、未采用方案、4.3.0 安装结果与限制说明。
- Marketplace 真实安装 smoke 已覆盖 `writing-style`、`research-writing`、`presentations`，三者均报告安装为 `4.3.0`。
- Planner 独立读取真实 GitHub Actions：当前最新 `main` 提交 `109b333ed73a7ed2c304f45e4b294bc996b4eb48` 的 `Codex Marketplace` workflow 已 `completed / success`；发布实现提交 `0e7939bcd914448e2dfef94ae2b98b25a213ce85` 的 workflow 也为 `completed / success`。
- 发布实现 diff 显示 CLI、registry 生成版本、十插件 metadata 和 README/CHANGELOG 已同步到 `4.3.0`；没有发现六插件基线回退。

## Blocker 1 — `presentation-desktop` 的 secondary skills 没有进入真实安装结果

### 冻结依据

最新 `automation/reviewed_handoff/tasks/CURRENT_LIBRARY_REFINEMENT_GOAL.md` 的真实安装验收明确要求：通过 Source CLI 实际安装 `presentation-desktop`，确认 `research-presentations`、`business-presentations`、`writing-fidelity`、`scientific-prose`、`chinese-prose` **以及 secondary skills 按 profile 进入目标环境**。

当前 `profiles/presentation-desktop.json` 明确声明两个 `secondary_skills`：

- `skills/tools/documents-media/render-chinese-math-pdf`
- `skills/writing/research/citation-verification`

### 真实观察证据

当前 `results/004_current_library_acceptance/RESULT.md` 的 Source CLI smoke 明确只报告安装 5 个 skills：

- `research-presentations`
- `business-presentations`
- `writing-fidelity`
- `scientific-prose`
- `chinese-prose`

最终用户报告也只列出这 5 个，没有证明 `render-chinese-math-pdf` 与 `citation-verification` 进入目标环境。

Planner 进一步检查当前 `scripts/skills.py`：profile 过滤逻辑只遍历 `profile.get("skills", [])` 构造实际安装集合，没有把 `secondary_skills` 加入 profile 安装选择。因此这不是 RESULT 漏写，而是当前真实安装语义确实不会安装这两个 secondary skills。

### 最小修复

不要全局扩大所有 profile，也不要重构安装器。优先采用对现有行为影响最小、能够让 `presentation-desktop` 自身合同成立的修复：

- 让 `presentation-desktop` 的这两个当前必需辅助能力在正常 `--profile presentation-desktop` 安装时真实进入目标环境；
- 如果仓库既有语义规定 `secondary_skills` 只是非安装型提示，则把这两个本轮验收要求明确依赖的能力移入该 profile 的实际 `skills` 安装集合，并同步相关 profile 文档/测试；不要为了这一处改变所有 profile 的 `secondary_skills` 语义；
- 如果选择修改安装器，则必须证明不会让其他 profile 意外扩大安装范围，并补相应回归测试。

### 修复后必须看到的证据

1. 在新的干净临时目录再次执行 `presentation-desktop` Source CLI 安装；
2. 目标环境实际存在 7 个相关 `SKILL.md`，除原 5 个外还必须包含：
   - `render-chinese-math-pdf`
   - `citation-verification`
3. `verify_server_installation.py --profile presentation-desktop --json` 或当前等价 smoke 对新的安装结果通过；
4. 更新 `results/004_current_library_acceptance/RESULT.md` 和最终用户报告中的安装说明，使其与真实安装集合一致；
5. 重跑受影响测试、全库验证、`git diff --check`；
6. push 后新的最终 `main` 对应 GitHub Actions 必须 `completed / success`；
7. 版本继续保持 `4.3.0`，十插件拓扑和 `marketplacePluginBudget=10` 不变。

## 本轮不要求返修的内容

不要因为此次 `REVISE` 再调整科研写作、writing-style 或 Presentation 路由；这些已经通过。也不要新增顶级插件、重新整理 149 个 skill、处理新的 Notion/Research 候选，或为了“更完整”修改无关 profile。

当上述唯一 blocker 关闭后，Planner 下一轮只需复核新的真实安装结果、相关 diff、最终用户报告和最新 GitHub Actions；若无新阻断问题，即可给出 `ACHIEVED`。
