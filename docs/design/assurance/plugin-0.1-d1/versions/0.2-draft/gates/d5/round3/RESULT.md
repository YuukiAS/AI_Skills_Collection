# D5 第 3 次执行：D6 round2 修正后的机械检查

废弃语义扫描零残留。固定检查器离线、在线均检查 62 个节点；按既有 D1 口径排除冻结快照差异与待 D8 项后通过，状态为 PASS_WITH_DECLARED_EXCLUSIONS。原始检查器退出码均为 **1**，不改记为零。

## 实际执行

从设计目录运行：

```sh
python tools/scan_deprecated_semantics.py --report versions/0.2-draft/gates/d5/round3/deprecated-after.json
```

扫描覆盖全部当前节点、走查与当前证据文字，排除内嵌 versions 历史；检查 62 个节点、8062 个字符串，残留 0，允许的明确删除说明或历史引用 39 处。扫描脚本未改。

固定检查器为 YuukiAS/Asteria-Blueprint@229e1736f445bdecffd84773ad543e5f452d65df。15 个检查器/schema/包文件逐一与该 commit 的 Git 对象及既有身份清单核对，字节一致。运行副本、缓存和原始日志位于机器本地临时目录；使用原有依赖，只配置现有来源位置和链接工具。检查规则、schema、runCheck、verifyLive 均未改。

通过原 runCheck 实际执行 `--stage draft --offline` 与 `--stage draft`，输入为当前 Blueprint 的字节相同副本，分别落盘报告。沿用原有真实读者记录，没有补造批准、冻结或读者通过记录。

| 模式 | 节点 | 原始退出码 | 错误 | 人工判断提示 | 未核实 |
|---|---:|---:|---:|---:|---:|
| 离线 | 62 | 1 | 6 | 191 | 1（声明未做在线核实） |
| 在线 | 62 | 1 | 6 | 191 | 0 |

两份报告均仅有既有的 6 项错误：freeze:versions（当前草稿与最近冻结快照不同），以及 reader-current-hash 的 wb-capability、wr-gates、wr-freeze、fail-freeze-explanation-whole、fail-freeze-explanation-step-1。按既有排除口径，无新增机械错误；这些排除不代表已经冻结或 D8 已经通过。191 条人工判断提示保留。

## 身份与证据

- Blueprint 原始字节 SHA-256：`2d6efbe759fa40202a385eca53dec8cb2250930e1574c3b7c424d686af790ec9`。
- snapshot_sha256：`dc6953587e95044854b914447effacaaa9edc9187b2a63fa4315dd999238a886`，由原 snapshotOf 与 JCS 计算；schema 解析成功。
- deprecated-after.json：扫描逐处记录。
- offline-report.json、online-report.json：完整检查报告。公开副本仅将 file 和 offline.path 的执行位置统一为受审文件的仓库相对路径，检查条目及时间不变。
- checker-identity.json、snapshot-identity.json、RESULT.json：固定检查器身份、当前输入身份及真实退出码和时间。

本轮未执行 D7 独立冷读、D8 round3、实际插件或 9 个回归用例；没有作冻结或交付通过判断。[D8 round3 提示词](../../d8/round3/PROMPT.md)仅含 wr-gates。
