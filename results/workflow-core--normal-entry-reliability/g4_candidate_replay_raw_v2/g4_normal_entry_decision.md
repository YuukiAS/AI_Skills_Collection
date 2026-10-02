# 中文数学 PDF 路线决策

决策：保留 PDF 交付身份，选择普通 `workspace-write` 下的 Pandoc + XeLaTeX + 已发现的本地中文资源作为后续渲染候选路线。本轮仅完成能力发现与路线判断，不执行完整渲染，不声明成品 PDF 已通过验收。

## 依据与职责

- 输入：`inputs/01-g4_capability_discovery_input_v2.md`。要求中文正文和一个行内公式；HTML、PNG 截图不等价于交付 PDF。
- 流程：已使用当前安装的 Verified Workflow（`workflow-core/0.5/skills/workflow/SKILL.md`），按普通入口优先、专业路由、证据强度与交付身份不变的规则判断。
- PDF 指引：已读取 `/overflow/htzhu/mingcheng_new/AI_Skills_Collection/skills/tools/documents-media/pdf/SKILL.md`。
- 中文数学专项：已读取 `/users/a/e/aereinh/.codex/skills/tools-documents-media-render-chinese-math-pdf/SKILL.md` 及其 `references/portable-rendering.md`。中文字体、公式和成品检查由该专项规则约束；流程技能不替代专业判断。

## 实际探针证据

按输入原样运行，退出码为 0：

```bash
python3 /overflow/htzhu/mingcheng_new/AI_Skills_Collection/results/workflow-core--normal-entry-reliability/g4_probe_project/tools/pdf_capability_probe.py outputs/g4_probe
```

原始记录：[probe.json](g4_probe/probe.json)。本次 `default_path.xelatex` 为 `/usr/bin/xelatex`，`typst` 为 `null`。因此题设的首次 PATH 未找到现象没有在本次探针中重现，不能继续据此断言 TeX 不可用。缺失对照 `definitely_missing_renderer` 为 `null`，仅证明该名称未在当前 PATH 解析到，不证明所有 PDF 路线都不存在。

`project_probe.minimal_pdf_writer.available` 为 `true`，生成了 [minimal_probe.pdf](g4_probe/minimal_probe.pdf)，SHA-256 为 `651c1d5beb8810f5442741b99bc878e2dc218f470838655cc38c1397f5925bae`。已检查探针源码：它写入固定的英文 PDF 字节并检查 `%PDF-` 文件头，没有排版中文或公式，也没有验证字体、PDF 结构或阅读器表现。该文件只作诊断证据，不可交付为所需成品。

另运行专项环境探针，退出码为 0，全量结果保存在 [g4_render_env.json](g4_render_env.json)：

```bash
python3 /users/a/e/aereinh/.codex/skills/tools-documents-media-render-chinese-math-pdf/scripts/probe_pdf_render_env.py --root . --pretty > outputs/g4_render_env.json
```

- 已找到 Pandoc 2.14.0.3、XeTeX（TeX Live 2020）、LuaLaTeX，以及 `pdfinfo`、`pdftotext`、`pdffonts`、`pdftoppm`。
- 系统搜索未找到 `xeCJK.sty`、`ctexart.cls`，但本地配置发现两个可用中文资源包。推荐资源目录为 `/users/a/e/aereinh/render_resources/chinese_math_pdf`，包含上述宏包、Noto 中文字体、模板和渲染包装脚本。这是本机探测事实，不是通用固定路径要求。
- 系统有 Droid 中文字体及 Liberation Serif / Nimbus Roman。不能把 Noto 字体名匹配到 DejaVu Sans 的结果误认为系统安装了 Noto；资源包中的 Noto 字体文件则有独立路径证据。
- 探针推荐 `pandoc_xelatex_named_fonts`。这证明依赖候选存在，尚未证明实际排版与成品质量。
- Chromium 虽被标记为候选，其版本探测输出含只读 home 目录错误：`mkdir: cannot create directory ‘/users/a/e/aereinh/.local/share/applications’: Read-only file system`。不能把候选标记当作可运行或等价质量证明。

## 后续执行与替代边界

后续获得渲染任务后，先按实际源文档选择入口：Markdown 使用 Pandoc + XeLaTeX；已有 `.tex` 使用直接 XeLaTeX。优先核对已发现的项目/资源包装脚本；使用本地 `texmf` 和具名中文字体，将输出、头文件及 `TEXMFVAR`、`TEXMFCONFIG`、`TEXMFCACHE` 放在 `outputs/` 下。当前没有必要安装工具、联网、修改共享环境或提权。能力发现属于 `AGENT_RESOLVABLE`，不需要用户再次确认。

HTML 可以作为最终打印为 PDF 的内部中间格式，PNG 可以作为视觉检查证据，但两者都不能替代交付 PDF。只有 TeX 路线确实失败、浏览器本地入口可用且中文与公式保真、字体和视觉质量满足要求时，才考虑 Chromium 打印 PDF。当前浏览器错误尚未解决，因此不选择它作为已验证替代路线。最小字节写入器和通用 ReportLab 示例同样没有证明本任务的中文数学质量。

任何自动恢复都必须保持原效果、专业质量、验收证据强度、安全隐私、交付身份、授权范围六项等价，且不扩大权限。若无法证明等价，应保留现有证据并返回具体依赖或决策问题；不能用截图、删中文、删公式或原始宽权限命令绕过失败。只有相关普通入口和专业资源均无法满足要求时，才能报告精确的能力缺失；本次证据不支持这种结论。

真正交付前仍须验证 PDF 页数、中文及公式上下文提取、字体嵌入和中文字体 `uni yes`、版面，以及首页和公式所在页的视觉表现。当前没有真实成品源文档或完整渲染证据，不将这些检查写成已通过。

本轮状态：`complete`（仅限路线发现与本决策文件）。未联网，未执行完整渲染；探针输出均保存在 `outputs/`。中文数学 PDF 成品尚未生成或验收。
