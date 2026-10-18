# Clear Writing 最终 Web 收尾测试协议 v0.1

日期：2026-10-19  
状态：FROZEN_FOR_CRITIC_REVIEW  
任务：`clear-writing--final-web-closure-minimal-gate`

本协议只冻结最终 4 个真实 ChatGPT Web 回答。Critic PASS 前不得执行。

## 0. 固定前提

- frozen production candidate：
  `fd7a1578a5042a46a55c5b638f6d550655b1096b`
- 真实 PRIVATE plugin：
  - name：`writing-style`
  - display name：`Clear Writing`
  - version：`0.4.0`
  - plugin_id：`plugins_6ad4fc9abae08191a9ecd81879b2c919`
  - current_release_id：`pluginrel_6ad4fc9c33888191b33350e50ac92b5d`
- 四回答总数固定，不增加第五个回答。
- 每个回答只取一次有效模型输出。
- 基础设施中断且完全没有 usable answer 时，最多允许一次技术 retry。
- 回答质量差、格式错误、行为不符都属于真实结果，不得重跑到成功。
- 不得在看到回答后修改输入、rubric 或 PASS threshold。

## 1. 测试 Project 的冻结薄策略

Project Turn 1–3 使用一个专门测试 Project。只加入以下调用策略，不复制 Clear Writing 内部写作规则：

```text
对每条面向用户的自然语言最终回答，以及自然语言与机器内容混合的最终回答，如果当前 Clear Writing 可用，则使用其最合适的现有写作能力；纯 JSON、YAML、代码、命令、原始日志、逐字引用或其他要求精确机器输出的请求不为此强制调用 Clear Writing，直接保持精确原样。不要模拟、重建或复制 Clear Writing 内部规则。
```

Project Turn 1–3 必须在同一 conversation 连续执行，不手工 `@Clear Writing`。

本协议只观察用户侧行为，不声称后台每轮具体加载了哪个 Skill。

# Test 1 — 显式真实 Clear Writing 入口

在新的普通 ChatGPT 对话中显式选择真实 PRIVATE `@Clear Writing`，发送：

```text
下面是一个任务的原始状态：

Build and unit tests are PASS.
The staging page is reachable.
The production restore drill has not been run.
The reviewer says the implementation looks correct, but release readiness is still unproven.

branch = reviewed/cache--repair
status = WAITING_FOR_RESTORE_CHECK
command = python -m unittest tests.test_cache

请直接告诉我这意味着什么、我现在需不需要做什么。

面向我的解释请用自然中文。普通英文技术/流程表达如果没有必须保留的机器身份，就不要直接堆英文；不要一句话一段，也不要把上面的状态逐条翻译成日志。

但 branch、status、command 后面的机器字符串必须保持原样。
```

### PASS

必须同时满足：

- 第一段直接说明：当前还不能把发布准备视为已证明；
- 给出用户是否需要动作及最直接下一步；
- 中文自然；
- 不把原始状态逐条翻译成日志；
- 不用一句话一段制造碎片；
- 不把普通英文流程词堆进中文；
- 不把“implementation 看起来正确”拔高成“可以发布”；
- 下列字符串完全原样：
  - `reviewed/cache--repair`
  - `WAITING_FOR_RESTORE_CHECK`
  - `python -m unittest tests.test_cache`

# Project Turn 1 — scientific-rewrite 兄弟任务族

不手工 `@Clear Writing`。发送：

```text
请把下面这段科研技术说明重写成自然、连贯、可以直接给合作者阅读的中文。允许重组段落和调整说明顺序，但不能改变事实、公式、变量含义、结论强度或“尚未验证”的状态；不要为了简短删掉必要解释。

原始说明：

研究对象按 cohort g 分组，每个受试者为 i，每次随访为 t。观测量记为 (y_{g,i,t})。我们先估计同一 cohort 在时间 t 的基线 (widehat{mu}_{g,t})，再定义偏差
(r_{g,i,t}=y_{g,i,t}-widehat{mu}_{g,t})。
为了比较不同时间点的偏差大小，又定义
(z_{g,i,t}=r_{g,i,t}/widehat{sigma}_{g,t})，其中 (widehat{sigma}_{g,t}) 是 cohort g 在时间 t 的估计尺度。

当前内部验证只说明：在现有内部数据中，使用 (z_{g,i,t}) 后，不同时间点的数值更容易放在同一尺度上比较。外部中心验证尚未完成，因此不能声称该标准化在新的中心仍然有效，也不能把它写成已经证明的跨中心泛化结论。

文档后面还出现 (q_{a,b})，但没有给出 q 的定义，也没有说明 a、b 分别代表什么。这里不能根据下标形式猜它的科学含义。

以下机器身份必须逐字保留：
experiment_id = CW-FWC-241
model_tag = longitudinal_norm_v3
status = EXTERNAL_VALIDATION_PENDING

请把它整理成读者能顺着理解的说明：先让人知道这些量分别是什么层级、为什么先得到 r 再得到 z、当前结果到底支持什么和不支持什么。对于 (q_{a,b})，只说明现在缺什么定义，不要自行补定义。
```

### PASS

必须同时满足：

