# Clear Writing 0.5 Release Closure Plan v0.1 — 独立 Critic Prompt

你现在担任 AI Research Stack 的独立 Critic，审查 Clear Writing 最终正式 release closure 方案。

本轮不是重新审产品行为，不重新跑 Web Gate，也不重开旧设计。

## Active Review Context

- target_repo:
  `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain:
  `writing-style / Clear Writing`
- design_topic_or_task_key:
  `clear-writing--release-closure`
- source/evidence branch:
  `reviewed/clear-writing--scientific-explanation-readability-repair`
- review_stage:
  `RELEASE_CLOSURE_DESIGN_REVIEW_V0_1`
- frozen production candidate:
  `fd7a1578a5042a46a55c5b638f6d550655b1096b`
- release-closure plan:
  `docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_PLAN_V0_1_2026-10-19.md`
- plan commit:
  `8e55b993cf9663947c642fa31cc50d952225b4af`
- tracking Issue:
  `#13`

用户已经明确报告最终 4-answer ChatGPT Web closure gate 全部 PASS：

- explicit real PRIVATE Clear Writing：PASS
- Project scientific-rewrite：PASS
- pure exact JSON：PASS
- complex scientific explanation + recovery：PASS

并明确冻结：

```text
FINAL_WEB_GATE=PASS
FINAL_WEB_GATE_TEST_COUNT=4
W2_RELEASE_BLOCKER=NO
READY_FOR_RELEASE_CLOSURE=YES
```

历史 `W2=INCONCLUSIVE` 保留，不改判、不重跑。

## 强制读取

先读取最新 `main`：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

然后读取：

- release-closure Plan v0.1；
- current `main` / `release` refs 与 `VERSION`；
- current `scripts/codex_marketplace_config.json` 的 writing-style version；
- current `README.md`；
- root `CHANGELOG.md`；
- `docs/plugin-changelogs/writing-style.md`；
- frozen candidate `fd7a157...` 的实际 writing-style diff；
- 真实 PRIVATE Clear Writing plugin 当前 identity；
- Issue #13 当前状态。

不要执行 release，不修改任何文件、分支、Project setting 或 plugin。

## 已冻结且禁止重开的内容

不得重新审：

- invocation-policy proposal v0.2；
- 六技能架构；
- `response-clarity` 产品方向；
- KR-WEB-01..09；
- 四组 should-not-change；
- 最终 4-answer Web Gate；
- W2 matched experiment；
- PIE；
- Mica；
- Research Authoring；
- Presentations。

本轮只审 formal release closure 是否最小、正确、可执行。

# 重点复核

## 1. Version decision

Planner 冻结：

```text
Repository bump decision: PATCH
Repository: 5.5.0 -> 5.5.1

Affected plugins:
- writing-style: 0.4 -> 0.5
- all others: NO_BUMP
```

请根据最新版本政策判断：

- 当前 refinement 是否确实是 existing repository capability 内的 compatible improvement，而不是 repository MINOR；
- writing-style 从 0.4 -> 0.5 是否满足“正式 user-facing improvement batch + implementation/replay/regression/review complete -> exactly once bump”；
- 是否不应推进 1.0 或 maturity；
- Plugin Creator 的 `0.5 -> 0.5.0` 是否可作为 platform normalization，而不是 repository version contract 变化。

如果正确，标 `CW-RC-01=CLOSED`。

## 2. Release isolation 是否必要且正确

Planner 实测：

```text
origin/main    = 23f51b0bebd8a32f49d899f7fae1ee0e5f17e4cd
origin/release = 6daafa779e1c4af1ef9ec58b4a5df5f30b0c4b17

main VERSION    = 5.5.0
release VERSION = 5.5.0
```

current main 比 formal release 多大量无关开发提交，且已经包含用户明确禁止本轮顺带发布的其他插件 drift。

Planner 因此不允许 current main 整体推进 release，而采用现有 formal release-isolation 模式：

- 从 current formal `release` 基线构建 Clear Writing-only candidate；
- exact candidate 全绿后 fast-forward-only 推进 release；
- 再把已发布 exact release commit merge 回 latest main。

请判断这是否符合仓库现有 formal producer / fast-forward-only contract，并能避免把 Presentations 等无关开发状态顺带发布。

特别检查：

- 不能 wholesale merge 当前旧 evidence branch；
- 不能把 current main 当 formal release target；
- 如果 release baseline 在执行前移动，必须 stop + late-bind；
- main reintegration 必须保留无关 main work，不能通过 release closure“修”其他 plugin。

如果正确，标 `CW-RC-02=CLOSED`。

## 3. Product allowlist 是否绑定 frozen candidate

Planner 只允许把 frozen candidate 中已经通过验收的 writing-style 差异移植到 formal release baseline：

