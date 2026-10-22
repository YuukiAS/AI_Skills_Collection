# 评估记录

团队使用正式模型 `Temporal Fusion Transformer (TFT)` 预测公开的用电负荷序列，并用过去 24 小时的数据预测下一小时。评估按建筑划分训练集和测试集，避免同一建筑同时出现在两侧。

讨论记录把以下普通概念写成了英文：

- `building structure`：不同记录属于哪一栋建筑；
- `feature memory`：模型从过去时间窗保留的历史信息；
- `audit trail`：从原始数据到指标的可追溯记录；
- `benchmark`：供比较的基线结果。

当前结果显示，`TFT` 的平均绝对误差低于季节性均值基线，但尚未进行跨季节测试，因此不能声称模型在全年都更好。下一步是运行 `python tools/evaluate.py --config configs/tft_public.yaml`，配置中的精确值为 `split_mode=building_holdout`，输出写入 `artifacts/tft_eval/metrics.json`。
