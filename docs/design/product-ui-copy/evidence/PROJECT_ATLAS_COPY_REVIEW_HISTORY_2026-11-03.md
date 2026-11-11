# Project Atlas 用户可见文案逐项返工证据 — 2026-11-03

这份文件保存 Project Atlas A/B 在实施前连续内容审查中**每一条实际 REVISE / REJECT 以及后续再次发现的漏项**。它是 Frontend Design、Clear Writing / Product UI Copy 与未来 artifact-content-design 的长期回归证据，不是 Project Atlas 的产品规范。

## 范围与来源

- 第一轮 A：`prototype/atlas-a@086801e26543f2932233657b5682a460d4aec9eb`
- 第一轮 B：`prototype/atlas-b@52d07fbea43addf5292d6fba6cc111d6cdadb88a`
- 第二轮 A：`prototype/atlas-a@a9d4fd4e5e5f1db9a49fee187b9b04e14cb5fe7b`
- 第二轮 B：`prototype/atlas-b@2b534c63c648e71f1bf3bd1160804c61b13437e1`
- 第三轮：2026-11-03 独立终审，尚未应用到 Atlas 分支；用于证明前两轮 `COPY_REVIEW=PASS` 后仍存在的自然语言与动态状态覆盖缺口。

## 数量

| 阶段 | A | B |
|---|---:|---:|
| 第一轮 REVISE | 472 | 139 |
| 第一轮 REJECT | 36 | 39 |
| 第二轮新增/再次修改 | 72 | 25 |
| 第三轮独立终审新发现 | 14 | 0 |

第一轮完整清单共有 A 2682 条、B 381 条。下面不重复 ACCEPT 项，只保留所有实际发生过内容变化或删除的条目；因此每一条返工都可单独回放。

## 第一轮 A：全部 508 条修改 / 删除

