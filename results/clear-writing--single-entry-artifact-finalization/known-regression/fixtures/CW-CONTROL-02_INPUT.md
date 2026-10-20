# 导入失败处理

1. 先运行 `python tools/inspect_import.py --job JOB-2048`。
2. 如果 `schema_status=INVALID`，停止写入，修正列名后从第 1 步重新开始。
3. 如果 `schema_status=VALID` 但 `row_status=PARTIAL`，保留 `imports/JOB-2048/rejected.csv`，只重试失败行。
4. 如果 `schema_status=VALID` 且 `row_status=COMPLETE`，运行 `python tools/finalize_import.py --job JOB-2048`。
5. 只有终态为 `READY` 时才算完成。
