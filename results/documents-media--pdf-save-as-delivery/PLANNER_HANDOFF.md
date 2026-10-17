# PDF 首次文件交付：继续原任务的 Planner 交接

当前客户端已有真实可用的 PDF 文件入口，用户已直接确认可以另存为、打开。请在原任务中冻结小范围实施计划；不要重新探测同一客户端能力，不要创建 successor 或扩大为上传设施改造。

## 完整交接提示词

你是本任务的 Reviewed Handoff Planner。读取最新 `main` 的 `AGENTS.md`、`docs/workflows/PLANNER_ROLE_CONTRACT.md`、`docs/workflows/CRITIC_ROLE_CONTRACT.md` 与维护看板规则，然后在下面唯一任务分支工作：

- repo：`YuukiAS/AI_Skills_Collection`
- task：`documents-media--pdf-save-as-delivery`
- execution branch：`reviewed/documents-media--pdf-save-as-delivery`
- execution worktree：`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-documents-media--pdf-save-as-delivery`
- CURRENT：`automation/reviewed_handoff/tasks/documents-media--pdf-save-as-delivery/CURRENT.json`，最近核对为 `PLAN_REQUESTED` / `RUN_GPT_PLANNER`。
- REQUEST：同目录 `REQUEST.md`。
- approved package commit：`2f04291c0d802a010836b955d3b6167cb235be78`，设计分支 `design/documents-media--pdf-save-as-delivery-20261014`。
- proposal：`docs/design/pdf-artifact-delivery/PDF_SAVE_AS_DELIVERY_PROPOSAL_V0_1.md`。
- canonical Goal：`docs/goals/DOCUMENTS_MEDIA_PDF_SAVE_AS_DELIVERY_GOAL_V0_1.md`。
- current evidence：任务分支的 `results/documents-media--pdf-save-as-delivery/PREFLIGHT.md`。

用户已用同版 Kickoff 授权执行，并称 Critic 已通过；设计文件仍有审查前标签，未归档独立 verdict。核对用户所指批准身份，不把 `PDF_SAVE_AS_DELIVERY_CRITIC_PROMPT_V0_1.md` 当作 verdict，也不要用标签陈旧机械否定用户确认。

新增真实证据：本任务正常回复中的绝对路径 Markdown 文件链接呈现 `probe.pdf`，用户随后明确说“你这个下面显示的probe.pdf我可以另存为/打开”。源 PDF 为 1 页 A4、27,294 bytes，SHA-256 为 `dd3682df2bcaabde416e826f36d3fe4ca324584e3f4ccb2d9c8594822a423605`。因此已有正常交付通道，不需要上传服务、虚构 `sandbox:` URL 或跨插件改造。原生 `open_in_codex` 曾返回 `queued`，该返回值不代表文件入口失败。客户端保存副本的哈希未回读；这只是通道基线证据，不是最终修复 D1 PASS。

按已批准 Proposal/Goal 冻结 `AI_BRIDGE_REVIEWED_PLAN_V2` 的 `PLAN.md`，范围限 `render-chinese-math-pdf` 的首次最终回复交付与检查清单及必要受限回归。由 Planner 按正常入口最后推进 `CURRENT` 到 `PLAN_FROZEN`；Executor 不代写计划或代签 review。为原 task + exact branch 确认现有 Planner/Reviewer transport；缺失时如实记录，不使用可能选择其他 task 的 generic watcher，不擅自新增自动化。

计划保留 D1–D3 和同一最终候选要求：首次回复给出经当前宿主确认可取用的最终 PDF；无通道或附件失败时如实报告未交付；原渲染、字体、公式、模板、Markdown/TeX 及非 PDF 边界保持兼容。固定最终候选后再做真实正常入口验收和独立复核，不能用本次基线或静态字符串测试替代最终候选证据。

保留 maintenance companion=`ai-skills-core`，domain owner=`render-chinese-math-pdf`。版本只有在完整行为修复、回归、真实交付、独立复核满足后才按当时政策推进；不提前 bump。维护看板精确待同步动作见 PREFLIGHT，要求真实 Clear Writing 调用、Issue 查重与 source backlink，不冒充已同步。

用户授权范围不变：允许任务内可逆仓库变更、受限回归/CI、exact task branch 普通非强制发布；禁止付费 API、新 Slurm 作业或取消/GPU、私有文件或凭据外传、Bridge/跨插件改造、全局安装部署、强制推送及自动 release 扩项。不要把 bootstrap、Plan 冻结或 PDF 渲染成功写成 overall Goal 完成。