| ID | 界面 / 位置 | 原文 | 处理 | 最终文案 | 原因 |
|---|---|---|---|---|---|
| A-0011 | 需要我 / text / `body>div#content>div>article>a` | 阅读数值方法地图，确定下一步数值路线。 | REVISE | 打开数值方法地图，在可行方案中确定下一步要验证的方法。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0015 | 需要我 / 待我操作 / text / `body>div#content>div>header>div:nth-of-type(1)>h1` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0016 | 需要我 / 待我操作 / text / `body>div#content>div>p:nth-of-type(1)` | 只显示目前确实需要本人作出的判断。执行器能完成的测试与修复，继续留在各项目内。 | REVISE | 这里只显示已经准备好、现在就需要你完成的判断。其他测试和修复仍留在各项目中。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0017 | 需要我 / 待我操作 / text / `body>div#content>div>p:nth-of-type(2)` | 未来需要的审批会在前提成熟后出现。课程教师决定、日常软件 QA 和缺少资料，不自动变成本人待办。 | REVISE | 尚未准备好的选择不会提前出现；课程教师决定和日常软件检查也不会算作你的待办。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0018 | 需要我 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0029 | 需要我 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0041 | 需要我 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-0045 | 需要我 / 待我操作 / text / `body>span#tab-title` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0053 | 空筛选状态 / 全部项目 / attr:aria-label / `body>select#focus-filter` | 按关注与本人事项筛选 | REVISE | 按关注与需要我筛选 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0059 | 空筛选状态 / 全部项目 / option / `body>select#focus-filter` | 待本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0081 | 空筛选状态 / 全部项目 / text / `body>div#content>div>div:nth-of-type(1)>span` | 0 项 · 关注顺序优先 | REVISE | 0 项 · 先显示当前关注 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0088 | 空筛选状态 / text / `body>div#content>div>div:nth-of-type(2)>table>thead>tr>th:nth-of-type(7)` | 本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0092 | 空筛选状态 / 全部项目 / text / `body>div#content>div>header>div:nth-of-type(2)` | 登记与关注分开 | REVISE | 20 个项目 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0093 | 空筛选状态 / 全部项目 / text / `body>div#content>div>header>div:nth-of-type(2)` | 20 个项目 | REVISE | 按关注顺序排列 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0094 | 空筛选状态 / 全部项目 / text / `body>div#content>div>p` | “—”表示当前没有对应记录；“未确认”保留证据边界。状态由原项目提供，关注顺序由本人决定。长内容可进入项目页完整阅读。 | REVISE | “—”表示当前没有记录；“未确认”表示资料还没核实。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0095 | 空筛选状态 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0106 | 空筛选状态 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0118 | 空筛选状态 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-0130 | 全部项目 / 全部项目 / attr:aria-label / `body>select#focus-filter` | 按关注与本人事项筛选 | REVISE | 按关注与需要我筛选 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0136 | 全部项目 / 全部项目 / option / `body>select#focus-filter` | 待本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0158 | 全部项目 / 全部项目 / text / `body>div#content>div>div:nth-of-type(1)>span` | 20 项 · 关注顺序优先 | REVISE | 20 项 · 先显示当前关注 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0161 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(3)>span` | 数值路线待定 | REVISE | 数值方法仍待确定 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0163 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(5)>span` | 明确必要前置条件，再选择下一步方法。 | REVISE | 先明确必要前置条件，再解决当前方法的可靠性问题，之后才能进行完整验证。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0165 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(7)>span` | 待本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0177 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(11)>td:nth-of-type(5)>span` | 修正旧兼容入口结构，再配置灾备凭据并验收。 | REVISE | 先修复旧设备兼容入口，再配置灾备所需凭据，并实际检查网页迁移入口是否可用。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0191 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(13)>td:nth-of-type(5)>span` | 补齐测试环境匹配验收，再形成上线决策包。 | REVISE | 先在测试环境完成真实匹配流程检查；确认结果可靠后，再决定是否启用真实匹配。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0203 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(15)>td:nth-of-type(3)>span` | 重建设计已冻结 | REVISE | 底层重建方案已确定 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0205 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(15)>td:nth-of-type(5)>span` | 实现重建基础，再接入低内存模式。 | REVISE | 先把插件底层和 ChatGPT 兼容方式做稳定，避免页面一变功能就坏。之后优先恢复长对话优化，再做高亮和 PDF。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0238 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(2)>td:nth-of-type(3)>span` | 选题重整 | REVISE | 重新梳理选题 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0240 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(2)>td:nth-of-type(5)>span` | 整合三份根因研究与导师反馈，再决定新一轮选题。 | REVISE | 先总结前 8 轮为什么一直没选出值得长期投入的方向，并结合导师反馈改进选题方法，再决定是否开始下一轮。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0252 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(3)>span` | 验证器待修 | REVISE | 课程验证器仍需修正 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0254 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(5)>span` | 按三份限定修复包修正验证器，再复验课程材料。 | REVISE | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0259 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(4)>td:nth-of-type(3)>span` | 候选待补证 | REVISE | Windows 新主题仍待实际验证 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0261 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(4)>td:nth-of-type(5)>span` | 完成验收器加固，补齐候选的原生界面证据。 | REVISE | 先让两个 Windows 新主题都能实际运行，并补齐真实界面验证；准备好后再由用户选一个继续。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0275 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(6)>td:nth-of-type(5)>span` | 继续写作交付验收；具体顺序见正式维护看板。 | REVISE | 继续完善写作交付、科研文档和交付检查；具体顺序见维护看板。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0287 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(8)>td:nth-of-type(3)>span` | 0.2 已验收 | REVISE | 0.2 已完成并确认可用 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0305 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>thead>tr>th:nth-of-type(7)` | 本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0308 | 全部项目 / 全部项目 / text / `body>div#content>div>header>div:nth-of-type(2)` | 登记与关注分开 | REVISE | 20 个项目 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0309 | 全部项目 / 全部项目 / text / `body>div#content>div>header>div:nth-of-type(2)` | 20 个项目 | REVISE | 按关注顺序排列 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0310 | 全部项目 / 全部项目 / text / `body>div#content>div>p` | “—”表示当前没有对应记录；“未确认”保留证据边界。状态由原项目提供，关注顺序由本人决定。长内容可进入项目页完整阅读。 | REVISE | “—”表示当前没有记录；“未确认”表示资料还没核实。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0311 | 全部项目 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0322 | 全部项目 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0334 | 全部项目 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-0346 | 需要留意筛选 / 全部项目 / attr:aria-label / `body>select#focus-filter` | 按关注与本人事项筛选 | REVISE | 按关注与需要我筛选 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0352 | 需要留意筛选 / 全部项目 / option / `body>select#focus-filter` | 待本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0374 | 需要留意筛选 / 全部项目 / text / `body>div#content>div>div:nth-of-type(1)>span` | 2 项 · 关注顺序优先 | REVISE | 2 项 · 先显示当前关注 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0377 | 需要留意筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(3)>span` | 数值路线待定 | REVISE | 数值方法仍待确定 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0379 | 需要留意筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(5)>span` | 明确必要前置条件，再选择下一步方法。 | REVISE | 先明确必要前置条件，再解决当前方法的可靠性问题，之后才能进行完整验证。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0381 | 需要留意筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(7)>span` | 待本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0386 | 需要留意筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(2)>td:nth-of-type(5)>span` | 修正旧兼容入口结构，再配置灾备凭据并验收。 | REVISE | 先修复旧设备兼容入口，再配置灾备所需凭据，并实际检查网页迁移入口是否可用。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0395 | 需要留意筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>thead>tr>th:nth-of-type(7)` | 本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0398 | 需要留意筛选 / 全部项目 / text / `body>div#content>div>header>div:nth-of-type(2)` | 登记与关注分开 | REVISE | 20 个项目 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0399 | 需要留意筛选 / 全部项目 / text / `body>div#content>div>header>div:nth-of-type(2)` | 20 个项目 | REVISE | 按关注顺序排列 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0400 | 需要留意筛选 / 全部项目 / text / `body>div#content>div>p` | “—”表示当前没有对应记录；“未确认”保留证据边界。状态由原项目提供，关注顺序由本人决定。长内容可进入项目页完整阅读。 | REVISE | “—”表示当前没有记录；“未确认”表示资料还没核实。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0401 | 需要留意筛选 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0412 | 需要留意筛选 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0424 | 需要留意筛选 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-0436 | 47 行容量 / 容量样张 / attr:aria-label / `body>select#focus-filter` | 按关注与本人事项筛选 | REVISE | 按关注与需要我筛选 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0442 | 47 行容量 / 容量样张 / option / `body>select#focus-filter` | 待本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0465 | 47 行容量 / 容量样张 / text / `body>div#content>div>div:nth-of-type(2)>span` | 47 项 · 关注顺序优先 | REVISE | 47 项 · 先显示当前关注 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0468 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(3)>span` | 数值路线待定 | REVISE | 数值方法仍待确定 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0470 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(5)>span` | 明确必要前置条件，再选择下一步方法。 | REVISE | 先明确必要前置条件，再解决当前方法的可靠性问题，之后才能进行完整验证。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0472 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(7)>span` | 待本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0491 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(12)>td:nth-of-type(3)>span` | 0.2 已验收 | REVISE | 0.2 已完成并确认可用 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0530 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(17)>td:nth-of-type(5)>span` | 修正旧兼容入口结构，再配置灾备凭据并验收。 | REVISE | 先修复旧设备兼容入口，再配置灾备所需凭据，并实际检查网页迁移入口是否可用。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0550 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(2)>td:nth-of-type(3)>span` | 选题重整 | REVISE | 重新梳理选题 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0552 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(2)>td:nth-of-type(5)>span` | 整合三份根因研究与导师反馈，再决定新一轮选题。 | REVISE | 先总结前 8 轮为什么一直没选出值得长期投入的方向，并结合导师反馈改进选题方法，再决定是否开始下一轮。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0559 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(20)>td:nth-of-type(5)>span` | 补齐测试环境匹配验收，再形成上线决策包。 | REVISE | 先在测试环境完成真实匹配流程检查；确认结果可靠后，再决定是否启用真实匹配。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0635 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(3)>span` | 验证器待修 | REVISE | 课程验证器仍需修正 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0637 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(5)>span` | 按三份限定修复包修正验证器，再复验课程材料。 | REVISE | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0642 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(30)>td:nth-of-type(3)>span` | 重建设计已冻结 | REVISE | 底层重建方案已确定 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0644 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(30)>td:nth-of-type(5)>span` | 实现重建基础，再接入低内存模式。 | REVISE | 先把插件底层和 ChatGPT 兼容方式做稳定，避免页面一变功能就坏。之后优先恢复长对话优化，再做高亮和 PDF。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0719 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(4)>td:nth-of-type(3)>span` | 候选待补证 | REVISE | Windows 新主题仍待实际验证 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0721 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(4)>td:nth-of-type(5)>span` | 完成验收器加固，补齐候选的原生界面证据。 | REVISE | 先让两个 Windows 新主题都能实际运行，并补齐真实界面验证；准备好后再由用户选一个继续。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0796 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(6)>td:nth-of-type(5)>span` | 继续写作交付验收；具体顺序见正式维护看板。 | REVISE | 继续完善写作交付、科研文档和交付检查；具体顺序见维护看板。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0828 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>thead>tr>th:nth-of-type(7)` | 本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0833 | 47 行容量 / 容量样张 / text / `body>div#content>div>p` | “—”表示当前没有对应记录；“未确认”保留证据边界。状态由原项目提供，关注顺序由本人决定。长内容可进入项目页完整阅读。 | REVISE | “—”表示当前没有记录；“未确认”表示资料还没核实。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0834 | 47 行容量 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0845 | 47 行容量 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0857 | 47 行容量 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-0887 | 近期节点 / 近期节点 / text / `body>div#content>div>div>a` | 打开冻结课程时刻表 | REVISE | 打开课程时刻表 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0894 | 近期节点 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0905 | 近期节点 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0917 | 近期节点 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-0929 | 当前关注筛选 / 全部项目 / attr:aria-label / `body>select#focus-filter` | 按关注与本人事项筛选 | REVISE | 按关注与需要我筛选 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0935 | 当前关注筛选 / 全部项目 / option / `body>select#focus-filter` | 待本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0957 | 当前关注筛选 / 全部项目 / text / `body>div#content>div>div:nth-of-type(1)>span` | 4 项 · 关注顺序优先 | REVISE | 4 项 · 先显示当前关注 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0960 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(3)>span` | 数值路线待定 | REVISE | 数值方法仍待确定 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0962 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(5)>span` | 明确必要前置条件，再选择下一步方法。 | REVISE | 先明确必要前置条件，再解决当前方法的可靠性问题，之后才能进行完整验证。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0964 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(1)>td:nth-of-type(7)>span` | 待本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0967 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(2)>td:nth-of-type(3)>span` | 选题重整 | REVISE | 重新梳理选题 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0969 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(2)>td:nth-of-type(5)>span` | 整合三份根因研究与导师反馈，再决定新一轮选题。 | REVISE | 先总结前 8 轮为什么一直没选出值得长期投入的方向，并结合导师反馈改进选题方法，再决定是否开始下一轮。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0974 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(3)>span` | 验证器待修 | REVISE | 课程验证器仍需修正 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0976 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(5)>span` | 按三份限定修复包修正验证器，再复验课程材料。 | REVISE | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0981 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(4)>td:nth-of-type(3)>span` | 候选待补证 | REVISE | Windows 新主题仍待实际验证 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0983 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(4)>td:nth-of-type(5)>span` | 完成验收器加固，补齐候选的原生界面证据。 | REVISE | 先让两个 Windows 新主题都能实际运行，并补齐真实界面验证；准备好后再由用户选一个继续。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-0992 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>thead>tr>th:nth-of-type(7)` | 本人 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0995 | 当前关注筛选 / 全部项目 / text / `body>div#content>div>header>div:nth-of-type(2)` | 登记与关注分开 | REVISE | 20 个项目 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0996 | 当前关注筛选 / 全部项目 / text / `body>div#content>div>header>div:nth-of-type(2)` | 20 个项目 | REVISE | 按关注顺序排列 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-0997 | 当前关注筛选 / 全部项目 / text / `body>div#content>div>p` | “—”表示当前没有对应记录；“未确认”保留证据边界。状态由原项目提供，关注顺序由本人决定。长内容可进入项目页完整阅读。 | REVISE | “—”表示当前没有记录；“未确认”表示资料还没核实。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-0998 | 当前关注筛选 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1009 | 当前关注筛选 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1021 | 当前关注筛选 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1036 | 深色首页 / text / `body>div#content>div>div>aside>section:nth-of-type(1)>article>a` | 阅读数值方法地图，确定下一步数值路线。 | REVISE | 打开数值方法地图，在可行方案中确定下一步要验证的方法。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1040 | 深色首页 / 待我处理 / text / `body>div#content>div>div>aside>section:nth-of-type(1)>div>h2` | 待我处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1041 | 深色首页 / 待我处理 / text / `body>div#content>div>div>aside>section:nth-of-type(1)>p` | 仅显示已就绪、须由本人处理的事项。 | REVISE | 只显示已经准备好、现在必须由本人完成的事项。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1049 | 深色首页 / 未来 30 天 / text / `body>div#content>div>div>aside>section:nth-of-type(2)>p` | 仅显示已确认日期。课程节点不等于本人待办。 | REVISE | 只显示已确认日期；课程日期不会自动变成你的待办。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1054 | 深色首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(1)>div:nth-of-type(1)` | 科研 · 方法验证 · 数值路线待定 | REVISE | 科研 · 方法验证 · 数值方法仍待确定 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1056 | 深色首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(1)>div:nth-of-type(2)` | 明确必要前置条件，再选择下一步方法。 | REVISE | 先明确必要前置条件，再解决当前方法的可靠性问题，之后才能进行完整验证。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1058 | 深色首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(2)>div:nth-of-type(1)` | 科研 · 整合八轮研究与导师反馈 · 选题重整 | REVISE | 科研 · 总结前八轮研究与导师反馈 · 重新梳理选题 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1060 | 深色首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(2)>div:nth-of-type(2)` | 整合三份根因研究与导师反馈，再决定新一轮选题。 | REVISE | 先总结前 8 轮为什么一直没选出值得长期投入的方向，并结合导师反馈改进选题方法，再决定是否开始下一轮。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1062 | 深色首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(3)>div:nth-of-type(1)` | 课程与教学 · 课程材料与独立复验 · 验证器待修 | REVISE | 课程与教学 · 课程材料检查 · 课程验证器仍需修正 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1064 | 深色首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(3)>div:nth-of-type(2)` | 按三份限定修复包修正验证器，再复验课程材料。 | REVISE | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1066 | 深色首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(4)>div:nth-of-type(1)` | 软件 · Windows 产品收口与验收加固 · 候选待补证 | REVISE | 软件 · 两个 Windows 新主题的动态原型 · Windows 新主题仍待实际验证 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1068 | 深色首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(4)>div:nth-of-type(2)` | 完成验收器加固，补齐候选的原生界面证据。 | REVISE | 先让两个 Windows 新主题都能实际运行，并补齐真实界面验证；准备好后再由用户选一个继续。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1073 | 深色首页 / 需要留意 / text / `body>div#content>div>div>section:nth-of-type(2)>div:nth-of-type(2)>div` | 修正旧兼容入口结构，再配置灾备凭据并验收。 | REVISE | 先修复旧设备兼容入口，再配置灾备所需凭据，并实际检查网页迁移入口是否可用。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1074 | 深色首页 / 需要留意 / text / `body>div#content>div>div>section:nth-of-type(2)>div:nth-of-type(2)>div` | 网页灾备入口尚未启用；当前缺口不等于 VPS 故障。 | REVISE | 网页灾备入口还不能使用；这不代表 VPS 当前故障。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1083 | 深色首页 / 当前重点 / text / `body>div#content>div>header>div:nth-of-type(2)` | 资料核对 | REVISE | 资料更新至 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1085 | 深色首页 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1096 | 深色首页 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1108 | 深色首页 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1123 | 首页 / text / `body>div#content>div>div>aside>section:nth-of-type(1)>article>a` | 阅读数值方法地图，确定下一步数值路线。 | REVISE | 打开数值方法地图，在可行方案中确定下一步要验证的方法。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1127 | 首页 / 待我处理 / text / `body>div#content>div>div>aside>section:nth-of-type(1)>div>h2` | 待我处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1128 | 首页 / 待我处理 / text / `body>div#content>div>div>aside>section:nth-of-type(1)>p` | 仅显示已就绪、须由本人处理的事项。 | REVISE | 只显示已经准备好、现在必须由本人完成的事项。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1136 | 首页 / 未来 30 天 / text / `body>div#content>div>div>aside>section:nth-of-type(2)>p` | 仅显示已确认日期。课程节点不等于本人待办。 | REVISE | 只显示已确认日期；课程日期不会自动变成你的待办。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1141 | 首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(1)>div:nth-of-type(1)` | 科研 · 方法验证 · 数值路线待定 | REVISE | 科研 · 方法验证 · 数值方法仍待确定 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1143 | 首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(1)>div:nth-of-type(2)` | 明确必要前置条件，再选择下一步方法。 | REVISE | 先明确必要前置条件，再解决当前方法的可靠性问题，之后才能进行完整验证。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1145 | 首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(2)>div:nth-of-type(1)` | 科研 · 整合八轮研究与导师反馈 · 选题重整 | REVISE | 科研 · 总结前八轮研究与导师反馈 · 重新梳理选题 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1147 | 首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(2)>div:nth-of-type(2)` | 整合三份根因研究与导师反馈，再决定新一轮选题。 | REVISE | 先总结前 8 轮为什么一直没选出值得长期投入的方向，并结合导师反馈改进选题方法，再决定是否开始下一轮。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1149 | 首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(3)>div:nth-of-type(1)` | 课程与教学 · 课程材料与独立复验 · 验证器待修 | REVISE | 课程与教学 · 课程材料检查 · 课程验证器仍需修正 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1151 | 首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(3)>div:nth-of-type(2)` | 按三份限定修复包修正验证器，再复验课程材料。 | REVISE | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1153 | 首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(4)>div:nth-of-type(1)` | 软件 · Windows 产品收口与验收加固 · 候选待补证 | REVISE | 软件 · 两个 Windows 新主题的动态原型 · Windows 新主题仍待实际验证 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1155 | 首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(4)>div:nth-of-type(2)` | 完成验收器加固，补齐候选的原生界面证据。 | REVISE | 先让两个 Windows 新主题都能实际运行，并补齐真实界面验证；准备好后再由用户选一个继续。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1160 | 首页 / 需要留意 / text / `body>div#content>div>div>section:nth-of-type(2)>div:nth-of-type(2)>div` | 修正旧兼容入口结构，再配置灾备凭据并验收。 | REVISE | 先修复旧设备兼容入口，再配置灾备所需凭据，并实际检查网页迁移入口是否可用。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1161 | 首页 / 需要留意 / text / `body>div#content>div>div>section:nth-of-type(2)>div:nth-of-type(2)>div` | 网页灾备入口尚未启用；当前缺口不等于 VPS 故障。 | REVISE | 网页灾备入口还不能使用；这不代表 VPS 当前故障。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1170 | 首页 / 当前重点 / text / `body>div#content>div>header>div:nth-of-type(2)` | 资料核对 | REVISE | 资料更新至 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1172 | 首页 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1183 | 首页 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1195 | 首页 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1215 | 项目页 / ai-skills / AI Skills Collection / text / `body>div#content>article>div:nth-of-type(3)>p` | 继续写作交付验收；具体顺序见正式维护看板。 | REVISE | 继续完善写作交付、科研文档和交付检查；具体顺序见维护看板。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1216 | 项目页 / ai-skills / AI Skills Collection / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有需要本人推进的已就绪事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1217 | 项目页 / ai-skills / AI Skills Collection / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1218 | 项目页 / ai-skills / AI Skills Collection / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1219 | 项目页 / ai-skills / AI Skills Collection / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1220 | 项目页 / ai-skills / AI Skills Collection / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1225 | 项目页 / ai-skills / 当前判断 / text / `body>div#content>article>section:nth-of-type(1)>p` | 写作交付、科研文档与验收保障。持续维护。 | REVISE | 写作交付、科研文档与交付检查。持续维护。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1227 | 项目页 / ai-skills / 维护边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | Atlas 不保存维护卡片、不提供拖动状态列、不重算完成语义。需要查看具体维护顺序时直接进入 AI Skills Maintenance。 | REVISE | Atlas 不保存具体维护卡片，也不重复计算完成状态。需要查看顺序时直接打开 AI Skills Maintenance。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1229 | 项目页 / ai-skills / 正式维护入口 / text / `body>div#content>article>section:nth-of-type(3)>h2` | 正式维护入口 | REVISE | 维护入口 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1232 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1234 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>a` | 维护看板规则 | REVISE | 维护看板说明 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1235 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1237 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>a` | 正式看板身份 | REVISE | 维护看板入口 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1238 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1240 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>a` | 写作交付维护证据 | REVISE | 写作交付计划 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1241 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1243 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(4)>a` | 科研文档维护证据 | REVISE | 科研文档计划 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1244 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(4)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1246 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(5)>a` | 交付验收维护证据 | REVISE | 交付检查计划 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1247 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(5)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1249 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(6)>a` | 写作交付维护方向 | REVISE | 写作交付事项 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1250 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(6)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1251 | 项目页 / ai-skills / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1262 | 项目页 / ai-skills / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1274 | 项目页 / ai-skills / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1294 | 项目页 / asteria / Asteria / text / `body>div#content>article>div:nth-of-type(3)>p` | 尚无已登记的下一步；保留项目与材料入口。 | REVISE | 目前还没有确认下一步；先保留项目和材料入口。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1295 | 项目页 / asteria / Asteria / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有已核实的本人事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1296 | 项目页 / asteria / Asteria / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1297 | 项目页 / asteria / Asteria / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1298 | 项目页 / asteria / Asteria / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1299 | 项目页 / asteria / Asteria / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1305 | 项目页 / asteria / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 资料边界 | REVISE | 当前资料情况 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1306 | 项目页 / asteria / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 项目存在与旧规划入口已确认；当前状态、下一步和本人动作保留未确认。旧材料年龄不会自动转成项目阻塞。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1309 | 项目页 / asteria / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>p` | 本页保留旧 Atlas 登记；当前状态与下一步尚未重新核对。 | REVISE | 当前进度尚未重新核对。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1312 | 项目页 / asteria / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1313 | 项目页 / asteria / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1324 | 项目页 / asteria / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1336 | 项目页 / asteria / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1352 | 项目页 / bobbio / Bobbio / text / `body>div#content>article>div:nth-of-type(2)>span:nth-of-type(1)` | 0.2 已验收 | REVISE | 0.2 已完成并确认可用 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1357 | 项目页 / bobbio / Bobbio / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有需要本人推进的已就绪事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1358 | 项目页 / bobbio / Bobbio / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1359 | 项目页 / bobbio / Bobbio / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1360 | 项目页 / bobbio / Bobbio / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1361 | 项目页 / bobbio / Bobbio / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1366 | 项目页 / bobbio / 当前判断 / text / `body>div#content>article>section:nth-of-type(1)>p` | 阅读器基础完成。0.2 已验收。 | REVISE | 阅读器基础完成。0.2 已完成并确认可用。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1367 | 项目页 / bobbio / 已确认的基线 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 已确认的基线 | REVISE | 当前已完成内容 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1368 | 项目页 / bobbio / 已确认的基线 / text / `body>div#content>article>section:nth-of-type(2)>p` | 0.2 已获正式接受，原生阅读与标注往返等验收已通过。这是当前已完成版本，不等于后续 0.3 也已实现。 | REVISE | 0.2 已确认可用，原生阅读和标注往返等检查已经通过。这只代表 0.2 已完成，不代表后续 0.3 已经实现。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1369 | 项目页 / bobbio / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>div` | 0.2 接受记录优先。旧里程碑摘要仍写待验收，不能再次生成验收待办。 | REVISE | 0.2 的完成记录优先。旧里程碑仍写着待检查，不会再次生成同一项待办。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1371 | 项目页 / bobbio / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1373 | 项目页 / bobbio / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li:nth-of-type(1)>a` | 0.2 正式接受记录 | REVISE | 0.2 完成记录 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1374 | 项目页 / bobbio / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1376 | 项目页 / bobbio / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li:nth-of-type(2)>a` | 滞后的里程碑摘要 | REVISE | 旧里程碑摘要 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1377 | 项目页 / bobbio / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1380 | 项目页 / bobbio / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1381 | 项目页 / bobbio / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1392 | 项目页 / bobbio / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1404 | 项目页 / bobbio / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1424 | 项目页 / bridge / Bridge Kit / text / `body>div#content>article>div:nth-of-type(3)>p` | 尚无已登记的下一步；保留项目与材料入口。 | REVISE | 目前还没有确认下一步；先保留项目和材料入口。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1425 | 项目页 / bridge / Bridge Kit / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有已核实的本人事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1426 | 项目页 / bridge / Bridge Kit / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1427 | 项目页 / bridge / Bridge Kit / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1428 | 项目页 / bridge / Bridge Kit / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1429 | 项目页 / bridge / Bridge Kit / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1435 | 项目页 / bridge / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 资料边界 | REVISE | 当前资料情况 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1436 | 项目页 / bridge / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 项目存在与旧规划入口已确认；当前状态、下一步和本人动作保留未确认。旧材料年龄不会自动转成项目阻塞。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1439 | 项目页 / bridge / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>p` | 本页保留旧 Atlas 登记；当前状态与下一步尚未重新核对。 | REVISE | 当前进度尚未重新核对。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1442 | 项目页 / bridge / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1443 | 项目页 / bridge / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1454 | 项目页 / bridge / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1466 | 项目页 / bridge / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1486 | 项目页 / cardiac / CardiacNexus / text / `body>div#content>article>div:nth-of-type(3)>p` | 尚无已登记的下一步；保留项目与材料入口。 | REVISE | 目前还没有确认下一步；先保留项目和材料入口。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1487 | 项目页 / cardiac / CardiacNexus / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有已核实的本人事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1488 | 项目页 / cardiac / CardiacNexus / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1489 | 项目页 / cardiac / CardiacNexus / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1490 | 项目页 / cardiac / CardiacNexus / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1491 | 项目页 / cardiac / CardiacNexus / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1497 | 项目页 / cardiac / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 资料边界 | REVISE | 当前资料情况 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1498 | 项目页 / cardiac / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 项目存在与旧规划入口已确认；当前状态、下一步和本人动作保留未确认。旧材料年龄不会自动转成项目阻塞。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1501 | 项目页 / cardiac / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>p` | 本页保留旧 Atlas 登记；当前状态与下一步尚未重新核对。 | REVISE | 当前进度尚未重新核对。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1504 | 项目页 / cardiac / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1505 | 项目页 / cardiac / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1516 | 项目页 / cardiac / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1528 | 项目页 / cardiac / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1545 | 项目页 / private-project / 某私有统计研究项目 / text / `body>div#content>article>div:nth-of-type(2)>span:nth-of-type(2)` | 数值路线待定 | REVISE | 数值方法仍待确定 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1549 | 项目页 / private-project / 该项目 / text / `body>div#content>article>div:nth-of-type(3)>p` | 待明确前置条件，再选择下一步方法。 | REVISE | 先明确前置条件，再选择下一步要验证的方法。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1550 | 项目页 / private-project / 该项目 / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 阅读数值方法地图，确定下一步数值路线。 | REVISE | 打开数值方法地图，在可行方案中确定下一步要验证的方法。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1551 | 项目页 / private-project / 该项目 / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 方法尚未选定；参考结果仍需确认。 | REVISE | 方法还没选定，参考结果也还需确认，暂时无法进行完整验证。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1552 | 项目页 / private-project / 该项目 / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1553 | 项目页 / private-project / 该项目 / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1554 | 项目页 / private-project / 该项目 / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1561 | 项目页 / private-project / 当前科学问题 / text / `body>div#content>article>section:nth-of-type(2)>p` | 局部比较已有结果，仍需确认其余计算是否可靠。 | REVISE | 局部比较已有结果，下一步要确认其余计算是否可靠。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1562 | 项目页 / private-project / 已获得的证据 / text / `body>div#content>article>section:nth-of-type(3)>h2` | 已获得的证据 | REVISE | 已有证据 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1563 | 项目页 / private-project / 已获得的证据 / text / `body>div#content>article>section:nth-of-type(3)>p` | 部分材料已获限定范围的使用认可，仍有问题待修正。 | REVISE | 部分材料已确认可用，但适用范围有限，仍有问题要修正。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1564 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>div` | 根路线图仍写 9 月 15 日；当前下一步以 10 月 28 日决策为准。 | REVISE | 旧路线图仍停留在 9 月 15 日；当前下一步以 10 月 28 日的研究结论为准。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1566 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1568 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>a` | 当前研究决策 | REVISE | 当前研究结论 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1569 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1571 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>a` | 数值路线与本人判断 | REVISE | 数值方法与本人判断 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1572 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1574 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>a` | 预测与日志独立审查 | REVISE | 预测与运行记录检查 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1575 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1577 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(4)>a` | 研究图的使用范围 | REVISE | 研究图的适用范围 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1578 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(4)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1580 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(5)>a` | 实施材料入口 | REVISE | 模型实现材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1581 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(5)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1584 | 项目页 / private-project / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(6)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1585 | 项目页 / private-project / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1596 | 项目页 / private-project / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1608 | 项目页 / private-project / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1628 | 项目页 / clash / Clash Profile / text / `body>div#content>article>div:nth-of-type(3)>p` | 修正旧兼容入口结构，再配置灾备凭据并验收。 | REVISE | 先修复旧设备兼容入口，再配置灾备所需凭据，并实际检查网页迁移入口是否可用。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1629 | 项目页 / clash / Clash Profile / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 动作尚未满足就绪条件，当前不进入本人操作。 | REVISE | 前提还没准备好，现在不需要你处理。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1630 | 项目页 / clash / Clash Profile / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 旧兼容入口结构门禁未过，专用凭据尚未配置。 | REVISE | 旧设备兼容入口仍有结构问题，灾备所需的专用凭据也还没配置。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1631 | 项目页 / clash / Clash Profile / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1632 | 项目页 / clash / Clash Profile / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1633 | 项目页 / clash / Clash Profile / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1639 | 项目页 / clash / 当前维护边界 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 当前维护边界 | REVISE | 当前维护事项 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1640 | 项目页 / clash / 当前维护边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 网页灾备入口已开发但尚未启用。先完成兼容入口的结构修复，再完成专用凭据配置与网页验收。 | REVISE | 网页灾备入口已经开发，但还不能使用。先修复旧设备兼容入口，再配置专用凭据并实际检查网页入口。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1641 | 项目页 / clash / 运行状态 / text / `body>div#content>article>section:nth-of-type(3)>h2` | 运行状态 | REVISE | 当前运行情况 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1642 | 项目页 / clash / 运行状态 / text / `body>div#content>article>section:nth-of-type(3)>p` | 未读取实时设备探针。文档中的功能准备缺口不能证明代理或 VPS 当前不可用。 | REVISE | 本页没有读取设备实时状态，因此不能据此判断代理或 VPS 当前是否可用。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1645 | 项目页 / clash / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1648 | 项目页 / clash / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1651 | 项目页 / clash / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1654 | 项目页 / clash / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1655 | 项目页 / clash / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1666 | 项目页 / clash / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1678 | 项目页 / clash / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1698 | 项目页 / cmrx / CMRxRecon25 / text / `body>div#content>article>div:nth-of-type(3)>p` | 尚无已登记的下一步；保留项目与材料入口。 | REVISE | 目前还没有确认下一步；先保留项目和材料入口。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1699 | 项目页 / cmrx / CMRxRecon25 / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有已核实的本人事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1700 | 项目页 / cmrx / CMRxRecon25 / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1701 | 项目页 / cmrx / CMRxRecon25 / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1702 | 项目页 / cmrx / CMRxRecon25 / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1703 | 项目页 / cmrx / CMRxRecon25 / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1709 | 项目页 / cmrx / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 资料边界 | REVISE | 当前资料情况 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1710 | 项目页 / cmrx / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 项目存在与旧规划入口已确认；当前状态、下一步和本人动作保留未确认。旧材料年龄不会自动转成项目阻塞。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1713 | 项目页 / cmrx / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>p` | 本页保留旧 Atlas 登记；当前状态与下一步尚未重新核对。 | REVISE | 当前进度尚未重新核对。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1716 | 项目页 / cmrx / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1717 | 项目页 / cmrx / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1728 | 项目页 / cmrx / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1740 | 项目页 / cmrx / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1760 | 项目页 / cuhk-date / CUHK Date / text / `body>div#content>article>div:nth-of-type(3)>p` | 补齐测试环境匹配验收，再形成上线决策包。 | REVISE | 先在测试环境完成真实匹配流程检查；确认结果可靠后，再决定是否启用真实匹配。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1761 | 项目页 / cuhk-date / CUHK Date / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 动作尚未满足就绪条件，当前不进入本人操作。 | REVISE | 前提还没准备好，现在不需要你处理。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1762 | 项目页 / cuhk-date / CUHK Date / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1763 | 项目页 / cuhk-date / CUHK Date / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1764 | 项目页 / cuhk-date / CUHK Date / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1765 | 项目页 / cuhk-date / CUHK Date / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1772 | 项目页 / cuhk-date / 环境边界 / text / `body>div#content>article>section:nth-of-type(2)>dl>dd:nth-of-type(2)` | 用于产品与匹配验收；不代替生产完成。 | REVISE | 用于检查产品流程和匹配结果，不代表真实匹配已经启用。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1776 | 项目页 / cuhk-date / 下一验收 / text / `body>div#content>article>section:nth-of-type(3)>h2` | 下一验收 | REVISE | 上线前检查 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1777 | 项目页 / cuhk-date / 下一验收 / text / `body>div#content>article>section:nth-of-type(3)>p` | 先完成测试环境的匹配验证和交付验收加固，再形成真实匹配启用决策。当前材料不能证明该决策包已经就绪。 | REVISE | 先在测试环境完成匹配流程检查和必要修正，再决定是否启用真实匹配。现在还没有准备好需要本人作出的上线决定。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1778 | 项目页 / cuhk-date / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>div` | 测试环境的持续评阅是可选入口，不是当前开发阻塞。真实匹配上线决定须等工程前提与决策包就绪。 | REVISE | 测试环境评阅是可选入口，不是当前阻塞。真实匹配是否启用，要等工程前提和检查结果都准备好。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1780 | 项目页 / cuhk-date / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1782 | 项目页 / cuhk-date / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>a` | 当前产品合同 | REVISE | 当前产品说明 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1783 | 项目页 / cuhk-date / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1785 | 项目页 / cuhk-date / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>a` | 测试环境评阅边界 | REVISE | 测试环境检查说明 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1786 | 项目页 / cuhk-date / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1788 | 项目页 / cuhk-date / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>a` | 验收加固任务 | REVISE | 测试修正任务 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1789 | 项目页 / cuhk-date / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1792 | 项目页 / cuhk-date / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(4)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1793 | 项目页 / cuhk-date / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1804 | 项目页 / cuhk-date / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1816 | 项目页 / cuhk-date / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1833 | 项目页 / dii / DII / text / `body>div#content>article>div:nth-of-type(2)>span:nth-of-type(2)` | 选题重整 | REVISE | 重新梳理选题 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1837 | 项目页 / dii / DII / text / `body>div#content>article>div:nth-of-type(3)>p` | 整合三份根因研究与导师反馈，再决定新一轮选题。 | REVISE | 先总结前 8 轮为什么一直没选出值得长期投入的方向，并结合导师反馈改进选题方法，再决定是否开始下一轮。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1838 | 项目页 / dii / DII / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有需要本人推进的已就绪事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1839 | 项目页 / dii / DII / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1840 | 项目页 / dii / DII / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1841 | 项目页 / dii / DII / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1842 | 项目页 / dii / DII / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1847 | 项目页 / dii / 当前判断 / text / `body>div#content>article>section:nth-of-type(1)>p` | 整合八轮研究与导师反馈。选题重整。 | REVISE | 总结前八轮研究与导师反馈。重新梳理选题。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1848 | 项目页 / dii / 研究边界 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 研究边界 | REVISE | 研究现状 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1849 | 项目页 / dii / 研究边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 八轮研究尚未形成几项可放心投入数月的原创课题。22 个去重科学目标属于机会库，第九轮尚未启动。 | REVISE | 前 8 轮提出了 22 个去重科学目标，但还没有选出值得连续投入数月的原创课题。下一轮尚未开始。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1851 | 项目页 / dii / 下一次判断前 / text / `body>div#content>article>section:nth-of-type(3)>p` | 先完成三份根因研究、历史问题与导师反馈的综合。目前没有证据表明决策包已经准备好等待本人选择。 | REVISE | 先总结前 8 轮为什么一直没选出来，并结合导师反馈改进选题方法。目前还没有准备好需要本人选择的方案。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1854 | 项目页 / dii / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1857 | 项目页 / dii / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1860 | 项目页 / dii / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1863 | 项目页 / dii / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1864 | 项目页 / dii / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1875 | 项目页 / dii / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1887 | 项目页 / dii / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1907 | 项目页 / echo / Echo Select / text / `body>div#content>article>div:nth-of-type(3)>p` | 尚无已登记的下一步；保留项目与材料入口。 | REVISE | 目前还没有确认下一步；先保留项目和材料入口。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1908 | 项目页 / echo / Echo Select / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有已核实的本人事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1909 | 项目页 / echo / Echo Select / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1910 | 项目页 / echo / Echo Select / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1911 | 项目页 / echo / Echo Select / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1912 | 项目页 / echo / Echo Select / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1918 | 项目页 / echo / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 资料边界 | REVISE | 当前资料情况 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1919 | 项目页 / echo / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 项目存在与旧规划入口已确认；当前状态、下一步和本人动作保留未确认。旧材料年龄不会自动转成项目阻塞。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1922 | 项目页 / echo / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>p` | 本页保留旧 Atlas 登记；当前状态与下一步尚未重新核对。 | REVISE | 当前进度尚未重新核对。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1925 | 项目页 / echo / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1926 | 项目页 / echo / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1937 | 项目页 / echo / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1949 | 项目页 / echo / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-1970 | 项目页 / local / 本地计算环境 / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 动作尚未满足就绪条件，当前不进入本人操作。 | REVISE | 前提还没准备好，现在不需要你处理。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1971 | 项目页 / local / 本地计算环境 / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1972 | 项目页 / local / 本地计算环境 / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1973 | 项目页 / local / 本地计算环境 / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1974 | 项目页 / local / 本地计算环境 / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1980 | 项目页 / local / 客户端验收 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 客户端验收 | REVISE | 网络盘检查 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1981 | 项目页 / local / 客户端验收 / text / `body>div#content>article>section:nth-of-type(2)>p` | Windows 端共享及回环读写已通过；仍需 Mac mini 的真实客户端验收。先交给设备端执行器完成挂载与读写，仅在出现不可代办的账户认证时转交本人。当前没有证据表明认证已成为阻塞。 | REVISE | Windows 端共享和读写已经通过；Mac mini 还需要实际挂载并测试读写。先由设备端执行器完成，只有遇到无法代办的账户认证时才需要本人处理。目前没有证据表明认证已经成为阻塞。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1983 | 项目页 / local / 本地 AI / text / `body>div#content>article>section:nth-of-type(3)>p` | Homebrew 已完成前置安装；Miniforge、模型与后续运行环境尚未部署。规划中的模型与容量不能作为已安装能力。 | REVISE | Homebrew 已完成前置安装；Miniforge、模型和后续运行环境尚未部署。规划中的模型和容量不能算作已经安装。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1985 | 项目页 / local / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-1987 | 项目页 / local / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>a` | 本地 AI 当前状态 | REVISE | 本地 AI 当前进度 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1988 | 项目页 / local / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1990 | 项目页 / local / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>a` | 网络盘客户端验收 | REVISE | Mac mini 网络盘检查 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-1991 | 项目页 / local / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1993 | 项目页 / local / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>a` | 本地环境职责 | REVISE | 本地环境说明 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1994 | 项目页 / local / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-1995 | 项目页 / local / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2006 | 项目页 / local / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2018 | 项目页 / local / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-2035 | 项目页 / lucerna / Lucerna / text / `body>div#content>article>div:nth-of-type(2)>span:nth-of-type(2)` | 候选待补证 | REVISE | Windows 新主题仍待实际验证 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2039 | 项目页 / lucerna / Lucerna / text / `body>div#content>article>div:nth-of-type(3)>p` | 完成验收器加固，补齐候选的原生界面证据。 | REVISE | 先让两个 Windows 新主题都能实际运行，并补齐真实界面验证；准备好后再由用户选一个继续。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2040 | 项目页 / lucerna / Lucerna / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有需要本人推进的已就绪事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2041 | 项目页 / lucerna / Lucerna / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 部分原生画面证据与系统环境隔离仍未闭合。 | REVISE | 两个新主题还没有同时达到可实际运行、可比较的状态。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2042 | 项目页 / lucerna / Lucerna / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2043 | 项目页 / lucerna / Lucerna / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2044 | 项目页 / lucerna / Lucerna / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2047 | 项目页 / lucerna / Lucerna / text / `body>div#content>article>p` | 在托盘与菜单栏集中查看资源用量、计算与网络基础设施状态。已有 Windows 产品候选，仍需完成候选证据与验收收口。 | REVISE | 在托盘集中查看资源用量、计算与网络状态。两个 Windows 新主题已经有设计方向，但还需要做成可实际运行的动态原型并完成真实界面检查。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2049 | 项目页 / lucerna / 当前判断 / text / `body>div#content>article>section:nth-of-type(1)>p` | Windows 产品收口与验收加固。候选待补证。 | REVISE | 两个 Windows 新主题的动态原型。Windows 新主题仍待实际验证。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2051 | 项目页 / lucerna / 当前产品阶段 / text / `body>div#content>article>section:nth-of-type(2)>p` | 01056r4 已有 Windows 产品候选，但精确候选的部分原生画面仍缺有效证据；01057 只完成部分治理。01058 是已准备的加固任务，不是已执行的结果。 | REVISE | 两个 Windows 新主题已经有设计结果，但仍缺少完整的真实界面验证。下一步先把两个版本都做成可实际运行的动态原型。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2052 | 项目页 / lucerna / 本人介入条件 / text / `body>div#content>article>section:nth-of-type(3)>h2` | 本人介入条件 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2053 | 项目页 / lucerna / 本人介入条件 / text / `body>div#content>article>section:nth-of-type(3)>p` | 现有结果明确普通 QA 不需要用户，最终用户验收尚未就绪。主题选择也要等可操作动画准备好后再发起。 | REVISE | 现在不用你处理。等两个版本都能实际运行以后，再打开两个版本，选一个继续。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2054 | 项目页 / lucerna / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>div` | 旧 README 仍称原型前。当前候选结果优先；最终用户验收尚未就绪。 | REVISE | 旧 README 仍停留在原型前阶段；当前主题结果更新，但还没准备好让用户二选一。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2056 | 项目页 / lucerna / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2058 | 项目页 / lucerna / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>a` | 当前候选结果 | REVISE | 当前主题结果 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2059 | 项目页 / lucerna / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2061 | 项目页 / lucerna / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>a` | 执行环境结果 | REVISE | 运行环境检查 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2062 | 项目页 / lucerna / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2064 | 项目页 / lucerna / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>a` | 下一验收任务 | REVISE | 下一步验证 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2065 | 项目页 / lucerna / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2067 | 项目页 / lucerna / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(4)>a` | 总体路线图 | REVISE | 产品路线图 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2068 | 项目页 / lucerna / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(4)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2069 | 项目页 / lucerna / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2080 | 项目页 / lucerna / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2092 | 项目页 / lucerna / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-2108 | 项目页 / mica / Mica for ChatGPT / text / `body>div#content>article>div:nth-of-type(2)>span:nth-of-type(1)` | 重建设计已冻结 | REVISE | 底层重建方案已确定 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2112 | 项目页 / mica / Mica for ChatGPT / text / `body>div#content>article>div:nth-of-type(3)>p` | 实现重建基础，再接入低内存模式。 | REVISE | 先把插件底层和 ChatGPT 兼容方式做稳定，避免页面一变功能就坏。之后优先恢复长对话优化，再做高亮和 PDF。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2113 | 项目页 / mica / Mica for ChatGPT / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有需要本人推进的已就绪事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2114 | 项目页 / mica / Mica for ChatGPT / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2115 | 项目页 / mica / Mica for ChatGPT / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2116 | 项目页 / mica / Mica for ChatGPT / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2117 | 项目页 / mica / Mica for ChatGPT / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2122 | 项目页 / mica / 当前判断 / text / `body>div#content>article>section:nth-of-type(1)>p` | 基础重建待落实。重建设计已冻结。 | REVISE | 插件底层与 ChatGPT 兼容性。底层重建方案已确定。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2124 | 项目页 / mica / 功能顺序 / text / `body>div#content>article>section:nth-of-type(2)>p` | 基础重建 → 低内存 → 内置高亮 → 保留高亮及可选择数学文本的 PDF 导出。高级自动恢复与 Notion 延后。 | REVISE | 先稳定插件底层和 ChatGPT 兼容方式，再恢复低内存模式；之后做内置高亮和可保留高亮、可选择数学文本的 PDF 导出。自动恢复和 Notion 支持延后。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2125 | 项目页 / mica / 验收条件 / text / `body>div#content>article>section:nth-of-type(3)>h2` | 验收条件 | REVISE | 需要我 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2126 | 项目页 / mica / 验收条件 / text / `body>div#content>article>section:nth-of-type(3)>p` | 未确认当前就绪候选，不向本人派发日常 QA。最终用户评阅由原项目在工程前提成熟后发起。 | REVISE | 当前还没有可供日常检查的版本，暂时不需要本人处理。等工程条件成熟后，再由原项目发起用户评阅。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2127 | 项目页 / mica / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>div` | 当前顺序以最终重建任务为准；仅凭规格通过，不能宣称代码已重建完成。 | REVISE | 当前顺序以底层重建方案为准；方案已经确定，不代表代码已经完成。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2129 | 项目页 / mica / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2131 | 项目页 / mica / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>a` | 正式重建任务 | REVISE | 底层重建方案 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2132 | 项目页 / mica / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2134 | 项目页 / mica / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>a` | 规格审查 | REVISE | 方案核对记录 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2135 | 项目页 / mica / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2137 | 项目页 / mica / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>a` | 历史路线图 | REVISE | 旧路线图 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2138 | 项目页 / mica / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2139 | 项目页 / mica / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2150 | 项目页 / mica / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2162 | 项目页 / mica / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-2183 | 项目页 / remote / Remote Compute / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有需要本人推进的已就绪事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2184 | 项目页 / remote / Remote Compute / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2185 | 项目页 / remote / Remote Compute / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2186 | 项目页 / remote / Remote Compute / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2187 | 项目页 / remote / Remote Compute / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2192 | 项目页 / remote / 当前判断 / text / `body>div#content>article>section:nth-of-type(1)>p` | 客户端接入规范。客户端部署待核对。 | REVISE | Mac 客户端接入。客户端部署待核对。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2193 | 项目页 / remote / 运行状态 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 运行状态 | REVISE | 当前连接情况 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2194 | 项目页 / remote / 运行状态 / text / `body>div#content>article>section:nth-of-type(2)>p` | 未读取实时探针，保持安静展示。只有确认的新异常、维护请求或本人动作才升级到首页。 | REVISE | 本页没有实时检测设备状态，因此这里只记录已经确认的部署情况；是否在线仍以实际连接为准。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2195 | 项目页 / remote / 接入状态 / text / `body>div#content>article>section:nth-of-type(3)>h2` | 接入状态 | REVISE | Mac 客户端 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2196 | 项目页 / remote / 接入状态 / text / `body>div#content>article>section:nth-of-type(3)>p` | macOS AUTO 选择器已有源码和部署合同；两台 Mac 的实际安装与验收需要设备记录确认，不能据此直接要求本人操作。 | REVISE | macOS 自动选择器已有代码和安装说明，但两台 Mac 是否已经安装并通过连接检查，还需要设备记录确认。现在不需要本人操作。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2199 | 项目页 / remote / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2201 | 项目页 / remote / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>a` | 接入职责与现状 | REVISE | 远程接入说明 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2202 | 项目页 / remote / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2204 | 项目页 / remote / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>a` | macOS 部署合同 | REVISE | macOS 安装说明 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2205 | 项目页 / remote / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2207 | 项目页 / remote / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>a` | 已完成的 A25 验收 | REVISE | A25 切换完成记录 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2208 | 项目页 / remote / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2210 | 项目页 / remote / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(4)>a` | 架构路线图 | REVISE | 远程接入路线图 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2211 | 项目页 / remote / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(4)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2212 | 项目页 / remote / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2223 | 项目页 / remote / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2235 | 项目页 / remote / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-2255 | 项目页 / seminar / SeminarArc / text / `body>div#content>article>div:nth-of-type(3)>p` | 尚无已登记的下一步；保留项目与材料入口。 | REVISE | 目前还没有确认下一步；先保留项目和材料入口。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2256 | 项目页 / seminar / SeminarArc / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有已核实的本人事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2257 | 项目页 / seminar / SeminarArc / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2258 | 项目页 / seminar / SeminarArc / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2259 | 项目页 / seminar / SeminarArc / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2260 | 项目页 / seminar / SeminarArc / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2266 | 项目页 / seminar / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 资料边界 | REVISE | 当前资料情况 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2267 | 项目页 / seminar / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 项目存在与旧规划入口已确认；当前状态、下一步和本人动作保留未确认。旧材料年龄不会自动转成项目阻塞。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2270 | 项目页 / seminar / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>p` | 本页保留旧 Atlas 登记；当前状态与下一步尚未重新核对。 | REVISE | 当前进度尚未重新核对。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2273 | 项目页 / seminar / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2274 | 项目页 / seminar / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2285 | 项目页 / seminar / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2297 | 项目页 / seminar / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-2317 | 项目页 / shione / Shione / text / `body>div#content>article>div:nth-of-type(3)>p` | 尚无已登记的下一步；保留项目与材料入口。 | REVISE | 目前还没有确认下一步；先保留项目和材料入口。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2318 | 项目页 / shione / Shione / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有已核实的本人事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2319 | 项目页 / shione / Shione / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2320 | 项目页 / shione / Shione / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2321 | 项目页 / shione / Shione / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2322 | 项目页 / shione / Shione / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2328 | 项目页 / shione / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 资料边界 | REVISE | 当前资料情况 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2329 | 项目页 / shione / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 项目存在与旧规划入口已确认；当前状态、下一步和本人动作保留未确认。旧材料年龄不会自动转成项目阻塞。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2332 | 项目页 / shione / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>p` | 本页保留旧 Atlas 登记；当前状态与下一步尚未重新核对。 | REVISE | 当前进度尚未重新核对。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2335 | 项目页 / shione / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2336 | 项目页 / shione / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2347 | 项目页 / shione / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2359 | 项目页 / shione / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-2379 | 项目页 / stat5050 / STAT5050 / text / `body>div#content>article>div:nth-of-type(3)>p` | 尚无已登记的下一步；保留项目与材料入口。 | REVISE | 目前还没有确认下一步；先保留项目和材料入口。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2380 | 项目页 / stat5050 / STAT5050 / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有已核实的本人事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2381 | 项目页 / stat5050 / STAT5050 / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2382 | 项目页 / stat5050 / STAT5050 / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2383 | 项目页 / stat5050 / STAT5050 / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2384 | 项目页 / stat5050 / STAT5050 / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2396 | 项目页 / stat5050 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2399 | 项目页 / stat5050 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2402 | 项目页 / stat5050 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2405 | 项目页 / stat5050 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2406 | 项目页 / stat5050 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2417 | 项目页 / stat5050 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2429 | 项目页 / stat5050 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-2446 | 项目页 / stat5060 / STAT5060 TA / text / `body>div#content>article>div:nth-of-type(2)>span:nth-of-type(2)` | 验证器待修 | REVISE | 课程验证器仍需修正 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2450 | 项目页 / stat5060 / STAT5060 TA / text / `body>div#content>article>div:nth-of-type(3)>p` | 按三份限定修复包修正验证器，再复验课程材料。 | REVISE | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2451 | 项目页 / stat5060 / STAT5060 TA / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 等待任课教师决定；不属于本人操作。 | REVISE | 等待任课教师决定，现在不需要你处理。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2452 | 项目页 / stat5060 / STAT5060 TA / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 独立验收仍有限定修复；评分分项与政策决定属于任课教师。 | REVISE | 三组验证器仍有已确认的问题需要修正；评分分项和课程政策由任课教师决定。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2454 | 项目页 / stat5060 / STAT5060 TA / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2455 | 项目页 / stat5060 / STAT5060 TA / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2460 | 项目页 / stat5060 / 当前判断 / text / `body>div#content>article>section:nth-of-type(1)>p` | 课程材料与独立复验。验证器待修。 | REVISE | 课程材料检查。课程验证器仍需修正。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2462 | 项目页 / stat5060 / 当前教学工作 / text / `body>div#content>article>section:nth-of-type(2)>p` | 三组验证器已实质实现，10 月 25–26 日独立报告给出三个修复包。课程真实使用闭环仍未完成。 | REVISE | 三组验证器已经实现，独立检查确认了三个需要修正的问题。修正并重新检查后，才能用于课程。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2464 | 项目页 / stat5060 / 已过去的节点 / text / `body>div#content>article>section:nth-of-type(3)>p` | HW1 的学生截止为 11 月 1 日 23:59。收齐和提交状态未确认，不能把这条学生节点标成本人逾期。 | REVISE | HW1 的学生截止时间是 11 月 1 日 23:59。提交与收齐状态还没有确认，因此不会记成 TA 本人逾期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2466 | 项目页 / stat5060 / 教师决定 / text / `body>div#content>article>section:nth-of-type(4)>p` | 分项评分、课程政策附件与评分合并公式留给任课教师。Atlas 保留外部等待原因，不将教师职责塞进“待我操作”。 | REVISE | 分项评分、课程政策附件和评分合并公式由任课教师决定，不会进入“需要我”。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2467 | 项目页 / stat5060 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(5)>div` | 旧 CURRENT 索引仍写未实施；三组验证器已有代码，但未达课程生产验收。历史教学路线图已归档。 | REVISE | 旧索引仍写着尚未实施，但三组验证器已经有代码；修正已确认的问题并重新检查后，才能用于课程。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2469 | 项目页 / stat5060 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(5)>p` | 本页按 2026 年 11 月 2 日读取的固定来源核对；没有读取设备实时状态。 | REVISE | 资料更新至 2026 年 11 月 2 日。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2471 | 项目页 / stat5060 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(5)>ul>li:nth-of-type(1)>a` | 验证器独立验收 | REVISE | 验证器问题清单 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2472 | 项目页 / stat5060 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(5)>ul>li:nth-of-type(1)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2474 | 项目页 / stat5060 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(5)>ul>li:nth-of-type(2)>a` | 冻结课程时刻表 | REVISE | 课程时刻表 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2475 | 项目页 / stat5060 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(5)>ul>li:nth-of-type(2)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2477 | 项目页 / stat5060 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(5)>ul>li:nth-of-type(3)>a` | 教学材料顺序 | REVISE | 课程材料顺序 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2478 | 项目页 / stat5060 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(5)>ul>li:nth-of-type(3)>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2479 | 项目页 / stat5060 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2490 | 项目页 / stat5060 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2502 | 项目页 / stat5060 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-2522 | 项目页 / zotero / Zotero 文献镜像 / text / `body>div#content>article>div:nth-of-type(3)>p` | 尚无已登记的下一步；保留项目与材料入口。 | REVISE | 目前还没有确认下一步；先保留项目和材料入口。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2523 | 项目页 / zotero / Zotero 文献镜像 / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 当前没有已核实的本人事项。 | REVISE | 目前没有必须你现在处理的事情。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2524 | 项目页 / zotero / Zotero 文献镜像 / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 未记录确定的项目阻塞。 | REVISE | 目前没有已确认的问题。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2525 | 项目页 / zotero / Zotero 文献镜像 / text / `body>div#content>article>dl>dd:nth-of-type(3)` | 未设定日期；不据此制造催办。 | REVISE | 目前没有已确认日期。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2526 | 项目页 / zotero / Zotero 文献镜像 / text / `body>div#content>article>dl>dt:nth-of-type(1)` | 本人处理 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2527 | 项目页 / zotero / Zotero 文献镜像 / text / `body>div#content>article>dl>dt:nth-of-type(2)` | 阻塞与判断 | REVISE | 当前问题 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2533 | 项目页 / zotero / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>h2` | 资料边界 | REVISE | 当前资料情况 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2534 | 项目页 / zotero / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 项目存在与旧规划入口已确认；当前状态、下一步和本人动作保留未确认。旧材料年龄不会自动转成项目阻塞。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2537 | 项目页 / zotero / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>p` | 本页保留旧 Atlas 登记；当前状态与下一步尚未重新核对。 | REVISE | 当前进度尚未重新核对。 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2540 | 项目页 / zotero / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>ul>li>span` | 原始材料 | REVISE | 查看材料 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2541 | 项目页 / zotero / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2552 | 项目页 / zotero / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2564 | 项目页 / zotero / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-2588 | 工作关系 / 工作关系 / text / `body>div#content>div>div>svg>text:nth-of-type(2)` | 共享资源，不建第二套状态 | REVISE | 共享中继资源 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2598 | 工作关系 / 工作关系 / text / `body>div#content>div>header>div:nth-of-type(2)` | 不另存项目状态 | REVISE | 只显示关系，不重复保存状态 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2599 | 工作关系 / 工作关系 / text / `body>div#content>div>p:nth-of-type(1)` | 此专题只呈现远程接入与状态显示的职责。关系线不表示任务先后、阻塞或完成状态；正式实现为原生 Canvas 笔记引用。 | REVISE | 此专题只呈现远程接入与状态显示的职责。关系线不表示任务先后、阻塞或完成状态。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2600 | 工作关系 / 工作关系 / text / `body>div#content>div>p:nth-of-type(2)` | 旧工作关系图保留为历史规划；其中未勾选项不转换为实时任务。 | REJECT | — | 历史实现说明不影响当前关系阅读，删除可减少干扰。 |
| A-2601 | 工作关系 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2612 | 工作关系 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2624 | 工作关系 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |
| A-2640 | 资料与来源 / 资料与来源 / text / `body>div#content>div>p` | 本次核对覆盖 12 个项目的当前固定主分支来源，另外 8 个保留旧 Atlas 登记。这里显示资料是否已核对，不判断服务器是否在线。 | REVISE | 本次更新核对了 12 个项目的当前资料，另外 8 个项目暂时只保留已有登记。这里显示的是资料核对情况，不代表设备或服务器实时在线。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2642 | 资料与来源 / 资料与来源 / text / `body>div#content>div>ul>li:nth-of-type(1)` | ：来自原仓库的当前决定、结果、验收记录与课程时刻表。所有详情页保留固定提交链接。 | REVISE | ：来自原项目的当前结论、结果、完成记录和课程时刻表。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2644 | 资料与来源 / 资料与来源 / text / `body>div#content>div>ul>li:nth-of-type(2)` | ：首页四项是 A 候选的初始设置，可由本人调整；不是已经获批的新工作安排。 | REVISE | ：首页四项是当前初始设置，可由本人调整，不会改变原项目的真实优先级。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2646 | 资料与来源 / 资料与来源 / text / `body>div#content>div>ul>li:nth-of-type(3)` | ：今天能读到旧路线图，不代表旧内容重新有效。Bobbio 的接受记录、该项目的当前决策优先于旧摘要。 | REVISE | ：旧路线图仍可查看，但不会覆盖更新的项目结论。Bobbio 的完成记录和 该项目的当前研究结论优先于旧摘要。 | 信息值得保留，但原文暴露内部实施或检查语言；改为直接说明现实状态和影响。 |
| A-2647 | 资料与来源 / 资料与来源 / text / `body>div#content>div>ul>li:nth-of-type(4)>strong` | 同步边界 | REJECT | — | 这是设计或同步过程说明，不帮助用户判断现实工作。 |
| A-2648 | 资料与来源 / 资料与来源 / text / `body>div#content>div>ul>li:nth-of-type(4)` | ：原 Atlas 的 11 项访问失败提示是旧同步器的记录。当前样张使用本轮独立核对，不把该提示当实时同步结果。 | REJECT | — | 这段文字不提供新的现实状态、决定或行动，删除后更清楚。 |
| A-2649 | 资料与来源 / 资料与来源 / text / `body>div#content>div>ul>li:nth-of-type(5)>strong` | 原型边界 | REJECT | — | 这是设计或同步过程说明，不帮助用户判断现实工作。 |
| A-2650 | 资料与来源 / 资料与来源 / text / `body>div#content>div>ul>li:nth-of-type(5)` | ：此文件是可点击的静态设计样张。筛选与页面切换用于审阅设计；没有连接 GitHub 实时更新，也没有替代 Obsidian 实机验收。 | REJECT | — | 这段文字不提供新的现实状态、决定或行动，删除后更清楚。 |
| A-2655 | 资料与来源 / text / `body>div:nth-of-type(1)>div>span` | 静态设计样张 · 资料截点 2026-11-02 | REVISE | 静态设计样张 · 资料更新至 2026-11-02 | 保留事实与行动含义，改成用户能直接理解的状态和下一步。 |
| A-2666 | 资料与来源 / text / `body>div:nth-of-type(2)>aside>a:nth-of-type(3)` | 待我操作 | REVISE | 需要我 | 保留原有界面作用，改成更直接、自然的用户语言。 |
| A-2678 | 资料与来源 / text / `body>div:nth-of-type(2)>aside>div:nth-of-type(5)` | 候选 A | REJECT | — | 候选标记属于设计过程，不应进入实际工作台。 |


