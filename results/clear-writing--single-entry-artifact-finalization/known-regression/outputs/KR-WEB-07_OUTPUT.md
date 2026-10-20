当前评估中，`TFT` 的平均绝对误差低于季节性均值基线，说明它在这次评估中的预测误差更小。不过，目前尚未进行跨季节测试，因此还不能声称模型在全年都更好。

这次评估使用 `Temporal Fusion Transformer (TFT)` 预测公开的用电负荷序列：输入过去 24 小时的数据，预测下一小时的用电负荷。训练集和测试集按建筑划分，依据每条记录所属的建筑分组，避免同一栋建筑同时出现在两侧。

讨论中提到的“历史信息”，指模型从过去时间窗中保留的信息；“可追溯记录”，指从原始数据到指标的完整记录；“基线结果”，则是供比较的参照，这次使用的是季节性均值基线。

下一步运行 `python tools/evaluate.py --config configs/tft_public.yaml`，配置中的精确值为 `split_mode=building_holdout`，输出写入 `artifacts/tft_eval/metrics.json`。跨季节表现仍需后续测试确认。
