目前还不能交付上线或安排生产切换。构建和单元测试已通过，备份也已创建，但恢复演练尚未执行；只有恢复演练通过，才能安排生产切换。这些是不同的发布条件，状态并不矛盾。

对你而言，当前仍在上线前的验证阶段，尚未发生任何生产写入，你不需要立即操作。下一步由维护者运行恢复检查：

python tools/restore_check.py --snapshot snapshots/sample-service-2026-10-15.tar.zst

当前状态为 release_status=WAITING_FOR_RESTORE_CHECK，相关部署配置是 deploy/production.yaml。以上判断依据所提供的维护状态，并不表示恢复检查已经执行。
