# 导入失败处理

按以下步骤检查导入结果，并根据条件执行对应操作：

1. 先运行 `python tools/inspect_import.py --job JOB-2048`，检查导入状态。
2. 如果 `schema_status=INVALID`，停止写入。修正列名后，返回第 1 步重新开始。
3. 如果 `schema_status=VALID` 但 `row_status=PARTIAL`，保留 `imports/JOB-2048/rejected.csv`，只重试失败行。
4. 如果 `schema_status=VALID` 且 `row_status=COMPLETE`，运行 `python tools/finalize_import.py --job JOB-2048`。
5. 检查终态：只有终态为 `READY` 时才算完成；否则仍未完成。