## 第一轮 B：全部 178 条修改 / 删除

| ID | 界面 / 位置 | 原文 | 处理 | 最终文案 | 原因 |
|---|---|---|---|---|---|
| B-0001 | HOME_DESKTOP_MOCKUP.svg / SVG 可访问名称 | Project Atlas B 首页静态设计稿 | REVISE | Project Atlas 首页 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0002 | HOME_DESKTOP_MOCKUP.svg / text[1] / x=720 y=37 | Project Atlas · Designed Workspace | REVISE | Project Atlas · 个人项目工作台 | 设计阶段元数据不应进入最终工作台。 |
| B-0007 | HOME_DESKTOP_MOCKUP.svg / text[6] / x=173.0 y=200 | 3 | REVISE | 0 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0010 | HOME_DESKTOP_MOCKUP.svg / text[9] / x=48 y=324 | 同步与新鲜度 | REVISE | 资料与来源 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0022 | HOME_DESKTOP_MOCKUP.svg / text[21] / x=28 y=858 | Border · 浅色 | REJECT | — | 设计阶段元数据不应进入最终工作台。 |
| B-0027 | HOME_DESKTOP_MOCKUP.svg / text[26] / x=986 y=166 | 按组合优先级，而不是最近提交 | REVISE | 按当前关注顺序，不按最近提交排序 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0031 | HOME_DESKTOP_MOCKUP.svg / text[30] / x=282 y=272 | 内部计算检查仍未完成 | REVISE | 数值方法仍待确定 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0033 | HOME_DESKTOP_MOCKUP.svg / text[32] / x=338 y=305 | 完成当前参考轮廓与证据收口，再决定是否设计后继采样器 | REVISE | 先解决当前计算问题，再进行完整验证 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0034 | HOME_DESKTOP_MOCKUP.svg / text[33] / x=282 y=346 | 下一次实现阶段批准 | REVISE | 第一个完整模型验证 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0035 | HOME_DESKTOP_MOCKUP.svg / text[34] / x=956 y=346 | 来源已核对 · 10月28日 | REVISE | 资料更新至 10 月 28 日 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0036 | HOME_DESKTOP_MOCKUP.svg / text[35] / x=290 y=398 | 等待收敛 | REVISE | 研究方向待确定 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0038 | HOME_DESKTOP_MOCKUP.svg / text[37] / x=276 y=451 | 冻结下一版选题方式 | REVISE | 总结前 8 轮为何没选出方向 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0039 | HOME_DESKTOP_MOCKUP.svg / text[38] / x=276 y=475 | 需要我 | REJECT | — | 当前没有已经准备好且只能由用户完成的动作。 |
| B-0042 | HOME_DESKTOP_MOCKUP.svg / text[41] / x=518 y=451 | 收口验证器修复并准备展示 | REVISE | 修正验证工具并准备 12 月展示 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0044 | HOME_DESKTOP_MOCKUP.svg / text[43] / x=774 y=398 | 基础层 | REVISE | 底层稳定性 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0046 | HOME_DESKTOP_MOCKUP.svg / text[45] / x=760 y=451 | 完成 foundation 与真实设备验收 | REVISE | 先稳定插件底层和 ChatGPT 适配 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0047 | HOME_DESKTOP_MOCKUP.svg / text[46] / x=760 y=475 | 需要我 | REJECT | — | 当前没有已经准备好且只能由用户完成的动作。 |
| B-0049 | HOME_DESKTOP_MOCKUP.svg / text[48] / x=1030 y=212 | DII | REVISE | 目前没有必须你现在处理的事情。 | 原有条目把尚未准备好的未来决策列为当前待办，改为真实空状态。 |
| B-0050 | HOME_DESKTOP_MOCKUP.svg / text[49] / x=1030 y=234 | 审核选题方式并决定是否启动第九轮 | REJECT | — | 动作尚未准备好，不能提前进入“需要我”。 |
| B-0051 | HOME_DESKTOP_MOCKUP.svg / text[50] / x=1314 y=212 | 无硬期限 | REJECT | — | 动作尚未准备好，不能提前进入“需要我”。 |
| B-0052 | HOME_DESKTOP_MOCKUP.svg / text[51] / x=1030 y=273 | Mica | REJECT | — | 动作尚未准备好，不能提前进入“需要我”。 |
| B-0053 | HOME_DESKTOP_MOCKUP.svg / text[52] / x=1030 y=295 | 在目标设备完成真实浏览器验收 | REJECT | — | 动作尚未准备好，不能提前进入“需要我”。 |
| B-0054 | HOME_DESKTOP_MOCKUP.svg / text[53] / x=1314 y=273 | 待候选准备 | REJECT | — | 动作尚未准备好，不能提前进入“需要我”。 |
| B-0055 | HOME_DESKTOP_MOCKUP.svg / text[54] / x=1030 y=334 | Lucerna | REJECT | — | 动作尚未准备好，不能提前进入“需要我”。 |
| B-0056 | HOME_DESKTOP_MOCKUP.svg / text[55] / x=1030 y=356 | 查看两套动态原型并选择方向 | REJECT | — | 动作尚未准备好，不能提前进入“需要我”。 |
| B-0057 | HOME_DESKTOP_MOCKUP.svg / text[56] / x=1314 y=334 | 材料就绪后 | REJECT | — | 动作尚未准备好，不能提前进入“需要我”。 |
| B-0058 | HOME_DESKTOP_MOCKUP.svg / text[57] / x=1010 y=426 | 异常信号 | REJECT | — | 当前没有真实异常，整个条件区应从首页消失。 |
| B-0059 | HOME_DESKTOP_MOCKUP.svg / text[58] / x=1028 y=470 | 11 个来源快照未刷新 · 查看同步状态 | REJECT | — | 维护数量没有说明现实影响，不值得占据首页。 |
| B-0061 | HOME_DESKTOP_MOCKUP.svg / text[60] / x=1334 y=534 | 未来 45 天 | REVISE | 近期已确认日期 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0063 | HOME_DESKTOP_MOCKUP.svg / text[62] / x=430 y=581 | Final Project presentation · Session 1 | REVISE | 期末项目第一场展示 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0064 | HOME_DESKTOP_MOCKUP.svg / text[63] / x=1310 y=581 | 30 天 · 12月02日 | REVISE | 12 月 2 日 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0066 | HOME_DESKTOP_MOCKUP.svg / text[65] / x=430 y=612 | Final Project presentation · Session 2 | REVISE | 期末项目第二场展示 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0067 | HOME_DESKTOP_MOCKUP.svg / text[66] / x=1310 y=612 | 37 天 · 12月09日 | REVISE | 12 月 9 日 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0069 | HOME_DESKTOP_MOCKUP.svg / text[68] / x=430 y=643 | Final Project final submission | REVISE | 期末项目最终提交 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0070 | HOME_DESKTOP_MOCKUP.svg / text[69] / x=1310 y=643 | 51 天 · 12月23日 | REVISE | 12 月 23 日 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0081 | HOME_DESKTOP_MOCKUP.svg / text[80] / x=728 y=783 | 完成当前参考轮廓与证据收口 | REVISE | 解决关键数值方法问题 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0086 | HOME_DESKTOP_MOCKUP.svg / text[85] / x=728 y=814 | 冻结下一版选题方式 | REVISE | 总结前 8 轮为何没选出方向 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0091 | HOME_DESKTOP_MOCKUP.svg / text[90] / x=728 y=845 | 准备 Final Project 展示支持 | REVISE | 准备期末项目展示 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0093 | HOME_DESKTOP_MOCKUP.svg / text[92] / x=1336 y=886 | 设计静态稿 · 使用真实项目种子数据 | REJECT | — | 设计阶段元数据不应进入最终工作台。 |
| B-0094 | ALL_PROJECTS_MOCKUP.svg / SVG 可访问名称 | Project Atlas B 全部项目静态设计稿 | REVISE | Project Atlas 全部项目 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0095 | ALL_PROJECTS_MOCKUP.svg / text[1] / x=720 y=37 | Project Atlas · Designed Workspace | REVISE | Project Atlas · 个人项目工作台 | 设计阶段元数据不应进入最终工作台。 |
| B-0102 | ALL_PROJECTS_MOCKUP.svg / text[8] / x=48 y=324 | 同步与新鲜度 | REVISE | 资料与来源 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0112 | ALL_PROJECTS_MOCKUP.svg / text[18] / x=34 y=686 | 阻塞与过期 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0113 | ALL_PROJECTS_MOCKUP.svg / text[19] / x=28 y=858 | Border · 浅色 | REJECT | — | 设计阶段元数据不应进入最终工作台。 |
| B-0115 | ALL_PROJECTS_MOCKUP.svg / text[21] / x=260 y=128 | 高密度项目组合视图 · 状态与个人关注分离 | REVISE | 集中查看所有项目，并把项目状态与当前关注分开 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0122 | ALL_PROJECTS_MOCKUP.svg / text[28] / x=786 y=194 | 当前重点 → 需要我 → 节点 → 项目名 | REVISE | 当前重点 → 需要我 → 日期 → 项目名 | 保留事实边界，但避免把尚未准备好的未来动作冒充当前待办。 |
| B-0131 | ALL_PROJECTS_MOCKUP.svg / text[37] / x=1250 y=250 | 新鲜度 | REVISE | 资料状态 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0135 | ALL_PROJECTS_MOCKUP.svg / text[41] / x=650 y=290 | 当前 1 | REVISE | 重点 1 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0136 | ALL_PROJECTS_MOCKUP.svg / text[42] / x=720 y=290 | C04 可靠性 · 完成参考轮廓与证据收口 | REVISE | 数值方法仍待确定 · 先解决关键计算问题 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0139 | ALL_PROJECTS_MOCKUP.svg / text[45] / x=1250 y=290 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0143 | ALL_PROJECTS_MOCKUP.svg / text[49] / x=650 y=332 | 当前 2 | REVISE | 重点 2 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0144 | ALL_PROJECTS_MOCKUP.svg / text[50] / x=720 y=332 | 冻结下一版选题方式，再决定是否启动第九轮 | REVISE | 总结前 8 轮未选出方向的原因，再改进选题方法 | 保留事实边界，但避免把尚未准备好的未来动作冒充当前待办。 |
| B-0146 | ALL_PROJECTS_MOCKUP.svg / text[52] / x=1170 y=332 | 是 | REJECT | — | 这段文字对用户当前理解或行动没有价值，应从界面删除。 |
| B-0147 | ALL_PROJECTS_MOCKUP.svg / text[53] / x=1250 y=332 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0151 | ALL_PROJECTS_MOCKUP.svg / text[57] / x=650 y=374 | 当前 3 | REVISE | 重点 3 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0152 | ALL_PROJECTS_MOCKUP.svg / text[58] / x=720 y=374 | 收口 validator 修复证据并准备 Final Project 展示 | REVISE | 修正三组课程验证工具，并准备期末项目展示 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0155 | ALL_PROJECTS_MOCKUP.svg / text[61] / x=1250 y=374 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0159 | ALL_PROJECTS_MOCKUP.svg / text[65] / x=650 y=416 | 当前 4 | REVISE | 重点 4 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0160 | ALL_PROJECTS_MOCKUP.svg / text[66] / x=720 y=416 | 完成 foundation 与真实登录态设备验收 | REVISE | 稳定插件底层与 ChatGPT 兼容方式 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0162 | ALL_PROJECTS_MOCKUP.svg / text[68] / x=1170 y=416 | 是 | REJECT | — | 这段文字对用户当前理解或行动没有价值，应从界面删除。 |
| B-0163 | ALL_PROJECTS_MOCKUP.svg / text[69] / x=1250 y=416 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0168 | ALL_PROJECTS_MOCKUP.svg / text[74] / x=720 y=458 | 继续课程材料数字化；作业日期只取权威来源 | REVISE | 继续整理课程材料；作业日期只使用课程正式信息 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0171 | ALL_PROJECTS_MOCKUP.svg / text[77] / x=1250 y=458 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0176 | ALL_PROJECTS_MOCKUP.svg / text[82] / x=720 y=500 | 完成两套动态原型；材料就绪后由用户选方向 | REVISE | 先完成两套可运行的动态主题，再由用户选择一个继续 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0178 | ALL_PROJECTS_MOCKUP.svg / text[84] / x=1170 y=500 | 条件式 | REJECT | — | 这段文字对用户当前理解或行动没有价值，应从界面删除。 |
| B-0179 | ALL_PROJECTS_MOCKUP.svg / text[85] / x=1250 y=500 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0184 | ALL_PROJECTS_MOCKUP.svg / text[90] / x=720 y=542 | 完成 staging closure，再进入 founder go/no-go | REVISE | 先完成测试环境的真实匹配检查，再决定是否启用 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0187 | ALL_PROJECTS_MOCKUP.svg / text[93] / x=1250 y=542 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0192 | ALL_PROJECTS_MOCKUP.svg / text[98] / x=720 y=584 | 在正式 Maintenance Board 推进成熟候选 | REVISE | 在正式维护看板中处理已经准备好的改进项 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0195 | ALL_PROJECTS_MOCKUP.svg / text[101] / x=1250 y=584 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0200 | ALL_PROJECTS_MOCKUP.svg / text[106] / x=720 y=626 | 0.2.0 已验收；决定并启动 0.3.0 第一项 | REVISE | 0.2.0 已确认可用；下一步确定 0.3.0 的第一项功能 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0203 | ALL_PROJECTS_MOCKUP.svg / text[109] / x=1250 y=626 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0208 | ALL_PROJECTS_MOCKUP.svg / text[114] / x=720 y=668 | 仅在 staffed 窗口执行剩余真实验证 | REVISE | 只在有人可现场配合时完成剩余真实验证 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0211 | ALL_PROJECTS_MOCKUP.svg / text[117] / x=1250 y=668 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0216 | ALL_PROJECTS_MOCKUP.svg / text[122] / x=720 y=710 | 回港后完成 Mac mini 本地 AI 与 agent 基线 | REVISE | 回港后完成 Mac mini 本地 AI 与常驻服务配置 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0219 | ALL_PROJECTS_MOCKUP.svg / text[125] / x=1250 y=710 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0224 | ALL_PROJECTS_MOCKUP.svg / text[130] / x=720 y=752 | 灾备迁移完成后保持安静，仅异常时升级 | REVISE | 迁移完成后保持安静，只有异常时提醒 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0227 | ALL_PROJECTS_MOCKUP.svg / text[133] / x=1250 y=752 | 已核对 | REJECT | — | 正常资料状态不需要逐行重复，表格只显示需要留意的例外。 |
| B-0232 | ALL_PROJECTS_MOCKUP.svg / text[138] / x=720 y=794 | 冻结复杂系统机制并验证实现充分性 | REVISE | 先确定复杂系统机制，再验证实现是否足够 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0235 | ALL_PROJECTS_MOCKUP.svg / text[141] / x=1250 y=794 | 待复核 | REVISE | 资料待核对 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0236 | ALL_PROJECTS_MOCKUP.svg / text[142] / x=282 y=826 | 13 个真实项目 · 原型视图可扩展到 30–50 行 | REJECT | — | 设计阶段元数据不应进入最终工作台。 |
| B-0238 | ALL_PROJECTS_MOCKUP.svg / text[144] / x=1336 y=886 | 设计静态稿 · 高密度项目扫描 | REJECT | — | 设计阶段元数据不应进入最终工作台。 |
| B-0239 | CODEX_HANDOFF.md / 首页“需要我”种子状态 | DII、Mica、Lucerna 三项未来人工动作 | REVISE | 目前没有必须你现在处理的事情。 | 三个动作都还没有准备到可立即执行，首页必须显示真实空状态。 |
| B-0240 | CODEX_HANDOFF.md / 原型种子数据 / 设计阶段提示 | 原型优先级待用户确认 | REJECT | — | 这是设计阶段说明，不应显示在用户每天使用的工作台。 |
| B-0241 | DESIGN.md / 首页结构图 / 需要我 | 1. DII 启动判断 | REVISE | 目前没有必须你现在 | 当前动作尚未准备好，结构图必须显示真实空状态。 |
| B-0242 | DESIGN.md / 首页结构图 / 需要我 | 2. Mica 真实机验收 | REVISE | 处理的事情。 | 当前动作尚未准备好，结构图必须显示真实空状态。 |
| B-0243 | DESIGN.md / 首页结构图 / 需要我 | 3. Lucerna 方向选择 | REJECT | — | 当前动作尚未准备好，结构图必须显示真实空状态。 |
| B-0244 | REAL_PROJECT_WALKTHROUGH.md / DII / 右侧动作栏种子 | Distributed Imaging Inference / 审核选题方式并决定是否启动第九轮 / 无硬期限 | REVISE | 目前没有必须你现在处理的事情。 | 选题总结尚未完成，不能把未来决策显示成当前待办。 |
| B-0245 | VISUAL_SYSTEM.md / 资料状态 / current | 已核对 | REJECT | — | 正常资料状态不需要在每一行重复，只有异常才值得显示。 |
| B-0246 | DATA_MODEL.md / ### DII / 当前“需要我”种子 | 审核收敛后的选题方式，并决定是否启动第九轮 | REJECT | — | 动作材料尚未准备好，当前不能要求用户执行。 |
| B-0247 | REAL_PROJECT_WALKTHROUGH.md / ## DII：没有传统 Roadmap 也能成为完整项目 / 当前“需要我”种子 | 审核收敛后的选题方式，并决定是否启动第九轮 | REJECT | — | 动作材料尚未准备好，当前不能要求用户执行。 |
| B-0248 | REAL_PROJECT_WALKTHROUGH.md / ## Lucerna：产品阶段、下一验收与用户选择分开 / 当前“需要我”种子 | 查看两套实际动态原型并选择进入 Figma 的方向 | REJECT | — | 动作材料尚未准备好，当前不能要求用户执行。 |
| B-0249 | REAL_PROJECT_WALKTHROUGH.md / ## Mica for ChatGPT：真实设备验收是人工动作，不是产品百分比 / 当前“需要我”种子 | 在目标 Chrome/Edge 或 MacBook Neo 上完成最终真实浏览器验收 | REJECT | — | 动作材料尚未准备好，当前不能要求用户执行。 |
| B-0250 | CODEX_HANDOFF.md / UI 种子 / 第 58 行 / occurrence 1 | 04 同步与新鲜度.md | REVISE | 04 资料与来源.md | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0251 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 24 行 / occurrence 1 | 04 同步与新鲜度.md | REVISE | 04 资料与来源.md | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0252 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 245 行 / occurrence 2 | 04 同步与新鲜度.md | REVISE | 04 资料与来源.md | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0253 | OBSIDIAN_IMPLEMENTATION_SPEC.md / UI 种子 / 第 78 行 / occurrence 1 | 04 同步与新鲜度.md | REVISE | 04 资料与来源.md | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0254 | OBSIDIAN_IMPLEMENTATION_SPEC.md / UI 种子 / 第 338 行 / occurrence 2 | 04 同步与新鲜度.md | REVISE | 04 资料与来源.md | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0255 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 68 行 / occurrence 1 | 同步与新鲜度 | REVISE | 资料与来源 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0256 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 92 行 / occurrence 2 | 同步与新鲜度 | REVISE | 资料与来源 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0257 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 245 行 / occurrence 3 | 同步与新鲜度 | REVISE | 资料与来源 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0258 | OBSIDIAN_IMPLEMENTATION_SPEC.md / UI 种子 / 第 205 行 / occurrence 1 | 同步与新鲜度 | REVISE | 资料与来源 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0259 | OBSIDIAN_IMPLEMENTATION_SPEC.md / UI 种子 / 第 205 行 / occurrence 2 | 同步与新鲜度 | REVISE | 资料与来源 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0260 | CODEX_HANDOFF.md / UI 种子 / 第 300 行 / occurrence 1 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0261 | DATA_MODEL.md / UI 种子 / 第 132 行 / occurrence 1 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0262 | DESIGN.md / UI 种子 / 第 10 行 / occurrence 1 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0263 | DESIGN.md / UI 种子 / 第 59 行 / occurrence 2 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0264 | DESIGN.md / UI 种子 / 第 73 行 / occurrence 3 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0265 | DESIGN.md / UI 种子 / 第 118 行 / occurrence 4 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0266 | DESIGN.md / UI 种子 / 第 138 行 / occurrence 5 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0267 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 141 行 / occurrence 1 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0268 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 143 行 / occurrence 2 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0269 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 366 行 / occurrence 3 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0270 | OBSIDIAN_IMPLEMENTATION_SPEC.md / UI 种子 / 第 230 行 / occurrence 1 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0271 | OBSIDIAN_IMPLEMENTATION_SPEC.md / UI 种子 / 第 427 行 / occurrence 2 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0272 | VISUAL_SYSTEM.md / UI 种子 / 第 195 行 / occurrence 1 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0273 | VISUAL_SYSTEM.md / UI 种子 / 第 204 行 / occurrence 2 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0274 | VISUAL_SYSTEM.md / UI 种子 / 第 340 行 / occurrence 3 | 异常信号 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0275 | CODEX_HANDOFF.md / UI 种子 / 第 264 行 / occurrence 1 | 阻塞与过期 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0276 | DESIGN.md / UI 种子 / 第 83 行 / occurrence 1 | 阻塞与过期 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0277 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 200 行 / occurrence 1 | 阻塞与过期 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0278 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 354 行 / occurrence 2 | 阻塞与过期 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0279 | OBSIDIAN_IMPLEMENTATION_SPEC.md / UI 种子 / 第 187 行 / occurrence 1 | 阻塞与过期 | REVISE | 需要留意 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0280 | DATA_MODEL.md / UI 种子 / 第 134 行 / occurrence 1 | 来源与新鲜度 | REVISE | 来源与资料状态 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0281 | DESIGN.md / UI 种子 / 第 99 行 / occurrence 1 | 来源与新鲜度 | REVISE | 来源与资料状态 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0282 | OBSIDIAN_IMPLEMENTATION_SPEC.md / UI 种子 / 第 279 行 / occurrence 1 | 来源与新鲜度 | REVISE | 来源与资料状态 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0283 | CODEX_HANDOFF.md / UI 种子 / 第 326 行 / occurrence 1 | 来源/新鲜度 | REVISE | 来源/资料状态 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0284 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 269 行 / occurrence 1 | 来源新鲜度 | REVISE | 资料状态 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0285 | DESIGN.md / UI 种子 / 第 80 行 / occurrence 1 | 项目 &#124; 类型 &#124; 状态 &#124; 当前阶段 &#124; 关注 &#124; 下一步 &#124; 节点 &#124; 需要我 &#124; 新鲜度 | REVISE | 项目 &#124; 类型 &#124; 状态 &#124; 当前阶段 &#124; 关注 &#124; 下一步 &#124; 节点 &#124; 需要我 &#124; 资料状态 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0286 | CODEX_HANDOFF.md / UI 种子 / 第 288 行 / occurrence 1 | 默认列为项目、类型、状态、当前阶段、关注、下一步、节点、需要我、新鲜度 | REVISE | 默认列为项目、类型、状态、当前阶段、关注、下一步、节点、需要我、资料状态 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0287 | OBSIDIAN_IMPLEMENTATION_SPEC.md / UI 种子 / 第 174 行 / occurrence 1 | 列：项目、类型、状态、当前阶段、关注、下一步、节点、需要我、新鲜度 | REVISE | 列：项目、类型、状态、当前阶段、关注、下一步、节点、需要我、资料状态 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0288 | VISUAL_SYSTEM.md / UI 种子 / 第 244 行 / occurrence 1 | 类型、状态、新鲜度使用短标签 | REVISE | 类型、状态、资料状态使用短标签 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0289 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 23 行 / occurrence 1 | 完成当前参考轮廓与证据收口，再决定是否设计后继采样器 | REVISE | 先解决当前计算问题，再进行完整验证 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0290 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 41 行 / occurrence 2 | 完成当前参考轮廓与证据收口，再决定是否设计后继采样器 | REVISE | 先解决当前计算问题，再进行完整验证 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0291 | DATA_MODEL.md / UI 种子 / 第 29 行 / occurrence 1 | 完成当前参考分布轮廓并据证据决定是否设计后继采样器 | REVISE | 先解决当前计算问题，再进行完整验证 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0292 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 38 行 / occurrence 1 | 内部计算检查仍未完成 | REVISE | 数值方法仍待确定 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0293 | DATA_MODEL.md / UI 种子 / 第 26 行 / occurrence 1 | C04 reference reliability 与开放尾部数值问题 | REVISE | 数值方法仍待确定 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0294 | DATA_MODEL.md / UI 种子 / 第 33 行 / occurrence 1 | 下一次实现阶段批准 | REVISE | 第一个完整模型验证 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0295 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 25 行 / occurrence 1 | 下一次实现阶段批准 | REVISE | 第一个完整模型验证 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0296 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 43 行 / occurrence 2 | 下一次实现阶段批准 | REVISE | 第一个完整模型验证 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0297 | DATA_MODEL.md / UI 种子 / 第 34 行 / occurrence 1 | 内部计算问题仍未解决 | REVISE | 当前计算方法仍不够可靠 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0298 | DATA_MODEL.md / UI 种子 / 第 333 行 / occurrence 1 | 八轮历史与三份根因审计的选题方式收敛 | REVISE | 前 8 轮仍未选出值得长期投入的方向 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0299 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 70 行 / occurrence 1 | 八轮历史与三份根因审计的选题方式收敛 | REVISE | 前 8 轮仍未选出值得长期投入的方向 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0300 | DATA_MODEL.md / UI 种子 / 第 336 行 / occurrence 1 | 合并根因审计、历史与导师反馈，冻结下一版选题方式 | REVISE | 总结前 8 轮为什么没有选出方向，改进选题方法，再决定是否开始下一轮 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0301 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 73 行 / occurrence 1 | 合并根因审计、历史与导师反馈，冻结下一版选题方式 | REVISE | 总结前 8 轮为什么没有选出方向，改进选题方法，再决定是否开始下一轮 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0302 | DATA_MODEL.md / UI 种子 / 第 270 行 / occurrence 1 | 冻结下一版选题方式，再决定是否启动第九轮 | REVISE | 总结前 8 轮未选出方向的原因，再改进选题方法 | 保留事实边界，但避免把尚未准备好的未来动作冒充当前待办。 |
| B-0303 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 88 行 / occurrence 1 | 冻结下一版选题方式 | REVISE | 总结前 8 轮为何没选出方向 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0304 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 142 行 / occurrence 1 | Tutorial / HW1 / Project validator 限定修复与 Final Project 准备 | REVISE | 三组课程验证工具修正与期末项目准备 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0305 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 145 行 / occurrence 1 | 收口 validator 修复证据，并准备 12 月展示与最终提交支持 | REVISE | 先修正三组课程验证工具，再准备 12 月 2 日的第一场期末项目展示 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0306 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 148 行 / occurrence 1 | Final Project presentation · Session 1 | REVISE | 期末项目第一场展示 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0307 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 189 行 / occurrence 1 | Living Atmosphere 视觉阶段 2 + validator hardening 准备 | REVISE | 两套 Windows 动态主题制作中 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0308 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 191 行 / occurrence 1 | 完成两套可见动态原型；通过后由用户选一套进入 Figma | REVISE | 先完成两套可运行的 Windows 动态主题，再由用户选择一个继续 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0309 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 220 行 / occurrence 1 | Product System Rebuild foundation | REVISE | 插件底层与 ChatGPT 兼容方式 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0310 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 223 行 / occurrence 1 | 按冻结目标完成 foundation，并在真实登录态设备执行一次有界验收 | REVISE | 先把插件底层和 ChatGPT 兼容方式做稳定，之后优先恢复长对话优化，再做高亮和 PDF | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0311 | DATA_MODEL.md / UI 种子 / 第 371 行 / occurrence 1 | post-0.5.25 Matching staging closure | REVISE | 测试环境的真实匹配流程检查 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0312 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 241 行 / occurrence 1 | post-0.5.25 Matching staging closure | REVISE | 测试环境的真实匹配流程检查 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0313 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 248 行 / occurrence 2 | post-0.5.25 Matching staging closure | REVISE | 测试环境的真实匹配流程检查 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0314 | DATA_MODEL.md / UI 种子 / 第 373 行 / occurrence 1 | 完成 staging 产品与黑箱证据，再进入独立 founder go/no-go | REVISE | 先完成测试环境的真实匹配流程检查；确认结果可靠后，再决定是否启用真实匹配 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0315 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 250 行 / occurrence 1 | 完成 staging 产品与黑箱证据，再进入独立 founder go/no-go | REVISE | 先完成测试环境的真实匹配流程检查；确认结果可靠后，再决定是否启用真实匹配 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0316 | DATA_MODEL.md / UI 种子 / 第 375 行 / occurrence 1 | Founder go/no-go after staging closure | REVISE | 真实匹配启用决定（检查完成后） | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0317 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 252 行 / occurrence 1 | Founder go/no-go after staging closure | REVISE | 真实匹配启用决定（检查完成后） | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0318 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 283 行 / occurrence 1 | 0.2.0 accepted · 0.3.0 enhanced annotations 待启动 | REVISE | 0.2.0 已确认可用；0.3.0 尚未开始 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0319 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 285 行 / occurrence 1 | 决定并启动 0.3.0 第一项 straight line / arrow | REVISE | 先确定 0.3.0 最值得做的第一项标注功能 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0320 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 304 行 / occurrence 1 | 真实项目反馈收集与维护候选收敛 | REVISE | 收集真实使用反馈并整理下一批改进 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0321 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 306 行 / occurrence 1 | 在正式维护看板中推进已成熟候选，不在 Atlas 复制状态 | REVISE | 在正式维护看板中处理已经准备好的改进项 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0322 | DATA_MODEL.md / UI 种子 / 第 391 行 / occurrence 1 | Longleaf 与 Workstation 生产访问体系运行；部分 staffed validation 待窗口 | REVISE | Longleaf 与 Workstation 远程访问正常；仍有少量现场验证待完成 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0323 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 336 行 / occurrence 1 | Longleaf 与 Workstation 生产访问体系运行；部分 staffed validation 待窗口 | REVISE | Longleaf 与 Workstation 远程访问正常；仍有少量现场验证待完成 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0324 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 338 行 / occurrence 1 | 仅在 staffed 窗口执行尚未完成的真实验证 | REVISE | 只在有人可现场配合时完成剩余真实验证 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0325 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 393 行 / occurrence 1 | Mac mini 本地 AI 与常驻 agent 基线待部署 | REVISE | Mac mini 本地 AI 与常驻服务尚未配置完成 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0326 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 395 行 / occurrence 1 | 回港后按冻结基线完成本地 AI、agent 与服务安装 | REVISE | 回港后完成本地 AI、常驻服务与必要工具配置 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0327 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 367 行 / occurrence 1 | 完成 emergency operator 启用条件与真实灾备验收 | REVISE | 完成灾备迁移设置并做一次真实切换检查 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0328 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 369 行 / occurrence 1 | 配置明确要求的 Secrets，并执行一次受控网页迁移验收 | REVISE | 按迁移说明补齐必要凭据，并做一次受控切换检查 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0329 | VISUAL_SYSTEM.md / UI 种子 / 第 299 行 / occurrence 1 | 待复核 | REVISE | 资料待核对 | 信息值得保留，但原文暴露内部实施、维护或机器语言；改为现实状态和行动。 |
| B-0330 | VISUAL_SYSTEM.md / UI 种子 / 第 11 行 / occurrence 1 | 来源不可用 | REVISE | 资料暂时无法核对 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0331 | VISUAL_SYSTEM.md / UI 种子 / 第 87 行 / occurrence 2 | 来源不可用 | REVISE | 资料暂时无法核对 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0332 | VISUAL_SYSTEM.md / UI 种子 / 第 300 行 / occurrence 3 | 来源不可用 | REVISE | 资料暂时无法核对 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0333 | VISUAL_SYSTEM.md / UI 种子 / 第 303 行 / occurrence 4 | 来源不可用 | REVISE | 资料暂时无法核对 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |
| B-0334 | VISUAL_SYSTEM.md / UI 种子 / 第 301 行 / occurrence 1 | 手工维护 | REVISE | 手工更新 | 保留原有信息作用，改成用户能直接理解的现实状态、影响或下一步。 |


