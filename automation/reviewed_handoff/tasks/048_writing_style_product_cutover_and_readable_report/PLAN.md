---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 048_writing_style_product_cutover_and_readable_report
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

本任务不再做架构实验，而是把 `writing-style` 的中文科研长文重写能力真正收口成可用产品，并用用户那份 22 页 Deep Research 报告作为最终真实交付物验证。

最终必须同时交付两件东西：

1. 一个通过正常安装入口即可使用的 `writing-style`，能够把“已有中文科研/技术长文说人话但不能改科学内容”自动路由到内部 `scientific-rewrite`；
2. 一份完整、信息不缩水、科学含义不漂移、但明显更容易连续阅读的 Deep Research 报告重写版，供用户随后直接阅读并据此开展实验。

二者缺一不可。047 的实验实现已经证明 meaning-first 路线值得继续，但 047 把私有报告生成错误地绑定到受限的 Codex 私有外发路径，因此没有 Product PASS。用户随后明确纠正：现有 Bridge Kit 的 age + GitHub Actions + OpenAI Responses API `store=false` 路径已经可以安全处理私有 plaintext；真正缺的是“私有文本生成结果如何安全返回本机”，不是 OpenAI API 本身不可用。

本次是 048 唯一允许的 Plan revision。修订只解决这个已证实的 private-transform 架构缺口，不重新设计 `scientific-rewrite`。

Feedback promotion decision: `PROMOTE_NOW`。

Target layer: `writing`

Maintenance companion: `ai-skills-core`

Domain owner: `writing-style`

## Frozen decisions

### 1. 产品边界保持不变

- 顶级用户入口仍然只有现有 `writing-style`，不新建 humanizer / scientific-rewrite 顶级 plugin。
- `scientific-rewrite` 是 `writing-style` 内部 heavy route，只处理**已有原文**的中文或中文为主科研/技术长文高保真重表达。
- `chinese-prose` 继续负责短文本、轻度润色、中文最终语言审阅；不得让所有中文请求都升级成 heavy route。
- `writing-fidelity` 负责字面不变量和语义关系保真；不得因为“保护内容”而把普通标题、句法、中文表达骨架锁死。
- `scientific-prose` 继续负责英文科研 prose；`research-writing` 继续负责从证据新写报告/论文结构。048 不修改这两个 ownership。
- 044 Reviewed Handoff 永久保持历史只读；底层 Deep Research 报告只作为本轮目标私有 artifact / known regression，不 reopen 044 control plane。
- 047 保持历史实验分支；不得整分支 merge/cherry-pick。只允许从 implementation freeze commit `ade5a1f653f88df07eb0c70edfd016c744b1611a` 按当前 main 逐项重放仍然成立的 production source changes。

### 2. 用户最新 private-artifact 决定覆盖旧 Plan / Request 中的 ChatGPT-only 路径

旧 048 Plan 中“私有完整重写只能由 ChatGPT/File Library surface 生成、不得通过 OpenAI API 生成”的决定作废。

已核实 Bridge Kit `main@c8422bd9ad75030dd481e6330c938c9c05fbc453` 的现有 Text Review 路径能够：

```text
local private UTF-8 text
-> age public-key encryption
-> encrypted payload + manifest in Git
-> GitHub Actions temporary decrypt
-> OpenAI Responses API, store=false
-> structured TEXT_REVIEW.json
```

其 consumer 已使用 `AI_BRIDGE_PRIVATE_REVIEW_AGE_KEY`，OpenAI secret 优先为 `OPENAI_REVIEW_API_KEY`、兼容回退 `OPENAI_VISUAL_REVIEW_API_KEY`。现有 `text_review.py` 强制结构化 review JSON，因此它是 **review-only**，不能生成完整重写稿。

正确修复不是 raw `codex exec`、复制 `auth.json`、plaintext Git，也不是 ChatGPT 手工替代；而是在 Bridge Kit 现有私有文本传输旁增加一个最小、可复用的 **Private Text Transform** sibling capability。

### 3. Private Text Transform 的 owner 与边界

