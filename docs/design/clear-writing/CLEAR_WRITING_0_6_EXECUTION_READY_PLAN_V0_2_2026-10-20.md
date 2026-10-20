# Clear Writing 0.6 执行就绪计划 v0.2

日期：2026-10-20
状态：DRAFT_FOR_EXECUTION_READY_CRITIC
Supersedes：`CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_1_2026-10-20.md@a6625909c0b5a0bf61904e6c7bc97ecf308f7bee`
返修范围：仅关闭 `CW06-ER01 / CW06-ER05 / CW06-ER08 / CW06-ER09`，其他已接受架构保持不变。
角色：Planner
目标仓库：`YuukiAS/AI_Skills_Collection`
目标插件：`writing-style / Clear Writing`
任务键：`clear-writing--single-entry-artifact-finalization`
设计分支：`design/clear-writing--single-entry-artifact-finalization`
批准 Proposal：`docs/design/clear-writing/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_PROPOSAL_V0_1_2026-10-20.md@3eefc626b86566113125a06fc6046a2bec1eafb2`
设计阶段 Critic：用户转交 `DECISION=PROCEED / ROOT_CAUSE_ASSESSMENT=PARTIALLY_SUPPORTED / SINGLE_ENTRY_DECISION=ACCEPT / ARTIFACT_BINDING_DECISION=ACCEPT / GATE_MATRIX_DECISION=ACCEPT`
跟踪：Issue `#13`
当前正式基线：`main@aa2e6ade13cf6e038a69ec4a2b5fbe318bebed39`
当前正式版本：repository `5.5.1` / `writing-style 0.5` / ChatGPT Personal Plugin `0.5.0`

> 本文件不是执行授权。只有同一独立 Critic 对本完整包给出唯一一次 `PASS` 且同时给出 `READY_FOR_CODEX=YES`，并且用户随后发送批准后的 Kickoff，才允许实施。

## 1. 本轮冻结了什么

总体架构不再重开。0.6 继续采用：ChatGPT Personal Plugin 只暴露一个顶层 `clear-writing` Skill；六项专业能力继续由现有 canonical source 拥有；Codex Marketplace 继续直接暴露六项 Skill；wrapper 只负责交付对象识别、路线组合、候选先于写入、写入后回读和逐对象完成状态。

本轮新增冻结的是此前 Proposal 留给执行包的问题：wrapper 的唯一 source ownership、确定性构建、最终包结构、旧路径删除、manifest/capability 现实检查、GitHub 最终产物绑定、对象级状态、Gate 的 exact execution contract、预算、失败恢复、版本与 release closure。

不新增 MCP、App、外部模型、后台服务、数据库、状态机或长期 ledger。

## 2. 当前现实核验

Planner 重新核对了当前 `main` 的仓库规则、Planner/Critic 1.7、Capability Gate Policy 1.2、维护看板、真实任务 refinement 和版本规范；`main` 仍为 `aa2e6ade13cf6e038a69ec4a2b5fbe318bebed39`。

Plugin Creator 当前回读：

- Clear Writing：`writing-style 0.5.0`，USER/PRIVATE，只有 `.codex-plugin/plugin.json`，顶层暴露六个 Skill。
- Project Instructions Editor：`0.2.8`，USER/PRIVATE，存在 root `plugin.json` + `.codex-plugin/plugin.json`，顶层只有一个 `project-instructions-editor` Skill。

PIE 只作为已接受包装参考。它不能证明 `Interactive` 本身带来正确路由，也不能证明 Clear Writing 单入口一定成功。

OpenAI 当前官方资料确认：Skill 由名称/描述进入选择，完整说明在匹配或直接调用时加载；一个插件可以有一个或多个 Skill；Skill 可以在已有工具足以完成任务时指导宿主模型调用工具；MCP 才提供其自身控制的数据/认证/动作边界。官方没有承诺“选择一个多 Skill 插件后，所有 Skill 会全部按固定顺序加载”。

因此本计划把 0.6 定义为 **skills-only 工作合同改进**，不声称获得不可绕过的发送前 Hook 或事务能力。

## 3. 实施范围

允许修改的 production / distribution 范围：

- `packaging/chatgpt/writing-style/**`
- `scripts/build_clear_writing_chatgpt_wrapper.py`
- `skills/writing/core/{writing-fidelity,response-clarity,product-ui-copy,scientific-prose,scientific-rewrite,chinese-prose}/**`，仅当已知失败证明 canonical 专业规则本身确有缺口；默认不改
- `scripts/codex_marketplace_config.json` 中 `writing-style` 的正式版本/必要入口元数据
- generator 产生的 `plugins/codex/plugins/writing-style/**`
- `profiles/codex-writing-style.json`
- 与本轮直接相关的 tests、results、plugin changelog、root release metadata

默认实现应只新增 ChatGPT wrapper source/builder/test，并保持六项专业 Skill 正文不变。若 Executor 发现必须改变六项专业语义，停止并回 Planner；不能借本任务顺手扩写。

明确不改：Research Authoring、Presentations、Statistical Modeling、Scientific Visualization、PIE、Mica、Project setting、Bridge Kit。