## 第二轮 A：第一轮 PASS 后再次发现的全部 72 条

| ID | 界面 / 位置 | 原文 | 处理 | 最终文案 | 原因 |
|---|---|---|---|---|---|
| A-0061 | 空筛选状态 / 全部项目 / option / `body>select#focus-filter` | 资料待复核 | REVISE | 资料待核对 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0138 | 全部项目 / 全部项目 / option / `body>select#focus-filter` | 资料待复核 | REVISE | 资料待核对 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0203 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(15)>td:nth-of-type(3)>span` | 底层重建方案已确定 | REVISE | 插件底层方案已确定 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0212 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(16)>td:nth-of-type(5)>span` | 核对两台 Mac 的实际部署与连接验收记录。 | REVISE | 核对两台 Mac 是否已经安装并能正常连接。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0252 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(3)>span` | 课程验证器仍需修正 | REVISE | 三组自动检查工具仍需修正 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0254 | 全部项目 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(5)>span` | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | REVISE | 先修正三组自动检查工具中已发现的问题，再确认课程材料能否正常运行。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0354 | 需要留意筛选 / 全部项目 / option / `body>select#focus-filter` | 资料待复核 | REVISE | 资料待核对 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0444 | 47 行容量 / 容量样张 / option / `body>select#focus-filter` | 资料待复核 | REVISE | 资料待核对 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0635 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(3)>span` | 课程验证器仍需修正 | REVISE | 三组自动检查工具仍需修正 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0637 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(5)>span` | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | REVISE | 先修正三组自动检查工具中已发现的问题，再确认课程材料能否正常运行。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0642 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(30)>td:nth-of-type(3)>span` | 底层重建方案已确定 | REVISE | 插件底层方案已确定 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0675 | 47 行容量 / text / `body>div#content>div>div:nth-of-type(3)>table>tbody>tr:nth-of-type(34)>td:nth-of-type(5)>span` | 核对两台 Mac 的实际部署与连接验收记录。 | REVISE | 核对两台 Mac 是否已经安装并能正常连接。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0937 | 当前关注筛选 / 全部项目 / option / `body>select#focus-filter` | 资料待复核 | REVISE | 资料待核对 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0974 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(3)>span` | 课程验证器仍需修正 | REVISE | 三组自动检查工具仍需修正 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-0976 | 当前关注筛选 / text / `body>div#content>div>div:nth-of-type(2)>table>tbody>tr:nth-of-type(3)>td:nth-of-type(5)>span` | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | REVISE | 先修正三组自动检查工具中已发现的问题，再确认课程材料能否正常运行。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1062 | 深色首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(3)>div:nth-of-type(1)` | 课程与教学 · 课程材料检查 · 课程验证器仍需修正 | REVISE | 课程与教学 · 课程材料检查 · 三组自动检查工具仍需修正 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1064 | 深色首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(3)>div:nth-of-type(2)` | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | REVISE | 先修正三组自动检查工具中已发现的问题，再确认课程材料能否正常运行。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1149 | 首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(3)>div:nth-of-type(1)` | 课程与教学 · 课程材料检查 · 课程验证器仍需修正 | REVISE | 课程与教学 · 课程材料检查 · 三组自动检查工具仍需修正 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1151 | 首页 / 关注项目 / text / `body>div#content>div>div>section:nth-of-type(1)>ul>li:nth-of-type(3)>div:nth-of-type(2)` | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | REVISE | 先修正三组自动检查工具中已发现的问题，再确认课程材料能否正常运行。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1230 | 项目页 / ai-skills / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>div` | 维护生命周期、Issue 与 Area 以 GitHub Project 为准；本轮没有读取实时看板字段。 | REVISE | 具体事项和分类以 GitHub Project 看板为准；这里没有读取看板的实时状态。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1295 | 项目页 / asteria / Asteria / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 目前没有必须你现在处理的事情。 | REVISE | 是否需要你处理还没有确认。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1306 | 项目页 / asteria / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要你处理，都还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1307 | 项目页 / asteria / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>div` | 保留原 Atlas 登记；只读到旧规划快照，本轮没有核对当前项目结果。 | REVISE | 目前只保留原来的项目登记和材料入口；当前项目进展还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1369 | 项目页 / bobbio / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>div` | 0.2 的完成记录优先。旧里程碑仍写着待检查，不会再次生成同一项待办。 | REVISE | 以 0.2 的完成记录为准；旧摘要里的待检查项已经过时，不需要再处理。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1425 | 项目页 / bridge / Bridge Kit / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 目前没有必须你现在处理的事情。 | REVISE | 是否需要你处理还没有确认。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1436 | 项目页 / bridge / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要你处理，都还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1437 | 项目页 / bridge / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>div` | 保留原 Atlas 登记；只读到旧规划快照，本轮没有核对当前项目结果。 | REVISE | 目前只保留原来的项目登记和材料入口；当前项目进展还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1487 | 项目页 / cardiac / CardiacNexus / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 目前没有必须你现在处理的事情。 | REVISE | 是否需要你处理还没有确认。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1498 | 项目页 / cardiac / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要你处理，都还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1499 | 项目页 / cardiac / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>div` | 保留原 Atlas 登记；只读到旧规划快照，本轮没有核对当前项目结果。 | REVISE | 目前只保留原来的项目登记和材料入口；当前项目进展还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1699 | 项目页 / cmrx / CMRxRecon25 / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 目前没有必须你现在处理的事情。 | REVISE | 是否需要你处理还没有确认。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1710 | 项目页 / cmrx / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要你处理，都还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1711 | 项目页 / cmrx / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>div` | 保留原 Atlas 登记；只读到旧规划快照，本轮没有核对当前项目结果。 | REVISE | 目前只保留原来的项目登记和材料入口；当前项目进展还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1777 | 项目页 / cuhk-date / 下一验收 / text / `body>div#content>article>section:nth-of-type(3)>p` | 先在测试环境完成匹配流程检查和必要修正，再决定是否启用真实匹配。现在还没有准备好需要本人作出的上线决定。 | REVISE | 先在测试环境完成匹配流程检查和必要修正，再决定是否启用真实匹配。现在还不到作出上线决定的时候。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1778 | 项目页 / cuhk-date / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>div` | 测试环境评阅是可选入口，不是当前阻塞。真实匹配是否启用，要等工程前提和检查结果都准备好。 | REVISE | 测试环境检查是可选入口，不是当前阻塞。是否启用真实匹配，要等匹配流程和检查结果都准备好。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1851 | 项目页 / dii / 下一次判断前 / text / `body>div#content>article>section:nth-of-type(3)>p` | 先总结前 8 轮为什么一直没选出来，并结合导师反馈改进选题方法。目前还没有准备好需要本人选择的方案。 | REVISE | 先总结前 8 轮为什么一直没选出来，并结合导师反馈改进选题方法。目前还没有准备好需要你选择的方案。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1908 | 项目页 / echo / Echo Select / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 目前没有必须你现在处理的事情。 | REVISE | 是否需要你处理还没有确认。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1919 | 项目页 / echo / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要你处理，都还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1920 | 项目页 / echo / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>div` | 保留原 Atlas 登记；只读到旧规划快照，本轮没有核对当前项目结果。 | REVISE | 目前只保留原来的项目登记和材料入口；当前项目进展还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-1981 | 项目页 / local / 客户端验收 / text / `body>div#content>article>section:nth-of-type(2)>p` | Windows 端共享和读写已经通过；Mac mini 还需要实际挂载并测试读写。先由设备端执行器完成，只有遇到无法代办的账户认证时才需要本人处理。目前没有证据表明认证已经成为阻塞。 | REVISE | Windows 端共享和读写已经通过；Mac mini 还需要实际挂载并测试读写。先在 Mac mini 上完成检查；只有需要账户认证时才需要你处理。目前还没有遇到账户认证问题。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2108 | 项目页 / mica / Mica for ChatGPT / text / `body>div#content>article>div:nth-of-type(2)>span:nth-of-type(1)` | 底层重建方案已确定 | REVISE | 插件底层方案已确定 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2122 | 项目页 / mica / 当前判断 / text / `body>div#content>article>section:nth-of-type(1)>p` | 插件底层与 ChatGPT 兼容性。底层重建方案已确定。 | REVISE | 插件底层与 ChatGPT 兼容性。插件底层方案已确定。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2126 | 项目页 / mica / 验收条件 / text / `body>div#content>article>section:nth-of-type(3)>p` | 当前还没有可供日常检查的版本，暂时不需要本人处理。等工程条件成熟后，再由原项目发起用户评阅。 | REVISE | 现在还没有可实际使用的版本，你暂时不用处理。等版本可以试用后，再打开检查。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2127 | 项目页 / mica / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>div` | 当前顺序以底层重建方案为准；方案已经确定，不代表代码已经完成。 | REVISE | 当前顺序以插件底层方案为准；方案已经确定，但代码还没有完成。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2131 | 项目页 / mica / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>ul>li:nth-of-type(1)>a` | 底层重建方案 | REVISE | 插件底层方案 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2182 | 项目页 / remote / Remote Compute / text / `body>div#content>article>div:nth-of-type(3)>p` | 核对两台 Mac 的实际部署与连接验收记录。 | REVISE | 核对两台 Mac 是否已经安装并能正常连接。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2190 | 项目页 / remote / Remote Compute / text / `body>div#content>article>p` | 维护 Longleaf、CUHK Workstation 与 WSL 的远程接入、连接生命周期和中继职责。 | REVISE | 维护 Longleaf、CUHK Workstation 与 WSL 的远程接入、连接切换和中继配置。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2196 | 项目页 / remote / 接入状态 / text / `body>div#content>article>section:nth-of-type(3)>p` | macOS 自动选择器已有代码和安装说明，但两台 Mac 是否已经安装并通过连接检查，还需要设备记录确认。现在不需要本人操作。 | REVISE | macOS 自动切换连接方式的工具已经有代码和安装说明，但还没有确认两台 Mac 是否已安装并能正常连接。现在不用你处理。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2197 | 项目页 / remote / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>div` | 代码与部署合同不证明两台 Mac 已部署；本轮未读取实时设备状态。旧 A25 切换待办已被正式验收覆盖。 | REVISE | 已有代码和安装说明不能证明两台 Mac 已经完成安装；本轮也没有读取实时设备状态。旧 A25 切换事项已有完成记录。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2256 | 项目页 / seminar / SeminarArc / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 目前没有必须你现在处理的事情。 | REVISE | 是否需要你处理还没有确认。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2267 | 项目页 / seminar / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要你处理，都还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2268 | 项目页 / seminar / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>div` | 保留原 Atlas 登记；只读到旧规划快照，本轮没有核对当前项目结果。 | REVISE | 目前只保留原来的项目登记和材料入口；当前项目进展还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2318 | 项目页 / shione / Shione / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 目前没有必须你现在处理的事情。 | REVISE | 是否需要你处理还没有确认。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2329 | 项目页 / shione / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要你处理，都还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2330 | 项目页 / shione / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>div` | 保留原 Atlas 登记；只读到旧规划快照，本轮没有核对当前项目结果。 | REVISE | 目前只保留原来的项目登记和材料入口；当前项目进展还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2380 | 项目页 / stat5050 / STAT5050 / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 目前没有必须你现在处理的事情。 | REVISE | 是否需要你处理还没有确认。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2394 | 项目页 / stat5050 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(4)>div` | 作业区尚无具体题目或截止时间；缺字段不等于逾期，也不自动产生本人任务。 | REVISE | 作业区还没有具体题目或截止时间；没有登记不等于逾期，也不会自动变成你的待办。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2446 | 项目页 / stat5060 / STAT5060 TA / text / `body>div#content>article>div:nth-of-type(2)>span:nth-of-type(2)` | 课程验证器仍需修正 | REVISE | 三组自动检查工具仍需修正 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2450 | 项目页 / stat5060 / STAT5060 TA / text / `body>div#content>article>div:nth-of-type(3)>p` | 先修正三组验证器中已经确认的问题，再重新检查课程材料是否能按预期运行。 | REVISE | 先修正三组自动检查工具中已发现的问题，再确认课程材料能否正常运行。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2452 | 项目页 / stat5060 / STAT5060 TA / text / `body>div#content>article>dl>dd:nth-of-type(2)` | 三组验证器仍有已确认的问题需要修正；评分分项和课程政策由任课教师决定。 | REVISE | 三组自动检查工具仍有已发现的问题需要修正；评分分项和课程政策由任课教师决定。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2458 | 项目页 / stat5060 / STAT5060 TA / text / `body>div#content>article>p` | 组织高级建模与数据分析课程的习题课、作业与期末项目材料，并检查评分、发布和课程使用证据。 | REVISE | 组织高级建模与数据分析课程的习题课、作业与期末项目材料，并核对评分、发布和实际使用情况。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2460 | 项目页 / stat5060 / 当前判断 / text / `body>div#content>article>section:nth-of-type(1)>p` | 课程材料检查。课程验证器仍需修正。 | REVISE | 课程材料检查。三组自动检查工具仍需修正。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2462 | 项目页 / stat5060 / 当前教学工作 / text / `body>div#content>article>section:nth-of-type(2)>p` | 三组验证器已经实现，独立检查确认了三个需要修正的问题。修正并重新检查后，才能用于课程。 | REVISE | 三组自动检查工具已经做出，现有检查发现三个需要修正的问题。修正并重新检查后，才能用于课程。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2464 | 项目页 / stat5060 / 已过去的节点 / text / `body>div#content>article>section:nth-of-type(3)>p` | HW1 的学生截止时间是 11 月 1 日 23:59。提交与收齐状态还没有确认，因此不会记成 TA 本人逾期。 | REVISE | HW1 的学生截止时间是 11 月 1 日 23:59。提交与收齐状态还没有确认，因此不会算作你的逾期事项。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2467 | 项目页 / stat5060 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(5)>div` | 旧索引仍写着尚未实施，但三组验证器已经有代码；修正已确认的问题并重新检查后，才能用于课程。 | REVISE | 旧索引还没有更新；三组自动检查工具已经做出，但发现的问题还没修完，因此暂时不能用于课程。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2471 | 项目页 / stat5060 / 材料与来源 / text / `body>div#content>article>section:nth-of-type(5)>ul>li:nth-of-type(1)>a` | 验证器问题清单 | REVISE | 自动检查工具问题清单 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2523 | 项目页 / zotero / Zotero 文献镜像 / text / `body>div#content>article>dl>dd:nth-of-type(1)` | 目前没有必须你现在处理的事情。 | REVISE | 是否需要你处理还没有确认。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2534 | 项目页 / zotero / 资料边界 / text / `body>div#content>article>section:nth-of-type(2)>p` | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要本人处理，都还没有重新核对。 | REVISE | 目前只确认了项目和材料入口；当前进度、下一步以及是否需要你处理，都还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2535 | 项目页 / zotero / 材料与来源 / text / `body>div#content>article>section:nth-of-type(3)>div` | 保留原 Atlas 登记；只读到旧规划快照，本轮没有核对当前项目结果。 | REVISE | 目前只保留原来的项目登记和材料入口；当前项目进展还没有重新核对。 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2582 | 工作关系 / 工作关系 / text / `body>div#content>div>div>svg>a:nth-of-type(2)>text:nth-of-type(2)` | 接入、中继与运行语义 | REVISE | 远程接入与中继 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2590 | 工作关系 / 工作关系 / text / `body>div#content>div>div>svg>text:nth-of-type(4)` | 提供状态 | REVISE | 提供连接状态 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |
| A-2598 | 工作关系 / 工作关系 / text / `body>div#content>div>header>div:nth-of-type(2)` | 只显示关系，不重复保存状态 | REVISE | 只显示实际关系 | 上一轮最终可见文字仍偏内部、抽象或机械；改为直接说明现实状态、下一步或是否需要你处理。 |


