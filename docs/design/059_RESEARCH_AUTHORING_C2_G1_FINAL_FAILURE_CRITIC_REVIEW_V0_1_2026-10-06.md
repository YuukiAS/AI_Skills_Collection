# 059 Research Authoring C2 G1 最终验收失败 — Critic Review v0.1

日期：2026-10-06  
角色：独立 Critic  
审查阶段：C2_FINAL_GATE_FAILURE_ATTRIBUTION  
任务：`research-authoring--formal-production-authoring`

## 结论

```text
RESULT=REVISE
FINAL_CANDIDATE_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0
FINAL_GATE_FAIL=G1
G1_FAILURE_IMMUTABLE=YES
G2_G3_G4_MUST_REMAIN_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```

C2 的最终验收失败成立，不能改写为环境误差，也不能通过重复运行、换提示词或拼旧证据恢复为 PASS。

这次失败不是候选未加载。exact C2 的 `research-writing@ai-skills-candidate` 已实际消费，问题是正式 PDF 请求在 Research Authoring 与 PDF 渲染器同时可发现时发生了所有权冲突。

## RA-C2G1-1 — 正式 PDF 路由仍允许渲染器越过 Research Authoring 的独立入口边界

### requirement

冻结的 G1 要求：

- 正式导师 PDF 请求先进入 Research Authoring；
- 在独立 Research Authoring / 无批准渲染伴随能力的入口中，只能产出稳定科研 source + 完整下游生产交接；
- 不能因为系统里存在通用文件、计算或渲染能力，就自行完成 PDF 编译、预览和 PDF 派生 QA。

### direct evidence

失败证据：

`results/research-authoring--formal-production-authoring/c2_final/C2_FINAL_GATE_STOP_G1_FAIL.md`

记录 exact C2 已消费：

```text
plugin_id=research-writing@ai-skills-candidate
candidate_path_reads=2
original_conflict_path_reads=0
quarantine_path_reads=0
```

但最终生成：

- `research_update.pdf`
- `build/research_update.generated.pdf`
- PNG preview
- extracted text
- PDF QA / render receipt

完整 child trace 进一步显示：

1. 在读取 Research Authoring report aggregate 之前，agent 已经声明将使用 `research-reporting`、`writing-fidelity` 和中文数学 PDF 渲染技能；
2. 随后确实读取 exact C2：
   `.../ai-skills-candidate/research-writing/0.3/skills/report/SKILL.md`
3. 该 aggregate 已明确写明：
   独立/skills-only 且无批准 renderer companion 时，只能 source + handoff，不得 compile/render/preview/QA PDF；
4. 但运行时随后又读取全局：
   `/users/a/e/aereinh/.agents/skills/tools-documents-media-render-chinese-math-pdf/SKILL.md`
5. 最终执行 Pandoc/XeLaTeX、`pdfinfo`、`pdffonts`、`pdftotext`、预览等完整渲染路线。

因此这是 normal-entry owner/routing failure，不是 candidate loading failure。

### causal risk

上一轮只加强 generated report aggregate，已经不足。

原因是 renderer Skill 自己的触发条件仍是：

“用户请求中文/数学 PDF -> 使用本 Skill”。

它没有表达：

“如果当前请求是 Research Authoring 拥有的研究文档生产任务，必须等待 Research Authoring 的显式下游交接；仅仅因为 renderer Skill 在全局可发现，不构成当前入口的渲染授权。”

所以 agent 可以在进入/读取 Research Authoring aggregate 之前就同时选中 renderer。继续只往 aggregate 里增加同义禁止语句，不能可靠阻止这种并行 owner 选择。

### minimum closure

Planner 必须做一次很窄的生产路由修复提案，不重开 Research Authoring 整体架构。

必须比较并选择最小可靠组合：

1. **Research Authoring canonical owner 边界**
   - 明确定义“批准的 renderer companion / downstream handoff”是什么；
   - 全局 Skill 可发现性本身不得被解释为已获得 renderer route；
   - 独立 Research Authoring 入口不得主动发现并调用 renderer。

2. **`render-chinese-math-pdf` 触发边界**
   - 对 Research Authoring 拥有的研究报告/论文文档生产请求，不得仅凭用户说“PDF”就自触发；
   - 只有 render-only 请求，或已经存在明确 Research Authoring/downstream handoff，才进入渲染；
   - 不改变它作为真正 renderer owner 的 PDF 生产与 QA 能力。

3. **profile / routing consumer**
   - `research-main` 中 Research Authoring -> renderer 的正式组合仍应可工作；
   - standalone `research-writing` / Marketplace Research Authoring 不得因为全局 renderer 安装而自动获得 renderer companion语义；
   - 不靠测试 prompt blacklist、fixture 名、路径或 G1 特判。

Planner应独立判断修复到底需要：
- canonical Research Authoring core/report；
- renderer trigger boundary；
- profile/routing metadata；
- 或其中最小组合。

但不得再次只修改 generated aggregate 并宣称关闭，因为本次最终证据已经证明 aggregate 被实际读取后仍不能阻止 renderer owner 并行进入。

### owner

Planner。

## 候选与证据处理

```text
C2=ac501d988f00cb6672fec105ae5fd51a0679cae0
C2_G1=FAIL
C2_FINAL_CANDIDATE_RELEASE_ADMISSION=FAILED
```

如果产品需要修复，必须形成新的 product candidate（后续可命名 C3）。

本次 G1 失败永久保留为回归证据。

C2 上尚未执行的 G2 Phase 1、G3、G4不得继续消费为 final evidence。

修复后的新候选必须重新：
- development regression；
- pre-final admission；
- 同一候选直接 final evidence。

不允许跨候选拼 PASS。

## 不需要修改的层

当前没有证据要求：

- 重做 shared candidate replay infrastructure；
- 修改 Bridge Kit；
- 修改统计建模、Presentations 或其他科研领域插件；
- 改写 frozen G1 natural request；
- 新建 G5；
- 启动 successor task。

本问题仍属于 AI_Skills_Collection 内部的 Research Authoring / renderer normal-entry routing ownership。

## 权限边界

本 review 只做归因与提出最小关闭条件，不授权 production mutation、live Plugin update、paid API、main merge 或 release。
