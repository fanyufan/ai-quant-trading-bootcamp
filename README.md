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
├── week9/                                          # 第九周：Xtquant 实盘与 Agent 搭建实战 + 强化学习与高频探索
│   │
│   ├── 17-Xtquant实盘与Agent搭建实战.pdf           # 第十七次课讲义
│   ├── 17-Xtquant实盘与Agent搭建实战-20260411/     # 第十七次课代码与数据
│   │   ├── CASE-AI量化助手（nanobot）/             # AI 量化助手完整案例
│   │   │   ├── agent.py                            # nanobot Agent 入口
│   │   │   ├── config.json                         # Agent 配置
│   │   │   ├── AGENTS.md                           # Agent 说明文档
│   │   │   ├── .env.example                        # 环境变量配置示例
│   │   │   ├── data/                               # 新闻、事件等输入数据
│   │   │   ├── output/                             # 情感、事件、恐惧指数等输出
│   │   │   ├── memory/                             # 记忆文件
│   │   │   ├── reports/                            # 生成的研报
│   │   │   ├── sessions/                           # 会话记录
│   │   │   └── skills/                             # Agent 技能目录
│   │   ├── CASE-XtQuant实盘交易/                   # XtQuant 实盘交易案例
│   │   │   ├── .env.example                        # 环境变量配置示例
│   │   │   ├── 1-query_account.py                  # 查询账户信息
│   │   │   ├── 2-order_and_cancel.py               # 下单与撤单
│   │   │   ├── 3-callback_demo.py                  # 回调演示
│   │   │   ├── 4-miniqmt_trader.py                 # miniQMT 交易员
│   │   │   └── 5-signal_to_order.py                # 信号转订单
│   │   ├── CASE-nanobot使用/                       # nanobot 使用案例
│   │   │   ├── content-builder/                    # 内容生成 Agent
│   │   │   ├── deep-research/                      # 深度研究 Agent
│   │   │   └── text-to-sql/                        # Text-to-SQL Agent
│   │   ├── skill-nanobot/                          # skill 化 nanobot 配置
│   │   └── nanobot-main/                           # nanobot 开源项目源码
│   │       ├── nanobot/                            # Python 核心代码
│   │       ├── bridge/                             # TypeScript Bridge
│   │       ├── tests/                              # 单元测试
│   │       ├── Dockerfile / docker-compose.yml     # 容器化配置
│   │       ├── pyproject.toml                      # 项目配置
│   │       ├── README.md                           # 官方说明
│   │       └── LICENSE                             # 开源协议
│   │
│   ├── 18-强化学习与高频探索.pdf                   # 第十八次课讲义
│   └── 18-强化学习与高频探索-20260415/             # 第十八次课代码与数据
│       ├── CASE-cartpole-qlearning/                # CartPole Q-Learning 案例
│       │   ├── agent.py                            # Q-Learning Agent
│       │   └── cartpole.py                         # CartPole 环境交互
│       ├── CASE-迷宫问题/                          # 迷宫 RL 案例
│       │   └── maze.py                             # 迷宫求解
│       └── CASE-基于RL的交易策略/                  # 基于 RL 的交易策略案例
│           ├── .env.example                        # 环境变量配置示例
│           ├── 1-搭建RL交易环境.py                 # 搭建 RL 交易环境
│           ├── 2-DQN择时策略.py                    # DQN 择时策略
│           ├── 3-策略回测与评估.py                 # 策略回测与评估
│           ├── 4-智能拆单环境.py                   # 智能拆单环境
│           ├── 5-TWAP与RL拆单对比.py               # TWAP 与 RL 拆单对比
│           ├── data_loader.py                      # 数据加载模块
│           ├── db_config.py                        # 数据库配置
│           ├── models/                             # 训练好的 RL 模型
│           └── outputs/                            # 训练与回测输出图表
│
├── week10/                                         # 第十周：强化学习与风控体系 + 团队架构设计
│   │
│   ├── 19-强化学习与风控体系.pdf                   # 第十九次课讲义
│   ├── 19-强化学习与风控体系-20260418/             # 第十九次课代码与数据
│   │   ├── CASE-Kris的风控体系/                    # Kris 的风控体系案例
│   │   │   ├── .env.example                        # 环境变量配置示例
│   │   │   ├── 1-风控引擎.py                       # 风控引擎
│   │   │   ├── 2-ATR风控实战.py                    # ATR 风控实战
│   │   │   ├── 3-事件风控实战.py                   # 事件风控实战
│   │   │   ├── 4-宏观门控实战.py                   # 宏观门控实战
│   │   │   ├── data_loader.py                      # 数据加载模块
│   │   │   ├── db_config.py                        # 数据库配置
│   │   │   └── outputs/                            # 风控可视化输出图表
│   │   └── CASE-基于RL的交易策略/                  # 基于 RL 的交易策略案例
│   │       ├── .env.example                        # 环境变量配置示例
│   │       ├── 6-高频做市模拟.py                   # 高频做市模拟
│   │       ├── 7-主力行为识别.py                   # 主力行为识别
│   │       ├── data_loader.py                      # 数据加载模块
│   │       └── db_config.py                        # 数据库配置
│   │
│   ├── 20-团队架构设计.pdf                         # 第二十次课讲义
│   └── 20-团队架构设计-20260422/                   # 第二十次课代码与数据
│       └── CASE-交易团队工作流（langgraph）/         # 交易团队工作流案例
│           ├── .env.example                        # 环境变量配置示例
│           ├── main.py                             # 团队工作流入口
│           ├── graph.py                            # LangGraph 工作流图
│           ├── state.py                            # 状态定义
│           ├── scheduler.py                        # 调度器
│           ├── requirements.txt                    # 依赖说明
│           ├── nodes/                              # 多角色 Agent 节点
│           │   ├── charles_node.py                 # Charles 投研节点
│           │   ├── kris_node.py                    # Kris 风控节点
│           │   ├── zoe_node.py                     # Zoe 宏观节点
│           │   ├── trader_node.py                  # Trader 交易节点
│           │   └── human_node.py                   # Human 人工审核节点
│           ├── lib/                                # 工具库
│           │   ├── miniqmt_trader.py               # miniQMT 交易员
│           │   └── risk_engine.py                  # 风控引擎
│           ├── scripts/                            # 辅助脚本
│           │   ├── get_kline.py                    # 获取 K 线数据
│           │   ├── run_backtest.py                 # 运行回测
│           │   └── sync_charles_vendor.py          # 同步投研数据
│           ├── vendor/charles_agent/               # Charles 投研 Agent
│           └── outputs/                            # 研报与运行记录
│
├── week11/                                         # 第十一周：投资晨会 + 实盘作战与 CEO 控制台
│   │
│   ├── 21-投资晨会.pdf                             # 第二十一次课讲义
│   ├── 21-投资晨会-20260425/                       # 第二十一次课代码与数据
│   │   ├── CASE-A-板块数据准备/                    # 板块指数与成分股数据准备
│   │   │   ├── sector_index_builder.py             # 板块指数构建
│   │   │   ├── stock_kline_loader.py               # 个股 K 线加载
│   │   │   ├── industry_meta.py                    # 行业元数据
│   │   │   ├── run_init.py                         # 初始化跑批
│   │   │   ├── run_daily.py                        # 每日更新
│   │   │   └── sql/schema.sql                      # 数据库表结构
│   │   ├── CASE-B-板块轮动分析/                    # 板块轮动与拐点识别
│   │   │   ├── industry_strength.py                # 行业强度计算
│   │   │   ├── inflection_detector.py              # 拐点检测
│   │   │   ├── rotation_insights.py                # 轮动洞察生成
│   │   │   ├── backtest.py                         # 轮动策略回测
│   │   │   └── outputs/                            # 轮动事件与阶段分布输出
│   │   ├── CASE-C-多因子选股/                      # 基本面多因子选股
│   │   │   ├── factor_lib.py                       # 因子库
│   │   │   ├── preprocessor.py                     # 数据预处理
│   │   │   ├── layered_backtest.py                 # 分层回测
│   │   │   ├── stock_pool.py                       # 股票池构建
│   │   │   ├── synthesizer.py                      # 因子合成
│   │   │   └── data/                               # 沪深300成分股与基本面数据
│   │   └── CASE-D-投资晨会工作流/                  # 投资晨会 LangGraph 工作流
│   │       ├── graph.py                            # 工作流图
│   │       ├── scheduler.py                        # 定时调度
│   │       ├── pusher.py                           # 结果推送
│   │       └── lib/                                # 因子与轮动运行器
│   │
│   ├── 22-实盘作战与CEO控制台.pdf                  # 第二十二次课讲义
│   └── 22-实盘作战与CEO控制台-20260429/            # 第二十二次课代码与数据
│       ├── CASE-AI量化系统/                        # 集成 AI 量化系统（CEO 控制台版）
│       │   ├── app.py                              # Web 控制台入口
│       │   ├── scheduler.py                        # 任务调度
│       │   ├── routes/                             # 路由：回测 / 实盘 / 晨会 / 系统
│       │   ├── pages/                              # Streamlit 页面
│       │   ├── templates/                          # Web 页面模板
│       │   ├── lib/                                # 回测、实盘、策略注册等工具库
│       │   ├── dragon_strategy/                    # 龙头战法策略模块
│       │   ├── live_trading/                       # 实盘交易循环与 miniQMT 交易员
│       │   ├── morning_brief/                      # 晨会简报生成
│       │   ├── alerting/                           # 告警路由
│       │   ├── config/                             # 策略池、观察池、模拟持仓配置
│       │   ├── outputs/                            # 运行输出与状态记录
│       │   └── .env.example                        # 环境变量配置示例
│       └── CASE-龙头战法/                          # 龙头战法独立案例
│           ├── dragon_strategy/                    # 龙头选股与回测
│           └── outputs/                            # 回测结果输出
│
├── week12/                                         # 第十二周：团队复盘与持续进化 + 毕业路演
│   │
│   ├── 23-团队复盘与持续进化.pdf                   # 第二十三次课讲义
│   ├── 23-团队复盘与持续进化-20260509/             # 第二十三次课代码与数据
│   │   ├── CASE-AI量化系统/                        # 复盘版 AI 量化系统
│   │   │   ├── app.py                              # Web 控制台入口
│   │   │   ├── routes/                             # 新增复盘 / 参数调优路由
│   │   │   ├── attribution/                        # Brinson 归因模块
│   │   │   ├── parameter_tuning/                   # Walk-Forward 参数调优
│   │   │   ├── strategy_lifecycle/                 # 策略生命周期注册表
│   │   │   ├── lib/                                # 包含 Brinson 真实归因实现
│   │   │   └── .env.example                        # 环境变量配置示例
│   │   ├── CASEA-Brinson归因/                      # Brinson 归因独立案例
│   │   ├── CASEB-Walk-Forward过拟合检测/           # Walk-Forward 过拟合检测
│   │   └── CASEC-策略生命周期/                     # 策略生命周期管理
│   │
│   ├── 24-毕业路演-AI私募基金发布会.pdf             # 第二十四次课讲义
│   └── 24-毕业路演-AI私募基金发布会-20260513/       # 第二十四次课代码与数据
│       └── CASE-AI量化系统/                        # 毕业版 AI 量化系统
│           ├── app.py                              # Web 控制台入口
│           ├── ml_strategy/                        # ML 概率策略模块
│           ├── routes/                             # 路演版路由
│           ├── outputs/                            # 路演材料输出（pitch deck 等）
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

