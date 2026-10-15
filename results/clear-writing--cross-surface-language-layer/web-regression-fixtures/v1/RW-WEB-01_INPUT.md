# SampleService 发布检查

结论所依据的事实如下：

- 构建与单元测试已经通过。
- 备份已经创建，但恢复演练尚未执行。
- 在恢复演练通过前，不得安排生产切换。
- 当前没有发生任何生产写入，用户也不需要立即操作。
- 维护者下一步应运行 `python tools/restore_check.py --snapshot snapshots/sample-service-2026-10-15.tar.zst`。

定位信息：

- `release_status=WAITING_FOR_RESTORE_CHECK`
- `deploy/production.yaml`
- `snapshots/sample-service-2026-10-15.tar.zst`

这些事实来自同一次检查。不要把“构建通过”“备份完成”和“尚不能切换生产”误写成互相矛盾的状态。
