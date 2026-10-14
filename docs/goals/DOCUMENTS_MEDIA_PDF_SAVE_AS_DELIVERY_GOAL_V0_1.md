# PDF 首次回复可另存为交付 — 执行 Goal 草案 v0.1

**状态：未获 Critic PASS；不能启动执行。**
- 仓库：`YuukiAS/AI_Skills_Collection`
- 任务键：`documents-media--pdf-save-as-delivery`
- 冻结方案：`docs/design/pdf-artifact-delivery/PDF_SAVE_AS_DELIVERY_PROPOSAL_V0_1.md`
- 来源：`main`；拟执行分支：`reviewed/documents-media--pdf-save-as-delivery`（在明确批准 Kickoff 后通过既有 Bridge Reviewed Handoff 入口合法创建/恢复）。
- 目标：真实正常用户一次请求生成 PDF 后，**首次完成回复直接包含可取得并另存为的最终 PDF**，不可取得时如实报告尚未交付。不是增加一个形式化报告字段。

## 工作合同

1. 先读取最新 main 的仓库 `AGENTS.md`、Planner 已审 Proposal、当前 `render-chinese-math-pdf` 正式 `SKILL.md`/回执/检查清单/相关测试、Bridge 当前 AGENTS/Reviewed Handoff 规范；检查已有任务/分支/授权，避免重复 bootstrap。
2. **先取证**：在已批准的真实 Codex 消费环境，用正常安装的相关 skill/profile、公开安全的中英数学示例做一次低成本、无付费、无新 Slurm 作业的“生成 PDF”任务。记录渲染回执/文件、首次最终回复、已有附件/文件卡能力、是否可实际下载或另存为。截图中“追问才出现文件卡”是历史证据，不是对当前入口能力的批准假设。
3. 若已有合法交付通道，只作最小修复：优先技能 `SKILL.md`、`references/checklists.md` 与相应用户完成条件，必要时加受限测试与已存在正常入口的消费者约束。允许核查回执及文件实际字节/路径，不得仅写一条新提示词却宣称自动交付已解决。原则上不改渲染算法、字体或 PDF 制作脚本；若现有回执不足以保持交付文件身份，需先说明并仅在已批准 renderer 范围内作最小身份核验修复。
4. 若必须修改仓库外 Codex App / Bridge Kit / 跨插件共用文件传输/平台附件接口、增添公共 URL 或扩大新数据权限，**停止**，留下事实与最小变更需求交 Planner–Critic；不得在此 Goal 偷做。
5. 使用同一最终候选完成 Proposal §6 D1–D3：真实安装后首次最终回复文件可取得、真实字节/页数内容与通过 QA 的 PDF 相符、失败不假报完成、既有数学字体模板/Markdown/TeX 兼容。单元测试/哈希/回执/模拟 UI 不能替代真实对话交付。
6. 经过独立产物/入口 Reviewer 后才形成正式 release，按仓库版本规范决定独立 skill `0.2→0.3` 和仓库最新 `PATCH`，更新需要的变更记录与 README；不要预先 bump。若缺 gate 或未实际交付，不称 release 成功。
7. 维护看板：该 TODO 在 `docs/skill-todos/render-chinese-math-pdf.md`；按维护看板政策，在具备真实 Clear Writing 和 Project 入口时创建/绑定 Issue 并回写 `tracking: #N`。工具不可用则记录 `CLEAR_WRITING_UNAVAILABLE` / 精确待同步动作，绝不伪造 Issue/Project 状态；在正式 closure 前补齐。
8. 成功时给出用户实际可取得的成品入口、对照原失败的交付证据、最终运行版本/提交、真实回归、独立审查与发行位置；失败保留可复现证据和原 PDF，不重试无限次、不公开私有资料。

**实施权限边界**：只能在用户后续明确批准的任务/分支/工作树内作仓库内变更、合理的安装回放及正常 CI；不授权公网/第三方上传、私有 CAT-TRACE 文件读取/发送、Slurm `sbatch/salloc/scancel`、GPU 占用、Cloud/SSH 凭据修改、外部付费、Bridge 源码修改、强制推送、生产机器全局配置更改或无关发布。新增任何这类动作必须重新确认。

**预计新能力**：用户不再需要追问第二次取得 PDF；如果实际入口不具交付能力，本轮必须如实失败而非交付假 PASS。
