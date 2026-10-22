# Quickstart

这是当前 `0.11.x`（`0.11.1` 补丁）的最短使用流程；机器安装应使用正式 `release` checkout，不追随任意开发分支。

## 1. 初始化真实项目

先本地安装一次：

```bash
pip install -e /path/to/GPT_Codex_AI_Bridge_Kit
```

以后进入任意真实项目根目录，运行：

```bash
ai-bridge
```

也可以指定目标项目：

```bash
ai-bridge init --target /path/to/project
```

如果目标项目已经有同名模板文件，默认不会覆盖。需要覆盖时运行：

```bash
ai-bridge init --target /path/to/project --force
```

`ai-bridge` 默认会创建或更新 `AGENTS.md` 中的协议片段，并安装 repo-local Codex skill。ChatGPT/GitHub MCP 读取 `prompts/CHATGPT_RULES.md`，Codex 读取 `prompts/AGENT_RULES.md`。长期论文和报告知识写入 `docs/wiki/`；任务、实验和脚本产物写入 `results/<task_key>/`。

如果 ChatGPT 没有自动读取仓库规则，只需要在该 ChatGPT Project 的长期 instructions 里放一次：

```text
使用 GitHub MCP 处理仓库时，先读取 AGENTS.md 和 prompts/CHATGPT_RULES.md；需要 Codex 执行时写 prompts/tasks/<task_key>.md。新 task_key 采用 `<scope-token>--<goal-token>`，两个部分都用 lowercase kebab-case；历史 `<id>_<short_slug>` 任务仍可读取和验证。
```

以后日常不需要再记完整提示词。

## 2. 日常三句话

给 ChatGPT：

```text
读取 AGENTS.md 和 prompts/CHATGPT_RULES.md，根据当前项目状态生成新的 prompts/tasks/repo--fix-ci.md。
```

给 Codex：

```text
读取 AGENTS.md、prompts/AGENT_RULES.md 和 prompts/tasks/repo--fix-ci.md，按任务单授权执行，完成后写 results/repo--fix-ci/result.md；如有文件型产物，写到 results/repo--fix-ci/，并写 results/repo--fix-ci/MANIFEST.md。
```

再给 ChatGPT：

```text
读取 prompts/tasks/repo--fix-ci.md、results/repo--fix-ci/result.md、results/repo--fix-ci/MANIFEST.md 和必要产物，写 results/repo--fix-ci/review.md，并判断下一步是 GO、STOP、NEEDS_EVIDENCE、NEEDS_HUMAN_APPROVAL 还是 OPEN_NEXT_TASK。
```

## 3. 研究笔记不要变成任务

如果只是研究笔记、方案分析、会议记录、文献总结、实验复盘或想法沉淀，给 ChatGPT：

```text
这只是后续参考，请写到 docs/notes/<date>_<topic>.md，不要生成 Codex task。
```

如果后来要执行 note 里的某个方向，再让 ChatGPT 从 note 中提炼一张新的 `prompts/tasks/<task_key>.md`。

## 4. 文件产物写入 results

如果 Codex 或脚本会生成日志、CSV/JSON、图、压缩包、评估表、长报告或中间输出，任务单应明确：

```text
执行报告写 results/<task_key>/result.md；文件型产物写 results/<task_key>/；产物索引写 results/<task_key>/MANIFEST.md；不要塞进 prompts/tasks/。
```

`results/<task_key>/result.md` 只记录摘要、证据、命令、失败信息、diff 摘要、`results/<task_key>/MANIFEST.md` 和产物清单。

## 5. 论文和 report 写入 wiki

如果仓库里有论文 PDF、论文 Markdown、报告或 Codex 生成的长 report，需要以后复用，不要每次临时重读。给 ChatGPT：

```text
读取 AGENTS.md、prompts/CHATGPT_RULES.md 和 docs/wiki/index.md，把这篇论文或 report 沉淀到 docs/wiki/，更新 index.md 和 log.md；如果要执行其中某个方向，再生成 prompts/tasks/<task_key>.md。
```

常见两步循环：

```text
先让 Codex 总结指定 report 并写 results/repo--summarize-report/result.md；再让 ChatGPT 读取 prompts/tasks/repo--summarize-report.md、result、MANIFEST 和 docs/wiki/index.md，写 review，必要时沉淀到 docs/wiki/，然后生成下一张 task。
```

## 6. 验证项目

```bash
ai-bridge validate --target /path/to/project
```

输出 `OK` 表示结构和任务文件基本合规。输出 `ERROR` 或 `WARN` 时，先修正路径、frontmatter 或命名，再交给 Codex 执行。

机器级规则使用当前显示名 **Machine Policy**，兼容命令仍是 `ai-bridge host ...`。
如果已经在当前分支完成任务，并且同名远端分支已经存在，GitHub HTTPS 的低打扰发布
使用受边界约束的入口，而不是原始 `git push origin main`：

