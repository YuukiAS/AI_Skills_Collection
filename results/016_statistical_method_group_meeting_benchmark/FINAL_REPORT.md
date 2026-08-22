---
schema: AI_BRIDGE_REVIEWED_FINAL_REPORT_V1
task_key: 016_statistical_method_group_meeting_benchmark
final_decision: REVISE
---

# 016 Statistical / Biostatistical Method Group Meeting Benchmark — Final Report

## 本轮解决了什么

016 原本只是一个“统计主题 benchmark fixture”，第一版虽然科学对象齐全，却明显低于成熟统计/生统组会的成品标准。用户检查真实 rendered slides 后明确指出：核心公式仍是源码式文本、RRL/reference retrieval 与 QA 元语言泄漏到观众页面、布局过度依赖 pastel boxes / wireframe、文案有明显自动生成痕迹。

本任务因此使用唯一一次 Plan revision，把目标重新冻结为“可以直接投影给统计/生统导师、PI 或顶会研究听众”的成熟科研汇报质量。Executor 随后重做了全部五页，而不是只修第一轮的单根错误箭头。

## 实际改了哪里

Revised implementation 保留原 DGP、固定随机种子、simulation grid、方法比较和全部数值结果，但重构了 audience-facing Presentation：

- slide 1 / 2 的核心统计公式从 ASCII/source-like 文本改为真正数学渲染；
- 删除观众页面中的 `RRL-*`、`Reference retrieval`、`EVIDENCE_MANIFEST`、`Diagram contract`、`Reading target`、`Observed in this synthetic run` 等内部制作/QA/provenance 元语言；
- 五页重新以 DGP、sandwich covariance、simulation design、coverage result、negative result 为主 scientific object，而不是默认 card/dashboard 布局；
- 增加 `reference_design_audit`，记录 inspected reference page 的具体视觉经验如何真正影响当前页面，同时保证这些内部记录不再泄漏到 slide；
- 加强 deterministic Presentation QA，提前阻断 audience-facing internal leak、明显 math-source leak 与 anti-meta-language；
- 016 专用 Terra rubric 新增数学排版、自然学术语言、视觉成熟度、投影可读性与 reference-informed quality 检查。

第一次 revised Terra review 又指出两个真实问题：slide 4 的标题/不确定性措辞过度概括，slide 5 的负结果图缺 Monte Carlo uncertainty。Executor 随后只修这两项，新的 visual identity 再运行一次 `gpt-5.6-terra` 后，五页全部得到 PASS，且没有 blocking finding。

## 以前没有、现在已经验证的能力

016 已经验证 Presentation 系统可以处理一条完整统计方法组会链路：从 clustered-data DGP 和 estimand，到 cluster-robust sandwich covariance、simulation design、带 Monte Carlo uncertainty 的主结果，再到 small-G undercoverage negative result 与 planned CR2 / wild-cluster-bootstrap experiment。

同时，本轮第一次把“成熟科研 slide”质量门槛真正落实到机器可执行与独立视觉审核中：核心数学不能继续是源码字符串，内部检索/QA 元数据不能进入观众页面，参考大牛 deck 必须转化为具体页面设计决策，Terra 不能只检查对象存在和箭头方向。

## 当前为什么仍不能 PASS

当前阻断项是机械 CI/test dependency contract，而不是新的 Presentation 内容 finding。

最新 handoff tip `e43a364fcbbecb56e13aa8d6d515ec24374dbac5` 的 GitHub Actions run `32575849316` 明确失败。Windows sparse checkout 与 Linux/Windows editable-install smoke 均通过；失败只发生在 `Codex Marketplace` 的全库单元测试。干净 runner 成功安装并导入 Pillow 与 `python-pptx`，随后 statistical benchmark generator 在顶层 `import matplotlib` 处报：

```text
ModuleNotFoundError: No module named 'matplotlib'
```

因此 revised implementation 尚未满足冻结 Plan 的“真实 GitHub CI PASS”门槛。Terra PASS、本地 112 tests 自报和机械 render PASS 都不能替代这个 CI 要求。

## 被拒绝的处理方式

本轮没有把 `matplotlib` 缺失解释成统计内容错误，也没有回退五页设计、修改 simulation 数值或扩大 source corpus；这些都没有证据支持。

同样没有自动开启第三轮返修。Reviewed Handoff 明确规定 CI failure 与普通 Reviewer finding 共用同一个两轮审核预算；016 第一轮已经用于内容/视觉审核，因此这次 CI failure 是第二轮 `REVISE`，必须停到人工决策点。

## 建议的人工决定

建议允许一次**纯机械的 CI/test dependency recovery**：完整核对 statistical Presentation regression generator 的实际第三方顶层依赖，并把缺失依赖一次性纳入 CI/test 环境，而不是继续按 ImportError 逐个补包。

该授权应严格限制为测试依赖契约，不允许修改：

- 016 的 DGP、simulation grid 或数值结果；
- 当前五页 audience-facing Presentation 内容；
- 已通过的新 Terra visual identity / rubric 语义；
- inspected reference corpus；
- 后续 medical-imaging benchmark。

修复后只需要重新跑真实 GitHub CI，并在 CI PASS 后恢复对当前 revised implementation 的内容级独立结算。

## 回归风险与剩余工作

当前最大的短期风险不是页面质量回退，而是 CI 环境没有显式表达统计 Presentation fixture 的完整测试依赖。如果不修，后续 medical-imaging / statistical benchmark 仍可能在干净 runner 重复暴露环境差异。

即使 016 最终通过，本次 Presentation improvement cycle 仍未完成；后续还必须做一轮 medical-imaging research group meeting benchmark，并继续使用真实 editable PPTX render、mechanical QA、成熟度增强后的 `gpt-5.6-terra` evidence 与 Planner 独立审核。

## 技术附录

Revised implementation commit：`7e3a4658909781d34899f6ad0b7d784648f1ac50`。

Handoff tip：`e43a364fcbbecb56e13aa8d6d515ec24374dbac5`。

当前 CI：FAIL，GitHub Actions run `32575849316`；失败 job 为 `codex-marketplace`，失败步骤为 `python3 -m unittest discover -s tests`，根因 `ModuleNotFoundError: No module named 'matplotlib'`。

最终 Terra evidence：`PASS`，review identity `82abc553945faf5d5911b86b4189680ae5b00f457b37617d976a1e8caa5cf97b`，五页均 PASS，无 blocking finding。

真实 render：`RENDER_STATUS=ok`，5 张 PNG；机械视觉检查为 `MECHANICAL_PASS`。
