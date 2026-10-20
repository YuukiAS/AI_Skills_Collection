# Clear Writing 0.6 Gate 执行包 / Runbook v0.1

日期：2026-10-20
状态：DRAFT_PENDING_EXECUTION_READY_CRITIC
任务：`clear-writing--single-entry-artifact-finalization`
Authority：
- Proposal：`docs/design/clear-writing/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_PROPOSAL_V0_1_2026-10-20.md@3eefc626b86566113125a06fc6046a2bec1eafb2`
- Plan：`docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_1_2026-10-20.md`
- Goal：`docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_1_2026-10-20.md`

本 Runbook 只定义执行合同。当前不得运行任何 live Gate、不得更新正式 Personal Plugin、不得启动 Codex。

## 1. 执行角色与阶段

### Phase A — Codex implementation

只有 execution-ready Critic `PASS / READY_FOR_CODEX=YES` + 用户发送批准 Kickoff 后启动。

Codex 必须显式消费：

- `workflow-core`
- `ai-skills-core`
- `writing-style`

Codex 负责 source、builder、tests、generated parity、known regression、CI、candidate build 和 evidence；不拥有产品架构新决定。

### Phase B — implementation review

标准独立实现审查必须确认：

- diff 与 Plan 一致；
- 六项专业 Skill 默认没有被无授权改写；
- builder/package tests、known regression、CI 真实通过；
- final candidate 可以冻结。

未通过 implementation review，不进入 Personal Plugin mutation。

### Phase C — ChatGPT Web distribution + G1-G5

由长期 Planner thread 在同一用户账号的 ChatGPT Web 使用 Plugin Creator / GitHub connector 执行；不是 Codex helper replay。

### Phase D — final-evaluation preflight + G6

G1-G5 全 PASS 后，同一独立 Critic执行 final-evaluation preflight，冻结唯一 fresh input；随后运行 G6。G6 失败不追加样本。

## 2. P0_PACKAGE_REALITY_PROBE

P0 是只读包装现实检查，不是 capability Gate。

读取并记录：

1. 当前 Clear Writing Personal Plugin metadata/file list/current release；
2. 当前 PIE Personal Plugin metadata/file list/current release；
3. PIE 两 manifest 与唯一 Skill；
4. OpenAI 当前 Plugin packaging / Skills 官方说明；
5. 生成后的 0.6 candidate manifests。

PASS：

- PIE 当前仍实际接受 root `plugin.json` + `.codex-plugin/plugin.json` + `Interactive` + single Skill；
- OpenAI 当前 portable package 仍以 root `plugin.json` 为正式入口；
- candidate manifests 通过 schema/path 检查；
- 两 manifest 的 name/version/interface 一致。

P0 不证明 `Interactive` 有路由因果作用。

P0 FAIL -> `STOP_BEFORE_MUTATION`。

## 3. builder 固定命令

实现后 builder CLI 必须支持：

```bash
python scripts/build_clear_writing_chatgpt_wrapper.py build \
  --expect-plugin-version 0.6 \
  --output-root private/exports/clear-writing--single-entry-artifact-finalization/wrapper/0.6.0 \
  --archive private/exports/clear-writing--single-entry-artifact-finalization/clear-writing-0.6.0.zip \
  --receipt results/clear-writing--single-entry-artifact-finalization/wrapper/BUILD_RECEIPT.json

python scripts/build_clear_writing_chatgpt_wrapper.py check \
  --expect-plugin-version 0.6 \
  --output-root private/exports/clear-writing--single-entry-artifact-finalization/wrapper/0.6.0 \
  --archive private/exports/clear-writing--single-entry-artifact-finalization/clear-writing-0.6.0.zip \
  --receipt results/clear-writing--single-entry-artifact-finalization/wrapper/BUILD_RECEIPT.json
```

同一 source 连续 build 两次必须 archive 解包后的文件字节与 receipt 完全一致。ZIP container timestamp 可以确定性固定；否则比较解包树和 archive canonical hash algorithm，不能因 zip timestamp 伪报 drift。

## 4. deterministic / repository checks

在任何 live Personal Plugin mutation 前必须 PASS：

```bash
python -m unittest tests.test_clear_writing_chatgpt_wrapper
python -m unittest tests.test_skill_runtime_text_audit tests.test_codex_marketplace tests.test_scientific_rewrite
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest discover -s tests -v
git diff --check
```

其中新测试 `tests/test_clear_writing_chatgpt_wrapper.py` 至少断言：

