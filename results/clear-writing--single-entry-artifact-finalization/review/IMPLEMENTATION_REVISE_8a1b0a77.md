# 独立实施审查：修正前记录

审查者：独立只读子任务 Hooke。
Reviewed commit：`8a1b0a77d6e182423ac24779f8748fc3e5362d9b`。
ZIP：`e4c451841583cb6e1ae4212f8d8559b93ef4272f66d687d3f6762f6114a73dc6`。
原始结论：`LOCAL_REGRESSION=PASS（13/13）`；`IMPLEMENTATION_REVIEW=REVISE`；`ALLOW_FINAL_CANDIDATE_FREEZE=NO`。

审查者完整读取了 13 份任务、13 份输入和 13 份实际输出，并核对原始产物与采集副本哈希。
全部语义 PASS，限于本地开发回放，不是 ChatGPT Web G1-G6 或 fresh holdout。
已确认 f86c4d0d 与 8a1b0a77 的回放 payload 相同，允许保留首次有效产物，不改写实际运行提交。

最后两个未关闭问题：

1. P2：`[appendix](<appendix.md>)` 的尖括号没有去掉，合法目标被误拒绝；
   reference-definition 正则把 `[^note]: This is explanatory prose` 脚注的首词误当文件路径。
2. P2，results-only：`collect_artifacts()` 没有创建输出目录；只运行 `--collect-only` 的恢复场景可能 FileNotFoundError。

Executor 随后在 `079bd7987bb33d624d244feb415327d5cf2343d8` 修正这两处，新增两个单测，
不修改 wrapper 或专业 payload。此文件保存真实 REVISE，不覆盖为 PASS。
修正后的独立结论另存 `IMPLEMENTATION_REVIEW.md`；未得到该结论前不冻结候选。

此前 helper 路径、通配符拒绝、嵌套链接相对基准、引用式链接缺失检测和请求前原子 attempt 保留问题，
审查者已确认关闭。恢复集合仅做本地模拟，没有账户 mutation。
38 个 transport part 的逐片、拼接、解码、ZIP 同字节检查也已由审查者独立通过。