- 明确这是 source-faithful rewrite，而不是另起炉灶回答研究问题；
- 可以重组结构，但不能改变：
  - (y_{g,i,t})
  - (widehat{mu}_{g,t})
  - (r_{g,i,t}=y_{g,i,t}-widehat{mu}_{g,t})
  - (z_{g,i,t}=r_{g,i,t}/widehat{sigma}_{g,t})
  - (widehat{sigma}_{g,t}) 的给定含义；
- 清楚解释 g / i / t 的层级；
- 清楚解释为什么先构造 r，再构造 z；
- 保留“只在内部数据中观察到”与“外部中心尚未验证”的边界；
- 不能把“更容易同尺度比较”扩大成性能改善、因果作用或跨中心泛化；
- 对 `q_{a,b}` 明确指出 q、a、b 定义不足，不猜；
- 不机械压短必要解释；
- 以下完全原样：
  - `CW-FWC-241`
  - `longitudinal_norm_v3`
  - `EXTERNAL_VALIDATION_PENDING`

# Project Turn 2 — pure exact JSON

紧接 Turn 1，发送：

```text
Return exactly the following JSON and nothing else:
{"status":"PENDING","retry":false,"count":2}
```

唯一允许的 assistant message：

```text
{"status":"PENDING","retry":false,"count":2}
```

### PASS

逐字符一致。

以下任一情况直接 FAIL：

- 多任何前言或结尾；
- Markdown code fence；
- 改字段顺序；
- 改大小写；
- 改值；
- 加空格、标点或解释；
- 省略任何字符。

# Project Turn 3 — 复杂科研普通解释 + exact 后恢复

紧接 Turn 2，不手工 `@Clear Writing`，发送：

```text
现在回到正常中文解释。

在一个多站点传感器研究里，s 表示站点，j 表示站点内的传感器，t 表示时间。已知：

(x_{s,j,t}) 是传感器 j 在时间 t 的观测值；
(widehat m_{s,t}) 是站点 s 在时间 t 的估计背景水平；
(d_{s,j,t}=x_{s,j,t}-widehat m_{s,t})；
(a_{s,j,t}=d_{s,j,t}/widehat v_{s,t})，其中 (widehat v_{s,t}) 只被描述为“站点 s 在时间 t 的一个估计尺度量”。

请详细解释这些对象各自处于什么层级，三个下标分别是谁，为什么分析里可能先得到 d 再得到 a，以及 a 后面可以怎样作为后续比较或异常筛查的输入。先让我建立对对象、层级和用途的直觉，再进入公式关系；必要的解释不要为了简短而删掉。

另外，附件最后出现 (h_{u,k})，但没有任何上下文说明 h 是什么，也没有定义 u、k。请明确告诉我目前最多能知道什么、还缺什么信息。不要根据字母或下标形状猜它的科学含义。
```

### PASS

必须同时满足：

- 自动恢复正常自然中文；
- 不延续上一轮 pure JSON 模式；
- 先建立对象、层级和用途，再进入形式关系；
- 明确 s / j / t；
- 正确说明 d 是相对站点-时间背景的偏差；
- 对 a 的解释只基于已知定义，不把 (widehat v_{s,t}) 猜成标准差、方差或其他未给定对象；
- “a 可作为后续比较或异常筛查输入”只能以可能用途/输入层面解释，不冒充已证明的科学效应；
- 对 (h_{u,k}) 明确说明 h、u、k 定义不足，不猜；
- 解释深度足够，不机械压短；
- 段落按完整推理单元组织，不是一句一段。

# 2. 总体判分

## Hard fail：任意一次即整组 FAIL

- 事实或 claim strength 漂移；
- exact machine string / JSON / code 被改；
- 未定义科学对象被猜成事实；
- 明确语言要求被违反；
- source-faithful rewrite 改动公式、变量含义或未验证状态；
- sibling route 错误并实质改变请求产物；
- exact-only 输出加入任何额外内容。

## Reader-quality repeat fail

以下同类问题若在不同回答中出现至少 2 次，则整组 FAIL：

- 不必要中英夹杂；
- 一句话一段；
- 内部流程词/状态字段主导正文；
- 真正结论埋在后面；
- 必要复杂解释被机械压短；
- 简单问题被膨胀成报告。

单个轻微措辞偏好不构成 release blocker。

# 3. 最终 claim boundary

四回答全部 PASS 只支持：

- 显式真实 Clear Writing 入口工作正常；
- 薄 Project policy + 已安装 Clear Writing 下连续用户行为达到预期；
- exact-only 输出不受污染；
- 至少一个非默认兄弟写作任务族在真实 Web 正常入口下行为正确；
- frozen candidate 的复杂科研解释关键修复在真实 Web 得到直接观察。

不得声称：

- `PLUGIN_LOADED_EVERY_TURN=PASS`
- 每轮后台必然加载 Clear Writing
- 插件相对于相同 Project setting 的独立因果增量已证明

历史 `W2=INCONCLUSIVE` 保留，不重跑。

# 4. 收尾条件

四回答全部 PASS 后：

`READY_FOR_RELEASE_CLOSURE=YES`

之后不得新增其他 Web release Gate，除非这 4 个回答真实暴露一个此前合同未覆盖的新产品失败。

release closure 只处理版本、README、changelog、release branch、source/generated/release identity、final CI 与 actual released plugin identity/parity。
