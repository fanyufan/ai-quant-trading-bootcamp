# AI 量化交易训练营

> 从零开始，用 Python 搭建量化交易研究体系。

本仓库记录「AI 量化交易训练营」的学习资料、示例代码、数据文件与策略回测结果。内容覆盖金融基础、数据获取、技术分析指标、经典策略回测与可视化，适合希望系统性入门量化交易的开发者与投资者。

量化投资的完整流程通常可分为数据获取、因子挖掘、模型构建、回测验证、风险管理、交易执行、实盘监控 7 大阶段。详见 [docs/quant-trading-lifecycle.md](docs/quant-trading-lifecycle.md)。

---

## 课程导航

本仓库按周组织课程内容，覆盖金融基础、数据获取、技术指标、策略回测、机器学习、RAG 投研、AI Agent、风控体系、团队架构、实盘作战与毕业路演。

- 完整目录结构见 [docs/course-catalog.md](docs/course-catalog.md)
- 详细课程内容概览见 [docs/course-catalog.md#课程内容概览](docs/course-catalog.md#课程内容概览)

## 环境依赖

本项目基于 **Python 3.11.9** 开发与测试，建议优先使用 Python 3.10 及以上版本。

核心 Python 依赖：

```bash
pip install pandas numpy matplotlib tushare
```

如果需要使用 **QMT（迅投）** 数据接口，还需安装 `xtquant`：

```bash
pip install xtquant
```

> `xtquant` 需要在已安装 QMT 客户端的 Windows 环境下运行，具体安装方式请参考迅投官方文档。

使用 **Tushare** 下载数据前，请配置环境变量 `TUSHARE_TOKEN`：

```bash
# Windows PowerShell
$env:TUSHARE_TOKEN="your_token_here"

# Windows CMD
set TUSHARE_TOKEN=your_token_here

# 或者在脚本中直接设置
import os
os.environ["TUSHARE_TOKEN"] = "your_token_here"
```

> 不同子项目的 `requirements.txt` 可能存在版本差异，完整说明请见 [docs/dependency-version-notes.md](docs/dependency-version-notes.md)。

---

## 快速开始

1. 克隆仓库：

```bash
git clone https://github.com/fanyufan/ai-quant-trading-bootcamp.git
cd ai-quant-trading-bootcamp
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

> 若只需核心数据接口，可手动安装：`pip install pandas numpy matplotlib tushare`。

3. 进入对应课程目录，运行脚本：

```bash
cd "week1/1-AI 量化交易-20260204"
python 2-macd_strategy_2025.py
```

4. 查看 `outputs/` 与 `result/` 目录中的回测结果与截图。

---

## 多平台同步推送

本仓库同时托管在 GitHub 与 Gitee。提交代码后，按以下命令分别推送到两个平台：

```bash
# 推送到 GitHub（本地 main → 远程 main）
git push origin

# 推送到 Gitee（本地 main → 远程 master）
git push gitee
```

> Gitee 仓库的主分支名为 `master`，因此已在 `.git/config` 中配置 `remote.gitee.push = refs/heads/main:refs/heads/master`，无需每次手动指定分支映射。

---

## 数据来源说明

| 数据类型 | 来源 | 说明 |
|---------|------|------|
| 行情数据 | QMT（xtquant） | A 股日线，需在 QMT 环境下运行 |
| 行情数据 | Tushare | A 股日线，需 Token |
| 财务数据 | Tushare | 基本面、财务指标数据 |
| 示例数据 | 本地 CSV | 课程配套数据，可直接复现 |

### 常用数据接口文档

| 数据接口 | 官方文档 / 仓库 |
|---------|----------------|
| QMT（迅投） | [https://dict.thinktrader.net/?id=7zqjlm](https://dict.thinktrader.net/?id=7zqjlm) |
| Tushare | [https://tushare.pro/document/2](https://tushare.pro/document/2) |
| AKShare | [https://akshare.akfamily.xyz/](https://akshare.akfamily.xyz/) / [GitHub](https://github.com/akfamily/akshare) |
| BaoStock | [https://baostock.com/](https://baostock.com/) |

更多数据源对比、按数据项选型建议及官方文档汇总，请见 [docs/data-sources.md](docs/data-sources.md)。

> 本仓库中的数据仅供学习与研究使用，不构成任何投资建议。

---

## 注意事项

1. **投资有风险，入市需谨慎。** 仓库中的所有策略均为教学示例，不代表实际投资建议。
2. 运行 `xtquant` 相关脚本前，请确保已正确安装并启动 QMT 客户端。
3. 部分脚本涉及中文字体显示，若遇到字体乱码，请根据本地环境调整 `matplotlib` 字体配置。
4. 建议为不同课程创建独立的 Python 虚拟环境，避免依赖冲突。

---

## 许可证

本项目采用 [MIT License](LICENSE) 开源许可。


