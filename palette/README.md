# Journal Palettes

顶刊常用论文图配色库。后续让 Cursor/Codex 画图时，可以直接指定：

```text
Use the palette from frontend/palette/palettes.json: lancet
```

## 文件结构

- `palettes.json`: 机器可读的主文件，推荐优先调用。

## Palette 结构

每个 palette 对应一组色号：

```json
{
  "id": "lancet",
  "name": "Lancet Oncology inspired",
  "type": "categorical",
  "colors": ["#00468B", "#ED0000", "#42B540"]
}
```

## 使用规则

- 分类变量优先用 `type: "categorical"` 的 palette。
- 连续变量、热图、表达量梯度再单独新增 `type: "sequential"` 或 `type: "diverging"`。
- 颜色数量不够时，优先减少分组或合并低频类别，不要随意插入随机颜色。
- 论文图默认避免大面积高饱和填充；高亮色用于重点组，对照组可用灰色或低透明度。
- 这些是 journal-inspired palettes，不等同于期刊官方品牌规范。

## 推荐命名

- `nature_npg`
- `science_aaas`
- `nejm`
- `lancet`
- `jama`
- `bmj`
- `jco`