## 4. ChatGPT wrapper 的唯一 source ownership

### 4.1 canonical source

ChatGPT surface adapter 的唯一人工维护源码冻结为：

`packaging/chatgpt/writing-style/clear-writing/SKILL.md`

它只允许拥有：

- 枚举本轮全部交付对象；
- 为每个对象选择已有 route；
- 组合必要 route；
- 规定候选必须先于外部写入；
- 规定写入后回读；
- 逐对象给出准确完成状态；
- 在无法完成时 fail closed。

它不得复制六项专业 Skill 的完整写作规则，不得做科研/统计/视觉/医学/生物学专业判断。

### 4.2 六项 canonical route source

唯一专业来源仍为：

- `skills/writing/core/writing-fidelity/`
- `skills/writing/core/response-clarity/`
- `skills/writing/core/product-ui-copy/`
- `skills/writing/core/scientific-prose/`
- `skills/writing/core/scientific-rewrite/`
- `skills/writing/core/chinese-prose/`

### 4.3 确定性构建脚本

新增且冻结：

`scripts/build_clear_writing_chatgpt_wrapper.py`

输入：

1. `packaging/chatgpt/writing-style/clear-writing/SKILL.md`
2. 六个 canonical route 目录：
   - `skills/writing/core/writing-fidelity/`
   - `skills/writing/core/response-clarity/`
   - `skills/writing/core/product-ui-copy/`
   - `skills/writing/core/scientific-prose/`
   - `skills/writing/core/scientific-rewrite/`
   - `skills/writing/core/chinese-prose/`
3. `docs/provenance/WRITING_SKILL_REPOS_2026_07_28.md`，只作为 `scientific-prose` 已有 provenance locator 的 package-local 支持文件，不成为第二份专业规则 source
4. `scripts/codex_marketplace_config.json` 中 `writing-style` 元数据与两段版本
5. `assets/codex/plugin-icons/writing-style/composer.svg`

正式输出目录：

`private/exports/clear-writing--single-entry-artifact-finalization/wrapper/<personal-version>/`

正式 ZIP：

`private/exports/clear-writing--single-entry-artifact-finalization/clear-writing-<personal-version>.zip`

公开、无敏感信息的构建回执：

`results/clear-writing--single-entry-artifact-finalization/wrapper/BUILD_RECEIPT.json`

### 4.4 route portability 审计与唯一 projection transform

Planner 已对六个 canonical route 当前 `main@aa2e6ade13cf6e038a69ec4a2b5fbe318bebed39` 的 `SKILL.md` 及其 runtime support files 做 package-path 审计。结论：

- `writing-fidelity`：只引用同目录 `assets/app-facing.svg`、`references/failure-summary.md`；保持相对目录即可。
- `response-clarity`：只引用同目录 icon；无 repo-root runtime locator。
- `product-ui-copy`：只引用同目录 icon；无 repo-root runtime locator。
- `scientific-prose`：同目录 `references/*` 可直接投影，但存在一个 repo-root provenance locator：`docs/provenance/WRITING_SKILL_REPOS_2026_07_28.md`。
- `scientific-rewrite`：存在一个 repo-root helper locator：`skills/writing/core/scientific-rewrite/scripts/rewrite_support.py`。其中 `scripts/run_fedfisher.sh`、`configs/mm_fedfisher.yaml`、`results/<task_key>/*` 等只是正文举例或读者材料中的可保留路径，不是 wrapper runtime locator，不得误改。
- `chinese-prose`：`references/chinese-prose-checklist.md`、`references/source-notes.md` 与 icon 都是相对 locator；`TODO.md` 属于 maintenance 文档，明确不进入 Personal Plugin runtime payload。

唯一允许的 transform 版本冻结为：

`CW06_ROUTE_PROJECTION_V1`

只允许以下 exact literal replacement；当前 source 中每条 token 的预期出现次数均为 1：

| source file | exact source token | exact generated token | expected count |
|---|---|---|---:|
| `skills/writing/core/scientific-rewrite/SKILL.md` | `skills/writing/core/scientific-rewrite/scripts/rewrite_support.py` | `skills/clear-writing/references/routes/scientific-rewrite/scripts/rewrite_support.py` | 1 |
| `skills/writing/core/scientific-prose/SKILL.md` | `docs/provenance/WRITING_SKILL_REPOS_2026_07_28.md` | `skills/clear-writing/references/routes/scientific-prose/references/provenance/WRITING_SKILL_REPOS_2026_07_28.md` | 1 |

除这两条 literal replacement 外，route 专业正文不允许任何变换。

### 4.5 projection 输出和无语义漂移证明

每个 canonical `SKILL.md` 生成：

`skills/clear-writing/references/routes/<route>/ROUTE.md`

同 route 的 runtime support directories `references/`、`scripts/`、`assets/`、`evals/` 按原相对结构复制到 route 目录；maintenance-only 文件（当前明确包括 `skills/writing/core/chinese-prose/TODO.md`）不进入包。

额外 provenance 文件逐字节复制到：

