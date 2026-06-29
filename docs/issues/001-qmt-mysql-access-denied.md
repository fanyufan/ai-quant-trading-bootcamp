# Issue #001: 行情数据采集脚本连接 MySQL 失败

## 问题描述

运行 `week2/4-数据获取与清洗-20260225/CASE-数据采集/1-行情数据采集.py` 时，QMT 连接成功，但在查询数据库已有数据时报错。

## 环境信息

- **OS**: Windows
- **Python**: 3.11.9
- **QMT**: 光大证券金阳光 QMT 实盘
- **数据库**: MySQL (localhost:3306)
- **错误来源**: `pymysql` 连接认证失败

## 复现步骤

1. 启动 QMT 客户端
2. 进入目录：`week2/4-数据获取与清洗-20260225/CASE-数据采集/`
3. 运行：`python 1-行情数据采集.py`
4. 脚本输出 `xtdata 连接成功`
5. 在 `查询数据库已有数据...` 步骤报错

## 错误日志

```text
连接QMT数据服务...
***** xtdata连接成功 2026-06-29 18:31:58*****
服务信息: {'tag': 'sp3', 'version': '1.0'}
服务地址: 127.0.0.1:58610
数据路径: C:\光大证券金阳光QMT实盘\bin.x64/../userdata_mini/datadir
  连接成功

[测试模式] 只采集 600519.SH
查询数据库已有数据...
Traceback (most recent call last):
  ...
  File "db_config.py", line 36, in get_connection
    return pymysql.connect(**DB_CONFIG)
  ...
pymysql.err.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: NO)")
```

## 根因分析

`db_config.py` 默认从 `week2/4-数据获取与清洗-20260225/.env` 读取配置，但用户习惯将 `.env` 放在 `CASE-数据采集/` 脚本同级目录下。当 `.env` 位置不正确时，`WUCAI_SQL_PASSWORD` 读取为空字符串，导致 MySQL 认证失败。

## 解决方案

### 方案一：修改 `db_config.py` 的 `.env` 路径（已采用）

修改 `week2/4-数据获取与清洗-20260225/CASE-数据采集/db_config.py`：

```python
# 修改前
_env_path = Path(__file__).parent.parent / '.env'

# 修改后
_env_path = Path(__file__).parent / '.env'
```

然后将 `.env` 文件放在 `CASE-数据采集/` 目录下，并正确填写数据库密码：

```env
WUCAI_SQL_HOST=localhost
WUCAI_SQL_USERNAME=root
WUCAI_SQL_PASSWORD=your_password
WUCAI_SQL_PORT=3306
WUCAI_SQL_DB=wucai_trade
```

### 方案二：保持原路径，将 `.env` 放在上一级目录

如果不修改代码，则需要将 `.env` 放在：

```
week2/4-数据获取与清洗-20260225/.env
```

## 其他排查点

如果按上述方案配置后仍然报错，请依次检查：

1. **MySQL 服务是否已启动**
   ```bash
   mysql -u root -p
   ```

2. **数据库 `wucai_trade` 是否已创建**
   ```sql
   CREATE DATABASE IF NOT EXISTS wucai_trade CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

3. **数据表是否已初始化**
   ```sql
   USE wucai_trade;
   SOURCE wucai_trade_charles.sql;
   ```

4. **MySQL 8.0 认证方式问题**
   如果 root 用户使用默认的 `caching_sha2_password`，pymysql 可能无法认证，需要改为 `mysql_native_password`：
   ```sql
   ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
   FLUSH PRIVILEGES;
   ```

## 状态

✅ **已修复**（commit: [b0979aa](https://github.com/fanyufan/ai-quant-trading-bootcamp/commit/b0979aa））

---

> 相关文件：
> - `week2/4-数据获取与清洗-20260225/CASE-数据采集/db_config.py`
> - `week2/4-数据获取与清洗-20260225/CASE-数据采集/.env.example`
> - `week2/4-数据获取与清洗-20260225/CASE-数据采集/wucai_trade_charles.sql`
