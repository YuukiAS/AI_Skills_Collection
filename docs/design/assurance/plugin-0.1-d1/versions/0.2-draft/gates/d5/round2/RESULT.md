# D1 定向修正与 D5 重跑结果

D6 的 3 项 blocking 和 D8 的 2 处歧义已按本轮 D1 裁决改写，废弃语义扫描从 10 处残留降至 0。D6/D8 第 2 轮只准备提示词，尚未实际执行；最终判断仍由 Claude 以 D1 身份裁决。

## 修改清单

- `role-D1.description` 改为将冻结审阅内容写入 Blueprint 的 `freeze-review` 节点组。
- `role-D6.description` 改为核对 `freeze-review` 节点内容与设计一致。
- `gates.terminal.mechanism` 和 `wr-gates.technical.action` 同步差异范围：D6 按节点自身字段变化，本轮 62 个；D8 按读者单位文字变化，并保留既有受影响相邻单位规则。
- 新增 `tools/scan_deprecated_semantics.py`，列出修订依据、删除/改名概念及旧回归数；在 D6/D8 之前作为 D5 的一部分运行。
- `wr-gates` 明确四关整体完成条件：D5 机械检查通过（快照差异与待 D8 项除外）、D6 无 blocking、D7 全部 9 个回归用例通过、D8 全部受审单位复述正确；任一关有 blocking 即未完成。
- `supp-clarify-0.2` 明确影响当前设计的用户决定须在进入设计前关闭；用户明确接受假设推进时，记录假设、接受依据、核实负责人和核实时点，冻结审阅时逐条复查。同步 `clarify` 正文、验收条及其验收器镜像，避免只改读者材料。
- 当前证据摘要中旧批准载体、旧回归数和定位改为 §30；登记其固定公开来源。同步 SPEC、REVISION_0.2_PLAN、MERGE_DECISIONS §30 的对应规则，以及验收清单文字与来源哈希。

逐字段完整前后文字见 `changes.json`（17 个 Blueprint 字段/来源条目）。`versions`、`versions/0.1/`、原 0.1 冻结说明和原关卡结果均未改。

## 废弃语义残留逐处记录

| JSON Pointer | 首跑残留数 | 修正 |
|---|---:|---|
| `/nodes/1/children/0/children/0/description` | 1 | D1 改为写入 freeze-review |
| `/nodes/1/children/0/children/5/description` | 1 | D6 改为核对 freeze-review |
| `/nodes/1/children/2/terminal/mechanism` | 1 | D6/D8 按实际差异定范围，加入前置扫描 |
| `/evidence/10/proves` | 5 | 按 §30 更新批准载体、回归数及分组，保留仍有效决定 |
| `/evidence/10/sources/0/locator` | 1 | 当前依据改为 §30 |
| `/walkthroughs/3/steps/1/technical/action` | 1 | 同步 gates 范围和前置扫描 |

扫描覆盖全部 62 个节点自身字段、走查和当前证据文字，排除冻结版本历史；共扫描 8062 个字符串。首跑 10 处，修正后 0。39 处明确删除说明或准确历史引用按逐短语规则保留；稳定机器 ID 未改名。扫描不声称能穷尽任意同义改写。

在本设计目录运行：

```sh
python tools/scan_deprecated_semantics.py --report versions/0.2-draft/gates/d5/round2/deprecated-after.json
```

`deprecated-before.json` 与 `deprecated-after.json` 保存每一处匹配、位置及修订依据；`verification.json` 保存旧稿失败、新稿通过、注入废弃语义后失败、同字段删除说明不掩盖正向残留、历史排除及身份/提示词核对等 43 项机械核对结果。

## D5 结果与限制

固定检查器：`YuukiAS/Asteria-Blueprint@229e1736f445bdecffd84773ad543e5f452d65df`，15 个检查器/schema/包文件哈希与原固定版本一致，没有修改检查规则。

离线和在线均实际检查 62 个节点，schema 解析成功；在线 `unresolved=0`，没有新增机械错误。按本轮 D1 口径，排除快照差异与待 D8 项后 D5 通过，新增扫描零残留。

原始退出码离线、在线均为 **1**，没有改写成零：原报告仍有 1 条当前草稿与冻结历史差异，以及 5 条当前文字尚未登记读者通过记录。191 条需相应角色判断的提示保留。未造冻结、批准或读者记录，已返回的首轮 D8 记录仍由 D1 正式登记。

首次运行发现来源映射分隔符、链接工具路径及新增文案的句数/来源登记问题，修正后重跑；本目录公开报告均来自最终候选。原始首次日志仅留机器本地，不发布本机路径或其他私有内容。

证据：`RESULT.json`、`offline-report.json`、`online-report.json`、`checker-identity.json`、`snapshot-identity.json`。

## 定向复核材料

- D6：`gates/d6/round2/PROMPT.md`，内嵌修改前后、三个目标节点的相关正文、直接引用上下文和扫描实现；不再次全量追问 62×7 项。
- D8：`gates/d8/round2/PROMPT.md`，只含 `wr-gates`、`supp-clarify-0.2` 两个读者单位。`wr-gates` 使用检查器 readerText 的真实当前文字，`units.json` 保存逐单位哈希；补充澄清单位明确标为 supplemental，未伪造 Blueprint 节点。
- 两份提示词均规定：只报告改动位置引入的问题；改动之外的新发现记为 non-blocking 留给 0.3，除非与改动直接矛盾。均自包含，结果直接写回对应 round2 路径。
- `gates/D8_PROMPT.md` 已同步到相同 round2 提示词，避免旧入口交出过期文字。

当前 Blueprint 原始字节 SHA-256：`d7c4055ca4485862230e8a3ab9edb4fc55e1bba4ca18c4a0e12f44d330ca8e9d`。

当前 `snapshot_sha256`：`3efb23ecf3d77ba81a1243d6d7b442f9878f876459941fae9c083a064b6a3b8d`。

本轮只完成修正、机械检查和复核准备。未运行 D6/D8 第 2 轮、实际插件回归、冻结或发布。

## 提交状态

本轮尝试暂存时，worktree 的 Git 管理目录无法创建 `index.lock`，返回 `Read-only file system`。因此尚未 commit、push；全部修正和证据仍保留在本工作树。未尝试更换索引、旁路提交或扩大 Git 权限。
