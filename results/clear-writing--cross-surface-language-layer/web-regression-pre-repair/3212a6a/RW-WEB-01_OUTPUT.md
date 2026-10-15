现在还不能交付到生产环境。构建和单元测试已通过，备份也已创建，但尚未执行恢复演练；在演练通过前，不得安排生产切换。这些是不同环节的进度，并不矛盾。

这意味着发布还需要验证备份能否恢复。目前没有发生任何生产写入，你不需要立即操作。

下一步由维护者运行恢复检查：
python tools/restore_check.py --snapshot snapshots/sample-service-2026-10-15.tar.zst

只有恢复演练通过后，才能安排生产切换。当前状态为 release_status=WAITING_FOR_RESTORE_CHECK；相关配置为 deploy/production.yaml。