## Week 9

### 17-Xtquant 实盘与 Agent 搭建实战（2026-04-11）

- XtQuant 实盘交易接口：账户查询、下单撤单、回调机制
- miniQMT 交易员封装与信号转订单
- AI 量化助手与 nanobot 框架实战
- nanobot 使用案例：内容生成、深度研究、Text-to-SQL
- skill 化 nanobot 配置与扩展

### 18-强化学习与高频探索（2026-04-15）

- 强化学习基础：Q-Learning、DQN
- CartPole 与迷宫问题实战
- 基于 RL 的交易策略：DQN 择时
- 智能拆单环境与 TWAP 对比
- 模型训练、回测与评估

## Week 10

### 19-强化学习与风控体系（2026-04-18）

- 量化风控体系框架与核心模块
- 风控引擎设计：仓位、止损、熔断
- ATR 风控实战
- 事件风控：大模型驱动的新闻事件识别
- 宏观门控：VIX/QVIX 映射与市场状态过滤
- 高频做市模拟与主力行为识别

### 20-团队架构设计（2026-04-22）

- 量化交易团队角色与分工
- LangGraph 多 Agent 协作工作流
- Charles 投研 / Kris 风控 / Zoe 宏观 / Trader 交易 / Human 审核节点
- 状态机、调度器与端到端策略执行
- 团队工作流的模块化设计与扩展