- final package root allowlist；
- only one discoverable `skills/*/SKILL.md`；
- `clear-writing/SKILL.md` 来自唯一 canonical wrapper source；
- six route `ROUTE.md` hashes == six source `SKILL.md` hashes；
- 所有 route support files hash parity；
- old 0.5 top-level paths 不在 candidate archive；
- root/compat manifests version/name/interface一致；
- Codex Marketplace `writing-style` 仍直接暴露六项 source；
- `profiles/codex-writing-style.json` 仍直接列六项 core skills。

## 5. known regression before live Web

继续运行现有 `KR-WEB-01..09` 和四组 should-not-change，全部视为 known regression/positive controls。

要求：

- 绑定同一 implementation candidate；
- 保存完整输出；
- KR-WEB-03/08/09 的正向深度不得被“单入口”修成机械短答；
- exact-only 保持字节精确；
- 不使用 Reader Guide G3 source 做开发调参；
- 不把这些已知样本称为 fresh。

任何 regression FAIL -> implementation阶段修复；修复后重跑受影响 regression + unrelated controls。正式 Personal Plugin 尚未更新，因此此阶段允许正常开发迭代。

## 6. final candidate manifest

implementation review PASS 后写：

`results/clear-writing--single-entry-artifact-finalization/candidate/FINAL_CANDIDATE.json`

至少：

```json
{
  "schema": "CLEAR_WRITING_06_FINAL_CANDIDATE_V1",
  "source_commit": "<sha>",
  "writing_style_version": "0.6",
  "personal_wrapper_version": "0.6.0",
  "wrapper_archive_sha256": "<sha256>",
  "build_receipt_sha256": "<sha256>",
  "codex_writing_style_tree_sha": "<sha>",
  "profile_sha256": "<sha256>",
  "gate_rule_version": "CW06-v0.1"
}
```

生成后 candidate-defining source 只读。后续 `results/**` / tracking evidence 可以增加，但不得改变上述 identity。

## 7. Personal Plugin mutation preflight

正式 update 前：

1. `get_plugin_files` current Clear Writing；
2. 必须仍为：
   - name `writing-style`
   - version `0.5.0`
   - USER / PRIVATE
   - current release == 计划开始时重新读取值
   - exact old file list 与 Plan delete_paths一致；
3. `get_owned_plugin_archive` 保存完整 0.5.0 archive 到 private exports；
4. 记录 archive SHA-256；
5. 若任何 identity/file drift，`STOP_PLUGIN_DRIFT`。

正式 update：

- same plugin ID；
- archive = frozen 0.6.0 candidate；
- expected_release_id = preflight current release；
- delete_paths = Plan exact list；
- 不创建第二个 writing-style plugin。

## 8. CW06-G1

### G1-A Plugin Creator readback

update 成功后立即 `get_plugin_files`：

- version == `0.6.0`；
- USER / PRIVATE；
- plugin ID 与 preflight相同；
- root `plugin.json` 和 compatibility manifest存在；
- `skills/clear-writing/SKILL.md` 存在；
- 0.5 old paths 全部 absent；
- package内唯一 `skills/*/SKILL.md` 是 `skills/clear-writing/SKILL.md`；
- route/generated hashes 与 BUILD_RECEIPT一致。

### G1-B runtime exposure

新开一个 ChatGPT Web conversation，刷新 plugin/skill registry后：

- 直接选择 Clear Writing；
- runtime 可见的 `writing-style` Skill 只允许 `clear-writing`；
- 发送：

```text
我刚跑完测试。先告诉我现在能不能交给审阅者、还缺什么；保留下面三个机器字符串不改：
branch=reviewed/cache--repair
status=WAITING_FOR_RESTORE_CHECK
command=python -m unittest tests.test_cache
```

PASS：正常中文结论，机器字符串精确；没有要求用户再选内部 Skill。

任何 G1 FAIL -> 停止 G2+。

## 9. CW06-G2 frozen task set

所有任务：
- ChatGPT Web；
- explicit Clear Writing selection；
- GPT-5.6 Sol；
- fresh conversation per task；
- one answer；
- infrastructure-only max one retry；
- prompt 不出现内部 Skill 名。

### G2-T1 普通聊天

使用 G1-B exact prompt。若 G1-B 已保存完整输出，可复用同一输出，不重复请求。

PASS：结论先行；不写成日志；三个机器字符串精确。

### G2-T2 正式中文 Markdown 终审

Prompt：

```text
把下面这段中文 Markdown 做成可以直接交给项目负责人看的终稿。事实和机器字符串不要改；开头先说实际结论，不要把内部流程词当成主叙事。

# 当前状态
audit candidate pipeline status 已经通过。
branch=reviewed/demo
command=python -m unittest tests.test_demo
现在唯一没做的是 production restore drill，所以还不能说 release ready。
```

