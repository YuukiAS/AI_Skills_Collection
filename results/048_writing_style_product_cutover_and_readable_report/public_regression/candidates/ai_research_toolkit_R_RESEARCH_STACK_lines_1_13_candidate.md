# R Research Stack

本文件记录 `AI_Research_Toolkit` 后续科研环境应当覆盖的 R 包。它面向统计建模、生物信息学、多组学、医学影像辅助分析和可复现研究，不是单个环境的安装脚本，也不建议把全部包安装进同一个 R library。

R 与 Bioconductor 的版本对应关系非常重要。正式项目必须记录 R 版本、Bioconductor release、包版本和系统依赖，不能只记录包名。

## 使用原则

1. 通用统计、组学分析和医学影像辅助分析应使用不同的 `renv` 项目。
2. Bioconductor 包必须通过匹配当前 R 版本的 `BiocManager` 安装。
3. 原始测序处理、比对、变异检测、DICOM 转换和大型影像配准仍应使用原生软件；R 包主要负责统计建模、数据整合和结果解释。
4. 对 Python 与 R 都存在的方法，例如 DESeq2/PyDESeq2、Scanpy/Seurat，应指定一个主实现，另一个只用于交叉验证或协作需要。
5. 关键分析必须保存 `sessionInfo()`、随机种子、输入数据版本和参数。