## 第二轮 B：第一轮 PASS 后再次发现的全部 25 条

| ID | 界面 / 位置 | 原文 | 处理 | 最终文案 | 原因 |
|---|---|---|---|---|---|
| B-0024 | HOME_DESKTOP_MOCKUP.svg / text[23] / x=260 y=128 | 个人多项目状态阅读器与行动入口 | REVISE | 集中查看项目状态、下一步和需要你处理的事项 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0025 | HOME_DESKTOP_MOCKUP.svg / text[24] / x=1334 y=102 | 全部项目   当前依赖   同步状态 | REVISE | 全部项目   当前依赖   资料状态 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0040 | HOME_DESKTOP_MOCKUP.svg / text[39] / x=532 y=398 | 教学交付 | REVISE | 教学准备 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0042 | HOME_DESKTOP_MOCKUP.svg / text[41] / x=518 y=451 | 修正验证工具并准备 12 月展示 | REVISE | 修正检查工具并准备 12 月展示 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0044 | HOME_DESKTOP_MOCKUP.svg / text[43] / x=774 y=398 | 底层稳定性 | REVISE | 兼容与稳定 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0046 | HOME_DESKTOP_MOCKUP.svg / text[45] / x=760 y=451 | 先稳定插件底层和 ChatGPT 适配 | REVISE | 稳定插件底层，确保 ChatGPT 中可用 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0120 | ALL_PROJECTS_MOCKUP.svg / text[26] / x=472 y=194 | 活跃 · 等待 · 暂停 · 稳定 | REVISE | 进行中 · 等待 · 暂停 · 稳定 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0152 | ALL_PROJECTS_MOCKUP.svg / text[58] / x=720 y=374 | 修正三组课程验证工具，并准备期末项目展示 | REVISE | 修正三组课程自动检查工具，并准备期末项目展示 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0160 | ALL_PROJECTS_MOCKUP.svg / text[66] / x=720 y=416 | 稳定插件底层与 ChatGPT 兼容方式 | REVISE | 稳定插件底层，确保 ChatGPT 中可用 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0176 | ALL_PROJECTS_MOCKUP.svg / text[82] / x=720 y=500 | 先完成两套可运行的动态主题，再由用户选择一个继续 | REVISE | 先完成两套可运行的动态主题，再比较后确定一套继续完善 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0192 | ALL_PROJECTS_MOCKUP.svg / text[98] / x=720 y=584 | 在正式维护看板中处理已经准备好的改进项 | REVISE | 在维护看板中处理已经准备好的改进项 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0208 | ALL_PROJECTS_MOCKUP.svg / text[114] / x=720 y=668 | 只在有人可现场配合时完成剩余真实验证 | REVISE | 只在有人能到现场配合时完成剩余连接检查 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0224 | ALL_PROJECTS_MOCKUP.svg / text[130] / x=720 y=752 | 迁移完成后保持安静，只有异常时提醒 | REVISE | 迁移完成后无需日常处理，只有异常时提醒 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0232 | ALL_PROJECTS_MOCKUP.svg / text[138] / x=720 y=794 | 先确定复杂系统机制，再验证实现是否足够 | REVISE | 先确定复杂系统机制，再检查方案能否直接指导实现 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0304 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 142 行 / occurrence 1 | 三组课程验证工具修正与期末项目准备 | REVISE | 三组课程自动检查工具修正与期末项目准备 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0305 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 145 行 / occurrence 1 | 先修正三组课程验证工具，再准备 12 月 2 日的第一场期末项目展示 | REVISE | 先修正三组课程自动检查工具，再准备 12 月 2 日的第一场期末项目展示 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0308 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 191 行 / occurrence 1 | 先完成两套可运行的 Windows 动态主题，再由用户选择一个继续 | REVISE | 先完成两套可运行的 Windows 动态主题，再比较后确定一套继续完善 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0309 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 220 行 / occurrence 1 | 插件底层与 ChatGPT 兼容方式 | REVISE | 插件底层与 ChatGPT 兼容性 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0310 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 223 行 / occurrence 1 | 先把插件底层和 ChatGPT 兼容方式做稳定，之后优先恢复长对话优化，再做高亮和 PDF | REVISE | 先稳定插件底层，确保能在 ChatGPT 中正常使用；之后优先恢复长对话优化，再做高亮和 PDF | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0321 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 306 行 / occurrence 1 | 在正式维护看板中处理已经准备好的改进项 | REVISE | 在维护看板中处理已经准备好的改进项 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0322 | DATA_MODEL.md / UI 种子 / 第 391 行 / occurrence 1 | Longleaf 与 Workstation 远程访问正常；仍有少量现场验证待完成 | REVISE | Longleaf 与 Workstation 远程访问正常；仍有少量现场连接检查待完成 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0323 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 336 行 / occurrence 1 | Longleaf 与 Workstation 远程访问正常；仍有少量现场验证待完成 | REVISE | Longleaf 与 Workstation 远程访问正常；仍有少量现场连接检查待完成 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0324 | REAL_PROJECT_WALKTHROUGH.md / UI 种子 / 第 338 行 / occurrence 1 | 只在有人可现场配合时完成剩余真实验证 | REVISE | 只在有人能到现场配合时完成剩余连接检查 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0335 | INFORMATION_ARCHITECTURE.md / UI 种子 / 第 91 行 / occurrence 1 | 个人多项目状态阅读器与行动入口 | REVISE | 集中查看项目状态、下一步和需要你处理的事项 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |
| B-0340 | OBSIDIAN_IMPLEMENTATION_SPEC.md / UI 种子 / 第 203 行 / occurrence 1 | 个人多项目状态阅读器与行动入口 | REVISE | 集中查看项目状态、下一步和需要你处理的事项 | 上一轮最终版本仍带内部实现、第三人称或界面不一致表达；改为直接说明现实状态与下一步。 |