## Week 11

### 21-投资晨会（2026-04-25）

- 投资晨会工作流设计：数据准备 → 板块轮动 → 多因子选股 → 简报推送
- 板块数据准备：行业指数构建、成分股 K 线、行业元数据
- 板块轮动分析：行业强度、拐点检测、轮动洞察与回测
- 多因子选股：基本面因子库、预处理、分层回测与因子合成
- LangGraph 投资晨会工作流：定时调度与结果推送

### 22-实盘作战与 CEO 控制台（2026-04-29）

- 实盘作战框架：回测、实盘、晨会、风控一体化控制台
- AI 量化系统 Web 控制台：路由、模板、任务调度与状态管理
- 龙头战法策略：选股逻辑、回测与结果输出
- 实盘交易循环：miniQMT 交易员、状态存储、告警路由
- CEO 控制台配置：策略池、观察池、模拟持仓与系统监控

## Week 12

### 23-团队复盘与持续进化（2026-05-09）

- 量化团队复盘框架：收益归因、过拟合检测、策略生命周期管理
- Brinson 归因：配置效应、选股效应、交互效应与真实交易归因
- Walk-Forward 过拟合检测：参数稳健性、样本外测试与实验记录
- 策略生命周期管理：策略注册、状态跟踪、上下线与绩效监控
- 复盘版 AI 量化系统：归因、参数调优与生命周期模块集成

### 24-毕业路演：AI 私募基金发布会（2026-05-13）

- AI 量化私募基金路演材料：策略体系、风控体系、团队架构与业绩展示
- 毕业版 AI 量化系统：整合回测、实盘、晨会、归因、风控与生命周期
- ML 概率策略模块：特征工程、机器学习引擎与概率化交易信号
- 路演材料自动化输出：HTML pitch deck、策略注册表与运行记录
- 从策略研究到基金产品的完整闭环

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


