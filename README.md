# AI 量化交易训练营

> 从零开始，用 Python 搭建量化交易研究体系。

本仓库记录「AI 量化交易训练营」的学习资料、示例代码、数据文件与策略回测结果。内容覆盖金融基础、数据获取、技术分析指标、经典策略回测与可视化，适合希望系统性入门量化交易的开发者与投资者。

---

## 目录结构

```
ai-quant-trading-bootcamp/
├── week1/                              # 第一周：量化世界的生存法则 + 金融基础速通
│   ├── 1-量化世界的生存法则.pdf        # 课程讲义
│   ├── 2-金融基础速通.pdf              # 课程讲义
│   │
│   ├── 1-AI 量化交易-20260204/         # 第一次课：量化交易概览与策略初探
│   │   ├── 1-qmt_download_data.py      # 使用 QMT（xtquant）下载股票日线数据
│   │   ├── 1-tushare_download_data.py  # 使用 Tushare 下载股票日线数据
│   │   ├── 2-macd_strategy_2025.py     # MACD 金叉死叉策略回测
│   │   ├── 3-grid_strategy_2025.py     # 网格交易策略回测
│   │   ├── data/                       # 原始行情数据
│   │   │   ├── 600519_SH_daily.csv     # 贵州茅台日线数据
│   │   │   └── 688256_SH_daily.csv     # 寒武纪日线数据
│   │   ├── outputs/                    # 策略回测输出（净值、交易记录、图表、汇总）
│   │   └── result/                     # 策略运行结果截图
│   │
│   └── 2-金融基础速通-20260207/        # 第二次课：金融基础与技术指标
│       ├── 1-K线图与成交量.py
│       ├── 2-获取贵州茅台的财务指标.py
│       ├── 3-格雷厄姆PB选股.py
│       ├── 4-制定你的基本面选股.py
│       ├── 5-贵州茅台MA交易信号.py
│       ├── 6-贵州茅台MACD交易信号.py
│       ├── 7-贵州茅台RSI指标计算.py
│       ├── 8-贵州茅台ATR指标计算.py
│       ├── 9-贵州茅台指标仪表盘.py
│       ├── 数据下载-QMT日线.py
│       ├── 数据下载-tushare财务数据.py
│       └── data/                       # 财务指标与股票基本面数据
├── .gitignore
├── LICENSE
└── README.md
```

---

## 环境依赖

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
pip install -r requirements.txt   # 如果后续提供
# 或手动安装
pip install pandas numpy matplotlib tushare
```

3. 进入对应课程目录，运行脚本：

```bash
cd "week1/1-AI 量化交易-20260204"
python 2-macd_strategy_2025.py
```

4. 查看 `outputs/` 与 `result/` 目录中的回测结果与截图。

---

## 课程内容概览

### Week 1 · 量化世界的生存法则

- 量化交易的基本概念与发展历程
- 量化策略的完整生命周期：数据 → 信号 → 交易 → 风控
- Python 量化生态概览

### Week 1 · AI 量化交易（2026-02-04）

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
