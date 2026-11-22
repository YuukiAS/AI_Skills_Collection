# 案例格式与脚本接口

v1 的 `case.yaml` 使用 **JSON 形式的 YAML**：它是合法 YAML，Python 标准库可直接读，不需要 PyYAML。多行原文保存在字符串中，以 `\n` 表示换行；写入剪贴板和 prompt 文件时恢复原来的多行文本。不支持任意 YAML 语法（如 `|` 块或锚点），不静默猜测解析。

```json
{
  "schema_version": 1,
  "id": "example",
  "name": "示例",
  "version": "test-v1",
  "model": "案例指定的模型",
  "plugins": [],
  "attachments": [],
  "turns": [
    {"n": 1, "prompt": "第一行\n第二行", "conversation": {"mode": "new"}},
    {"n": 2, "prompt": "追问", "conversation": {"mode": "continue"}},
    {"n": 3, "prompt": "另一问法", "conversation": {"mode": "branch", "after_turn": 1}}
  ],
  "criteria": [
    {"id": "C1", "text": "回答说明两个量的关系。", "kind": "requirement"}
  ]
}
```

`version` 是适用的被测版本，不是执行器版本。`plugins` 列待启用插件的精确名称，`attachments` 列用户需上传的本地相对路径或素材名；每轮弹窗均显示整案清单，不自动上传。不得写个人绝对路径、邮箱或账号标识。明确无需填 `[]`，来源未知填 `null`；空模型、空版本、空题面或无判据都记缺口，整案不执行。

轮次从 1 连续编号。`new` 为新对话；`continue` 续刚才那轮；`branch` 从指定轮次回答后创建分支，`after_turn` 必须为已存在的较早轮次。首次不能 `continue`。可选 `checkpoint` 保存原有继续/停止条件，由 Codex读归档回答后执行；脚本不替代语义判断。分支要求用户保留原对话位置，不自动创建分支，也不把复制历史到新聊天算成分支。

`criteria` 每项是一条原文判据；`kind` 默认为 `requirement`，条件成立才通过。`failure_condition` 命中则失败，`inconclusive_condition` 命中则无法判定；不命中时通过。原文包含复合条件时保持原文，不拆写成新标准。若文本无法证明满足或未命中，记无法判定。缺少执行工具、对象或成品证据时不能仅凭回答自称完成判通过。

批次为 UTF-8 文本（建议 `.batch`），**每行只有一个案例路径**，相对于批次文件所在目录；空行忽略，不写模型或其他配置。批次文件名仅用字母、数字、`_`、`-`，同批案例 id 不可重复。

兼容旧格式：原有四个中文字段的 `case.yaml` 可只读导入，保留 `legacy` 原文，将期望行为与判定方式作为两条判据；缺少的元数据和轮序仍留空，不能当作就绪案例。首批转换副本放在 `tools/regression-runner/examples/`，不修改旧案例。

## 本机命令

在包含 `tools/` 的本地副本根目录运行；Windows 将 `python3` 换为 `py -3`。这些命令由 Codex 按 skill 调用，用户通常只需回应弹窗。

```sh
python3 tools/regression-runner/check_case.py path/to/case.yaml
python3 tools/regression-runner/runner.py inspect path/to/batch.batch
python3 tools/regression-runner/runner.py next path/to/batch.batch
python3 tools/regression-runner/runner.py capture path/to/batch.batch --answer 好了
python3 tools/regression-runner/runner.py judge path/to/batch.batch --case example --input assessment.json
python3 tools/regression-runner/runner.py results path/to/batch.batch
```

检查草稿可加 `--allow-gaps`：格式错误仍返回非零；实际执行始终跳过有缺口案例。`--runs-dir` 可指定运行根目录；后续必须保持一致。`next --copy-pending` 仅用于明确需要再次复制待完成提示词时。`simulate --mock-clipboard <文本文件>` 在集群上用标准输入模拟弹窗；真实运行禁止该参数。

脚本首次处理批次时冻结案例内容与来源 hash，之后输入有变化就拒绝混用旧输出。每个已完成轮次跳过；尚无 reply 文件的轮次保留为待完成。已有判定不覆盖。跳过余下本案例会留下 `skipped.json`，结果仍为跳过，不是通过。

## 判定文件

Codex 读完整归档对话和判据后生成 `assessment.json`，而不是脚本用关键词判卷。按判据顺序逐条填写：

```json
[
  {"criterion": "C1", "status": "通过", "reason": "回答直接说明该关系。",
   "evidence": [{"turn": 1, "quote": "此处必须是已保存回答中的原文。"}]}
]
```

`status` 只能为 `通过`、`失败`、`无法判定`。通过/失败必须提供原句和轮次；无法判定也要写明缺失证据，有相关原句时同样引用。脚本核对引句确在指定 reply 文件中，生成 `judgement.md` 和 JSON 副本，记录判定输入 hash；结果表链接到逐条判定和各轮回答。引句定位核对只验证引用存在，不替代 Codex 的语义判定，更不代表独立审阅。

本机实测前仍不能声称 Mac/Windows 剪贴板或 Codex 弹窗已经验证；本轮只验证集群上的模拟路径。隐私扫描能识别常见邮箱、个人目录和账号链接，不能自动识别所有任意用户名；案例维护者和 Codex 仍需通读检查。发现原文有个人信息即停，不能自动改写、落盘或外发。
