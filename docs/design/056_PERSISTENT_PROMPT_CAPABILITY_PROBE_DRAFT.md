# 056 Persistent User-Input Capability Probe — Draft

状态：`DRAFT_FOR_CRITIC_REVIEW / NOT_AUTHORIZED_TO_RUN`  
任务：`056_product_delivery_discipline`  
用途：只验证当前 Windows Codex Desktop/App + CLI 在 **Default mode** 下的 user-input transport 生命周期。不是 production implementation，不修改 Bridge Kit、AI_Skills plugin 或项目规则。

## 为什么必须 probe

当前公开 Codex source 已能证明 Default-mode `request_user_input` 与 Plan-mode语义不同：app-server test 期望 Default `is_blocking=false`、Plan `is_blocking=true`。当前 Default-mode instruction 对 truly required input 推荐 concise plain-text question；公开 issue 又报告 Default/Desktop prompt 的 client auto-resolution。Bridge Kit 当前只验证 feature flag 已启用，不能证明 no-expiry / exact-once resume。

因此本 probe 的结果会影响 056 的 transport 选择；在 Critic 审核和用户明确发送本 prompt 前不得执行。

## 运行边界

- 运行位置：Windows Codex Desktop，AI_Skills_Collection checkout 内；
- collaboration mode：必须是 `Default`，不得为了让测试通过切 Plan；
- 不联网；
- 不调用 paid API；
- 不修改 tracked files；
- 不 commit/push/branch；
- 不安装/升级/降级 Codex；
- 不修改 `~/.codex/config.toml`；
- 不启动 watcher、daemon、tmux、Persistent Run、Control 或轮询提醒；
- 唯一允许写入：repo 内 `private/exports/056_persistent_prompt_probe/`，用于本机 probe evidence；
- 用户未回答时不得通过任何其他通道替用户选择。

## 观察时间

公开 issue #34455 描述过 60 秒 grace + 60 秒 countdown 的 auto-resolution 路径；#37472 报告 Default mode 约 1–2 分钟自动 resolve。因此本 probe 使用 `150 seconds` 观察窗。

`150s PASS` 只证明“超过该已知公开窗口仍等待”，不声称数学意义上的无限等待。production no-expiry claim 仍必须绑定实际 installed version 和观察结果。

## Native PASS 条件

全部满足才允许 `NATIVE_DEFAULT_PERSISTENT_PROMPT=PASS`：

1. exact CLI version 与 exact Desktop/App version 可定位；
2. 当前确为 Default mode；
3. feature 状态被实际核实；
4. tool 在该 turn 实际可用；
5. 用户 150 秒不回答期间没有 empty/default auto-resolution；
6. dependent execution 没有在明确回答前继续；
7. 150 秒后用户明确回答一次，task 只 resume 一次；
8. 没有 terminal `BLOCKED` / 自动失败；
9. cancel semantics 不执行 dependent action；
10. probe 没修改 tracked workflow state。

## Negative path

- native FAIL → 不得再声称 feature flag 等于 persistent prompt；进入 durable transcript fallback 测试；
- fallback 成立 → capability 名称只能是 `DURABLE_TRANSCRIPT_WAIT_RESUME`，不得叫 native prompt；
- fallback 也不能可靠恢复 → `HOST_CAPABILITY_GAP`；停止，不新增 watcher/state machine。

## 待 Critic 审核的 Codex prompt