## 第三轮独立终审：前两轮 PASS 后仍发现的全部 14 条

状态：**OPEN / 尚未应用到 Project Atlas**。这些条目不是新的设计要求，而是用于证明“交付前语言验收仍未真正完成”的回归证据。

| ID | 界面 / 位置 | 当前文案 | 处理 | 建议最终文案 | 原因 |
|---|---|---|---|---|---|
| R3-A-001 | A 首页 / 深色首页“需要我”说明（对应 A-1041、A-1128） | 只显示已经准备好、现在必须由本人完成的事项。 | REVISE | 这里只显示已经准备好、现在需要你处理的事项。 | 仍使用“本人/必须”政策口吻；这是交付前终审仍发现的漏项。 |
| R3-A-002 | A “需要我”页面标题说明（preview.html 动态渲染，上一轮逐项表未单列） | 现在就能处理 / 且必须由本人完成 | REVISE | 现在需要你处理 | 动态生成文字未被逐项表完整覆盖，同时仍是内部政策口吻。 |
| R3-A-003 | A-0889 近期节点 / 已过去的课程节点 | 11 月 1 日 23:59 · HW1 学生提交截止。提交与收齐状态未确认，不记作 TA 本人逾期。 | REVISE | 11 月 1 日 23:59 · HW1 学生提交截止。提交和收齐情况还没确认，不会算作你的逾期事项。 | “TA 本人逾期”不像个人工作台语言。 |
| R3-A-004 | A-2644 资料与来源 / 关注顺序 | 首页四项是当前初始设置，可由本人调整，不会改变原项目的真实优先级。 | REVISE | 首页四项只是当前初始设置，你可以随时调整，不会改变原项目的实际优先级。 | “可由本人调整”仍是制度/审计口吻。 |
| R3-A-005 | A-1295 Asteria / 需要我 | 是否需要你处理还没有确认。 | REVISE | 暂时无法确认是否需要你处理。 | 语义方向正确，但中文机械。 |
| R3-A-006 | A-1425 Bridge Kit / 需要我 | 是否需要你处理还没有确认。 | REVISE | 暂时无法确认是否需要你处理。 | 同一未知状态应统一自然表达。 |
| R3-A-007 | A-1487 CardiacNexus / 需要我 | 是否需要你处理还没有确认。 | REVISE | 暂时无法确认是否需要你处理。 | 同一未知状态应统一自然表达。 |
| R3-A-008 | A-1699 CMRxRecon25 / 需要我 | 是否需要你处理还没有确认。 | REVISE | 暂时无法确认是否需要你处理。 | 同一未知状态应统一自然表达。 |
| R3-A-009 | A-1908 Echo Select / 需要我 | 是否需要你处理还没有确认。 | REVISE | 暂时无法确认是否需要你处理。 | 同一未知状态应统一自然表达。 |
| R3-A-010 | A-2256 SeminarArc / 需要我 | 是否需要你处理还没有确认。 | REVISE | 暂时无法确认是否需要你处理。 | 同一未知状态应统一自然表达。 |
| R3-A-011 | A-2318 Shione / 需要我 | 是否需要你处理还没有确认。 | REVISE | 暂时无法确认是否需要你处理。 | 同一未知状态应统一自然表达。 |
| R3-A-012 | A-2380 STAT5050 / 需要我 | 是否需要你处理还没有确认。 | REVISE | 暂时无法确认是否需要你处理。 | 同一未知状态应统一自然表达。 |
| R3-A-013 | A-2523 Zotero 文献镜像 / 需要我 | 是否需要你处理还没有确认。 | REVISE | 暂时无法确认是否需要你处理。 | 同一未知状态应统一自然表达。 |
| R3-A-014 | A 该项目 attention_reason（条件式可见文案，上一轮逐项表未单列） | 方法选择需要本人判断；局部认可不能代表整体可靠。 | REVISE | 方法选择需要你判断；目前确认可靠的部分不能代表整体可靠。 | 条件式文案仍含“本人/独立认可”等内部评审口吻，且说明逐项清单对动态状态覆盖不足。 |

## 这份证据必须怎样使用

1. Frontend Design 回归不能只检查布局。至少要从本文件抽取“本来就不该显示”的 REJECT、删除后布局重排、动态条件文案漏审、重复出现语义单元等案例。
2. Product UI Copy / Clear Writing 回归不能只做禁词替换。至少要覆盖“本人/用户/你”的人称选择、none / unknown / not-ready / ready 四类状态、内部流程名词转现实动作、整屏连续阅读。
3. Artifact Content Design 必须把 REJECT 作为一等结果，并在最终文案生成之前完成内容准入。
4. 正常生产中，类似本文件第二轮、第三轮这种大批返工必须发生在**第一次向用户交付之前**。如果用户首次看到成品后仍能成批发现同类问题，应判定联合交付失败。