Owner 固定为 `YuukiAS/GPT_Codex_AI_Bridge_Kit`。AI_Skills 不得复制第二套 age/secret/OpenAI transport。

Bridge Kit companion 的冻结用户入口为：

```text
ai-bridge text-transform ...
```

具体 CLI 子命令参数可以按 Bridge Kit 现有 CLI 风格实现，但行为合同不得改变。建议实现模块/模板范围仅限：

```text
ai_bridge_kit/text_transform.py
ai_bridge_kit/cli.py                    # 只接入新 CLI group
templates/text_transform/
tests/test_text_transform.py            # 或现有命名体系下等价测试
README/CHANGELOG 中最小能力说明
```

不得修改 Reviewed Handoff schema/state、Agent-Flow、Overleaf、Visual Review、v0.7 Project State Bridge、Notion 或 unrelated Host Policy。

048 不要求 Bridge Kit 为此另开大型 release；AI_Skills 只要求一个通过 Bridge Kit 自身测试的 exact companion commit，并把 consumer workflow pin 到该 exact SHA。若 Bridge Kit 自身当前版本规范强制要求版本记录，按其规范做最小闭环，但不得扩大 048 scope。

### 4. Private Text Transform 安全合同

#### 输入侧

- 只接受 UTF-8 Markdown/plain text private source。
- 本机继续复用已有 age public recipient 对 source 加密；Git 中只允许 ciphertext + manifest + public metadata。
- GitHub Actions 在 ephemeral temp dir 中用现有 `AI_BRIDGE_PRIVATE_REVIEW_AGE_KEY` 解密。
- transform manifest 必须记录显式 `external_upload_authorization`、source plaintext SHA-256、ciphertext SHA-256、source size/MIME、task identity、AI_Skills implementation commit、instruction bundle identity、output recipient identity。
- 用户已明确授权当前 Deep Research 报告由 OpenAI 用于 048 rewrite + review；同一 artifact/provider/purpose 不得再次询问。只有 provider、artifact scope、purpose 或 live-global mutation 实质变化时才能重新请求授权。

#### OpenAI 调用

- Provider 固定为 OpenAI Responses API。
- 必须 `store=false`。
- 默认模型固定为 `gpt-5.6-terra`；允许 `OPENAI_TEXT_TRANSFORM_MODEL` 显式覆盖，但本轮真实 artifact 必须记录最终模型。
- 不要求新增 GitHub secret；使用现有 `OPENAI_REVIEW_API_KEY`，缺失时兼容回退 `OPENAI_VISUAL_REVIEW_API_KEY`。
- 不得声称“plaintext 从未上传”。准确语义是：plaintext **不提交到 GitHub**；它会在 ephemeral runner 中被解密，并在用户已授权的 API request 中传输给 OpenAI，`store=false`。
- API 失败、输出为空、status 非 completed 或可观察到截断/不完整时 fail closed，不写伪造成功结果。

#### 指令绑定

Private Text Transform 是通用 transport，不拥有 `writing-style` 业务逻辑。它必须支持显式、SHA-bound 的 public instruction files / instruction bundle。

048 私有报告 transform 的 instruction bundle 固定来自**当前 048 已生成的 writing-style payload**，至少绑定：

```text
plugins/codex/plugins/writing-style/skills/scientific-rewrite/SKILL.md
plugins/codex/plugins/writing-style/skills/fidelity/SKILL.md
plugins/codex/plugins/writing-style/skills/zh/SKILL.md
scientific-rewrite 中 meaning/fidelity、positive-style、seed transformation 等本轮实际使用的 reference files
```

manifest/result 必须记录每个 instruction file 的 path + SHA-256，并形成一个整体 instruction-bundle identity。Seed examples 只有 transformation authority，不得提供事实。

#### 输出侧

