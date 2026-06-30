# Issue #002: MASTER 截面预测脚本缺少 csi300_dl_test.pkl 测试数据文件

## 问题描述

运行 `week6/12-论文复现与策略进化-20260325/CASE-论文复现与策略进化/2-MASTER截面预测.py` 时，脚本在加载测试数据阶段报错，提示找不到 `csi300_dl_test.pkl` 文件。

## 环境信息

- **OS**: Windows
- **Python**: 3.11.9
- **课程**: Week 6 · 12-论文复现与策略进化（2026-03-25）
- **相关脚本**: `2-MASTER截面预测.py`
- **相关目录**: `week6/12-论文复现与策略进化-20260325/MASTER-master/data/opensource/`

## 复现步骤

1. 进入目录：
   ```bash
   cd "week6/12-论文复现与策略进化-20260325/CASE-论文复现与策略进化"
   ```

2. 运行脚本：
   ```bash
   python 2-MASTER截面预测.py
   ```

3. 脚本输出模型配置信息后，在 `[1] 加载测试数据` 步骤报错。

## 错误日志

```text
======================================================================
  MASTER截面预测 - CSI300
  beta=5, d_model=256, T_nhead=4, S_nhead=2
======================================================================

[1] 加载测试数据: C:\Fan\ai-quant-trading-bootcamp\week6\12-论文复现与策略进化-20260325\CASE-论文复现与策略进化\..\MASTER-master\data\opensource\csi300_dl_test.pkl
Traceback (most recent call last):
  File "C:\Fan\ai-quant-trading-bootcamp\week6\12-论文复现与策略进化-20260325\CASE-论文复现与策略进化\2-MASTER截面预测.py", line 92, in <module>
    with open(test_path, 'rb') as f:
         ^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Fan\\ai-quant-trading-bootcamp\\week6\\12-论文复现与策略进化-20260325\\CASE-论文复现与策略进化\\..\\MASTER-master\\data\\opensource\\csi300_dl_test.pkl'
```

## 根因分析

`2-MASTER截面预测.py` 默认从以下路径加载测试集 pickle：

```python
../MASTER-master/data/opensource/csi300_dl_test.pkl
```

当前仓库中 `MASTER-master/data/opensource/` 目录不存在，仅存在 `MASTER-master/data/csi_market_information.csv`。因此脚本无法找到对应的测试数据文件，导致 `FileNotFoundError`。

## 解决方案

### 方案一：补充官方开源测试数据文件（推荐）

从 MASTER 官方仓库提供的网盘链接下载开源数据集，将 `csi300_dl_test.pkl` 放置到：

```
week6/12-论文复现与策略进化-20260325/MASTER-master/data/opensource/csi300_dl_test.pkl
```

官方数据来源：

- **GitHub 仓库**: [SJTU-DMTai/MASTER](https://github.com/SJTU-DMTai/MASTER)
- **OneDrive**: [https://1drv.ms/f/c/652674690cc447e6/Eu8Kxv4xxTFMtDQqTW0IU0UB8rnpjACA5twMi8BA_PfbSA](https://1drv.ms/f/c/652674690cc447e6/Eu8Kxv4xxTFMtDQqTW0IU0UB8rnpjACA5twMi8BA_PfbSA)
- **MEGA**: [https://mega.nz/folder/MS8mUTbL#qeVz3KR1-MyXc_uLPtkvTg](https://mega.nz/folder/MS8mUTbL#qeVz3KR1-MyXc_uLPtkvTg)
- **百度网盘**: [https://pan.baidu.com/s/1qmDIepmGY1DVBTGGiipxfA?pwd=pm49](https://pan.baidu.com/s/1qmDIepmGY1DVBTGGiipxfA?pwd=pm49)

### 方案二：修改脚本数据路径

如果本地已将测试数据放在其他位置，可修改 `2-MASTER截面预测.py` 中的 `test_path` 变量指向实际路径。

### 方案三：自行生成测试数据

参考 MASTER 官方仓库的数据处理流程，从原始行情数据生成 `csi300_dl_test.pkl`。该方案需要额外的数据预处理脚本和 Qlib 环境支持。

## 状态

⏳ **待修复**

- GitHub Issue: [#3](https://github.com/fanyufan/ai-quant-trading-bootcamp/issues/3)
- Gitee Issue：未创建（缺少 GITEE_TOKEN）

---

> 相关文件：
> - `week6/12-论文复现与策略进化-20260325/CASE-论文复现与策略进化/2-MASTER截面预测.py`
> - `week6/12-论文复现与策略进化-20260325/MASTER-master/data/opensource/`（待创建）