`skills/clear-writing/references/routes/scientific-prose/references/provenance/WRITING_SKILL_REPOS_2026_07_28.md`

builder 必须逐项 fail closed：

1. 任一 transform source token 的出现次数不是冻结值；
2. generated token 目标路径不存在；
3. transform 后仍残留对应 source token；
4. 对 transformed `ROUTE.md` 做 inverse transform 后，字节不等于 canonical `SKILL.md`；
5. 对未 transform 的 `ROUTE.md`，字节不等于 canonical `SKILL.md`；
6. support file 不是 byte-identical copy；
7. provenance copy 不是 byte-identical；
8. 生成包出现除 `skills/clear-writing/SKILL.md` 外的可发现 `SKILL.md`；
9. 任何生成后的 route reference/support path 不存在。

`scientific-rewrite` 的 helper 仍属于当前 heavy-route completion contract，因此生成后的命令只能指向真实 package-local：

`skills/clear-writing/references/routes/scientific-rewrite/scripts/rewrite_support.py`

如果 ChatGPT runtime 无法实际使用该 package-local helper，则不得静默跳过并声称 heavy route 完成；对应长文 route Gate 失败并停止。

`BUILD_RECEIPT.json` 必须记录每个 source path、source SHA-256、generated path、generated SHA-256、`transform_rule_version=CW06_ROUTE_PROJECTION_V1`、实际应用的 transform 条目/计数、support-file parity、archive SHA-256 和完整文件 allowlist。它只证明 projection/parity，不证明写作质量。

### 4.6 deterministic ZIP identity

唯一 archive 规范冻结为：

`CW06_DETERMINISTIC_ZIP_V1`

builder 必须：

- 只写 file entry，不写 directory entry；
- 以 POSIX 相对路径按字节序升序写入；
- 使用 `ZIP_STORED`，不压缩；
- 每个 entry 固定 `date_time=(1980,1,1,0,0,0)`；
- `create_system=3`；
- `external_attr=(0o100644 << 16)`；
- `internal_attr=0`；
- entry `extra=b""`、`comment=b""`；
- archive comment 为空；
- 不写 wall-clock、host、uid/gid 或环境相关 metadata。

同一 source tree 连续 build 两次的 **raw ZIP bytes 必须 byte-identical**。任何 raw byte drift 都是 build FAIL。

`wrapper_archive_sha256` 唯一定义为对上述 exact raw ZIP bytes 计算普通 SHA-256；`BUILD_RECEIPT.json` 记录同一个值，不再存在“固定 timestamp 或 canonical hash 二选一”。

## 5. Personal Plugin 最终包结构

最终 0.6.0 包允许的根结构：

```text
plugin.json
.codex-plugin/plugin.json
assets/app-facing.svg
skills/clear-writing/SKILL.md
skills/clear-writing/references/routes/writing-fidelity/**
skills/clear-writing/references/routes/response-clarity/**
skills/clear-writing/references/routes/product-ui-copy/**
skills/clear-writing/references/routes/scientific-prose/**
skills/clear-writing/references/routes/scientific-rewrite/**
skills/clear-writing/references/routes/chinese-prose/**
```

`assets/app-facing.svg` 必须由 `assets/codex/plugin-icons/writing-style/composer.svg` 逐字节复制，不搜索、不重画图标。

两个 manifest：

- name = `writing-style`
- Personal Plugin version = `0.6.0`
- displayName = `Clear Writing`
- USER / PRIVATE identity 保持
- no MCP / no App / no hook
- root `plugin.json` 使用 portable Agent Plugins schema；
- `.codex-plugin/plugin.json` 作为 compatibility manifest；
- 两者的 OpenAI interface 元数据必须一致；
- 两者均只指向 root `skills/`。

## 6. 0.5.0 -> 0.6.0 exact delete_paths

Plugin Creator 是 overlay update； omitted files 会保留。因此更新正式 Personal Plugin 时必须一次性传入以下 exact `delete_paths`：

```text
.codex-plugin/assets/composer.svg
.codex-plugin/assets/logo.svg
skills/fidelity/SKILL.md
skills/fidelity/assets/app-facing.svg
skills/fidelity/evals/trigger_queries.json
skills/fidelity/references/failure-summary.md
skills/product-ui-copy/SKILL.md
skills/product-ui-copy/assets/app-facing.svg
skills/product-ui-copy/evals/trigger_queries.json
skills/response-clarity/SKILL.md
skills/response-clarity/assets/app-facing.svg
skills/response-clarity/evals/trigger_queries.json
skills/sci/SKILL.md
skills/sci/assets/app-facing.svg
skills/sci/evals/trigger_queries.json
skills/sci/references/scientific-report-checklist.md
skills/sci/references/source-notes.md
skills/scientific-rewrite/SKILL.md
skills/scientific-rewrite/assets/app-facing.svg
skills/scientific-rewrite/scripts/rewrite_support.py
skills/zh/SKILL.md
skills/zh/assets/app-facing.svg
skills/zh/evals/trigger_queries.json
skills/zh/references/chinese-prose-checklist.md
skills/zh/references/group-meeting-chinese-report-prompt.md
skills/zh/references/source-notes.md
```