- model-generated rewritten plaintext 只能存在于 runner temp dir；绝不能写入 Git working tree。
- 本机/Longleaf 必须生成一套**独立的 output receiver age keypair**：private identity 只保存在 `${AI_BRIDGE_STATE_HOME:-~/.ai-bridge}/...` 或用户指定的本机私有 state，不得 commit、不得成为 GitHub Secret；public recipient 可以写入 transform manifest / public recipient file。
- GitHub Actions 只持有 output public recipient，将 rewritten plaintext 加密为 `output.age` 后删除 temp plaintext。
- Git 中只允许 commit `output.age` 和一个不含正文的 `TEXT_TRANSFORM.json`（或等价固定结果文件），其中记录 source SHA、instruction bundle identity、model、`store=false`、output plaintext SHA、output ciphertext SHA、implementation commit、Bridge Kit commit。
- 本地 `ai-bridge text-transform decrypt` 使用 receiver private identity 解密 `output.age`，并在写出 `rewritten_report.md` 前校验 metadata 中的 output plaintext SHA。
- GitHub Actions writeback 只能 stage 明确允许的 encrypted output + metadata 路径，不能 `git add` temp dir 或广泛目录。

### 5. Bridge Kit companion 的最小测试门槛

至少覆盖：

1. private input age encrypt/decrypt round trip；
2. wrong key / corrupt ciphertext fail closed；
3. private source plaintext 永不进入 tracked path；
4. transformed plaintext 永不写入 Git working tree；
5. output.age 可被 local receiver private identity 解密；
6. runner/manifest 只需要 output public recipient，不需要 output private key；
7. source、instruction bundle、output 的 SHA/identity binding；
8. Responses request 明确 `store=false`；
9. API error / malformed / incomplete response fail closed；
10. secret/private identity 不打印、不写 metadata；
11. writeback 只 stage ciphertext + metadata；
12. 现有 `text-review` 测试与行为不 regression；
13. 一个 public/non-private live transform smoke 证明真实 API transform 通路可运行。mock API 只能证明 mechanics，不能冒充 live transform PASS。

### 6. AI_Skills consumer 只消费 Bridge Kit exact commit

Bridge Kit companion PASS 后，记录 exact commit SHA。AI_Skills 通过 Bridge Kit install/template 机制安装或同步 `.github/workflows/ai-bridge-text-transform.yml`（名称允许按 Bridge Kit canonical template），其中 `AI_BRIDGE_KIT_PIP_SPEC` 必须 pin 到该 exact commit；不得使用 floating `main`。

现有 `.github/workflows/ai-bridge-text-review.yml` 继续作为独立 Reviewer evidence transport。它当前 pin 到 `9e8ab90fb13e92d268b08ad7fc7aa64ed9f9877a`；除非 Bridge Kit companion 的兼容实现确实需要同步该 workflow，否则不为了统一 SHA 制造无关 diff。最终 evidence 必须同时记录 transform pin 与 text-review pin。

### 7. 保留 047 已验证的 `scientific-rewrite` 核心架构

Production contract 固定为：

```text
original document
-> compact document map
-> complete argument/discourse units
-> Meaning Card + Fidelity Ledger
-> source-to-card coverage check
-> metadata-selected positive transformations
-> rewrite from meaning + original
-> deterministic exact verification
-> semantic claim/relation audit
-> targeted local repair
-> Chinese language-quality review
-> whole-document terminology/coherence review
```

Meaning Card 不是摘要，也没有 factual authority；原始 source unit 始终与 Meaning Card 一起进入 writer。长文按完整论证单元切分，默认一整个 subsection 或约 2–5 个逻辑紧密段落；不得为 token 均匀切断定义、实验条件、结果、限制或结论。

`writing-fidelity` 必须明确区分：

- literal preservation：数字、日期、范围、单位、公式/变量/符号、引用/DOI、精确引文、代码/命令/路径/config/identifier、需要精确命名的正式算法/数据集/benchmark/metric/package/product/method name、用户明确 no-touch span；
- semantic preservation：claim/polarity、uncertainty/evidence strength、scope/condition/exception、comparator、chronology、causality、attribution、caveat、negative result、decision logic、conclusion strength。

Semantic-protected 内容允许彻底换句法。普通 reader-facing heading、内部 workflow label、section wording、英文抽象标签默认不是 literal-protected。

### 8. 中文目标是正向表达，不是禁词表

