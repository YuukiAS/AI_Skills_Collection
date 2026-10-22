# v0.4 本地机械验证

代码提交：`0b4248c7eb2abd4b03a06c97061aa895a556a0e7`。
批准包：`48c42f89d23ba168e2d2045034a7f7117c2e0448`。

| 检查 | 实际结果 |
| --- | --- |
| wrapper / archive tests | 31/31 PASS；真 ZIP/tar.gz/tgz、目录、危险成员、重复/冲突、损坏 gzip 与 9 种 CLI restore 组合 |
| unified delivery contract tests | 6/6 PASS；只证明合同与投影存在，不证明文字质量 |
| existing skill runtime text audit | 9/9 PASS；三处旧短语断言随批准的新职责更新，其他保护保留 |
| full repository tests | 389/389 PASS，90.464 s；`python -m unittest discover -s tests` |
| skills validate | PASS；156 active skills，18 profiles |
| skills audit --all | PASS；既有预算提示保留 |
| Marketplace write/validate/check/path-report | PASS；10 plugins，30 active skills，73 snapshots，0 path over budget |
| second generator check | PASS；未再改生成物 |
| deterministic wrapper build | PASS；连续两次 raw ZIP 同字节，30 文件、一个顶层 Skill |
| source / generated / support parity | PASS；新增 final-delivery 同字节，仍仅两条 allowlisted transform |
| required GitHub CI | PASS；run 39723814005，四个 job success，head 与上述代码提交一致 |
| git diff --check | PASS |

早期全仓 386 项中有 3 个失败，均为直接相关的旧文案短语断言。
没有删测试、skip 或改无关插件；已改为验证批准的新流程、领域边界和完整候选质量责任。
独立检查还发现一个 gzip 尾部未校验 P2，已修复并新增三项回归；最终 389 项全通过。

新开发 ZIP SHA-256：`978b93115a0f66aab6f7a4cce2f590118ce2f0804d7113b02c3626c3b88cfc00`，182374 bytes。
归档与 wrapper 目录长期副本在中央 checkout 的
`private/exports/clear-writing--single-entry-artifact-finalization/v0.4/`。
构建回执见 `../wrapper/BUILD_RECEIPT.json`；source、生成树、profile 与 reader 身份见 `SOURCE_PARITY_SCOPE.json`。

README 本轮无修改；科学英文/UI source、profile、其他插件、候选回放 helper、Bridge、角色合同、VERSION、main/release 未修改。
只读核对的正式 release 为 `f4517798a73adf29d3484306d60845488739f1fc` / repository 5.5.2，
不能把本 task checkout 的旧 5.5.1 或历史 0.5 语言 PASS 当作本轮发布基线/新产品 PASS。

Repository bump decision: NONE (unreleased implementation)
Reason: required model regressions, formal Gates and final artifact review are incomplete; repository PATCH remains late-bound at release.
Affected plugins:
- writing-style: 0.6 candidate remains the same batch; formal release not advanced
- all other central plugins: NO_BUMP

新版 known regressions / should-not-change 实际模型输出尚无；正式 G1-G6 未运行。
独立代码复核无剩余 finding 不等于整体 implementation acceptance、artifact PASS 或 final candidate freeze。
精确回放入口证据见 `CODEX_RUNTIME_PREFLIGHT.json` 和 `../PLANNER_HANDOFF.md`。