```bash
ai-bridge host publish-current-branch \
  --expected-repo YuukiAS/GPT_Codex_AI_Bridge_Kit \
  --expected-branch work/repo--feature
```

这两个参数只是 equality assertion；真实 repo、branch、upstream、remote ref 和
transport/credential/hook 边界都由 helper 从当前 Git 状态重新读取。
这个入口只把 `https://github.com/<owner>/<repo>.git` 加上现有
system/global/gh credential helper 视为可信低打扰路径。SSH、scp-style
或 custom remote 会回到普通原始 Git push 审批；Bridge Kit 不配置 SSH key、agent
或 `known_hosts`。

Bridge-managed Lite 执行使用真正的启动入口，而不是手工拼接 `codex exec`：

```bash
ai-bridge task run \
  --target /path/to/project \
  --task-key repo--fix-ci
```

它先绑定当前 repo/worktree/branch/HEAD 与 `AGENTS.md`、执行规则和 task 的 exact
commit blob；任一 mandatory source 不一致时不会创建 Codex child。

## 7. 可选：选择更重的 workflow

日常默认是 Lite，也就是 `ai-bridge init` / `ai-bridge validate` 安装的基础交接。

如果需要 GPT 先规划、Codex 执行、再由 GPT 独立复核，使用 Reviewed Mode。命令仍保持兼容名称：

```bash
ai-bridge reviewed-handoff install --target /path/to/project
ai-bridge reviewed-handoff validate --target /path/to/project
```

如果任务属于高风险科研、生产或安全敏感工作，且需要严格多角色控制与验证，使用 Controlled Mode。命令仍保持兼容名称：

```bash
ai-bridge agent-flow install --target /path/to/project
ai-bridge agent-flow validate --target /path/to/project
```

## 8. 可选：给长期 Goal 启用 Persistent Run

如果某个已经冻结的 Goal 需要长时间运行，并且希望它在 Codex / SSH 断开后继续执行，可以给仓库安装 Persistent Run：

```bash
ai-bridge persistent-run install --target /path/to/project
ai-bridge persistent-run validate --target /path/to/project
```

然后在具体 Goal 中复制或引用：

```text
automation/persistent_run/CONTRACT_TEMPLATE.md
```

GPT 写这个 Goal/task 时要先把三件事分开：启动前授权预检、进程寿命归属、项目原生进度报告。`run overnight`、`unattended`、`run until morning`、`multi-hour` 或 `leave it running` 只说明要做这套判断，不自动意味着 Persistent Run/tmux，也不代表必须把 Lite 任务改成 Reviewed Mode / Controlled Mode 或 `task_type: "controller"`。

如果任务是 scheduler-owned batch（例如已接受的 `sbatch`）或 already-detached service/job，让调度器或服务拥有寿命，并写清资源/调度器授权边界和项目原生进度证据，不要仅因 duration 增加 tmux。只有 terminal-owned foreground process/orchestrator 必须 survive Codex/SSH/terminal disconnect，且没有项目原生 owner 已经提供寿命时，才写 Persistent Run contract。如果这种断线存活能力确实必需，但仓库没有安装 Persistent Run，也没有用户选择的等价项目原生合同，不要把任务写成普通 live Codex session。

真正启动前，由用户生成并发送 kickoff 授权：

```bash
ai-bridge persistent-run prompt kickoff \
  --target /path/to/project \
  --goal prompts/tasks/repo--long-run.md
```

这个命令只打印授权文本，不会启动 tmux。打印结果包含 Goal SHA-256 和 exact
`persistent-run start` 命令。真正启动后，一个 run identity 只有一个 full-hash tmux
session、一个 supervisor、一个 binding JSON 和一个 child；用相同 Goal SHA-256 的
`persistent-run status` 查询运行事实。active run 再次 `start` 不会产生第二个 child；
stale、mismatch、partial start 或 supervisor loss 不会自动 relaunch、takeover 或猜测
terminal；没有 progress 时明确返回 `UNKNOWN`。异常状态先用 `persistent-run recover`
分类，只有 `SAFE_TO_CLOSE_STALE` 才能用带 exact launch id 的
`persistent-run resolve --close-stale` 关闭重复执行风险；不要删除 machine state。
`bridge-child` 用 `persistent-run progress update` 原子写进度，count/fraction 至少三个
有效点且跨十分钟后才会出现 ETA。它不依赖 app-server、Progress display thread 或
持久 Codex thread。

Persistent Run 不把 session/PID/heartbeat 当作完成，也不自动 fallback 到 `setsid`、
`nohup`、裸后台 `&`、`screen` 或 `sudo`。Lite / Reviewed Mode / Controlled Mode 的
workflow 选择和原 Goal 完成标准保持不变。

