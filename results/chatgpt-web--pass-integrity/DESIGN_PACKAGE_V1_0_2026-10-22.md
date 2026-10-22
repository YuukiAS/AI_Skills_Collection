# Planner–Critic 1.8 v1.0 设计包：真正核对用户可读批准产物

日期：2026-10-22
任务：`chatgpt-web--pass-integrity`
来源分支：`design/chatgpt-web--pass-integrity-v0-4`
审查阶段：`DESIGN_ARCHITECTURE_REVIEW_V1_0`，仅 `PROCEED/REVISE`
本清单不包含自身所在提交 SHA；调用方在用户提示词中提供唯一 PACKAGE_COMMIT，避免自引用哈希。

## 本版需要完整审查的同版文件

- `docs/workflows/CHATGPT_WEB_USER_NEEDS_AND_PLANNER_LESSONS_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_PROPOSAL_V1_0_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_PLAN_V1_0_2026-10-22.md`
- `docs/goals/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_GOAL_V1_0.md`
- `docs/operations/prompts/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_KICKOFF_DRAFT_V1_0_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_CRITIC_PROMPT_V1_0_2026-10-22.md`
- 本文件

## 版本变更

前一 v0.9 设计包提交：`074327fb212dce018972421289b65601b6910799`。其核心有价值改动是提前形成同版用户说明并交独立 Critic审。但与旧 1.7 一样，仍完全依赖 Web 模型自由回复，缺可执行的批准内容身份核对与用户界面正式呈现，所以不能作为用户“多轮以后必然说人话”的充分证明。

v1.0 明确区分：专业语义审查、机器身份核对、用户实际看到的准确审定正文。这三条链只有都实际发生才宣称完整能力。新增计划中的一致性工具和 Mica 研究目前完全没有实施，不可因为设计文件存在就改写事实。

## 已直接核查的当前事实

正式 AI Skills `main@f1de8e85957d32a50f4458349f450ec65add13bb`：Planner 1.7、Critic 1.7、Capability Gate Policy 1.2、Project setting 2026-10-19、Maintenance Board 与 AGENTS。
旧 v0.7/v0.8/v0.9 设计文件及 Phase C、Slurm 事故证据。
Mica `YuukiAS/Mica-for-ChatGPT main@7059c0dc24b908b57bd0e1f475142ba4f4520621`：`extension/src/content.ts` 有 DOM 选择器和观察器，dist `manifest.json` 当前版本 0.1.7 且权限限 ChatGPT Web；Mica `AGENTS.md` P0 明确不得在长线程性能恢复证据完成前随意扩到其它功能，真实浏览器验收不得偷偷复用登录账户自动化。
Bridge `YuukiAS/GPT_Codex_AI_Bridge_Kit main@bc94e41f44bd5b534d8ab8caa304114b8bf90685`：已有 Reviewed Handoff 独立复核运行协议与 CLI，但不是本项目默认 ChatGPT Web 用户回复的受控显示入口，不能凭其存在声称已完成。
GitHub main 当前未启用受保护分支规则，不能只新增 CI 就声称 merge 被强制拦截。

## 需要独立 Critic 特别审查的取舍

1. 是否真的需要受控 UI，还是成熟的更简单原生能力可以提供等价效果；
2. 是否有能力在不增加用户重复动作的情况下获取完整、同一版本的审定内容并直接在其阅读界面展示；
3. 是否有合理的 AI Skills 轻量批准包核对正常入口，不能只运行一个可以绕过的测试；
4. 跨 repo Mica/Bridge 是否改变冻结职责和权限，不能由本轮 Planner 单方面批准；
5. 用户实际满意度和专业判断仍须独立全文评审，机器字符串校验不是自然语言质量保证。

## 当前权限和状态

只写当前设计分支文档。不修改 main、正式角色合同、任何产品实现、Mica/Bridge、用户浏览器或工作区。未进行付费调用、真实产品 Gate 或正式实施。v1.0 只待独立设计 Critic `PROCEED/REVISE`；不存在可以直接发给 Codex 的批准入口。

README checked: current change is unpublished design docs; no update required.