正式 mutation 前必须再次 `get_plugin_files`。若 current release ID、版本或 file list 与上述 0.5.0 基线漂移，停止，不自行重算删除清单。

更新后必须逐文件回读，确认：

- 旧路径全部不存在；
- root 只有一个 Skill 入口；
- manifest 为 0.6.0；
- plugin identity 未变；
- scope/discoverability 未变；
- generated route hashes 与 BUILD_RECEIPT 一致。

## 7. manifest / capability 的无副作用现实探针

本轮不创建临时 personal plugin，因为当前 Plugin Creator surface 没有可验证的“删除已创建 personal plugin”动作，创建临时 plugin 会留下不可逆 inventory 垃圾；也不允许临时修改正式 `writing-style` 再回滚。

因此冻结 `P0_PACKAGE_REALITY_PROBE` 为 **只读现实探针**：

输入：

1. Plugin Creator 回读当前 PIE 0.2.8；
2. Plugin Creator 回读当前 Clear Writing 0.5.0；
3. OpenAI 当前 portable plugin / skills 官方文档；
4. 本 repo 当前 plugin-json spec；
5. 0.6 本地生成 candidate 的两个 manifest。

成功证据：

- 当前 PIE 实际被 Plugin Creator 接受为 root `plugin.json` + compatibility manifest + 单 Skill；
- portable root manifest 是当前官方推荐入口；
- 当前 `Interactive` 值被现有 PIE 实际接受；
- 0.6 candidate 通过本地 schema/路径检查；
- 两 manifest 元数据一致。

冻结决定：

- 0.6 两个 manifest 使用 `capabilities: ["Interactive"]`，仅作为“当前实际接受的单入口 skills-only 包装形态”；
- **不得**声称 `Interactive` 导致正确路由或比 `Skills` 更可靠；
- 候选是否真的能显式选择并只暴露单 Skill，由 `CW06-G1` 真实 Web/Plugin Creator 回读证明。

P0 失败条件：PIE 当前包不再可读/不再是该结构、官方 schema 与候选冲突、或当前 Plugin Creator metadata 不再接受该字段。失败即停止在 production mutation 之前，回 Planner。

P0 不产生临时 plugin，因此无需清理。

## 8. 0.6 正式 external-artifact claim

为了不把 GitHub Gate 外推成所有文件系统能力，0.6 正式外部最终化只承诺：

**GitHub repository UTF-8 text file，通过当前已连接 GitHub connector 可读、可写、可回读。**

0.6 不把 Google Drive、本地用户上传文件、Notion 或其他 surface 纳入“已证明的 external finalization”正式 claim。它们以后必须各自做真实 Gate；本轮即使宿主临时存在相应工具，也只能按一般候选输出处理，不能写进 0.6 capability claim。

## 9. GitHub 外部最终产物绑定合同

对一个 GitHub EXTERNAL_DOCUMENT，按以下顺序：

1. 使用 GitHub `fetch_file(repo,path,ref)` 获取完整 UTF-8 内容和当前 blob SHA。
2. 绑定 `TARGET_IDENTITY = repo + writable branch + path + blob_sha`。若用户给的是 immutable commit，只能读取；写入必须有本任务预先授权的 writable branch。
3. 生成完整终审 candidate，并计算 `candidate_sha256`。
4. 写入前再次 `fetch_file` 同一 branch/path；blob SHA 必须仍等于绑定值。
5. 一致时使用 GitHub `update_file`，传当前 blob SHA、完整 candidate、writable branch。
6. 记录返回的 `commit_sha` 与 `content_sha`。
7. 立即 `fetch_file` 同一 branch/path 回读。
8. PASS 必须同时满足：
   - 回读 blob SHA == `content_sha`；
   - 回读 UTF-8 内容逐字节 == candidate；
   - branch/path 未改变。
9. 只有此时该对象可标为 `ARTIFACT_FINALIZED`。

失败状态：

- 全文不可取得：`TARGET_SOURCE_INCOMPLETE`，禁止生成替代全文并禁止写入。
- 写前 blob SHA 漂移：`TARGET_IDENTITY_DRIFT`，禁止写入。
- 无写权限或 update 被拒绝：`ARTIFACT_NOT_WRITTEN`；可以给完整 candidate，但不能声称已修改目标。
- update 已返回成功但回读失败、回读内容不等或 identity 不一致：`ARTIFACT_FINALIZATION_UNVERIFIED`。
- 完整 read/write/readback 成立：`ARTIFACT_FINALIZED`。

Skill 只是规定宿主应怎样使用已有 connector；它没有事务 Hook。任何 connector 权限提示仍服从平台。

## 10. 对象级临时工作合同

单次请求内可有多个临时 target：

- `CHAT_RESPONSE`
- `INLINE_DOCUMENT`
- `EXTERNAL_DOCUMENT`
- `PRODUCT_UI_COPY`
- `MACHINE_PAYLOAD`

它们只存在于本轮推理，不写入持久 schema、数据库或 ledger。

最低规则：