- `response-clarity/**`
- chinese-prose 对 ordinary-response 的 approved routing 差异
- writing-style marketplace source 中 response-clarity exposure + approved description/default prompt
- codex-writing-style profile exposure
- 直接相关 tests

generated layer 必须由 canonical generator 产生，不手改。

请判断：

- 这个 allowlist 是否足够构造实际 0.5；
- 是否遗漏了一个 release-critical source consumer；
- 是否错误允许旧 branch 的 control/evidence/W2 docs进入 production；
- 是否能保证六技能其它行为不因 release closure 再被修改。

如果正确，标 `CW-RC-03=CLOSED`。

## 4. README / changelog / release metadata

Planner 只允许：

- VERSION -> 5.5.1
- root CHANGELOG 新增 5.5.1
- writing-style changelog 新增 0.5
- README repo version -> 5.5.1
- README Clear Writing -> v0.5 + 一句面向用户的普通解释能力
- generated registry/catalog/Marketplace metadata 随 canonical generator更新
- tests 中对应 version contract 更新

并要求 README 实际调用当前安装的 Clear Writing做受影响区域语言检查。

请判断是否完整且没有把 README 变成审计流水账。

如果正确，标 `CW-RC-04=CLOSED`。

## 5. Final CI 是否足够且不重新做产品 Gate

Planner 要求 exact formal candidate：

- writing-style focused tests
- source/generated parity
- Marketplace/version/changelog/README consistency
- full repository tests
- skill validation
- required GitHub CI

但明确禁止重新执行最终 4-answer Web Gate。

请判断：

- 这些是否足以做 release-candidate mechanical/regression closure；
- 是否错误把旧 Web Gate 又变成发布前重复人工测试；
- 是否有任何必须在正式 release candidate 上重跑、但当前 Plan遗漏的 deterministic release check。

如果正确，标 `CW-RC-05=CLOSED`。

## 6. Formal release + PRIVATE ChatGPT plugin identity

Planner 顺序：

1. final candidate Critic PASS；
2. canonical `ai-skills-repository-maintainer` producer fast-forward-only 推进 `release` 到 exact candidate；
3. remote readback SHA + 5.5.1 + writing-style 0.5；
4. 更新现有 PRIVATE ChatGPT plugin：
   `plugins_6ad4fc9abae08191a9ecd81879b2c919`
   而不是新建第二个；
5. expected Web version = `0.5.0`，保持 USER / PRIVATE；
6. re-read six Skills/support/script；
7. 与 formal repository generated writing-style 做逐文件 parity；
8. 除已知 host normalization 外任何 drift都停；
9. 最后把 exact release commit merge回 latest main。

请判断：

- 这个顺序是否比“先改私人 plugin 再 release”更安全；
- formal release后若 PRIVATE plugin update失败，是否应保持 Issue #13 DOING 而不是回滚 formal release；
- parity boundary 是否诚实处理 Plugin Creator 的 version/owner normalization；
- 是否应该禁止替换 plugin_id、PUBLIC discoverability 或第二 candidate。

如果正确，标 `CW-RC-06=CLOSED`。

## 7. Issue #13 closure

Plan 要求正式 release、main reintegration、final CI、PRIVATE plugin 0.5.0 identity/parity全部完成后才 DONE。

此前继续 `DOING / writing-style`。

请判断这个 lifecycle 是否正确；没有 GitHub Project mutation surface 时，只记录 exact pending mutation，不让用户手工拖看板。

如果正确，标 `CW-RC-07=CLOSED`。

# Change-impact / anti-expansion

本 plan 不应重新引入任何：

- W2；
- 新 Web Gate；
- product rules；
- new Skill；
- new router/state machine；
- Presentations/Research Authoring changes；
- PIE/Mica；
- release outside writing-style + repository patch metadata。

若发现 plan 里有不必要扩项，作为 blocker指出。

# 输出

给 `PASS` 或 `REVISE`。

若 `REVISE`：

- 使用稳定 finding ID；
- 只要求 release closure 必须修的内容；
- 不重开产品 Gate；
- 自动生成给 Planner 的最小返修 prompt。

若 `PASS`：

明确输出：

```text
DECISION=PASS
APPROVED_PLAN_PATH=docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_PLAN_V0_1_2026-10-19.md
APPROVED_PLAN_COMMIT=8e55b993cf9663947c642fa31cc50d952225b4af
REPOSITORY_BUMP=5.5.0->5.5.1
WRITING_STYLE_BUMP=0.4->0.5
READY_FOR_EXECUTION_PACKAGE=YES
NEXT_HANDOFF=PLANNER
```

并明确：

本 PASS 只批准 release-closure 设计；不授权 Codex、不推进 release、不更新 PRIVATE plugin。

PASS 后下一步是 Planner 基于同一设计冻结 Goal + Kickoff execution package，再交 execution-ready Critic。
