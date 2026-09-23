# Project Thread Handoff ChatGPT Personal Plugin 更新 Prompt

把下面这份 Prompt 复制给 GPT Work / Plugin Creator 使用。运行时把 `PLUGIN_URL_OR_ID` 替换为你自己的 existing personal Plugin URL 或 ID。

```text
你是 Plugin Creator。请更新一个已经存在的 ChatGPT personal Plugin，使它重新打包当前 GitHub main 上的 Project Thread Handoff standalone Skill。

Repository:
YuukiAS/AI_Skills_Collection

Branch:
main

Canonical Skill path:
skills/science/communication/project-thread-handoff/

Existing Plugin:
PLUGIN_URL_OR_ID = <由用户填写>

目标：
canonical Skill on GitHub main
-> 读取 existing personal Plugin
-> 重新生成 skills-only plugin archive
-> 更新 existing Plugin
-> 保持同一 Plugin identity

必须先做：
1. 读取 existing plugin 的当前 metadata、source/current release、manifest version 和 current release id。
2. 读取 GitHub `main` 上 canonical Skill 的完整目录：
   - SKILL.md
   - agents/openai.yaml
   - assets/app-facing.svg
   - evals/trigger_queries.json
3. 记录 `SOURCE_SKILL_COMMIT`，必须是读取 canonical Skill 时对应的 Git commit SHA。
4. 比较 existing plugin 中已打包的 Skill 文件和 canonical source。

打包要求：
1. 使用当前 canonical main Skill 重新生成完整 skills-only plugin package。
2. bundled Skill 必须与 canonical source 保持一致。
3. 不添加 MCP。
4. 不添加 connector。
5. 不添加 Developer Mode dependency。
6. 不添加 external API。
7. 不添加 database。
8. 不添加 app。
9. 不添加 state。
10. `MCP_ADDED = NO`。

Plugin identity / version 要求：
1. 更新 existing Plugin，不创建新 Plugin。
2. 保持 existing plugin name、identity、URL/ID 和用户可见入口。
3. 提升 plugin manifest version。compatible Skill update 默认只做正常 version increment。
4. 不把 Project Thread Handoff 变成中央 Marketplace Plugin；它仍然只是 personal Plugin 中 bundled 的 skills-only distribution wrapper。

并发保护：
1. 每次更新前先取得 current release id。
2. 使用该值作为本次更新的 `expected_release_id` / optimistic-concurrency guard。
3. 不要长期硬编码旧 release id；release id 每次更新后都会变化。
4. 如果 update 失败并提示 release id stale，重新读取 existing plugin current release 后再判断是否可以安全重试。

删除/重命名保护：
如果 canonical source update 删除或重命名了 Plugin 中已有文件，不要假设“上传时省略文件”会删除旧文件。当前 Plugin Creator update 是 overlay/update semantics；遇到这种结构性删除或重命名时，停止并明确报告需要人工处理 stale files，不要继续发布一个可能残留旧文件的 Plugin。

更新成功后，请报告：

PLUGIN_ID = ...
PLUGIN_URL = ...
OLD_VERSION = ...
NEW_VERSION = ...
OLD_RELEASE_ID = ...
NEW_RELEASE_ID = ...
SOURCE_SKILL_COMMIT = ...
MCP_ADDED = NO

同时确认：
- existing Plugin identity preserved = YES
- bundled Skill matches canonical source = YES
- no MCP / connector / Developer Mode dependency / external API / database / app / state added = YES
```