目标是让技术上有能力的研究者直接读懂：谁做了什么、为什么这样比较、证据说明什么、还有什么不确定、下一步决策是什么。

不得把 044 中出现的 `provenance`、`estimand`、`scientific gap`、`resource contract`、`state of the art` 等做成项目专用 blacklist。不得使用英文比例、禁词数量、AI detector 分数作为 release gate。

### 9. 外部来源决定保持不变

- `MrGeDiao/shuorenhua@6de1fcfeca5fff6fd15b28c619c11b6d41d1f657`, MIT：`SELECTIVELY_PORTED`。
- `whh110112/human-writing-skills@2b02ae77bd1ea009ea2d7a1cc6d2dcdce1437a00`, MIT：`SELECTIVELY_PORTED`。
- `AIScientists-Dev/academic-humanizer@94b88b23703bed7df507acae7d6d5876209a0cdf`：`REFERENCE_ONLY`，留给以后英文 academic-writing 审计。
- 不再 Source Scout；不引入 Gemini、Claude routing、fine-tuning、embedding、FAISS、Chroma、BGE、sentence-transformers 或任何新 runtime dependency。

### 10. 公开验证集固定为 regression，不再冒充 unseen proof

重放 047 已冻结的四个 public units，角色固定：

- positive A：`YuukiAS/Bobbio@2d8a054bd34291dc061b8b64d5d841d458cc6296`, `README.md` lines 1–70；
- positive B：`YuukiAS/Distributed_Imaging_Inference@0e895fdbce37c34967d8375059154df1d76397f4`, `docs/SEGCOMM_CORRECTION_STABILITY_REPORT_2026-08-28.md` lines 1–8；
- should-not-fix A：`YuukiAS/AI_Research_Toolkit@b822dff09794766a1a013b100eb8f78a45514c7b`, `R_RESEARCH_STACK.md` lines 1–13；
- should-not-fix B：`YuukiAS/Asteria@80ad881bc88ad1caf017959e320e539028eb5a25`, `ROADMAP.md` lines 5–17。

这些只能证明 regression/compatibility。真正的长文产品证明来自完整 Deep Research 报告的 fresh transform + independent Text Review + 用户实际验收。

### 11. 私有 Deep Research source 准备

目标 artifact 固定为：

`共享预训练医学分割模型下的极低通信联邦适应：项目事实审计、算法前沿与下一轮实验决策`

Executor 不 reopen 044 workflow，但可以读取本机历史 replay state 来**定位同一 artifact 的 canonical source**。输入优先级固定为：

1. 044/047 之前真实 replay 使用过、且能与原报告 identity 对上的 UTF-8 Markdown/text source；
2. 若只剩原始 text-based PDF，则对该 PDF 做本地 deterministic text extraction，记录 PDF SHA-256、extractor/version、页数与基本 text sanity；禁止 OCR，禁止在 transform 前做语义改写；
3. 如果既没有可靠 UTF-8 source，也无法从原始 text-based PDF 做可靠文本提取，才进入 human decision，明确缺的是 source locator；不得把它伪装成“private OpenAI 不可用”。

### 12. Release / version decision

Repository bump decision: `PATCH`，**仅在两个产品 gate 都通过且用户明确 ACCEPT 后执行**。

当前 Planner 复核时 `main` repository version 仍为 `5.0.3`，`writing-style` 仍为 `0.1`。最终 release 语义固定为：integration-time 最新 main 的下一个 compatible repository patch；`writing-style` 从当时的 current released version推进 exactly one release。若 integration 时仍为上述版本，则为 repository `5.0.4`、`writing-style 0.1 -> 0.2`。

Affected plugins:

- `writing-style`: `0.1 -> 0.2`（若 integration 前仍为 0.1）；仅在两个产品 gate 都通过时 exactly once bump。
- 其他 plugin：`NO_BUMP`。

失败、用户 REJECT、只完成技术 candidate 或只完成报告时：`NO_BUMP / NO_CUTOVER`。

`writing-style` capability status 本轮默认保持 `unclassified`；一次真实长报告成功不足以自动宣称 stable。

## Implementation scope

### A. Bridge Kit companion prerequisite

