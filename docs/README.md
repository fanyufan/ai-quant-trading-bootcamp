# 项目文档

本目录存放 AI 量化交易训练营的补充文档与参考资料。

## 文档列表

| 文档 | 说明 |
| --- | --- |
| [data-sources.md](./data-sources.md) | 量化数据源全景总结：主流数据源特性对比、按数据项选型建议、官方文档链接 |
| [issues/001-qmt-mysql-access-denied.md](./issues/001-qmt-mysql-access-denied.md) | 常见问题：行情数据采集脚本连接 MySQL 失败的排查与解决 |
| [issues/002-master-missing-test-pkl.md](./issues/002-master-missing-test-pkl.md) | 常见问题：MASTER 截面预测脚本缺少 csi300_dl_test.pkl 测试数据文件 |

## 常见问题

### 数据采集与数据库

- [Issue #001: 行情数据采集脚本连接 MySQL 失败](./issues/001-qmt-mysql-access-denied.md)

### 论文复现与策略进化

- [Issue #002: MASTER 截面预测脚本缺少 csi300_dl_test.pkl 测试数据文件](./issues/002-master-missing-test-pkl.md)

---

> 如果你遇到新的问题并找到了解决方案，欢迎提交到 `docs/issues/` 目录，按 `XXX-问题简述.md` 的格式命名。
