# Research Authoring 共享层

本目录保存三个新读者技能共用的 GPT→Codex 交接、机械制作接口和历史学生合同。当前入口按需读取，避免每次任务顺序加载全部旧合同。

## v0.1 正常入口

- GPT 端：`research-notes`、`research-story`、`student-materials` 完成读者判断、内容计划、科研或教学含义和写作，并调用 `content-selection` 与 `clear-writing`。
- Codex 端：读取确定正文和 handoff，只执行渲染、机械检查、打包、发布和回读。
- 共同文件：
  - [production-contract.md](production-contract.md)：两端职责与制作返回要求；
  - [mechanical-interface.md](mechanical-interface.md)：机械脚本的输入、输出和判定边界；
  - [handoff.template.json](handoff.template.json)：静态交接字段；
  - `scripts/check_research_artifact.py`：机械检查入口。

旧 `paper` 和 `litcite` 名称的转接位于 `compatibility/`。旧的五份学生合同继续保留为历史来源和旧任务定位；新 `student-materials` 已将 v0.1 需要的规则压缩到自己的 references 中。

[student-assessment-cumulative-acceptance-contract.md](student-assessment-cumulative-acceptance-contract.md)
[student-assessment-delivery-closure-amendment-v1.md](student-assessment-delivery-closure-amendment-v1.md)
[student-assessment-end-to-end-pre-execution-runbook.md](student-assessment-end-to-end-pre-execution-runbook.md)
[student-assessment-hw1-nonrecurrence-amendment-v1.md](student-assessment-hw1-nonrecurrence-amendment-v1.md)
[student-assessment-semantic-pagination-amendment-v1.md](student-assessment-semantic-pagination-amendment-v1.md)