在 `YuukiAS/GPT_Codex_AI_Bridge_Kit` 最新 `main` 上先实现上述最小 `text-transform` sibling capability。开始前重新读取该 repo `AGENTS.md`、当前 Text Review 代码/模板/tests 和当前 main；不得把 048 task state 写进 Bridge Kit。

完成后必须：

- Bridge Kit focused/full relevant tests PASS；
- public live transform smoke PASS；
- working tree clean；
- commit/push 一个 exact companion SHA；
- 记录本轮没有暴露 secret/private plaintext；
- 将 exact SHA 带回 AI_Skills 048 evidence。

### B. AI_Skills production source

从 048 task branch 开始，逐项对照 047 implementation freeze `ade5a1f653f88df07eb0c70edfd016c744b1611a`，只重放仍成立的 production source changes：

- 新增 `skills/writing/core/scientific-rewrite/`：`SKILL.md`、`assets/app-facing.svg`、必要 references、`scripts/rewrite_support.py`；
- 最小修改 `skills/writing/core/writing-fidelity/SKILL.md`；
- 最小修改 `skills/writing/core/chinese-prose/SKILL.md`；
- 修改 `scripts/codex_marketplace_config.json`：仍只有 `writing-style` 顶级入口，加入 `scientific-rewrite` copy skill 与自然 routing/default prompt；
- 与上述能力直接相关的 focused tests；
- 稳定 provenance 记录；
- `docs/plugin-todos/writing-style.md` 将 Deep Research 问题收口为 048 active refinement，最终 release 后才标 promoted；
- 安装/同步 Bridge Kit `text-transform` consumer workflow，并 pin exact companion SHA；
- `results/048_writing_style_product_cutover_and_readable_report/` 只保存 public regression、routing、fidelity、encrypted private transform/review evidence 和不泄露正文的 metadata/receipts。

Generated `.agents/plugins/marketplace.json` 与 `plugins/codex/plugins/` 只能由 canonical generator regenerate，禁止手改。

Planner 复核时 AI_Skills `main` 已从 task base `0b3aa144...` 前进到 `8faafd5a...`，新增的是 presentations 相关记录，不直接改变本 task frozen writing source。Executor 开始实现前仍必须 fetch 最新 main 并做 source-area drift check；若最新 main 在 `writing-style`、shared Marketplace generator、Text Review consumer 等同一 source area 出现竞争性修改，不得强行覆盖。由于本次已用完唯一 Plan revision，实质冲突进入 human decision；纯无关 main drift 留到 integration preflight。

### C. Private transform request / output

AI_Skills candidate source、generated payload、public regression 和 normal routing冻结后，创建 task-local transform evidence：

```text
results/048_writing_style_product_cutover_and_readable_report/text_transform/
```

只允许 tracked：input ciphertext、transform manifest、output public recipient、output ciphertext、`TEXT_TRANSFORM.json`、不敏感 summary。不得 tracked 原始/重写 plaintext。

transform instruction bundle 必须绑定当前 generated writing-style paths + SHA，不得用 047 branch 文件或手写另一套项目专用 prompt 代替 production contract。

local decrypt 后的 `rewritten_report.md` 保持 private/local。随后运行 exact fidelity helper，并生成不含正文的 exact report。

### D. Independent private Text Review

Private Text Review 为本 task **REQUIRED**。

本地生成一个仅用于 review 的 private UTF-8 bundle，包含完整 source 与完整 candidate，清晰分隔并带 source/candidate SHA；该 bundle 绝不 commit plaintext。用现有：

```text
ai-bridge text-review encrypt
```

加密到：

```text
results/048_writing_style_product_cutover_and_readable_report/text_review/payload.age
results/048_writing_style_product_cutover_and_readable_report/text_review/text_inputs.json
```

Rubric 必须要求独立读取完整 source + candidate，并同时判断：科学/来源保真、信息完整性、自然中文可读性、长文一致性；不得用摘要、phrase scan、English ratio 或 Executor self-report 代替。

Text Review evidence 固定为：

```text
results/048_writing_style_product_cutover_and_readable_report/text_review/TEXT_REVIEW.json
```