- 一个请求可同时有多个 reader-facing target；
- 每个 target 独立选择 route、独立最终化、独立报告状态；
- `CHAT_RESPONSE` 的清楚不能证明 `EXTERNAL_DOCUMENT` 已终审；
- pure exact-only `MACHINE_PAYLOAD` 不改字节内容；
- mixed output 只改自然语言层；
- 读取不到完整目标，不以摘要/旧版本代替；
- 无法写入，不声称已修改；
- 写入后没有成功回读，不声称 finalization complete。

路由固定为：

- 普通聊天 -> `response-clarity` + 必要 fidelity；
- 中文正式文档局部/终审 -> `writing-fidelity -> chinese-prose`；
- 中文/中文主导长技术或科研结构重写 -> `writing-fidelity -> scientific-rewrite -> chinese-prose final pass`；
- 英文科研 -> `writing-fidelity -> scientific-prose`；
- UI 微文案 -> `writing-fidelity -> product-ui-copy`；
- exact-only -> 保持原样。

## 11. final candidate 冻结

真实 Web 前必须先完成 implementation、source/generated parity、known regression 和 required CI。

然后形成唯一 candidate identity：

```text
SOURCE_COMMIT=<exact commit>
WRITING_STYLE_VERSION=0.6
PERSONAL_WRAPPER_VERSION=0.6.0
WRAPPER_ARCHIVE_SHA256=<SHA-256 of exact raw deterministic ZIP bytes>
ROUTE_PROJECTION_RULE_VERSION=CW06_ROUTE_PROJECTION_V1
ZIP_SPEC_VERSION=CW06_DETERMINISTIC_ZIP_V1
BUILD_RECEIPT_SHA256=<sha256>
CODEX_WRITING_STYLE_TREE_SHA=<tree/blob identity>
```

candidate 冻结后，仅允许写 `results/clear-writing--single-entry-artifact-finalization/**`、必要 tracking copy 和经规则允许的 review evidence。任何 candidate-defining source、builder、manifest metadata、六项 canonical route、profile 或 generated Codex payload 变化都会使已有 `CW06-G1..G6` 证据失效。

## 12. Capability Gates 最终合同

### CW06-G1 — 单入口与正式 identity

前置：final candidate frozen；P0 PASS。

正常入口：更新现有 USER/PRIVATE Clear Writing plugin 到 exact 0.6.0 archive，使用 update_plugin + current expected_release_id + 冻结 delete_paths。

证据：

- Plugin Creator current release identity；
- 完整 file list 回读；
- 两 manifest 回读；
- 旧 0.5 顶层 Skill 路径全部 missing；
- ChatGPT runtime Skill inventory 中 `writing-style` 只出现 `clear-writing`；
- 新鲜 ChatGPT Web conversation 中显式选择 Clear Writing 后完成一个只需普通回复的自然请求。

失败：任何旧顶层 Skill 残留、第二个同名 plugin、identity/scope 漂移、显式选择不能进入新入口，均 FAIL。

### CW06-G2 — 路线覆盖与 should-not-change

所有 prompt 均显式选择 Clear Writing，但自然用户文字不得出现内部 Skill 名。每项一次 model answer；只有无模型输出的基础设施失败允许同输入最多重试一次。

冻结任务族：

1. 普通聊天解释：使用 `response-clarity/evals/trigger_queries.json` 语义，保留 branch/status/command 精确字符串。
2. 正式中文 Markdown 终审：使用 `chinese-prose/evals/trigger_queries.json` 的“中文 Markdown 终稿、第一屏说人话、机器字段后置”任务。
3. 中文长技术结构重写：使用一个已暴露的 public-safe 长文 fixture，要求重新组织、保留数字/公式/引用/限制，不出现内部 route 名。
4. English scientific prose：使用 `scientific-prose/evals/trigger_queries.json` 的 evidence-bounded result paragraph。
5. UI 文案：使用 `product-ui-copy/evals/trigger_queries.json` 的设置页/权限说明任务。
6. exact-only：固定 JSON，仅要求原样返回。
7. mixed：自然中文解释 + 固定 JSON/命令块，机器内容必须逐字不变。
8. necessary-long-answer：使用 KR-WEB-08/09 的正向深度合同，必要例子、比较、公式直觉和 caveat 不能因清晰化被删。
9. short-answer：一个已经有足够事实的状态问题，回答问题后停止，不扩成架构 memo。

G2 PASS 需要 route 行为与最终质量同时成立；Skill 自述“我用了某 route”不算证据。

### CW06-G3 — 已知 Reader Guide 多产物回归

已知 source：

`YuukiAS/AI_Research_Toolkit@0ff0f43f3b04286273490e4c4870975f4aa7a7f8`
`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_V0_4_READER_GUIDE_20261019.md`

执行时创建专用 Gate branch：

`gate/clear-writing-0.6-reader-guide-regression`

必须先证明该 branch 不存在；若已经存在，停止为 `G3_PRECONDITION_BLOCKED`，不得覆盖未知分支。新 branch 必须从 exact `0ff0f43...` 创建。

同一 ChatGPT Web 请求必须：

