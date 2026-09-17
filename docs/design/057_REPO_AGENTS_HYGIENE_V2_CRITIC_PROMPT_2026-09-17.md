# 057 Repo AGENTS Hygiene v2 — Critic Prompt

你是 AI Research Stack 的长期独立 Critic thread。

当前任务：

`TASK_KEY = 057_repo_agents_hygiene`

Repository:
`YuukiAS/AI_Skills_Collection`

Current review object:
`docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`

本轮只审方案，不实现，不修改任何产品 repo/AGENTS，不修改 Bridge Kit production，不创建 branch/worktree，不启动 Executor，不运行 paid API。

## 一、强制读取

先实际读取 AI_Skills_Collection 最新 main：

- `AGENTS.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- `docs/design/057_REPO_AGENTS_HYGIENE_REVIEW_PACKAGE.md`
- 056 v6 architecture / approved execution package，只用于确认 057 不偷改已冻结中央职责

然后独立读取当前 instruction surfaces：

### Bobbio develop
- `AGENTS.md`
- `docs/DEVELOPMENT_WORKFLOW.md`
- `docs/PRODUCT_DESIGN_BRIEF.md`
- `docs/design/FIGMA_HANDOFF.md`
- `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md`

### Lucerna main
- `AGENTS.md`
- `prompts/AGENT_RULES.md`
- screenshot / Longleaf canonical docs as needed

### Mica-for-ChatGPT main
- `AGENTS.md`
- `docs/PHASE_1_LONG_THREAD_RECOVERY.md`
- `docs/VERSIONING.md`

### Asteria main
- `AGENTS.md`
- `prompts/AGENT_RULES.md`
- `docs/operations/blackbox-audit/UI_BLACKBOX_BROWSER_CONTRACT.md`
- `docs/operations/development/DEVELOPER_VISUAL_SELF_QA_CONTRACT.md`
- `docs/design/SCIENTIFIC_GRAPH_VISUAL_SYSTEM.md`

### SeminarArc main
- `AGENTS.md`
- `prompts/AGENT_RULES.md`
- `docs/DEVICE_TESTING.md`
- relevant project-skill locators

### CUHK Date main
- verify tracked root `AGENTS.md` status
- `docs/design/prototype/AGENTS.md`

### Bridge Kit main
必须实际读取：

- `AGENTS.md`
- `ai_bridge_kit/cli.py`
- `codex/AGENTS_SNIPPET.md`
- `templates/prompts/AGENT_RULES.md`
- init/validate tests directly related to root AGENTS installation

确认 current behavior：fresh repo没有 root AGENTS 时只创建 managed handoff block；existing root 只 append/update managed block；目前没有 project-owned structural scaffold。

## 二、独立外部研究

至少独立核查：

- OpenAI current Codex `AGENTS.md` scope/precedence/instruction discovery；
- current `project_doc_max_bytes` behavior；
- OpenAI current harness-engineering recommendation about short AGENTS as map/table-of-contents；
- 必要时一个其他成熟 repo-instruction practice，但优先官方一手来源。

不要把“100 lines”或 32KiB 当硬格式指标；审的是 consumption risk 和 progressive disclosure。

## 三、先审 sequencing

Planner v2 建议：

```text
057 first
-> 057 implementation + audit/integration
-> return to 056
-> bounded source-drift revalidation/amendment
-> no v6 redesign unless 057 invalidates a frozen assumption
```

请判断：

- 这是否比直接执行 056 更符合用户当前要求；
- 057 若先修改 Bridge Kit，是否会使 056 的 Bridge version/ref/Bobbio locator 机械 stale；
- 是否只需窄 amendment/re-review，而不是重开 v6；
- 是否有更简单的 sequencing 能避免重复实现同一 locator/template。

## 四、审 Bridge Kit reusable root AGENTS scaffold

用户明确建议：Bridge Kit 应提供一套以后新 repo 可直接沿用的 AGENTS template，避免每个项目都从事故堆叠开始。

Planner proposes：

`templates/repo/AGENTS_TEMPLATE.md`

作为 **project-owned root structure scaffold**，与：

- `codex/AGENTS_SNIPPET.md` managed block；
- `prompts/AGENT_RULES.md` Lite/execution rules；

保持不同 owner。

请重点攻击：

### 是否真的需要

当前 `ai_bridge init` 已经会创建 root `AGENTS.md`，但内容只有 managed handoff block。这个事实是否足够支持增加 scaffold，而不是让每个 repo继续完全手写？

### 是否会重复 Lite

模板不得复制 056 Lite L1-L6 或 `prompts/AGENT_RULES.md` 全文。root 应只放 project-owned structure/invariants/locators。

### Fresh repo behavior

如果无 root `AGENTS.md`：

- normal `ai-bridge init` 应真正消费 scaffold；
- create one root file + exactly one managed Bridge block；
- 不制造假 project facts；
- 不塞一堆无用空 checklist；
- 能让以后规则按 authority/read-first/safety/testing/design/version/deeper-doc owners 生长。

### Existing repo behavior

如果 root已存在：

- 不自动迁移/重写用户内容；
- 继续只安装/更新 managed block；
- scaffold只作为显式 maintenance/migration参考；
- `--force` 不能变成“把现有 AGENTS 重置成模板”。

### 是否过重

检查是否需要新命令/schema/migration engine。Planner默认认为不需要：复用现有 init/install path即可。

如果你认为自动 fresh-repo scaffold也不应该默认启用，请给更小替代和原因。

## 五、审 existing repo cleanup

逐 repo给：

`KEEP_AS_IS | LIGHT_EDIT | SUBSTANTIAL_REORGANIZATION | EVIDENCE_NEEDED | OUT_OF_SCOPE`

并区分：

- exact/near duplicate；
- real internal contradiction；
- stale authority；
- long but necessary safety/domain rule；
- move-to-doc candidate；
- root必须保留的 hard invariant/locator。

重点：

### Bobbio

- Figma canonical authority vs four `Bobbio_Design_*.png` historical references；
- GUI/human gate/anti-blocking/pre-user/native acceptance是否有内部重复；
- Zotero/knowledge/iPad rules不能因精简丢失。

### Lucerna

- current Windows/live-provider/tray/screenshot/Longleaf sections是否是不同 project-specific owners；
- 如果只是轻整理，不要为了统一硬拆文件。

### Mica

- development testing budget / test tiers / focused iteration重复；
- real long conversation是最终 manual acceptance，browser boundary禁止的是 automated authenticated loop，是否需要澄清而非改变语义。

### Asteria

- root是否复制太多 canonical Browser contract / tunnel/runtime/dev-server mechanics；
- `prompts/AGENT_RULES.md` 已拥有 visual self-QA/scientific graph/generic fix，root应否主要做 locator；
- fixed public URL/GPT Work-before-human等hard invariants必须保留。

### SeminarArc

- root与 `docs/DEVICE_TESTING.md` 的 environment/device safety重复；
- physical-device high-risk summary哪些必须留 root；
- move detail后是否仍 discoverable；
- 不得为了缩短削弱 remote-device safety。

### CUHK Date

- 无 tracked root AGENTS 时，是否应继续不创建，仅保留短 prototype AGENTS；
- 不因 Bridge Kit有fresh template就retroactively给这个已有repo强加root文件。

## 六、审 common style target

Planner v2 proposes：

- root = map + hard project invariants；
- deeper docs = long procedures / volatile environment details / historical evidence；
- explicit current/canonical locators；
- one concept per bullet；
- no bulk translation solely for style；
- managed Bridge block不手改；
- no deletion just to hit line/byte target；
- project safety outranks cosmetic consistency。

判断这是否足够接近各 repo style，且没有把项目差异抹平。

## 七、审 H1-H9

057 v2 gates：

- H1 semantic preservation
- H2 no internal contradiction
- H3 discoverability
- H4 managed-block integrity
- H5 context quality
- H6 repo-specific regression
- H7 fresh Bridge scaffold normal entry
- H8 existing-repo should-not-change
- H9 no Lite duplication

请检查：

- H7必须走真实 `ai-bridge init` normal path，不是模板helper测试；
- H8必须证明 existing custom AGENTS不被自动reformat/overwrite；
- H9必须证明root scaffold没有建立第二份Lite authority；
- 是否有gate高度重复可合并；
- 是否漏掉Bridge install/validate normal entry或context regression。

## 八、主动攻击两个方向

### 过简

- existing repo只是换heading；
- template文件存在但init不消费；
- fresh root仍然只有handoff block；
- Bobbio authority ambiguity仍在；
- Mica测试重复仍在；
- Asteria/SeminarArc只移动文字却让重要规则更难找。

### 过重

- scaffold变成万能长AGENTS；
- Bridge自动迁移existing repos；
- 057创建新schema/state/controller；
- 为每个repo新建多份docs；
- 为统一style批量翻译/重写产品语义；
- 把056 Lite中央规则复制到root。

## 九、056边界

057不能直接改056 approved package。

如果057未来实现完成，Planner才做bounded source-drift revalidation，最多处理：

- Bridge version/source ref；
- Bobbio locator已经由057完成则从056 implementation scope去重；
- Bridge root scaffold vs 056 Lite distribution owner关系；
- exact Kickoff/Plan locators。

只有真实 owner/architecture assumption变化才重开v6。

## 十、结论

如果有blocker：

`RESULT=REVISE`，按 Critic contract自动附完整 Planner返修prompt。

如果方案可进入execution-package drafting：

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md
READY_FOR_EXECUTION_PLAN = YES
NEXT_HANDOFF = PLANNER
```

PASS不授权修改任何 repo 或 Bridge Kit；Planner仍需准备完整 057 Plan + Goal + Kickoff，再由 Critic审 execution-ready package。