## Acceptance and regression gates

### A. PROCESS PASS：只能证明工程流程正确

必须全部通过：

- Bridge Kit `text-transform` focused tests + existing Text Review regression；
- Bridge Kit public live transform smoke；
- AI_Skills canonical Marketplace build/check/validate；
- source/generated parity；
- `scripts/skills.py validate` / relevant audit；
- focused scientific-rewrite / writing-fidelity / routing / marketplace tests；
- task-local install smoke；
- branch GitHub CI；
- working tree/task branch tracked files不含 private plaintext、token、auth/private age identity。

### B. Installed production-entrypoint technical gate

在 isolated/shadow Codex home/cache 中通过正常 Marketplace/plugin install 机制安装当前 048 generated `writing-style`，启动 fresh session，用普通用户语言触发。

- long-form Chinese scientific rewrite 自动选择/暴露 `writing-style:scientific-rewrite`；
- light polish 留在 `chinese-prose`；
- 只做数字/公式/引用审计留在 `writing-fidelity`；
- source-tree 直接调用、benchmark helper、test-only router 不能冒充 production entrypoint PASS；
- 不修改 live global plugin cache；
- private Deep Research report **不需要**通过 Codex auth/replay来证明这个 gate。

### C. Public regression artifact gate

implementation identity 冻结后重放四个 fixed public regression units。

两个 positive regression 必须做到：literal critical drift = 0；semantic critical violation = 0；reader effort真实下降；seed example不引入事实。

两个 should-not-fix 必须保持低编辑/不深改，不破坏正式术语、版本/复现约束、产品/证据关系。

Scheduled GPT Reviewer 必须读取 committed public outputs 和 source identities，不能只看 Executor summary。

### D. Secure private-transform transport gate

在完整 Deep Research source 上真实执行：

```text
local source
-> age input encryption
-> GitHub Actions ephemeral decrypt
-> OpenAI Responses API store=false
-> generated full rewrite in runner temp
-> output age encryption
-> ciphertext + metadata writeback
-> local decrypt
```

必须验证：

- transform manifest/source/instruction/output identities一致；
- tracked Git 中无 source/candidate plaintext；
- API真实 completed 且无可观察截断；
- local decrypt SHA 与 `TEXT_TRANSFORM.json` output plaintext SHA一致；
- output 是完整长文，不是 executive summary。

### E. Private full-report fidelity + Text Review gate

local candidate 先做 deterministic exact fidelity；数字、日期、范围、单位、公式/符号、引用身份、正式算法/数据集/模型/metric/identifier 不得有 unresolved critical drift。

随后 existing Text Review 必须对**完整 source + 完整 candidate**做 fresh independent review。`TEXT_REVIEW.json` 必须：

- 绑定当前 implementation commit、private review bundle plaintext SHA 和 manifest identity；
- `overall_decision=PASS`；
- 无 blocking findings；
- 明确检查 source fidelity / completeness / natural Chinese / whole-document coherence；
- 对 claim polarity、uncertainty、scope、condition、comparator、causality、attribution、caveat、negative result、GO/STOP logic、conclusion strength 不得存在 unresolved critical violation。

缺失/stale/mismatch/non-PASS Text Review 不能进入 Product PASS，也不能用用户尚未阅读来替代。

### F. Scheduled GPT Reviewer gate

Reviewer 必须区分 PROCESS PASS 与 PRODUCT/ARTIFACT PASS，并检查：

- actual implementation diff；
- Bridge Kit exact transform commit + consumer pin；
- installed normal routing evidence；
- source/generated parity；
- actual public regression outputs；
- private transform metadata/identity；
- deterministic fidelity evidence；
- fresh `TEXT_REVIEW.json`。

Reviewer 不需要也不得要求 private plaintext 出现在 GitHub；private全文质量由 Text Review evidence提供合法可访问的独立 artifact-aware review path。

### G. Final user artifact gate

技术 gates + Reviewer PASS 后进入 `AWAIT_HUMAN_DECISION`。用户实际阅读 local/private 完整 `rewritten_report.md`（可按现有 PDF rendering route另生成 private PDF）并明确 `ACCEPT` 才能完成产品。