PASS：正式中文文档；结论“恢复演练未做，因此尚不能宣称可发布”不得弱化；branch/command精确。

### G2-T3 中文长技术结构重写

Source 固定为：

`docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md@1f905d294c3c2e5b0951c9d5e818c285d236cef7`

Prompt：

```text
把我给的这份现有中文技术方案重新组织成面向普通研发读者的完整中文文档。不要缩成摘要；事实、版本、状态、路径、权限边界、失败条件和所有明确限制都不能丢。不要按内部审查时间线组织。只返回完整改写稿。
```

PASS：完整性和保真成立；普通内部英文不承担句子骨架；不是简单压短。

### G2-T4 English scientific prose

Input：

```text
Our results appear to perhaps suggest that the proposed method may be beneficial, although this should not be over-interpreted. Across three prespecified seeds, the mean Dice increased from 0.781 to 0.794, while HD95 changed from 8.2 mm to 7.9 mm. No external cohort was evaluated.
```

Prompt：

```text
Rewrite this as concise manuscript Results prose. Keep every number and the limitation exactly supported; remove defensive wording without overclaiming.
```

PASS：数字不变；不能暗示外部泛化；表达不防御也不拔高。

### G2-T5 UI 文案

Input：

```text
按钮：Delete data
说明：This will permanently delete local history and cannot be undone.
状态：Deletion queued
```

Prompt：

```text
把这组设置页中文界面文案改得自然、简短，按钮、后果和当前状态都要清楚；不能弱化“永久删除、不可撤销”的含义。
```

PASS：界面式短文案；删除后果与 queued 状态不漂移。

### G2-T6 exact-only

Prompt：

```text
只返回下面 JSON，逐字不改，不要解释：
{"status":"WAITING_FOR_RESTORE_CHECK","branch":"reviewed/cache--repair","ready":false}
```

PASS：byte-content identical。

### G2-T7 mixed

Prompt：

```text
先用两三句中文说明这个状态对用户意味着什么，然后原样附上下面机器内容。机器内容逐字不改：
{"status":"WAITING_FOR_RESTORE_CHECK","ready":false}
command=python -m unittest tests.test_cache
```

PASS：解释自然；机器内容逐字一致。

### G2-T8 necessary-long-answer

Prompt：

```text
在一个多站点传感器研究里，s 表示站点，j 表示站点内传感器，t 表示时间。x_{s,j,t} 是观测值，mhat_{s,t} 是估计背景，d_{s,j,t}=x_{s,j,t}-mhat_{s,t}，a_{s,j,t}=d_{s,j,t}/vhat_{s,t}。请详细解释对象层级、三个下标、为什么先得到 d 再得到 a，以及 a 后面怎样用于比较或异常筛查。先建立直觉再讲公式；不要为了简短删掉必要解释。vhat 只被描述为“一个估计尺度量”，不要猜它具体是什么。
```

PASS：保留必要深度；不一句一段；不猜 `vhat`；解释下标和后续用途。

### G2-T9 short-answer

Prompt：

```text
构建和单元测试都通过，staging 可访问，但 production restore drill 还没跑。现在能发布吗？我需要做什么？
```

PASS：直接回答“还不能证明可发布”，给最小下一步；不扩成架构文档。

G2 由完整输出定性判定，不用关键词/字数/英文比例作 oracle。

## 10. CW06-G3 Reader Guide known regression

### 10.1 preflight

Source：

- repo：`YuukiAS/AI_Research_Toolkit`
- commit：`0ff0f43f3b04286273490e4c4870975f4aa7a7f8`
- path：`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_V0_4_READER_GUIDE_20261019.md`

Gate branch：

`gate/clear-writing-0.6-reader-guide-regression`

先 GET branch。若存在：`G3_PRECONDITION_BLOCKED`，不得覆盖/force。

若不存在，从 exact source commit创建。

然后 `fetch_file` Gate branch/path，保存 blob SHA 与完整 source hash。

### 10.2 exact prompt

在一个 fresh ChatGPT Web conversation 显式选择 Clear Writing，发送：

```text
请把这个 GitHub 文件改成真正给普通研发读者看的完整中文 Reader Guide，并直接写回我给你的 Gate branch：

repo = YuukiAS/AI_Research_Toolkit
branch = gate/clear-writing-0.6-reader-guide-regression
path = docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_V0_4_READER_GUIDE_20261019.md

要求：
- 必须先读取文件全文；
- 不改变 Delivery Assurance 0.4 的架构事实、职责边界、版本、路径、当前实现状态、未完成项和证据强度；
- 目标是让我不用先学内部 Gate、adapter、owner、claim、Executor 等流程词，也能理解这套架构解决什么、正常任务怎样走、失败怎么回来、目前哪些还没实现；
- 不是摘要，完整信息必须保留，只是重新组织成读者能顺着读的正文；
- 写入前先形成完整终审候选；
- 写回后重新读取目标文件确认；
- 最后在聊天里简短告诉我改了什么，以及是否已经实际写回并验证。
```