```text
你现在只执行 Task 056 的一个独立 host capability probe：

056_PERSISTENT_PROMPT_CAPABILITY_PROBE

这不是产品开发，不是 workflow implementation，不修改 production skill/plugin，
不修改 Bridge Kit production，不修改任何项目 AGENTS，不创建 execution Goal/branch，
不调用网络或 paid API。

目标只有一个：
验证当前这台 Windows 机器上“当前实际安装的 Codex Desktop/App + CLI”，
在 Default mode 下的 user-input transport 到底是否能够持续等待用户、
不自动 resolve，并在用户明确回答后精确恢复一次。

==================================================
一、严格写入边界
==================================================

只允许在当前 AI_Skills_Collection repo 内写：

private/exports/056_persistent_prompt_probe/

允许创建：

RESULT.md
pre_prompt.json
resume_marker.txt
cancel_marker.txt   # 只有错误实现才可能出现；正确 cancel path 不应创建
fallback_resume_marker.txt

不得修改任何 tracked file。
不得 git add / commit / push / branch / stash / reset / restore。
不得修改 Codex config、feature flags 或安装版本。
不得启动 tmux、Persistent Run、watcher、daemon、Control、后台轮询器或提醒循环。
不得联网。

==================================================
二、版本和模式 preflight
==================================================

先用只读方式记录：

1. `codex --version` 的 exact CLI version；
2. 当前 Codex Desktop/App exact version/build；
   - 优先当前 app 自身可读诊断 / 安装元数据；
   - 不安装工具、不改系统；
   - 如果无法可靠取得，写 `CODEX_APP_VERSION=UNAVAILABLE`，不要猜；
3. 当前 collaboration mode，必须明确为 `Default`；
4. `codex features list`（或当前版本等价的只读 feature discovery）中
   `default_mode_request_user_input` 的真实状态；
5. 当前 `request_user_input` 是否真的列在本 turn 可用 tools 中。

如果当前不是 Default mode：

RESULT=PROBE_INVALID_WRONG_MODE

立即停止。不要切 Plan mode来让测试通过。

把 preflight 写入 RESULT.md。

==================================================
三、Trial A：150 秒 unanswered persistence + exact-once resume
==================================================

开始前：

- 确认 `resume_marker.txt` 不存在；
- 写 `pre_prompt.json`：
  - probe start timestamp（带时区）；
  - CLI/App version；
  - mode；
  - feature state；
  - tool availability；
  - `resume_marker_exists_before=false`。

如果 `request_user_input` 在当前 turn 不可用：

NATIVE_TOOL_AVAILABLE=NO
NATIVE_DEFAULT_PERSISTENT_PROMPT=FAIL

不要假装调用成功，跳到第五节 fallback。

如果工具可用，则只调用一次 `request_user_input`。

问题内容必须表达：

“Task 056 persistent-prompt probe。
请暂时不要回答。请从 prompt 出现开始至少等待 150 秒。
如果 150 秒后这个同一个 prompt 仍然保持可回答状态，选择 `RESUME_TEST`。
不要提前回答，也不要用普通聊天消息替代。
如果它自己消失/自动结束，请不要补救，让 probe 记录真实行为。”

提供明确 option：

RESUME_TEST

记录发起 tool request 前时间 `T0`。

关键要求：

- tool call 发出后不得 sleep/poll/reissue prompt；
- 不得做任何 dependent action；
- 不得写 `resume_marker.txt`；
- 不得把空回答、默认回答或 timeout 当成用户同意；
- 不得因为等待而写 BLOCKED。

当 tool call 返回时记录 `T1` 和 elapsed seconds。

按真实返回分类：

A. 如果在用户明确选择 `RESUME_TEST` 之前 tool 就返回了空答案、默认答案、
   timeout/auto-resolution 或其它非明确回答：

   NATIVE_AUTO_RESOLVED=YES
   NATIVE_EXPLICIT_ANSWER=NO
   NATIVE_DEFAULT_PERSISTENT_PROMPT=FAIL
   DEPENDENT_EXECUTION_ALLOWED=NO

   不得创建 `resume_marker.txt`。

B. 如果用户明确选择 `RESUME_TEST`，且 elapsed >= 150 seconds：

   NATIVE_AUTO_RESOLVED=NO
   NATIVE_EXPLICIT_ANSWER=YES

   此时才创建一次 `resume_marker.txt`，内容包含：
   - 一个随机 probe id；
   - T0/T1；
   - exact answer；
   - `resume_count=1`。

   写完后立刻重读，确认只有一个 marker / resume_count=1。

   NATIVE_150S_PENDING=PASS
   EXACT_ONCE_RESUME=PASS

C. 如果用户明确回答但 elapsed < 150 seconds：

   记录真实情况；
   NATIVE_150S_PENDING=NOT_TESTED_USER_ANSWERED_EARLY

   不得宣称 persistence PASS。

==================================================
四、Trial B：cancel semantics
==================================================

只有 Trial A 结束后才进入。

如果 native tool 不可用，Trial B = NOT_RUN。

否则再调用一次独立 `request_user_input`，问题：

“Task 056 cancel-path probe。
请选择 `CANCEL_TEST`。这表示取消本次 dependent action；
取消后不得创建任何 dependent-action marker，也不得把 task 标成 terminal BLOCKED。”

options：

- CANCEL_TEST
- CONTINUE_TEST

用户选择 `CANCEL_TEST` 后：

- 不创建 `cancel_marker.txt`；
- 写 RESULT.md：
  `CANCEL_SEMANTICS=PASS_NO_DEPENDENT_ACTION`；
- 不把 cancel 改写成 failure/BLOCKED；
- 不重复询问。

如果 UI 提供独立的 dismiss/cancel 控件且用户实际用了它，另外记录：

NATIVE_UI_DISMISS_CANCEL=PASS

如果没有这类控件，只测试了 `CANCEL_TEST` option，则诚实写：

NATIVE_UI_DISMISS_CANCEL=NOT_TESTED

==================================================
五、Native fail 时的 durable transcript fallback
==================================================

只有 Native FAIL / tool unavailable / auto-resolved 时执行本节。

不要创建 watcher、轮询或第二套状态机。

先在 RESULT.md 写：

FALLBACK_REQUIRED=YES
FALLBACK_TYPE=DURABLE_TRANSCRIPT_WAIT_RESUME
NATIVE_PERSISTENT_PROMPT_CLAIM=NOT_SUPPORTED_BY_THIS_PROBE
RESUME_POINT=WAITING_FOR_LITERAL_FALLBACK_RESUME

然后向用户发送一条普通、清楚、单步、不会被你自己当成默认已回答的聊天问题：

“056 fallback probe：native Default-mode request_user_input 未通过 persistent test。
请在方便时回复精确文本 `FALLBACK_RESUME_056`。
在你回复之前，我不会继续 dependent step；这不是 native prompt，只是在 transcript 中保留的可恢复等待点。”

发送后结束当前 turn。

不要继续执行，不要轮询，不要写 BLOCKED。

当用户后续在同一个 Codex thread 回复精确文本：

FALLBACK_RESUME_056

才允许：

1. 重读 `private/exports/056_persistent_prompt_probe/RESULT.md`；
2. 确认 RESUME_POINT 正确；
3. 创建一次 `fallback_resume_marker.txt`；
4. 写 `fallback_resume_count=1`；
5. 不重新运行前面 probe；
6. 不重复问同一个问题。

若这个跨 turn resume 无法可靠恢复：

FALLBACK_RESUME=FAIL
HOST_CAPABILITY_GAP=YES

停止，不设计新 daemon/state machine。

==================================================
六、workflow / retry 边界记录
==================================================

这是 host transport probe，不得伪造不存在的 workflow counter。

记录：

- 本次是否出现 terminal `BLOCKED`；
- 是否因为等待自动重跑/重试；
- 是否修改任何 tracked workflow state；
- 若当前 probe 环境没有真实 review/repair counter，写：
  `WORKFLOW_COUNTER_PRESERVATION=NOT_DIRECTLY_TESTED_BY_HOST_PROBE`。

不要把 `NOT_DIRECTLY_TESTED` 写成 PASS。
完整 wait/retry-budget 行为以后仍需 normal-entry workflow capability gate。

==================================================
七、最终 RESULT.md
==================================================

至少给出：

RESULT = PASS | FAIL | PARTIAL
CODEX_CLI_VERSION =
CODEX_APP_VERSION =
VERSION_IDENTITY_COMPLETE = YES | NO
COLLABORATION_MODE = DEFAULT | OTHER
DEFAULT_MODE_REQUEST_USER_INPUT_FEATURE = ENABLED | DISABLED | UNKNOWN
NATIVE_TOOL_AVAILABLE = YES | NO
T0 =
T1 =
ELAPSED_SECONDS =
NATIVE_AUTO_RESOLVED = YES | NO | NOT_TESTED
EMPTY_OR_DEFAULT_ANSWER_RETURNED = YES | NO | NOT_TESTED
NATIVE_150S_PENDING = PASS | FAIL | NOT_TESTED
DEPENDENT_EXECUTION_BEFORE_EXPLICIT_ANSWER = YES | NO | UNKNOWN
EXACT_ONCE_RESUME = PASS | FAIL | NOT_TESTED
CANCEL_SEMANTICS = PASS | FAIL | NOT_TESTED
NATIVE_UI_DISMISS_CANCEL = PASS | FAIL | NOT_TESTED
TERMINAL_BLOCKED_EMITTED = YES | NO
AUTOMATIC_RETRY_OBSERVED = YES | NO
TRACKED_WORKFLOW_STATE_CHANGED = YES | NO
WORKFLOW_COUNTER_PRESERVATION = NOT_DIRECTLY_TESTED_BY_HOST_PROBE
FALLBACK_REQUIRED = YES | NO
FALLBACK_RESUME = PASS | FAIL | NOT_RUN
HOST_CAPABILITY_GAP = YES | NO | UNDETERMINED
NATIVE_DEFAULT_PERSISTENT_PROMPT = PASS | FAIL | NOT_PROVEN

最后只用几句话解释：

- 当前 installed Default mode 是否真正支持 150s persistent native prompt；
- 是否出现 auto-resolve/empty answer；
- 是否 exact-once resume；
- fallback 是否可恢复；
- 该 probe 证明什么、不证明什么。

不要修改 repo policy。
不要根据 FAIL 自动开始 Bridge Kit 修复。
NEXT_HANDOFF=GPT_PLANNER_AND_CRITIC
```