用户验收判断：是否信息完整；科学力度/限制未漂移；是否明显减少英文抽象标签、审计/仓库/流程语言和翻译腔；是否已经可以直接作为接下来阅读并跑实验的工作材料。

若用户 `REJECT`：本 task 不完成。若反馈可在 frozen architecture 内做 bounded generic repair，则回 `REVISE`；禁止报告专属词表/句子规则。若反馈证明 frozen architecture 本身需要第二次 re-plan，因为 `plan_revision=1` 已用尽，进入 human decision，不伪造第二次 Plan revision。

### H. Product completion / release / integration gate

`writing-style` Product PASS = plugin technical/public gates + secure private transform + fresh private Text Review PASS + Scheduled Reviewer PASS + 用户完整报告 ACCEPT。

用户 ACCEPT 之前：不得 bump version、不得 merge main、不得宣布 cutover。

用户 ACCEPT 之后：重新读取 integration-time 最新 main 和版本规范；按本 Plan 冻结的 `PATCH + writing-style next release` 完成版本/changelog/generated closure、integration preflight、最终回归，再合回 main/push。普通机械 integration 不再要求用户第二次决定。

Visual Review: `NOT_REQUIRED`。

Text Review: `REQUIRED`。

## Natural-language usage / routing expectations

Front door: `writing-style`。用户不需要知道 `scientific-rewrite`、Bridge Kit、外部 repo 名或内部 helper。

Should-trigger：

- “把这份中文科研长报告说人话一些，但不要改变事实、数字、公式、引用和结论强度。”
- “这篇技术报告内容没问题，但读起来像运行日志；按原意重新组织成自然中文。”
- “不是摘要，整份 Markdown 都要保留信息，只是把句子和段落重新讲清楚。”
- “普通标题和内部 workflow 词可以改，但数字、引用、公式、比较和科学含义不能动。”

Should-not-trigger：

- “把这两句话润色顺一点。” -> `chinese-prose`。
- “只检查数字、版本、公式和引用有没有被改坏。” -> `writing-fidelity`。
- “润色这段英文 Results/caption。” -> `scientific-prose`。
- “根据这些实验结果从头写一份新组会报告。” -> `research-reporting` / `research-writing`。

Private Text Transform 是本任务为私有 artifact 安全生成提供的基础设施，不是普通 `writing-style` 用户需要直接理解的入口。

## Out of scope

- 不修改 044 或 047 workflow 历史；不继续为旧状态机补 evidence。
- 不把 raw `codex exec`、`auth.json` copy 或 live global plugin mutation 当私有报告 transport。
- 不把 ChatGPT/File Library 当唯一私有报告生成路径；也不禁止用户以后在 ChatGPT 上使用已发布的 writing-style 思想。
- 不 commit 原始或重写后的 private plaintext；不打印任何 API key / age private identity / auth token。
- 不修改 `presentations`、`research-writing`、`scientific-prose` 或其他 plugin production behavior/version。
- 不在 AI_Skills 复制一套 private crypto/OpenAI transport；Bridge Kit 是唯一 owner。
- 不 redesign Bridge Kit Reviewed Handoff、Agent-Flow、Visual Review、Overleaf、Host Policy、v0.7 Project State Bridge/Notion。
- 不新建顶级 writing plugin、profile、Reviewed Handoff schema/state/role/requirement ledger。
- 不新增 Gemini、Claude provider、embedding/vector DB、FAISS/Chroma/BGE、fine-tuning/DPO。
- 不做新的广泛 Source Scout；`academic-humanizer` 本轮保持 reference-only。
- 不构建大型 humanizer corpus，不学习用户历史文章个人 voice，不做 AI detector evasion。
- 不为了 public regression 好看而 adaptive 更换输入、把失败 regression 加进 seed library，或宣称其为 unseen proof。
- 不以英文词数量、禁词数量、AI detector score、单一句长或标点 house style作为产品质量真值。
- 不在用户最终 ACCEPT 前做 writing-style/version bump、main merge 或 maturity status 升级。
