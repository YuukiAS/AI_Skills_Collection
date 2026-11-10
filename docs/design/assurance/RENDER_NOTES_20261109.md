# 合并流程图：生成与自查说明

流程图按用户提供的规格生成，结构、节点含义、角色颜色、形状和回流关系均沿用规格。草案正文原样复制，只在文件最前面加入 PNG 图片引用；两个插件 TODO 各增加一行草案链接。

## 文件

- [草案与图片入口](ASSURANCE_PROCESS_DRAFT_20261109.md)
- [PNG（4800×3000）](ASSURANCE_PROCESS_20261109.png)
- [SVG（2400×1500）](ASSURANCE_PROCESS_20261109.svg)
- [D2 图源](ASSURANCE_PROCESS_20261109.d2)
- [重建脚本](render_assurance_20261109.py)

原始草案和规格分别来自 `/users/a/e/aereinh/Asteria-Workspace/drafts/ASSURANCE_PROCESS_DRAFT_20261109.md` 与同目录的 `ASSURANCE_DIAGRAM_SPEC_20261109.md`，本轮没有修改这两个来源文件。

## 工具与字体

使用 D2 v0.9.0、内置 ELK 布局和 Noto Sans SC。最终 PNG 由 librsvg 2.50.7 从最终 SVG 导出，宽高均为 SVG 的 2 倍。

D2 可执行文件取自[官方 v0.9.0 release](https://github.com/d2lang/d2/releases/tag/v0.9.0)，下载包已按该 release 的 `SHA256SUMS` 核对。字体取自 Google Fonts 的 [Noto Sans SC](https://github.com/google/fonts/tree/main/ofl/notosanssc)，按 OFL 许可使用。下载的可变字体 SHA-256 为 `a3041811a78c361b1de50f953c805e0244951c21c5bd412f7232ef0d899af0da`；用 fontTools 分别生成 400 和 700 字重供渲染。

下载的工具、完整字体文件、许可证、原始试图、局部查看图及字体缓存都位于被 Git 忽略的 `.cache/assurance-diagram/`，不单独入库。SVG 保留 D2 导出时内嵌的已用字符字体子集，供打开 SVG 时显示中文。没有改动全局字体目录或其他项目。

## 怎样重建

在本工作树中运行：

```bash
python docs/design/assurance/render_assurance_20261109.py
```

脚本读取 `.cache/assurance-diagram/tools/d2-v0.9.0/bin/d2` 和 `fonts/NotoSansSC-Regular.ttf`、`fonts/NotoSansSC-Bold.ttf`。依赖 Python 的 `lxml`，并调用系统已有的 `rsvg-convert`；这些工具在本轮均已实际运行。缓存移除后，应先按上面的固定版本重新准备工具与字体。

图源用横向网格固定“设计—交接—交付”三个区域，区域内部由 ELK 纵向排布。D2 对[网格内跨单元连接使用直线](https://d2lang.com/tour/grid-diagrams/#connections-between-grid-cells)，直接导出会让交接线穿过节点。因此重建脚本还把跨区箭头和证据回流线放入空白边带，移动相应箭头标签，并补足外侧红色回流拐角的画布空间。没有改变任何连接的起点、终点或含义。最终 SVG 和 PNG 应通过该脚本生成，不能用 D2 的直接导出替代。

## 实际自查与修正

已打开最终 PNG 全图，并放大检查设计区、交付区、顶部回流、外侧拐角和底部图例。

- 首张试图把两个流程都排成横向，图过宽；改为横向外框、纵向内部流程。
- 交接斜线穿过冻结关卡；移到容器之间的空白交接带，改为折线。
- 红色与橙色回流重叠，并碰到容器标题；拆成上下两条独立通道，分别避开标题后进入设计负责人。
- 专业证据点线穿过诊断检查框；移到交付容器右侧空白边带，仍只把证据交回交付负责人。
- 最外侧红色回流拐角曾被画布裁切；扩大留白并重新导出，已查看完整拐角。
- 图例的短线难以看出虚线和点线区别；加长样线并拉开点线间距，保留全部颜色、形状和线型说明。

最终查看未见中文方块、文字截断或箭头穿字；红色粗虚线回流完整且醒目，图例完整。另实际核对了 PNG 尺寸、SVG 尺寸、图中文字的字体覆盖，以及六条调整后连接的完整坐标都在画布内。去除草案开头新增的图片引用后，与来源文件逐字节一致。

这些检查只针对本轮流程图和文件改动，没有运行或验收两个插件的生产能力。
