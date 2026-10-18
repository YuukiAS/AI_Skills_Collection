# Clear Writing Web Gate Task Bank v0.2

Date: 2026-10-18  
Status: FROZEN DEVELOPMENT / WEB-GATE INPUTS  
Task: `clear-writing--every-response-invocation-policy`

All inputs below are public-safe. They are development/Web-Gate evidence and are
permanently ineligible for fresh G7.

## Global run rule

- One model answer per task/turn unless the frozen infrastructure-only retry rule applies.
- Do not rewrite prompts after seeing outputs.
- Preserve the exact task order within each gate.
- W0/W1/W2/W3 outputs are all known after first execution and may never become G7 fresh evidence.

# W0-A — natural/mixed invocation safety

For W0-A, explicitly select Clear Writing at plugin level, or use the strongest
legal equivalent that the current Web surface exposes. Record exactly what was
selected; do not infer a specific Skill load from plugin-level selection.

## W0-A01 — ordinary technical status

Prompt:

```text
下面是当前状态：

- API 健康检查返回 200。
- 最近一次后台同步任务失败，错误是 timeout。
- 今早 03:00 的备份成功。
- 还没有做过从备份恢复到新环境的演练。

请直接告诉我：现在能不能宣布“可以上线”，以及我现在是否需要立刻做什么。不要把日志重新抄一遍。
```

Expected contract: lead with the decision; preserve uncertainty; do not claim
restore readiness.

## W0-A02 — complex scientific explanation

Prompt:

```text
有一个两层病例数据模型：患者属于不同中心。我们先用中心内历史数据估计每个中心的基线风险，再根据患者的新测量更新个体风险。请详细解释这两层信息为什么不能直接混成一个平均数、各自解决什么问题、什么时候中心信息会帮助、什么时候会误导。必要时可以用公式，但先让我知道每个量在现实里代表什么。不要为了简短删掉限制条件。
```

Expected contract: detailed but coherent explanation; reader model before formal
notation; limitations retained.

## W0-A03 — multi-index object and missing definition

Prompt:

```text
已知 (y_{c,p,t}) 是中心 c 中患者 p 在时间 t 的观测值，(widehat b_{c,t}) 是中心 c 在时间 t 的估计基线，(r_{c,p,t}=y_{c,p,t}-widehat b_{c,t})。

请解释这些量各自处于什么层级、三个下标分别是谁、为什么要先得到 r，以及 r 后面通常能拿来做什么。

另外，文档最后突然出现 (u_{a,b})，没有任何定义。不要猜 a、b 是谁；请明确告诉我现在最多能知道什么、缺什么定义。
```

Expected contract: explicit index roles and downstream use; no invented meaning
for `u_{a,b}`.

## W0-A04 — necessary long comparison

Prompt:

```text
我在有中心聚类的数据里要做不确定性评估。请详细比较三种思路：普通非参数 bootstrap、按中心重采样的 cluster bootstrap、以及 cluster-robust 标准误。我要知道它们各自隐含什么抽样单位、在中心数很少时哪里会出问题、计算成本和解释上的差别，以及我该根据什么条件选择。不要只给结论表，解释清楚原因。
```

Expected contract: long answer remains justified; causal comparison and caveats
retained.

## W0-A05 — one-turn English override

Prompt:

```text
For this reply only, answer in English. Explain why a model can have good average accuracy but still fail badly on one hospital, and give one concrete example. Do not change any long-term language preference.
```

Expected contract: English for this reply only; no claim about later recovery
from this single task.

## W0-A06 — complete executable prompt

Prompt:

```text
给我一段完整可直接发给 Codex 的执行提示词，要求它只做以下事情：

- 仓库：example/repo
- 分支：reviewed/example--repair
- 只允许修改 src/a.py、tests/test_a.py
- 先运行现有测试并保存失败证据
- 修复后运行 focused tests 和 full tests
- 禁止改 README、版本号、CI workflow
- 如果发现必须改第三个 production 文件，停止并回报，不要自行扩范围

不要把它压缩成摘要。我需要完整可执行提示词。
```

Expected contract: complete prompt/contract must not be shortened for style.

## W0-A07 — genuinely branched procedure

Prompt:

```text
把下面的恢复流程整理得更容易执行，但必须保留真实分支和回跳关系：

1. 先检查数据库只读副本是否可查询。
2. 如果不可查询，停止，不做后续迁移。
3. 如果可查询，运行 schema validation。
4. validation 失败时，只修 schema 映射，然后回到第 3 步重新验证。
5. validation 通过后才运行 dry-run import。
6. dry-run 有数据差异时，保存 diff 并停止。
7. dry-run 无差异时才标记 READY。

不要把这个流程改成一段没有分支的 prose。
```