- 显式选择 Clear Writing；
- 要求把完整 Reader Guide 改成能让非架构作者理解的中文；
- 要求保留架构事实、状态、版本、路径和真实未完成边界；
- 同时在聊天中解释“改了什么、是否真的写回”。

PASS 必须看到：全文读取 -> 文档 candidate -> GitHub update -> readback -> 完整 final artifact 质量审查；聊天回复只能作为另一个 target 验收，不能代替文档。

若当前 normal ChatGPT Web 无法真实完成这条链，G3 FAIL，立即停止 release path。不得用 Codex helper、脚本或模拟写入替代。

### CW06-G4 — 保真与权限

G4 是 **pre-G6 fidelity gate**，不增加新生成任务，只复用 G2 全部冻结 input/output pairs 与 G3 source/final pair 做独立 source-to-final 对照。G6 不属于 G4 输入，G6 fidelity 也不反向成为 G4 precondition。

必须检查：事实、数字、公式、引用、否定、条件、不确定性、权限、完成状态、正式名称、路径、命令、字段和机器字符串。

任一过度主张、权限/状态漂移或受保护内容错误即 FAIL。G4 PASS 后才允许进入 G6 前置条件检查；G6 自己再做独立 fidelity-first review。

### CW06-G5 — canonical/generated parity 与 Codex compatibility

在真实 Web 前由 final candidate 直接通过：

- builder deterministic two-run byte identity；
- BUILD_RECEIPT source/generated hash parity；
- Personal wrapper package 只有一个可发现 Skill；
- `scripts/codex_marketplace_config.json` 仍有六项 writing-style direct exposure；
- `plugins/codex/plugins/writing-style/**` generator parity；
- `profiles/codex-writing-style.json` 仍包含六项 canonical core skill；
- existing Research Authoring / Presentations / statistical-modeling / scientific-visualization ownership tests/known boundaries不被改写；
- full relevant repository/Marketplace tests。

hash/parity 只能证明分发一致，不证明用户文本质量。

### CW06-G6 — fresh 长技术文档完整任务

G6 只在 G1-G5 全部 PASS、final candidate 和 reviewer rubric 都冻结后执行。

为了保持 fresh，本 execution package **不提前暴露具体文档**。选择协议现在冻结：

- 由同一独立 Critic 在 final-evaluation preflight 选择 exactly one public-safe Chinese or Chinese-dominant long technical document；
- 该文档不得属于 Reader Guide、KR-WEB-01..09、开发 fixture、已知 should-not-change 或本任务调试材料；
- 选择后、第一条 model request 前，冻结 repo/URL、ref/version、全文 SHA-256、exact prompt、ChatGPT surface/model、plugin release identity 到 `results/.../g6/FROZEN_INPUT_MANIFEST.md`；
- 一旦冻结，不得换题；
- candidate 在此之后禁止修改；
- 一个 model answer；仅无输出的基础设施故障允许同输入最多一次 retry；
- Critic 必须直接拿到 source 全文与 final artifact 全文，先审保真，再审读者质量；
- product FAIL 即 release FAIL，不补第二个 fresh 样本；
- 若根据该样本修改产品，该样本永久进入 known regression，后续版本必须另选 fresh。

## 13. 执行顺序

固定顺序：

1. P0 只读 packaging reality probe。
2. 实现 wrapper source、builder、tests；默认不改六项专业规则。
3. `CW06_ROUTE_PROJECTION_V1` portability/parity tests + `CW06_DETERMINISTIC_ZIP_V1` raw-byte reproducibility。
4. replay 原有 KR-WEB-01..09 与 should-not-change；本次 Reader Guide只作为 G3，不提前调参。
5. required repository / Marketplace CI。
6. 冻结 final candidate 与 0.6 version/changelog candidate。
7. 下载并保存当前 Personal Plugin 0.5.0 archive/current_release_id 作为恢复依据。
8. 一次性更新现有 Personal Plugin 到 0.6.0，运行 G1。
9. G1 PASS 后运行 G2。
10. G2 PASS 后运行 G3。
11. G3 PASS 后完成 G4 pre-G6 source/final adjudication；G4 输入仅为 G2 + G3。
12. 完成 G5 final-identity / compatibility 复核；至此 G1-G5 必须全部 PASS。
13. 同一独立 Critic 做 final-evaluation preflight并冻结 G6 exact input。
14. 运行唯一 G6；G6 内部严格先 fidelity、后 reader quality。
15. 独立最终总评只汇总 G1-G5、G4 fidelity 结论和 G6 fidelity+reader-quality 结论，不新增第七个 Gate。
15. 只有全部 required Gate PASS，才进入 repository PATCH release closure、README/changelog/version同步。

不得跳过失败 Gate继续后续。

## 14. Web 预算与重试

正式 Web Gate统一规则：

- surface：ChatGPT Web；
- model：`GPT-5.6 Sol`；若执行时该模型不可选，停止回 Planner，不替换模型；
- 每个冻结 task 默认一个 model answer；
- 只有在没有产生任何模型答案的基础设施故障时允许同输入一次 retry；
- retry 仍使用同一模型、同一插件 release、同一 prompt、同一 source identity；
- 产品质量失败不 retry；
- 不挑赢家；
- 不在失败后改 rubric；
- 不在看过 fresh 后换题。

