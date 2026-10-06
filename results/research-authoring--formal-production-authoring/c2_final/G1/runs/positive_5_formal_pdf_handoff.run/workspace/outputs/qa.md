# PDF 交付检查

状态：complete。

正式 PDF 为 `research_update.pdf`，共 1 页，A4。已逐页查看 `previews/research_update-1.png`：标题、中文、比较表及区间清晰，没有遮挡、截断或乱码。`extracted_text.txt` 保留正文、表格和全部关键数值。字体检查确认 Noto Serif SC 与 TeX Gyre Termes 的常规、粗体字形均嵌入并支持 Unicode；本文无数学公式，无需实际使用数学字体。

渲染器自动报告未识别出中文字体名称；人工核对 `pdffonts` 中的 NotoSerifSC-Regular/Bold 后确认该提示属于名称识别误报，预览与中文提取均正常。

首次编译因旧版 Pandoc 将 `lang: zh-CN` 转为空的 `\setmainlanguage[]{}` 而失败。删除这项可选语言元数据后，仍使用相同 canonical-markdown / XeLaTeX 正式配置成功生成；中文内容、字体和科研语义均未改变。未使用浏览器替代路线。

## 重现命令

```bash
python /users/a/e/aereinh/.agents/skills/tools-documents-media-render-chinese-math-pdf/scripts/render_scientific_pdf.py outputs/research_update.md outputs/research_update.pdf --root . --work-dir outputs/build --preview-dir outputs/previews --preview-pages all --receipt outputs/render_receipt.json
```

未设置额外环境变量；资源目录由主机已有配置解析，具体配置与工具调用见 `render_receipt.json`。格式为默认正式笔记：A4、25 mm 页边距、11 pt、1.15 倍行距、无目录和章节编号。

## 文件校验值

- `original_notes.md` SHA-256：`ebd8adc73b1b5a215038a5e263967d1dd55dbdb50210f036359ea8db4298824c`
- `research_update.md` SHA-256：`dd5b997f4d1a1a8cfedf2cba8bb566f4b3ccdfb987714e9b0b7bf835438ae96a`
- `research_update.pdf` SHA-256：`5cd733f68f8165452e9ee6788e2e068088309570a383b319997af4e24a36fb8d`