通知 cadence 默认 60 分钟，非测试不得低于 15 分钟。普通 count/fraction 更新只刷新
latest/history；定时通知按上次逻辑投递计时，而不是按相邻 observation 计时。
阶段切换、stalled/blocked/failed、runtime terminal 或重大 ETA 变化可提前通知，
已知 ETA 与 `UNKNOWN` 互换也属于重大变化。Persistent Run 不是第四种 workflow；
Program Run 尚未实现，不会自主生成下一个 Goal 或自动串联任务。

Codex 收到 task 后会在实质执行前检查是否存在可预见的 approval-sensitive effect。
仓库里的 Goal/Plan/contract 只证明 frozen scope，不等于当前用户授权；如果当前用户
消息没有包含同一个 frozen Goal 的 bounded kickoff 授权，Codex 应先显示 kickoff 并
等待用户发送，而不是先启动 tmux 或做大量前置工作。

## 9. 可选：启用机器级邮件通知

Notifier 一台机器只配置一次，secret 固定保存在
`~/.ai-bridge/private/notifier.env`，不会复制进新仓库，也不能被生产进程的
`AI_BRIDGE_NOTIFY_*` 环境变量覆盖。自动通知默认 `OFF`；只有 Lite task、Review
REQUEST、Control REQUEST 或 Persistent contract 明确启用才会发送。

```bash
ai-bridge private sync --profile notifier
ai-bridge notifier validate
ai-bridge notifier status
```

有旧项目配置时可用 `ai-bridge notifier migrate-legacy --project /path/to/repo`，
不会删除旧文件或覆盖冲突配置。没有旧配置时，只在本机编辑权限为 `0600` 的上述
machine 文件，填入发件 Gmail、App Password、FROM、默认 TO 和 subject prefix；
不要把密码发到对话或提交到仓库。新项目直接复用机器配置，`recipient_override`
只影响当前逻辑投递，不改变默认收件人。需要真实测试邮件时，另行明确授权后才运行
`ai-bridge notifier send-test`。

自动通知使用 installed `writing-fidelity + response-clarity`；失败就用 deterministic
fallback，模型 retry=0。`SMTP_ACCEPTED` / `send-test` 成功只表示 SMTP server 接受
消息，不保证收件箱已投递。Clear Writing、
SMTP 或通知 helper 失败都不会回滚 workflow、改变语义结论或杀死 primary child；
`DELIVERY_UNKNOWN` 只能在明确接受可能重复后显式 retry。

## 10. 可选：同步论文目录到 Overleaf

如果项目是科研 monorepo，Codex 仍应在整个 repository 根目录工作；Overleaf 只应接收论文 publication root，例如 `paper/manuscript`。Overleaf 本身不能从一个 GitHub monorepo 中只 Pull 某个子目录，Overleaf Bridge 是在本机把该目录投影到 Overleaf Git project。

```bash
ai-bridge overleaf install \
  --target /path/to/research-repo \
  --paper-root paper/manuscript
```

在 Overleaf 创建 Blank Project、删除默认 `main.tex` 并取得 Git URL 后：

```bash
ai-bridge overleaf connect \
  --target /path/to/research-repo \
  --remote-url https://git@git.overleaf.com/<PROJECT_ID> \
  --bootstrap
```

新旧 Overleaf 项目可能使用不同默认分支。Bridge Kit 会在 `connect` 时读取
Overleaf Git remote 实际声明的分支，不需要也不应该在科研仓库配置
`main/master`。

日常使用：

```bash
ai-bridge overleaf status --target /path/to/research-repo
ai-bridge overleaf push --target /path/to/research-repo
ai-bridge overleaf pull --target /path/to/research-repo
ai-bridge overleaf validate --target /path/to/research-repo
```

`push` 会拒绝覆盖未拉取的 Overleaf 远端修改；`pull` 会把 Overleaf 改动留在本地 working tree，不会自动 commit 或 `git push origin main`。Overleaf token 由 Git credential helper 处理，不写入 Bridge Kit config。

同步前先让非 excluded 的 `paper_root` 保持 clean：tracked、staged、deleted、renamed 或 untracked manuscript 文件都应先 review/compile/commit，避免未提交草稿被用作 baseline 或被 pull 覆盖。`exclude_paths` 只用于不参与 Overleaf 编译的 GitHub-only 文件；编译需要的 `.tex`、`.bib`、figures、tables 和 style/class 文件必须留在 publication projection 中。

每台机器的 `connection.json` 和 `mirror/` 都在 `${AI_BRIDGE_STATE_HOME:-~/.ai-bridge}/overleaf/<repo-id>/`，不提交到 GitHub；多台机器要各自 `connect`。Overleaf Bridge 不会自动同步，local 和 Overleaf 双边变化时会 fail closed。
