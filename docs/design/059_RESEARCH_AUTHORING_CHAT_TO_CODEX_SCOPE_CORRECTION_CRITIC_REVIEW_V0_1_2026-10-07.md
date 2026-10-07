# 059 Research Authoring — ChatGPT → Codex scope correction Critic review v0.1

日期：2026-10-07  
角色：独立 Critic  
任务：`research-authoring--formal-production-authoring`  
审查对象：scope correction package @ `497bd2206bb33e316137bcb041e4958624599cbb`

## 结论

```text
RESULT=PASS
SCOPE_CORRECTION=PASS
FAILED_EXPLICIT_ONLY_IMPLEMENTATION_RETIRED=YES
RAW_CODEX_AUTHORING_OWNER_COMPETITION=REMOVED_FROM_CURRENT_0_3_RELEASE_BLOCKER

C2_G1_FAIL=PERMANENT
04a17a904ce522cb4a517cb33f22e062f2bcbc09=FAILED_PROVISIONAL_DEVELOPMENT_ATTEMPT

C3_FINAL_CANDIDATE_COMMIT=NOT_ADMITTED
FINAL_GATES_AUTHORIZED=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO

READY_FOR_PREFINAL_PREPARATION=YES
NEXT_HANDOFF=CODEX
```

## 为什么这次可以 PASS

这次修正终于和用户真正使用方式一致：

```text
ChatGPT Web
-> Research Authoring 写内容、稳定 source、生成生产交接
-> Codex 消费 exact source + handoff
-> repo-grounded production / render / file QA
-> final artifact
-> post-render scientific QA
```

上一轮失败的 pinned-runtime probe 只证明一件事：

```text
Codex 如果直接收到原始科研写作请求，
同名 user/global renderer 可能先于 project-local copy 被读取。
```

它没有证明 ChatGPT → Codex 正式生产链失败。

因此把该问题从当前 0.3 release blocker 中移除是正确的失败归因，不是删除失败证据或降低最终 artifact 标准。

## 原错误恢复已真实退出

从 `8194480f3c6a734ac391e68cda6601b2fa2aec03` 到当前 `497bd2206bb33e316137bcb041e4958624599cbb` 的 tracked diff只有 scope-correction docs/result 与保存的 preflight failure evidence。

没有新的：

- `skills/**` production source 修改；
- `profiles/**` 修改；
- `scripts/**` 修改；
- `tests/**` 修改；
- README / CHANGELOG / VERSION 修改。

因此上一轮未提交的 `explicit_only_skills` / installer overlay / project-local same-name containment实现没有被偷带进候选。

失败 preflight仍被完整保存，且明确保持：

```text
PROFILE_SCOPED_EXPLICIT_DELEGATE_UNSUPPORTED=YES
P2_NOT_CREATED=YES
```

## Gate 修正合理

### G1

G1现在验证真正的 Research Authoring用户入口：ChatGPT wrapper / Web上的自然科研文档请求及其边界。

不再要求 Codex面对同一原始科研写作请求重新竞争 owner。

Codex侧只检查它作为 production consumer时不篡改 frozen scientific meaning。

### G2 / G3

科研文档语义、增量更新、真实 manuscript/source package 与跨文件一致性继续保留，没有因为 scope correction降低科学质量要求。

### G4

G4恢复为真正的端到端能力：

```text
ChatGPT natural authoring
-> stable source + complete handoff
-> Codex consumes exact handoff
-> production/render/file QA
-> final artifact
-> post-render scientific QA
```

这直接对应用户实际消费流程。

没有新增 G5。

## 外部平台核对

当前 OpenAI官方文档仍支持 skills-only plugin；Skills可向 ChatGPT 和 Codex提供可复用工作流，而具体执行能力可以按 surface/runtime不同。

本次修正没有依赖新的跨作用域 Skill优先级、project-local shadowing或同名 Skill覆盖机制，因此不再把已失败的平台假设作为当前产品前提。

## 非阻塞文档瑕疵

`C3_CHAT_TO_CODEX_SCOPE_CORRECTION_RESULT.md` 的 Validation 段仍保留：

```text
To be filled by the Executor before commit
```

但用户交接与当前提交状态已经报告：

```text
git diff --check=PASS
tests.test_research_writing_routing=PASS
tests.test_codex_marketplace=PASS
```

这是 durable result 文档的陈旧占位，不影响 scope correction技术结论，但在 pre-final packet前必须机械改成真实结果，不能带占位进入冻结包。

## 下一步边界

当前还不能启动 final G1-G4。

下一步只允许准备新的 exact-candidate / pre-final admission packet：

1. 以当前 scope-corrected branch为基础核对 Research Authoring production source与 04a17之后无语义漂移；
2. 实际调用已安装 Clear Writing完成 README 读者层检查，并保存 durable evidence；
3. 运行完整 deterministic validation；
4. 对 exact candidate做与新产品链匹配的低成本 development smoke：
   - Codex消费 stable source + handoff；
   - render-only；
   - existing LaTeX compile/debug；
   - existing PDF operations；
   - 不再跑 raw Codex authoring-owner competition；
5. 如果 candidate-owned source没有变化，可以使用新的 exact commit作为 provisional/final-candidate候选身份；不得追认 04a17；
6. 基于 exact candidate重建 ChatGPT skills-only offline wrapper；
7. 冻结修正后的 G1-G4 pre-final packet；
8. 停止并回 Critic；不得启动 final Gate。

## 当前状态

```text
SCOPE_CORRECTION_READY_FOR_CRITIC=PASS
FAILED_EXPLICIT_ONLY_IMPLEMENTATION_RETIRED=YES

P2_FROM_FAILED_PREFLIGHT=NOT_CREATED
C3_FINAL_CANDIDATE_COMMIT=NOT_ADMITTED

FINAL_GATES_NOT_STARTED=YES
READY_FOR_PREFINAL_PREPARATION=YES
NEXT_HANDOFF=CODEX
```