### 10.3 PASS

必须有真实 tool evidence：

- source full read；
- candidate identity/hash；
- pre-write re-read 与 blob SHA unchanged；
- GitHub update_file；
- returned commit/content SHA；
- post-write fetch_file；
- readback == candidate；
- final artifact full-text qualitative review；
- chat response status truthful。

如果只输出候选、只解释、只生成 diff、只改部分或没有 readback：FAIL。

G3 FAIL -> release path停止。

## 11. CW06-G4 fidelity adjudication

输入：
- G2-T2/T3/T7 source+output；
- G3 source+final；
- G6 source+final（运行后补入）。

Reviewer逐项检查：

1. 命题/极性；
2. 数字、版本、单位；
3. 公式/变量关系；
4. 引用/归因；
5. 比较条件；
6. limitation/caveat；
7. 完成状态；
8. 权限/授权；
9. exact identifiers。

任何重大遗漏、过度主张、状态/权限改变 -> FAIL。

## 12. CW06-G5 parity / compatibility

G5 evidence bundle：

- `BUILD_RECEIPT.json`；
- candidate ZIP file list；
- root/compat manifests；
- `scripts/codex_marketplace_config.json` writing-style six-skill exposure；
- generated `plugins/codex/plugins/writing-style/**`；
- `profiles/codex-writing-style.json`；
- relevant tests + full CI；
- targeted normal Codex replay proving six direct routes remain callable。

明确不允许：用 hash parity 推断 G2/G3文本质量。

## 13. CW06-G6 fresh protocol

### 13.1 selection only after G1-G5 PASS

在 candidate immutable 后，由同一独立 Critic选择 exactly one source，需满足：

- public-safe；
- Chinese / Chinese-dominant；
- long technical document；
- 有足够事实/限制/精确项可做 fidelity review；
- 不是本任务 repo docs、Reader Guide、KR-WEB-01..09、开发 fixture或此前 reviewer材料；
- 当前 Planner/Codex 没有用它调整 candidate。

Critic在第一次模型请求前写：

`results/clear-writing--single-entry-artifact-finalization/g6/FROZEN_INPUT_MANIFEST.md`

内容必须冻结：
- source URL/repo/path/ref/version；
- full source SHA-256；
- exact prompt；
- ChatGPT Web；
- GPT-5.6 Sol；
- Personal Plugin release ID；
- candidate manifest SHA；
- one-answer budget；
- infra-only one retry；
- fidelity rubric；
- reader-quality rubric；
- stop condition。

### 13.2 prompt contract

exact prompt 必须是普通用户自然请求，只表达：

- 把这份现有长技术材料重写成清楚、完整、自然的中文；
- 保留事实/数字/公式/引用/限制/精确身份；
- 不要求内部 Skill 名或路由步骤。

### 13.3 final review order

Critic必须先看 source全文 -> fidelity，只有 fidelity PASS 才看 reader quality。

reader quality 至少判断：

- 是否有读者模型；
- 结构是否降低推理负担而非机械压短；
- 普通英文是否自然中文化；
- 必要技术身份是否保留；
- 公式/复杂对象是否得到必要解释；
- 内部过程语言是否抢占主叙事；
- 完整长文是否连贯。

一个产品输出。失败即 G6 FAIL；不增加第二个 fresh case。

## 14. evidence paths

标准结果根：

`results/clear-writing--single-entry-artifact-finalization/`

建议固定子目录：

```text
p0/
wrapper/
candidate/
known-regression/
g1/
g2/
g3/
g4/
g5/
g6/
release/
```

private archive / private Plugin metadata 只放：

`private/exports/clear-writing--single-entry-artifact-finalization/`

公开 evidence 不记录 private Plugin URL/ID；必要时使用 hash / release locator 的非敏感部分。

## 15. stop conditions

任一成立立即停止当前后续 Gate：

- candidate identity drift；
- Personal Plugin current release drift；
- P0 reality不成立；
- G1 FAIL；
- G2 release-critical route FAIL；
- G3 FAIL；
- G4 fidelity FAIL；
- G5 compatibility FAIL；
- G6 FAIL；
- model `GPT-5.6 Sol` 无法固定；
- reviewer 无法访问 source全文或 final全文。

等待、权限缺失或基础设施失败必须与产品 FAIL 分开记录，不能换题/降级后报告 PASS。
