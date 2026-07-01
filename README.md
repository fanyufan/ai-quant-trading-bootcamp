# AI 量化交易训练营

> 从零开始，用 Python 搭建量化交易研究体系。

本仓库记录「AI 量化交易训练营」的学习资料、示例代码、数据文件与策略回测结果。内容覆盖金融基础、数据获取、技术分析指标、经典策略回测与可视化，适合希望系统性入门量化交易的开发者与投资者。

---

## 目录结构

```text
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
├── week3/                                          # 第三周：Backtrader 回测 + Talib 技术指标库
│   │
│   ├── 5-Backtrader回测-20260228/                  # 第五次课：掌握回测引擎 Backtrader
│   │   ├── 5-掌握回测引擎Backtrader.pdf            # 第五次课讲义
│   │   ├── data_loader.py                          # 数据加载模块
│   │   ├── db_config.py                            # 数据库配置
│   │   ├── 1-双均线策略.py                         # 双均线策略回测
│   │   ├── 2-MACD策略.py                           # MACD 策略回测
│   │   ├── 3-RSI策略.py                            # RSI 策略回测
│   │   ├── 4-布林带策略.py                         # 布林带策略回测
│   │   ├── 5-乖离率策略.py                         # 乖离率策略回测
│   │   ├── 6-动量策略.py                           # 动量策略回测
│   │   ├── 7-自定义策略.py                         # 自定义策略框架
│   │   ├── strategies/                             # 策略模块目录
│   │   │   └── macd_divergence.py                  # MACD 底背离策略
│   │   ├── outputs/                                # 策略回测输出图表
│   │   └── .env.example                            # 环境变量配置示例
│   │
│   ├── 6-Talib技术指标库-20260304/                 # 第六次课：装备 Talib 技术指标库
│   │   ├── 6-装备Talib技术指标库.pdf               # 第六次课讲义
│   │   ├── data_loader.py                          # 数据加载模块
│   │   ├── db_config.py                            # 数据库配置
│   │   ├── 1-Talib vs Backtrader对比.py            # Talib 与 Backtrader 对比
│   │   ├── 1-行情数据采集.py                       # 行情数据采集
│   │   ├── 2-Talib基础用法.py                      # Talib 基础用法
│   │   ├── 3-K线形态识别.py                        # K 线形态识别
│   │   ├── 4-RSI策略-优化(穿越确认).py             # RSI 策略优化：穿越确认
│   │   ├── 5-MACD策略-优化(成交量确认).py          # MACD 策略优化：成交量确认
│   │   ├── 6-MACD策略-优化(利润锁定).py            # MACD 策略优化：利润锁定
│   │   ├── 7-布林带策略-优化(中轨止损).py          # 布林带策略优化：中轨止损
│   │   ├── 8-自适应策略.py                         # 自适应策略
│   │   ├── 9-形态选股雷达.py                       # 形态选股雷达
│   │   └── .env.example                            # 环境变量配置示例
│   │
│   └── 6-财经日历采集-20260307.py                  # 财经日历数据采集脚本
│
├── week4/                                          # 第四周：OpenClaw + 海龟交易法则
│   │
│   ├── 7-OpenClaw-20260307/                        # 第七次课：搭建你的量化交易同事
│   │   ├── 7-OpenClaw：搭建你的量化交易同事.pdf     # 第七次课讲义
│   │   ├── .openclaw/workspace/                    # OpenClaw 工作区配置
│   │   └── openclaw/workspace/                     # OpenClaw 工作区示例
│   │
│   └── 8-海龟交易法则-20260311/                    # 第八次课：海龟交易法则
│       ├── 8-海龟交易法则.pdf                      # 第八次课讲义
│       ├── data_loader.py                          # 数据加载模块
│       ├── db_config.py                            # 数据库配置
│       ├── 1-经典海龟策略.py                       # 经典海龟交易策略
│       ├── 2-ADX海龟策略.py                        # ADX 过滤版海龟策略
│       ├── 3-多周期海龟策略.py                     # 多周期确认海龟策略
│       ├── 4-ML增强海龟策略.py                     # 机器学习增强海龟策略
│       └── .env.example                            # 环境变量配置示例
│
├── week5/                                          # 第五周：缠论量化 + 网格与多因子
│   │
│   ├── 9-缠论量化-20260314/                        # 第九次课：缠论精华量化
│   │   ├── 9-缠论量化.pdf                          # 第九次课讲义
│   │   ├── CASE-缠论精华量化/                      # 缠论量化案例
│   │   │   ├── 1-K线包含处理与分型识别.py          # K 线包含处理与顶底分型识别
│   │   │   ├── 2-笔的自动化识别.py                 # 缠论“笔”的自动识别
│   │   │   ├── 3-中枢识别与可视化.py               # 中枢识别与可视化
│   │   │   ├── 4-三类买卖点信号.py                 # 三类买卖点信号识别
│   │   │   ├── 5-缠论三买策略回测.py               # 缠论三买策略回测
│   │   │   ├── 6-缠论+量价增强策略.py              # 缠论 + 量价增强策略
│   │   │   ├── 7-多周期缠论策略.py                 # 多周期缠论策略
│   │   │   ├── 8-ML增强缠论策略.py                 # 机器学习增强缠论策略
│   │   │   ├── data_loader.py                      # 数据加载模块
│   │   │   ├── db_config.py                        # 数据库配置
│   │   │   ├── chanpy_wrapper.py                   # chan.py 封装接口
│   │   │   ├── chan_analyzer.py                    # 缠论分析工具
│   │   │   ├── outputs/                            # 分型/笔/中枢/买卖点可视化输出
│   │   │   └── .env.example                        # 环境变量配置示例
│   │   └── chan.py/                                # 缠论分析开源库（已去内层 .git）
│   │
│   └── 10-网格与多因子-20260318/                   # 第十次课：网格与多因子
│       ├── 10-网格与多因子.pdf                     # 第十次课讲义
│       ├── CASE-网格与多因子/                      # 网格与多因子案例
│       │   ├── 1-经典网格策略.py                   # 经典网格交易策略
│       │   ├── 2-缠论中枢网格策略.py               # 缠论中枢网格策略
│       │   ├── 3-中枢网格+趋势联动.py              # 中枢网格 + 趋势联动
│       │   ├── 4-多因子评价框架.py                 # 多因子评价框架
│       │   ├── 5-多因子打分选股.py                 # 多因子打分选股
│       │   ├── 6-小市值轮动策略.py                 # 小市值轮动策略
│       │   ├── 7-因子选股+中枢网格.py              # 因子选股 + 中枢网格
│       │   ├── 8-ML增强多因子.py                   # 机器学习增强多因子
│       │   ├── data_loader.py                      # 数据加载模块
│       │   ├── db_config.py                        # 数据库配置
│       │   ├── grid_engine.py                      # 网格交易引擎
│       │   ├── factor_engine.py                    # 多因子引擎
│       │   ├── chanpy_wrapper.py                   # chan.py 封装接口
│       │   └── .env                                # 环境变量配置（已忽略）
│       └── chan.py/                                # 缠论分析开源库（已去内层 .git）
│
├── week6/                                          # 第六周：机器学习因子挖掘 + 论文复现与策略进化
│   │
│   ├── 11-机器学习因子挖掘-20260321/               # 第十一次课：机器学习因子挖掘
│   │   ├── 11-机器学习因子挖掘.pdf                 # 第十一次课讲义
│   │   ├── 1-贵州茅台因子分析.py                   # 单因子分析与可视化
│   │   ├── 2-工业级特征工程.py                     # 工业级特征工程实现
│   │   ├── 3-XGBoost涨跌预测.py                    # XGBoost 涨跌预测
│   │   ├── 4-LightGBM对比与调参.py                 # LightGBM 对比与调参
│   │   ├── data_loader.py                          # 数据加载模块
│   │   ├── db_config.py                            # 数据库配置
│   │   ├── feature_engine.py                       # 特征工程模块
│   │   ├── ml_engine.py                            # 机器学习引擎
│   │   └── .env.example                            # 环境变量配置示例
│   │
│   └── 12-论文复现与策略进化-20260325/             # 第十二次课：论文复现与策略进化
│       ├── 12-论文复现与策略进化.pdf               # 第十二次课讲义
│       ├── CASE-论文复现与策略进化/                # MASTER 论文复现案例
│       │   ├── 1-MASTER数据与因子.py               # MASTER 数据准备与因子构建
│       │   ├── 2-MASTER截面预测.py                 # MASTER 截面预测
│       │   ├── 3-XGBoost截面预测.py                # XGBoost 截面预测对比
│       │   ├── data_loader.py                      # 数据加载模块
│       │   ├── db_config.py                        # 数据库配置
│       │   ├── feature_engine.py                   # 特征工程模块
│       │   ├── evolution_engine.py                 # 策略进化引擎
│       │   ├── MASTER_csi300_prediction_results.png  # MASTER 预测结果图
│       │   └── .env.example                        # 环境变量配置示例
│       └── MASTER-master/                          # MASTER 官方论文复现源码
│           ├── base_model.py                       # MASTER 基础模型
│           ├── master.py                           # MASTER 核心实现
│           ├── main.py                             # 入口脚本
│           ├── data/                               # 市场信息数据
│           ├── model/                              # 预训练模型（.pkl 已忽略）
│           ├── qlib-update/                        # Qlib 适配代码
│           ├── README.md                           # 官方说明
│           └── LICENSE                             # 开源协议
│
├── week7/                                          # 第七周：QuantStats 绩效分析 + RAG 投研系统
│   │
│   ├── 13-QuantStats绩效分析与报告.pdf             # 第十三次课讲义
│   ├── 13-QuantStats绩效分析与报告-20260328/       # 第十三次课代码与数据
│   │   ├── 1-QuantStats绩效分析.py                 # 使用 QuantStats 生成策略绩效报告
│   │   ├── 2-SVD因子挖掘与分析.py                  # 基于 SVD 的因子挖掘与分析
│   │   ├── 3-实盘交易绩效分析.py                   # 实盘交易记录绩效分析
│   │   ├── 4-实盘交易绩效分析Plus.py               # 实盘交易绩效分析增强版
│   │   ├── data_loader.py                          # 数据加载模块
│   │   ├── db_config.py                            # 数据库配置
│   │   ├── feature_engine.py                       # 特征工程模块
│   │   ├── ml_engine.py                            # 机器学习引擎
│   │   ├── llm_engine.py                           # LLM 报告生成引擎
│   │   ├── report_engine.py                        # 报告引擎
│   │   ├── translations.yaml                       # 中文术语翻译配置
│   │   ├── 历史成交_cy_260101-260325.csv            # 示例实盘成交记录
│   │   └── .env.example                            # 环境变量配置示例
│   │
│   ├── 14-RAG投研系统搭建.pdf                      # 第十四次课讲义
│   └── 14-RAG投研系统搭建-20260401/                # 第十四次课代码与数据
│       ├── CASE-向量数据库/                        # 向量数据库与 embedding 实践
│       │   ├── 1-embedding计算.py                  # Embedding 计算
│       │   ├── 2-embedding-faiss-元数据.py         # FAISS 向量索引与元数据
│       │   └── requirements.txt                    # 依赖说明
│       ├── Case-ChatPDF-Faiss/                     # 基于 Faiss 的 ChatPDF 案例
│       │   ├── chatpdf-faiss.ipynb                 # Jupyter 交互示例
│       │   ├── chatpdf-faiss.py                    # ChatPDF 主脚本
│       │   ├── requirements.txt                    # 依赖说明
│       │   ├── vector_db/                          # FAISS 向量数据库
│       │   └── 财报_中芯国际：中芯国际2025年年度报告.pdf  # 示例财报 PDF
│       ├── hotel_recommendation/                   # Word2Vec 推荐系统案例
│       │   ├── hotel_rec.ipynb                     # 酒店推荐 Jupyter 示例
│       │   ├── hotel_rec.py                        # 酒店推荐脚本
│       │   ├── Seattle_Hotels.csv                  # 示例数据
│       │   └── requirements.txt                    # 依赖说明
│       └── word2vec/                               # Word2Vec 词向量训练案例
│           ├── word_seg.ipynb                      # 分词 Jupyter 示例
│           ├── word_seg.py                         # 中文分词脚本
│           ├── word_similarity.ipynb               # 词相似度 Jupyter 示例
│           ├── word_similarity.py                  # 词相似度计算脚本
│           ├── utils/                              # 工具函数
│           ├── models/                             # 训练好的 Word2Vec 模型
│           ├── journey_to_the_west/                # 《西游记》语料
│           └── three_kingdoms/                     # 《三国演义》语料
│
├── week8/                                          # 第八周：智能研报生成 + 舆情感知与事件驱动
│   │
│   ├── 15-智能研报生成.pdf                         # 第十五次课讲义
│   ├── 15-智能研报生成-20260404/                   # 第十五次课代码与数据
│   │   ├── agent.py                                # 智能研报生成 Agent
│   │   ├── preprocess.py                           # 数据预处理：解析 PDF、构建向量库
│   │   ├── requirements.txt                        # 依赖说明
│   │   ├── data/                                   # 研报、财报、新闻、向量库等数据
│   │   │   ├── reports/                            # 机构研报 PDF
│   │   │   ├── parsed/                             # PDF 解析后的文本与页码信息
│   │   │   ├── parsed_ocr/                         # OCR 解析结果
│   │   │   ├── financial_reports/                  # 上市公司财报 PDF
│   │   │   ├── financial_data/                     # 财务报表数据（CSV）
│   │   │   ├── news/                               # 新闻数据（JSON）
│   │   │   ├── sentiment/                          # 情感分析结果
│   │   │   ├── events/                             # 事件抽取结果
│   │   │   ├── vector_db/                          # 单文档 FAISS 向量索引
│   │   │   ├── vector_store/                       # 统一向量索引
│   │   │   └── documents.db                        # SQLite 文档元数据库
│   │   └── skills/                                 # Agent 技能目录
│   │       ├── read-pdf/                           # 读取与解析 PDF 财报/研报
│   │       ├── financial-analysis/                 # 财务分析技能
│   │       ├── compare-reports/                    # 研报对比技能
│   │       ├── sentiment-analysis/                 # 情感分析技能
│   │       ├── stock-price/                        # 股价查询技能
│   │       ├── web-search/                         # 网络搜索技能
│   │       └── write-report/                       # 研报生成技能
│   │
│   ├── 16-舆情感知与事件驱动.pdf                   # 第十六次课讲义
│   └── 16-舆情感知与事件驱动-20260408/             # 第十六次课代码与数据
│       ├── CASE-AI量化助手（nanobot）/             # AI 量化助手完整案例
│       │   ├── agent.py                            # nanobot Agent 入口
│       │   ├── config.json                         # Agent 配置
│       │   ├── AGENTS.md                           # Agent 说明文档
│       │   ├── data/                               # 新闻、事件等输入数据
│       │   ├── output/                             # 情感、事件、恐惧指数等输出
│       │   ├── memory/                             # 记忆文件
│       │   ├── reports/                            # 生成的研报
│       │   ├── sessions/                           # 会话记录
│       │   └── skills/                             # Agent 技能目录
│       └── nanobot-main/                           # nanobot 开源项目源码
│           ├── nanobot/                            # Python 核心代码
│           ├── bridge/                             # TypeScript Bridge
│           ├── tests/                              # 单元测试
│           ├── Dockerfile / docker-compose.yml     # 容器化配置
│           ├── pyproject.toml                      # 项目配置
│           ├── README.md                           # 官方说明
│           └── LICENSE                             # 开源协议
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

## 课程内容概览

## Week 1

### 1-量化世界的生存法则 / AI 量化交易（2026-02-04）

- 量化交易的基本概念与发展历程
- 量化策略的完整生命周期：数据 → 信号 → 交易 → 风控
- Python 量化生态概览
- 使用 QMT / Tushare 获取 A 股历史行情
- MACD 趋势跟踪策略回测
- 网格交易策略回测
- 策略绩效评估与可视化

### 2-金融基础速通（2026-02-07）

- K 线图与成交量解读
- 财务指标获取与基本面分析
- 格雷厄姆 PB 选股逻辑
- 技术指标计算：MA、MACD、RSI、ATR
- 多指标综合仪表盘

## Week 2

### 3-基础设施打造：构建数字化办公室（2026-02-11）

- 量化研究的数据基础设施搭建思路
- 多因子选股：从数据下载到筛选逻辑
- 多源数据采集对比：QMT / AKShare / Tushare
- 分钟线、日线、财务数据的获取方式与差异

### 4-数据获取与清洗（2026-02-25）

- 行情数据采集与清洗
- 财务数据采集与结构化存储
- 宏观数据、新闻事件、研报数据采集
- 财经日历与关键催化剂事件跟踪
- 数据库配置与表结构设计

## Week 3

### 5-Backtrader 回测（2026-02-28）

- Backtrader 回测引擎核心概念：Cerebro、Data、Strategy、Broker
- 双均线、MACD、RSI、布林带、乖离率、动量策略回测
- 自定义策略框架与 MACD 底背离策略
- 数据加载模块与回测结果可视化

### 6-Talib 技术指标库（2026-03-04）

- Talib 与 Backtrader 指标对比
- Talib 基础用法与 K 线形态识别
- RSI 策略优化：穿越确认
- MACD 策略优化：成交量确认与利润锁定
- 布林带策略优化：中轨止损
- 自适应策略与形态选股雷达

### 6-财经日历采集（2026-03-07）

- 财经日历数据采集实践

## Week 4

### 7-OpenClaw：搭建你的量化交易同事（2026-03-07）

- OpenClaw 量化 Agent 框架介绍
- 量化交易工作流规划与技能封装
- Backtrader / miniQMT / Talib 技能集成
- AI 驱动的策略推荐与协作模式

### 8-海龟交易法则（2026-03-11）

- 经典海龟交易策略原理与实现
- ADX 过滤版海龟策略
- 多周期确认海龟策略
- 机器学习增强海龟策略
- 数据加载与仓位管理

## Week 5

### 9-缠论精华量化（2026-03-14）

- 缠论基础：K 线包含处理、顶底分型识别
- 缠论“笔”的自动化识别与校验
- 中枢识别、可视化与级别划分
- 三类买卖点信号识别与分类
- 缠论三买策略回测与绩效分析
- 缠论 + 量价增强策略
- 多周期缠论策略与 ML 增强缠论策略
- 基于 chan.py 的缠论分析库封装与应用

### 10-网格与多因子（2026-03-18）

- 经典网格交易策略原理与实现
- 缠论中枢网格策略：结合中枢上下轨做网格
- 中枢网格 + 趋势联动策略
- 多因子评价框架：IC、IR、分层回测
- 多因子打分选股与小市值轮动策略
- 因子选股 + 中枢网格组合策略
- 机器学习增强多因子模型
- 网格引擎与多因子引擎的模块化设计

## Week 6

### 11-机器学习因子挖掘（2026-03-21）

- 单因子分析：以贵州茅台为例的因子分布与 IC 分析
- 工业级特征工程：截面特征、时序特征、标签构建
- XGBoost 涨跌预测模型
- LightGBM 对比实验与超参数调优
- 特征工程模块与机器学习引擎的模块化设计

### 12-论文复现与策略进化（2026-03-25）

- MASTER 论文（KDD 2022）核心思想与框架介绍
- MASTER 数据准备与因子构建
- MASTER 截面预测实现
- XGBoost 截面预测对比基准
- 策略进化引擎设计与论文复现流程
- 预训练模型与官方源码集成

## Week 7

### 13-QuantStats 绩效分析与报告（2026-03-28）

- QuantStats 策略绩效报告生成与解读
- 关键绩效指标：收益率、夏普比率、最大回撤、Calmar、Sortino 等
- 基于 SVD 的因子挖掘与可视化分析
- 实盘交易记录的绩效归因与多维度评估
- LLM 驱动的绩效报告自动生成
- 中文术语翻译配置与模块化报告引擎

### 14-RAG 投研系统搭建（2026-04-01）

- RAG（检索增强生成）基本原理与投研应用场景
- Embedding 计算与 FAISS 向量数据库构建
- 基于 ChatPDF-Faiss 的财报问答系统
- Word2Vec 词向量训练：分词、相似度计算与推荐系统
- 向量索引、元数据管理与页码溯源
- 多数据源（财报、新闻、研报）的向量化检索实践

## Week 8

### 15-智能研报生成（2026-04-04）

- AI Agent 驱动的智能研报生成流程
- PDF 财报/研报解析：基础解析与多模态 OCR 解析
- FAISS 向量知识库构建与 RAG 查询
- 财务分析技能：比率分析、同业对比
- 情感分析技能：新闻情绪、舆情打分
- 研报对比与事件抽取
- 网络搜索、股价查询与研报自动撰写

### 16-舆情感知与事件驱动（2026-04-08）

- 舆情监测与事件驱动策略框架
- nanobot 量化助手：配置、记忆、会话与技能管理
- 新闻情感分析、事件抽取与市场情绪指标
- 恐惧指数、Polymarket 等另类情绪数据源
- AI 量化助手完整工作流：数据 → 分析 → 报告
- nanobot 开源项目源码解析与二次开发

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
