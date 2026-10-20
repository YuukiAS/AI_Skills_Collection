# Clear Writing 0.6 执行就绪计划 v0.1

日期：2026-10-20
状态：DRAFT_FOR_EXECUTION_READY_CRITIC
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
2. 上述六个 canonical route 目录
3. `scripts/codex_marketplace_config.json` 中 `writing-style` 元数据与两段版本
4. `assets/codex/plugin-icons/writing-style/composer.svg`

正式输出目录：

`private/exports/clear-writing--single-entry-artifact-finalization/wrapper/<personal-version>/`

正式 ZIP：

`private/exports/clear-writing--single-entry-artifact-finalization/clear-writing-<personal-version>.zip`

公开、无敏感信息的构建回执：

`results/clear-writing--single-entry-artifact-finalization/wrapper/BUILD_RECEIPT.json`

### 4.4 route projection 形式

六项 route 不作为六个可发现 Skill 再打包。builder 对每个 canonical route 目录做完整投影：

`<source-route>/SKILL.md -> skills/clear-writing/references/routes/<route>/ROUTE.md`

同一 source route 目录下其余 `references/`、`scripts/`、`assets/`、`evals/` 等支持文件保持相对目录结构复制到：

`skills/clear-writing/references/routes/<route>/...`

除把顶层 `SKILL.md` 文件名确定性改为 `ROUTE.md` 外，不改文件正文。这样 route 内原有相对引用仍可解析，同时插件根 `skills/` 下只有 `clear-writing/SKILL.md` 一个可发现 Skill。

builder 必须 fail closed：

- source route 缺失；
- source route 出现未预期的第二个 `SKILL.md`；
- source 文件读取失败；
- 投影后的 `ROUTE.md` 内容哈希与 source `SKILL.md` 内容哈希不同；
- 任一支持文件哈希不一致；
- 生成包出现 `skills/<other>/SKILL.md`；
- manifest version / name / display name 与冻结配置不一致。

`BUILD_RECEIPT.json` 至少记录每个 source path、source SHA-256、generated path、generated SHA-256、archive SHA-256、生成脚本版本/commit 和完整文件 allowlist。它只证明 source/generated 一致，不证明写作质量。

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
WRAPPER_ARCHIVE_SHA256=<sha256>
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

G4 不增加新生成任务，复用 G2 文档/mixed 输出、G3 source/final pair 以及后续 G6 source/final pair做独立 source-to-final 对照。

必须检查：事实、数字、公式、引用、否定、条件、不确定性、权限、完成状态、正式名称、路径、命令、字段和机器字符串。

任一过度主张、权限/状态漂移或受保护内容错误即 FAIL。

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
3. deterministic build/parity/tests。
4. replay 原有 KR-WEB-01..09 与 should-not-change；本次 Reader Guide只作为 G3，不提前调参。
5. required repository / Marketplace CI。
6. 冻结 final candidate 与 0.6 version/changelog candidate。
7. 下载并保存当前 Personal Plugin 0.5.0 archive/current_release_id 作为恢复依据。
8. 一次性更新现有 Personal Plugin 到 0.6.0，运行 G1。
9. G1 PASS 后运行 G2。
10. G2 PASS 后运行 G3。
11. G3 PASS 后完成 G4 source/final adjudication和 G5 final-identity复核。
12. G1-G5 全 PASS 后，Critic 做 final-evaluation preflight并冻结 G6 exact input。
13. 运行唯一 G6。
14. 独立最终产物审查。
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

## 15. Personal Plugin mutation 与恢复

正式更新前必须保存：

- current plugin metadata；
- current release ID；
- 0.5.0 complete archive；
- archive SHA-256；
- complete file list。

若 `update_plugin` 在 mutation 前拒绝，记录失败并停止，0.5.0 不变。

若 0.6.0 update 成功但 G1/G2/G3 证明新 wrapper 破坏正常使用，本任务停止，repository 0.6 不发布。由于当前 Plugin Creator 不提供直接“切回旧 release”动作且拒绝 lower version，恢复方案只能是一次有界 forward restore：

- 用保存的 0.5.0 archive 内容恢复旧行为；
- manifest personal version 改为 `0.6.1`；
- update 同一 plugin identity；
- 删除 0.6-only `skills/clear-writing/**`、root `plugin.json` 和 root `assets/app-facing.svg`，重新上传 0.5.0 所需文件；
- 回读并验证除 manifest personal version 外，行为文件与保存的 0.5.0 archive 一致；
- 标记 `CLEAR_WRITING_0_6_RELEASE=FAILED_RESTORED`；
- 中央 `writing-style 0.6` 不发布；
- 回 Planner。

不得为了保住 0.6.0 版本号而留下已知坏的正式插件。

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
- G6 qualitative fail -> release fail；不得追加 fresh case。
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
- G1-G6 可执行且不过重；
- G3/G6 的 normal-entry 和 full-artifact 证据无法被 helper替代；
- budgets/retry/stop/recovery明确；
- final candidate identity与版本路径明确；
- 失败后的 Personal Plugin恢复可行；
- 没有产品/平台选择留给 Codex。

Critic PASS 仍不等于用户授权。用户随后必须发送批准后的 Kickoff 才可实施。