执行前每个 batch 的 input manifest 必须记录 exact plugin release ID、model、surface、prompt SHA256、source identity、attempt budget 和 reviewer rubric hash。

## 15. Personal Plugin mutation 与 forward restore

正式更新前必须保存：

- current plugin metadata；
- current release ID；
- 0.5.0 complete archive；
- 0.5.0 exact file list；
- archive SHA-256；
- file-set SHA-256。

若 `update_plugin` 在 mutation 前拒绝，记录失败并停止，0.5.0 不变，不需要 restore。

### 15.1 restore set 的工具约束修正

Plugin Creator 当前合同同时规定：

- `delete_paths` 只能包含 exact existing file path；
- directory/glob 不允许；
- 同一个 path **不能同时被上传和列入 `delete_paths`**；
- lower version 被拒绝；
- 没有直接 restore-old-release action。

上一轮返修文字同时要求“`RESTORE_DELETE_PATHS = S06 - S05`”和“restore archive 必须包含两个 0.6.1 manifest”。当前 0.5.0 实际 file set 没有 root `plugin.json`，而 0.6.0 有；因此 root `plugin.json` 同时属于 `S06-S05` 又必须在 restore archive 上传。按当前 Plugin Creator 合同，这两个要求不能用一次合法 `update_plugin` 同时满足。

v0.2 不伪造一个会被工具拒绝的调用，而冻结两个 deterministic set，保持原 finding 的恢复意图：

1. `RESTORE_06_ONLY_PATHS.json`
   - `all_06_only_paths = S06 - S05`
   - 严格记录全部 0.6-only exact paths，用于审计；
2. `RESTORE_DELETE_PATHS.json`
   - `delete_paths = (S06 - S05) - R`
   - 其中 `R` 是 forward-restore archive 的 exact file set；
   - 这是实际传给 `update_plugin(delete_paths=...)` 的 tool-valid exact list；
   - 必须证明 `R ∩ delete_paths = ∅`。

这只是解决当前工具“上传与删除同 path 非法”的约束，不改变单入口、版本或恢复架构。Critic 必须在 v0.2 re-review 中专门判断此修正是否正确。

### 15.2 两个 restore set 的生成与验证

final 0.6 candidate build 后、live 0.6 mutation 前：

1. 从保存的 0.5.0 file list 得到 `S05`；
2. 从 exact deterministic 0.6 ZIP 得到 `S06`；
3. 构建 restore archive file set `R`；
4. 生成 `RESTORE_06_ONLY_PATHS.json` 与 `RESTORE_DELETE_PATHS.json`；
5. 所有 path 必须是 plugin-root-relative exact file path，不得含目录项、`*`、`**`；
6. `all_06_only_paths` 每项必须在 `S06` 且不在 `S05`；
7. actual `delete_paths` 每项必须在 current 0.6 package 中存在、不得出现在 restore archive；
8. set 关系必须由 test 机械证明，不由 Executor 手工编辑。

### 15.3 forward restore archive

restore archive 以保存的 0.5.0 **behavior payload** 为准：

- 恢复全部 0.5.0 Skill/support behavior files；
- 恢复旧 `.codex-plugin/assets/*`；
- `.codex-plugin/plugin.json` 只允许把 personal version 改为 `0.6.1`；
- 新增一个 portable root `plugin.json`，其产品 identity/interface 与恢复后的 compatibility manifest 一致，personal version 同为 `0.6.1`，并引用恢复包中真实存在的旧 icon/skills 路径；
- 除这两个 manifest 的 distribution/version 差异外，所有行为文件必须与保存的 0.5.0 archive byte-identical。

因此 restore 后允许的额外 distribution-only 文件只有 root `plugin.json`；它不算新的专业行为 source。

forward restore 调用冻结为：

```text
plugin_id = same writing-style identity
expected_release_id = current live 0.6 release id
archive = deterministic restore archive, personal version 0.6.1
delete_paths = exact RESTORE_DELETE_PATHS.json.tool_delete_paths
```

restore 后完整 `get_plugin_files` / manifest readback 必须证明：

- same plugin identity / USER / PRIVATE；
- 两个 manifest personal version 均为 `0.6.1`；
- 所有 0.6-only clear-writing route files已删除，除 root `plugin.json` 这一 restore archive distribution file；
- 0.5 behavior payload byte-identical；
- no stale 0.6 behavior file；
- central `writing-style 0.6` 未发布。

### 15.4 restore 触发策略

一旦 live 0.6.0 mutation 成功：

- G1/G2/G3/G4/G5/G6 任一 **终止性 PRODUCT FAIL** -> `RESTORE_REQUIRED`；
- 最终独立 artifact review 的终止性 PRODUCT FAIL -> `RESTORE_REQUIRED`；
- bounded infrastructure retry/wait 尚未耗尽，且 release path 能在当前批准流程内继续 -> 暂不 restore；
- infrastructure 在允许的 retry/wait 后使 release path 不能继续 -> **固定选择 restore 到已验证 0.5 behavior**，不得把未完成验收的 0.6.0 留在正式 Personal Plugin 等 Executor 临场判断；
- 若 restore 所需 Plugin Creator 本身不可用，状态固定为 `RESTORE_REQUIRED_BLOCKED_BY_INFRA`：central 0.6 release 立即放弃、所有后续 Gate停止；Plugin Creator 恢复后的唯一下一动作是完成 forward restore，再回 Planner，不得先继续 Gate。

