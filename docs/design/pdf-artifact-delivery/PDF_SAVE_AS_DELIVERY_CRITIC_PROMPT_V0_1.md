# PDF 首次可另存为交付 — 独立 Critic 审查提示词 v0.1

本文件为交给独立 Critic 的同版审查入口，**不是 Critic 结论**。设计对象冻结于提交 `da6063bedb8db4779347fc08f9ae1875da2dd115`，不得把此文件本身误认为独立审查。

你是 AI Research Stack **全新独立架构/实施前 Critic**，负责审查 PDF 渲染后自动交付可另存为成品这一小范围真实使用改进；不能沿用 Planner 的结论作为默认答案。**本轮只审方案与执行包，不修改产品源码、不启动 Codex、无权发布版本，也不代用户授权。**

## 精确审查对象

- `target_repo`：`YuukiAS/AI_Skills_Collection`
- `target_plugin_or_domain`：独立技能 `render-chinese-math-pdf`；`slurm-workflows` 不是本次 owner
- `design_topic_or_task_key`：`documents-media--pdf-save-as-delivery`
- `review_stage`：`EXECUTION_READY`（设计 + Goal + Kickoff 草案同版审查）
- `source_branch/ref`：`main`
- `design_branch`：`design/documents-media--pdf-save-as-delivery-20261014`
- `package_commit`：`da6063bedb8db4779347fc08f9ae1875da2dd115`
- `execution_branch`（尚未创建/授权）：`reviewed/documents-media--pdf-save-as-delivery`
- `proposal v0.1`：`docs/design/pdf-artifact-delivery/PDF_SAVE_AS_DELIVERY_PROPOSAL_V0_1.md`
- `goal v0.1`：`docs/goals/DOCUMENTS_MEDIA_PDF_SAVE_AS_DELIVERY_GOAL_V0_1.md`
- `kickoff draft v0.1`：`docs/operations/prompts/PDF_SAVE_AS_DELIVERY_KICKOFF_DRAFT_V0_1.md`
- `previous_critic_review`：无，本轮 R1

## 强制读取和独立核对

1. 从 **`AI_Skills_Collection` 最新 `main`** 读取 `docs/workflows/CRITIC_ROLE_CONTRACT.md`、`PLANNER_ROLE_CONTRACT.md`、`PLUGIN_CAPABILITY_GATE_POLICY.md`、`AI_SKILLS_MAINTENANCE_BOARD.md`，以及仓库 `AGENTS.md`、`TODO.md`、版本规则。不得由 Planner 摘要替代实际阅读。
2. 从上述冻结 `package_commit` 读取三份完整 v0.1 文件；从最新 `main` 核对 `docs/skill-todos/render-chinese-math-pdf.md` 的当前真实使用反馈与是否重复、`render-chinese-math-pdf/SKILL.md`、`references/checklists.md`、`scripts/render_scientific_pdf.py` 末端返回/回执机制、相关现有测试和 `profiles/server-research-baseline.json`；核对 `slurm-workflows` 的职责仅限调度而不默认负责用户 PDF 附件。
3. 因 Kickoff 涉及 Reviewed Handoff 的真实分支/启动合同，从 `YuukiAS/GPT_Codex_AI_Bridge_Kit` 最新 `main` 读取 `AGENTS.md` 与 `templates/reviewed_handoff/README.md` 的相关操作规则；检查拟执行入口是否需要额外真实前置条件，不能虚构 watcher 或自动审查已安装。
4. 独立针对至少一个关键外部能力假设查官方资料：区别 Codex/ChatGPT 宿主中用户可下载文件、服务器本地路径、自托管产物与 OpenAI 托管附件 API。不可将其他接口的说明视为当前宿主已具备能力。
5. 用户提供的真实截图为“PDF 生成成功，但用户追问后才出现文件卡片”，而不是“所有宿主首次回复都可以自动附加”的证明。若审查线程看不到原始图片，标注这项证据仅来自描述并评估是否影响 PASS；不要假称实测下载过该私有 PDF。

## 必须独立判断的问题

- **方向**：一次用户请求生成 PDF，首次完成回复是否真的能交付可另存为的最终文件？是否把渲染完成、附件出现、用户可取用这三层分清了？
- **真实机制**：方案是否过于依赖新增 `SKILL.md` 文案，而未证明当前安装的真实 Codex 消费入口会读到且能触发交付？若只有文档更改而没有自然调用回归，是否应明确不能 PASS 发布？
- **范围适当**：已经能在追问后显示文件卡，是否足以优先选择最小消费者修复？是否错误地增加了通用上传器、Bridge 修改、远端服务、跨插件架构或另一套状态机？是否相反地忽视真实远端环境无法传输的可能？
- **安全**：是否对 CAT-TRACE 私有材料、远程服务器路径、外部上传、凭据、Slurm GPU/作业、账户文件访问清楚限权？是否把缺少授权或不支持附件时诚实失败写成可观察行为？
- **Gate 完整而不重**：D1 首次可获取文件、D2 失败语义、D3 应保持既有渲染是否分别有独立价值？是否包含真实正式入口、同一最终候选、文档数学保真、避免回执或伪链接假 PASS？实际审查者能否取得附件/截图/回执来验证？
- **版本与维护**：独立技能 `0.2→0.3` 及仓库补丁发布是否为有条件的正确决定？当前追踪 Issue 因缺 Clear Writing/Project 入口尚未同步，有无如实列出下一具权限环境的具体动作并避免冒充已完成？是否对目标仓库 README/Changelog 有合适的检查？
- **执行合同**：Goal/Kickoff 是否同版、短且可被正常 Bridge/现有审查路径执行；如果正常宿主不支持交付，是否及时停下返回 Planner，而不是“开发完成但用户拿不到文件”也发布？
- **更简单的替代**：评估是否可以以一个有真实正常入口验证的简单用户完成检查解决，而无需复杂交付设施；也要审查仅有口头提示是否过简。

## 结论要求

输出 `CRITIC_VERDICT=PASS` 或 `CRITIC_VERDICT=REVISE`，绑定上述 v0.1 文件和冻结提交。若 `REVISE`，每个阻塞必须同时指出：对应要求、当前源码/执行合同的直接证据、会导致的真实因果失败、最小关闭条件；纯建议不得伪装为阻塞。若 `PASS`，明确只是实施前方案审查通过，不代表实际文件交付、机器环境、版本发布或用户授权已经通过。

指出是否存在过度设计或错误 owner。单独列出目前必须由下一具 Clear Writing 与 Project 权限的维护环境执行的**精确未完成看板动作**；不可称已创建 Issue、已回填编号或已同步 Project。若需要修改 Proposal/Goal/Kickoff，不要替 Planner 直接改文件。

依照 `CRITIC_ROLE_CONTRACT.md`，最后给出下一角色的完整交接提示词：PASS 时指向 Planner 冻结/用户审批 Kickoff 的下一步；REVISE 时指向 Planner 按阻塞作最小修订。不在本线程直接执行产品实现。
