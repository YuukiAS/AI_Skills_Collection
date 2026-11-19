# Research Authoring 机械检查接口

`check_research_artifact.py` 消费已填写的 handoff 和实际文件，只检查可确定的文件、对应关系、允许差异、精确项、格式、回读和执行证据结构。科研含义、读者适用性、语义等价、版式阅读质量和用户认可由 GPT 或用户在相应环节判断。

## 调用

检查已有成品：

```bash
python skills/writing/research/shared/scripts/check_research_artifact.py \
  path/to/handoff.json \
  --require files \
  --require correspondence \
  --require format \
  --output path/to/mechanical-results.json
```

需要先制作正式 PDF 时：

```bash
python skills/writing/research/shared/scripts/check_research_artifact.py \
  path/to/handoff.json \
  --render path/to/source.md path/to/output.pdf \
  --preview-dir path/to/all-pages \
  --output path/to/mechanical-results.json
```

正式 PDF 路线会请求全部页面预览。幻灯片继续运行通用 deck 验收器及其硬规则，本脚本不替代 deck 验收。

## 状态含义

- `PASS`：该条机械检查在给定输入上满足。
- `FAIL`：观察到确定的机械错误，或必需文件、清单、精确项和允许差异不满足。
- `未观察`：当前输入或工具没有提供足够证据。该状态保留缺口，不能写成通过。

命令退出码由实际 `FAIL` 和通过 `--require` 声明的未观察项目决定。未列为必需的未观察项仍进入结果，供 GPT 继续处理。

## 主要检查

- `files`：handoff、来源、目标、组件和回读文件可读，哈希与已声明值一致。
- `correspondence`：正文与文本目标、声明的对应文件或来源身份一致。二进制内容的语义对应保持未观察。
- `edit_scope`：存在接受稿及唯一 `allowed_patches` 时，结果与这些替换完全一致。
- `exact_items`：指定文字出现在指定文件或行；其含义与归属仍由 GPT 判断。
- `format`：Markdown 编码、围栏、资源链接；PDF 的可打开性、文本层、字体线索、表格线索和全页预览；ZIP 的组件清单和字节内容。
- `readback`：提供的回读文件与本地产物一致；实际发布页面另行观察。
- `evidence`：执行证据包含骨架字段且已经填写。规则是否真正体现在成品中保持 GPT 判断。

## 结果交接

程序输出 `mechanical_results`、`observed_surfaces`、`unobserved_surfaces`、`findings`、`reader_review` 和 `exit_code`。`reader_review` 固定保持 `未观察`，直到 GPT 读取来源与完整成品。PDF 的密度、留白和语义分组依据当前文档家族由 GPT 查看；文档类 PDF 不使用无来源的统一阈值。

脚本中的错误码和分支属于机械接口。面向用户的说明应根据结果解释实际文件、影响和下一动作，保留原始机器输出供定位。
