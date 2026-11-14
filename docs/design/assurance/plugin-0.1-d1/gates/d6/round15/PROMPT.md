# D6 用户代理追问：第 15 轮（只检查冻结说明）

开一个全新的 GPT 对话（Thinking，推理强度调到最高），把下面整段贴进去。

---

你担任“用户代理追问”这一关的检查者。这是一个全新的对话。第 13 轮已对同一份设计做完逐组件追问，**设计本身没有阻塞缺口**；问题只在冻结说明，设计负责人已改写说明。按规则，说明改动后只需重做对说明的四项检查。**你不负责补答案，也不提出新需求。**

## 仓库与读取范围

- 仓库：`YuukiAS/AI_Skills_Collection`（公开）。
- 只读分支：`gates/assurance-0.1-d1`，固定提交 `12ae63d48eb2930bcb64cc9ad2763f99133d40b9`。
- 只读这三个文件：
  1. `docs/design/assurance/ASSURANCE_PROCESS_V0_1_20261110.md`：用户认可的流程。
  2. `docs/design/assurance/plugin-0.1-d1/blueprint.json`：受审设计（与第 10 轮相同）。
  3. `docs/design/assurance/plugin-0.1-d1/FREEZE_EXPLANATION.md`：改写后的冻结说明，用户批准前只读这一份。
- 不要读同目录的其他文件和 `gates/` 下的其他内容。

## 要做的

对照 `blueprint.json` 检查冻结说明四项（按设计 `freeze` 节点中冻结说明的规则）：
1. **漏写：** 只看设计规定的七类固定清单：用户做过的决定和设计者定的默认做法及被放弃方案；哪些情况交用户决定或确认；增加用户工作量、费用或权限的事；各角色何时启用、在哪里运行、谁派发、各负什么责任；验收器数量与分类及回归用例集；单项超过 100 MB 的下载或安装；不做的事和不保证的事。**清单之外的细节没写，不算漏写**。
2. **矛盾：** 说明有没有写设计里没有的承诺，或把设计写得更强或更弱。
3. **验收器与回归用例：** 验收器总数、各类个数与设计一致；回归用例的个数、内容、按检查条的分组、判定者和旧表现依据与设计一致。
4. **大件下载：** 是否都交代了，是否与设计相符。

只把会让用户误解或批准错对象的问题标为“阻塞”，其余标“非阻塞”。不要为了显得严格而凑问题；**这一轮请一次把所有问题都找出来**，不要留到下一轮。

## 写回

在同一分支写：
- `docs/design/assurance/plugin-0.1-d1/gates/d6/round15/questions.json`：数组，每项 `id, nodeId`（写 `FREEZE_EXPLANATION`）`, question, answerLocation, gap, impact, blocking, owner`。
- `docs/design/assurance/plugin-0.1-d1/gates/d6/round15/RESULT.md`：开头一行写你检查的说明的 `explanation_sha256`（该提交中 `FREEZE_EXPLANATION.md` 原始字节的 SHA-256）；然后用自然中文写结论：阻塞几条、分别是什么；非阻塞建议。

先在该目录写 `WRITE_PROBE.md`（内容 `D6 write probe passed.`），回读成功后再开始，结束前删除。只写这三个路径，不切分支。没有写入权限就把两份内容直接回复在对话里。

## 回复

最后用自然中文告诉我：说明还有哪些会让用户误解的地方，以及关上它们需要什么。