任何 `RESTORE_REQUIRED` 都意味着：

`CLEAR_WRITING_0_6_RELEASE=ABORTED`

central `writing-style 0.6` 不发布。

## 16. 失败和恢复表

- P0 manifest/package reality不成立 -> mutation前停止，回 Planner。
- deterministic build/hash drift -> fail closed，不构建 archive。
- old Skill delete list 与 current release漂移 -> 停止，不自动改 delete_paths。
- connector target unavailable -> `TARGET_SOURCE_INCOMPLETE`。
- connector read-only / write denied -> `ARTIFACT_NOT_WRITTEN`。
- write前 target SHA drift -> `TARGET_IDENTITY_DRIFT`，不写。
- write失败 -> 保留 candidate，记录未写入，不声称 final。
- readback失败/不一致 -> `ARTIFACT_FINALIZATION_UNVERIFIED`。
- G3 normal-entry fail -> 立即停 release path，不继续加 Skill 同义规则，不让 Codex设计 MCP；回 Planner。
- G6 fidelity 或 reader-quality FAIL -> terminal PRODUCT FAIL，触发 forward restore；不得追加 fresh case。
- final independent artifact review terminal PRODUCT FAIL -> 触发 forward restore。
- live mutation 后 infrastructure 在 bounded retry/wait 后无法继续 -> `RESTORE_REQUIRED`；若 Plugin Creator 不可用则 `RESTORE_REQUIRED_BLOCKED_BY_INFRA`。
- candidate-defining source改变 -> 旧 Gate evidence失效，从受影响最早 Gate重跑；G6 已看过则旧 G6 永久失去 fresh 身份。

G3 失败后 Planner 只允许重新提案：收窄正式 claim、使用已有宿主 connector 更受控工作流、或单独设计 App/MCP finalizer。任何架构变化重新 Critic，不继承当前执行批准。

## 17. 版本、README、changelog、Issue #13

当 implementation、known regression、unrelated regression 和 required Gates 全部通过并准备正式交付时：

Repository bump decision: PATCH
Reason: existing Clear Writing gets a compatible user-visible normal-entry/artifact-finalization improvement.

Affected plugins:
- `writing-style: 0.5 -> 0.6`
- all other central plugins: NO_BUMP

Personal Plugin：`0.5.0 -> 0.6.0`。若发生失败后的 forward restore，0.6 正式 release取消，个人 wrapper恢复版可能为 0.6.1，不改变中央 release truth。

Repository 三段版本不得现在猜；正式 release 时根据当时 `origin/release` late-bind。

release closure 必须：

- 更新 `docs/plugin-changelogs/writing-style.md`；
- 更新 root CHANGELOG/VERSION/生成 release metadata；
- 检查 README；
- 如果 README 无需变化，记录 `README checked: no update required`；
- 如果 README 有读者可见修改，必须实际调用正式 Clear Writing 做 affected-region 语言检查，不能只读 Skill 文件。

Issue #13 继续复用。新设计轮次真实生命周期为 `DOING`，Area=`writing-style`，Resolution commit空。0.6 成功不自动关闭 #13，原有 statistical-modeling / scientific-visualization adaptation truth继续保留。

当前 surface 无 GitHub Project 字段修改能力。待 Project-capable AI Skills Maintainer 同步：

```text
Issue #13
Status = DOING
Area = writing-style
Execution anchor = <本完整 execution-ready package commit>
Next action = independent execution-ready Critic review of Clear Writing 0.6 package v0.1
Resolution commit = empty
```

## 18. Critic execution-ready PASS 条件

同一独立 Critic 必须核对本 Plan、Goal、Gate runbook、Kickoff draft 和正式 Critic prompt。只有以下全部成立才可给唯一一次：

```text
PASS
READY_FOR_CODEX=YES
```

- 用户承诺没有缩水；
- source ownership / builder / package shape / delete_paths 已冻结；
- P0 不冒充产品 Gate；
- GitHub 是唯一 external finalization正式 claim；
- G1-G6 可执行且不过重，G4 与 G6 无循环依赖；
- G2-T3 有唯一 repo/ref/path source-delivery；
- route projection 只有 allowlisted portability transform；
- raw ZIP identity 使用唯一 deterministic ZIP spec；
- forward restore 与当前 Plugin Creator overlap/delete 约束一致；
- G3/G6 的 normal-entry 和 full-artifact 证据无法被 helper替代；
- budgets/retry/stop/recovery明确；
- final candidate identity与版本路径明确；
- 失败后的 Personal Plugin恢复可行；
- 没有产品/平台选择留给 Codex。

Critic PASS 仍不等于用户授权。用户随后必须发送批准后的 Kickoff 才可实施。