Expected contract: structure remains because branching is semantically useful.

## W0-A08 — mixed explanation plus exact payload

Prompt:

```text
先用两三句话解释为什么下面这个状态不能算“发布完成”。然后原样给出下面的 JSON，不要改键名、顺序、大小写或值：

{"release_status":"WAITING_FOR_RESTORE_CHECK","build":"PASS","backup":"PASS","restore":"PENDING"}
```

Expected contract: explanation may improve; JSON substring must be exact.

## W0-A09 — exact identities inside normal explanation

Prompt:

```text
请用自然中文说明下面这件事，但所有机器字符串必须保持原样：

branch = reviewed/cache--repair
commit = 7f4a1c2
status = WAITING_FOR_CI
command = python -m unittest tests.test_cache
file = automation/reviewed_handoff/tasks/cache--repair/CURRENT.json

核心问题：我现在应该继续开发，还是等 CI？
```

Expected contract: natural prose plus exact identifiers.

# W0-B — explicit-plugin-selection exact-only stress

Operator rule: explicitly select Clear Writing at plugin level if the surface
supports it. These are activation-exemption tasks. Without direct Skill-load
evidence, the maximum passing claim is
`PLUGIN_SELECTION_DOES_NOT_CONTAMINATE_EXACT_OUTPUT`.

The assistant message itself must equal the target payload exactly.

## W0-B01 — JSON

Prompt:

```text
Return exactly the following JSON and nothing else:
{"status":"PENDING","retry":false,"count":2}
```

Target assistant message:

```text
{"status":"PENDING","retry":false,"count":2}
```

## W0-B02 — YAML

Prompt:

```text
Return exactly the following YAML and nothing else:
state: WAITING
attempts: 1
enabled: false
```

Target assistant message:

```text
state: WAITING
attempts: 1
enabled: false
```

## W0-B03 — code

Prompt:

```text
Return exactly the following Python source and nothing else:
def add_one(x):
    return x + 1
```

Target assistant message:

```text
def add_one(x):
    return x + 1
```

## W0-B04 — raw log

Prompt:

```text
Return exactly these two log lines and nothing else:
2026-10-18T12:00:00Z worker=sync status=START
2026-10-18T12:00:03Z worker=sync status=TIMEOUT
```

Target assistant message:

```text
2026-10-18T12:00:00Z worker=sync status=START
2026-10-18T12:00:03Z worker=sync status=TIMEOUT
```

## W0-B05 — command

Prompt:

```text
Return exactly this command and nothing else:
python -m unittest tests.test_cache --failfast
```

Target assistant message:

```text
python -m unittest tests.test_cache --failfast
```

# W1 — Project-policy multi-turn behavior sequences

No manual `@Clear Writing` on individual turns. Use a disposable Project with
the frozen bridge bytes.

## W1-S01 — ordinary -> exact exemption -> ordinary recovery

Turn 1:

```text
一个任务的代码测试通过了，但真实数据回放还没跑。请告诉我现在能不能说“完成了”。
```

Turn 2:

```text
Return exactly this JSON and nothing else:
{"code_tests":"PASS","real_replay":"PENDING"}
```

Turn 3:

```text
那对我下一步意味着什么？用正常中文回答，不要重复 JSON。
```

## W1-S02 — Chinese -> temporary English -> Chinese recovery

Turn 1:

```text
用中文解释“校准误差”和“排序误差”为什么不是一回事，给一个简短例子。
```

Turn 2:

```text
For this turn only, answer in English. Which of those two errors can exist even when ranking is perfect?
```

Turn 3:

```text
继续解释：如果我要给医生看风险概率，为什么只看排序还不够？
```

## W1-S03 — short -> long -> complete prompt -> ordinary recovery

Turn 1:

```text
一句话告诉我：一次 smoke test 通过能不能证明整个产品稳定？
```

Turn 2:

```text
详细解释为什么，至少讨论测试覆盖、真实入口、环境差异和回归风险。需要长就长，不要机械压短。
```

Turn 3:

```text
现在给我一段完整可执行 Codex prompt：要求它只检查 tests/test_smoke.py 和 src/smoke.py，运行 focused + full tests，发现范围外问题就停止。不要省略条件。
```

Turn 4:

```text
回到普通回答：如果 full tests 也通过了，我还缺哪一类证据才能说真实用户入口可靠？
```

## W1-S04 — sibling route -> ordinary response

Turn 1:

```text
把下面这段正式中文报告文字润色成自然、完整的书面表达，事实不能变：

“本周完成了数据清理。当前结果仍属于初步结果。由于外部验证尚未完成，因此不应将其表述为最终结论。”
```

Turn 2:

```text
现在不要继续改报告。直接告诉我：为什么“初步结果”不能写成“已经验证的结论”？
```

# W2 — strict matched paired task set

Run the same frozen tasks in Treatment and Control under the Plan's strict
matching rules. Use fresh isolated conversation context for each task unless the
task itself is explicitly multi-turn.

Pair execution order is frozen to reduce time-order bias while preserving the
same task-order policy:

- P01: Control then Treatment
- P02: Treatment then Control
- P03: Control then Treatment
- P04: Treatment then Control
- P05: Control then Treatment
- P06: Treatment then Control
- P07: Control then Treatment
- P08: Treatment then Control

## W2-P01 — status decision

```text
现在的证据是：单元测试全部通过；staging 页面能打开；真实用户登录流程还没跑；回滚步骤写在文档里但没有演练。请告诉我现在最准确的完成状态，以及我下一步最该验证什么。
```

## W2-P02 — scientific reader model

```text
已知 (z_{h,i}) 是医院 h 的患者 i 的模型分数，(widehatmu_h) 是医院 h 的估计平均分，(d_{h,i}=z_{h,i}-widehatmu_h)。请解释为什么要构造 d、每个下标是谁、d 的正负意味着什么，以及它后面可以怎样用于比较患者。不要假设这里已经给了因果解释。
```

## W2-P03 — necessary long comparison

```text
详细比较交叉验证、外部验证和时间切分验证。我要知道三者分别在防什么错误、各自最容易给出什么假安全感、医学模型里什么时候必须优先外部验证。不要只给表格，也不要为了简短省掉限制。
```

## W2-P04 — source consensus vs recommendation

```text
三份内部评审都同意：当前模型在总体 AUC 上可接受；其中两份指出少数中心表现明显差；只有一份建议立刻扩大样本量。请总结这些材料共同支持什么、哪里并不一致，然后再单独告诉我你会建议下一步做什么。不要把你的建议写成三份评审共同结论。
```

## W2-P05 — formal Chinese sibling route

```text
把下面文字润色成正式但自然的中文报告段落，不能改变事实强度：

“当前实验只在内部验证集运行。平均性能有提升，但不同中心之间的差异仍然明显。外部数据尚未测试，因此这里不能声称方法已经具有跨中心泛化能力。”
```

## W2-P06 — complete executable prompt

```text
写一个完整可直接发给 Codex 的 prompt：

仓库 example/model；分支 reviewed/model--audit；只读检查 src/model.py、tests/test_model.py 和 results/；不允许修改文件；必须运行现有测试并核对最近一次结果；发现证据不一致时停止并列出冲突；不要给我摘要版。
```

## W2-P07 — mixed response + exact payload

```text
先解释下面状态为什么仍需要人工确认，然后把状态行原样保留：

review_status=AWAIT_HUMAN_DECISION
ci_status=PASS
release_status=NOT_RELEASED
```

## W2-P08 — multi-turn language recovery hard control

Turn 1:

```text
用中文解释为什么训练误差低不代表部署误差也低。
```

Turn 2:

```text
For this turn only, answer in English and give one distribution-shift example.
```

Turn 3:

```text
继续用默认语言回答：那上线前最值得补哪一类验证？
```

W2 preference scoring applies to P01-P07. P08 is a hard multi-turn control and
is not counted in the 4-of-7 preference threshold.

# W3 — no-bridge discoverability diagnostic

Run without the Project bridge. Do not use W3 for release-critical claims.

## W3-D01

```text
这个任务到底完成没有？测试过了，但真实恢复流程还没跑。直接告诉我结论和下一步。
```

## W3-D02

```text
详细解释一个有中心随机效应的模型，先说现实里每一层是什么，再给公式。
```

## W3-D03

```text
把这段正式中文报告润色一下：“当前结论只适用于内部验证数据，尚不能外推到其他中心。”
```

## W3-D04

```text
Return exactly this JSON and nothing else:
{"mode":"diagnostic","enabled":true}
```

## W3-D05

```text
给我一个完整的、带条件分支的故障恢复执行流程，不要把必要分支压成一段话。
```

# G7 exclusion record

The following are never fresh G7 evidence:

- KR-WEB-01..09;
- the four historical should-not-change controls;
- every W0 task above;
- every W1 turn above;
- every W2 task/turn above;
- every W3 diagnostic task above;
- any later debug prompt or recovery sample seen before G7 freeze.
