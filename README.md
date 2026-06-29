# AI 量化交易训练营

> 从零开始，用 Python 搭建量化交易研究体系。

本仓库记录「AI 量化交易训练营」的学习资料、示例代码、数据文件与策略回测结果。内容覆盖金融基础、数据获取、技术分析指标、经典策略回测与可视化，适合希望系统性入门量化交易的开发者与投资者。

---

## 目录结构

```
ai-quant-trading-bootcamp/
├── week1/                                          # 第一周：量化世界的生存法则 / AI 量化交易 + 金融基础速通
│   │
│   ├── 1-量化世界的生存法则.pdf                    # 第一次课讲义
│   ├── 1-AI 量化交易-20260204/                     # 第一次课代码与数据（与上为同一节课）
│   │   ├── 1-qmt_download_data.py                  # 使用 QMT（xtquant）下载股票日线数据
│   │   ├── 1-tushare_download_data.py              # 使用 Tushare 下载股票日线数据
│   │   ├── 2-macd_strategy_2025.py                 # MACD 金叉死叉策略回测
│   │   ├── 3-grid_strategy_2025.py                 # 网格交易策略回测
│   │   ├── data/                                   # 原始行情数据
│   │   │   ├── 600519_SH_daily.csv                 # 贵州茅台日线数据
│   │   │   └── 688256_SH_daily.csv                 # 寒武纪日线数据
│   │   ├── outputs/                                # 策略回测输出（净值、交易记录、图表、汇总）
│   │   └── result/                                 # 策略运行结果截图
│   │
│   ├── 2-金融基础速通.pdf                          # 第二次课讲义
│   └── 2-金融基础速通-20260207/                    # 第二次课代码与数据
│       ├── 1-K线图与成交量.py                      # K 线图与成交量可视化
│       ├── 2-获取贵州茅台的财务指标.py             # 获取贵州茅台财务指标
│       ├── 3-格雷厄姆PB选股.py                     # 格雷厄姆 PB 选股策略
│       ├── 4-制定你的基本面选股.py                 # 自定义基本面选股逻辑
│       ├── 5-贵州茅台MA交易信号.py                 # MA 均线交易信号
│       ├── 6-贵州茅台MACD交易信号.py               # MACD 交易信号
│       ├── 7-贵州茅台RSI指标计算.py                # RSI 指标计算
│       ├── 8-贵州茅台ATR指标计算.py                # ATR 指标计算
│       ├── 9-贵州茅台指标仪表盘.py                 # 多指标综合仪表盘
│       ├── 数据下载-QMT日线.py                     # 使用 QMT 下载日线数据
│       ├── 数据下载-tushare财务数据.py             # 使用 Tushare 下载财务数据
│       └── data/                                   # 财务指标与股票基本面数据
│
├── week2/                                          # 第二周：基础设施打造 + 数据获取与清洗
│   │
│   ├── 3-基础设施打造(构建数字化办公室)-20260211/  # 第三次课：构建量化数据基础设施
│   │   ├── 3-基础设施打造(构建数字化办公室).pdf    # 第三次课讲义
│   │   ├── CASE-多因子选股/                        # 多因子选股案例
│   │   │   ├── 多因子选股-下载数据.py              # 下载多因子选股所需数据
│   │   │   ├── 多因子选股-筛选1.py                 # 多因子筛选逻辑（一）
│   │   │   ├── 多因子选股-筛选2.py                 # 多因子筛选逻辑（二）
│   │   │   └── data/                               # 选股结果与行业可视化数据
│   │   └── CASE-数据采集/                          # 多源数据采集对比案例
│   │       ├── 分钟数据-QMT.py                     # QMT 分钟数据采集
│   │       ├── 分钟数据-akshare.py                 # AKShare 分钟数据采集
│   │       ├── 分钟数据-tushare.py                 # Tushare 分钟数据采集
│   │       ├── 日线数据-QMT.py                     # QMT 日线数据采集
│   │       ├── 日线数据-akshare.py                 # AKShare 日线数据采集
│   │       ├── 日线数据-tushare.py                 # Tushare 日线数据采集
│   │       ├── 财务数据-QMT.py                     # QMT 财务数据采集
│   │       ├── 财务数据-akshare.py                 # AKShare 财务数据采集
│   │       ├── 财务数据-tushare.py                 # Tushare 财务数据采集
│   │       └── data/                               # QMT/AKShare/Tushare 采集的示例数据
│   │
│   └── 4-数据获取与清洗-20260225/                  # 第四次课：多维度数据获取与清洗
│       ├── 4-数据获取与清洗.pdf                    # 第四次课讲义
│       └── CASE-数据采集/                          # 行情/财务/宏观/新闻/研报等数据采集
│           ├── 1-行情数据采集.py                   # 行情数据采集
│           ├── 2-财务数据采集.py                   # 财务数据采集
│           ├── 3-宏观数据采集.py                   # 宏观数据采集
│           ├── 4-新闻事件采集.py                   # 新闻事件数据采集
│           ├── 5-研报数据采集.py                   # 研报数据采集
│           ├── 6-财经日历采集.py                   # 财经日历数据采集
│           ├── 7-关键催化剂采集.py                 # 关键催化剂数据采集
│           ├── db_config.py                        # 数据库配置
│           ├── prompts.yaml                        # 提示词配置
│           ├── wucai_trade_charles.sql             # 数据库表结构
│           └── .env.example                        # 环境变量配置示例
│
├── .gitignore
├── LICENSE
└── README.md
```

---

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

## 课程内容概览

### Week 1 · 量化世界的生存法则 / AI 量化交易（2026-02-04）

- 量化交易的基本概念与发展历程
- 量化策略的完整生命周期：数据 → 信号 → 交易 → 风控
- Python 量化生态概览
- 使用 QMT / Tushare 获取 A 股历史行情
- MACD 趋势跟踪策略回测
- 网格交易策略回测
- 策略绩效评估与可视化

### Week 1 · 金融基础速通（2026-02-07）

- K 线图与成交量解读
- 财务指标获取与基本面分析
- 格雷厄姆 PB 选股逻辑
- 技术指标计算：MA、MACD、RSI、ATR
- 多指标综合仪表盘

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

---

## 作者

- **fanyufan** · [734051844@qq.com](mailto:734051844@qq.com)

欢迎通过 Issue 或 Pull Request 交流讨论。
