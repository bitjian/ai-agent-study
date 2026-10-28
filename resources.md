# 学习资源库：Python 后端 → AI Agent 工程师

> 使用规则：**只看当前阶段，别囤积**。每阶段给"主线"（必学）和"补充"（选学）。
> 链接均于 2026-10-28 实测可访问 ✅（realpython 的 403 是反爬，浏览器正常打开）

---

# 起步包：好懂优先（懒得挑，只看这 6 个）

按"从最容易理解"排序，适合 JS/Node 背景直接开干：

| # | 资源 | 好懂在哪 | 投入 |
|---|---|---|---|
| 1 | [LangShift：JavaScript → Python 中文模块](https://langshift.dev/zh-cn/docs/js2py) | **专为 JS 开发者写的** 12 个模块，每节都是"JS 这样写 → Python 这样写"，连包管理/异步都做了对照 | 2-3 天 |
| 2 | [Python Tutor 可视化执行](https://pythontutor.com/) | 把代码**一步步画出来**：list 别名、字符串不可变、栈帧、print vs return，肉眼可见 | 卡住就用 10 分钟 |
| 3 | [廖雪峰 Python 教程](https://liaoxuefeng.com/books/python/introduction/index.html) | 中文最经典，小节短、有在线运行环境 | 3-4 天（主线） |
| 4 | [learnpython.org](https://www.learnpython.org/) | 浏览器里直接敲代码，**零环境配置**，左讲右练 | 1 小时刷完基础 |
| 5 | [菜鸟教程 Python3](https://www.runoob.com/python3/python3-tutorial.html) | 语法字典，忘了就搜 | 随查随走 |
| 6 | [Learn X in Y Minutes: Python](https://learnxinyminutes.com/docs/python/) | 一页纸速查表，通勤路上看完 | 20 分钟 |

**视频党**：B 站搜「小甲鱼」或「黑马程序员」零基础教程——前者风趣、后者系统，**选一个跟到底，别两个都看**。

**中文对照仓库**：[shinder/from-js-to-python](https://github.com/shinder/from-js-to-python)（Jupyter Notebook 形式，边读边跑，含 JS↔Python 速查表）。

---

# 阶段 A · Python + 后端工程

## A1 · Python 语法速成（5-7 天）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [廖雪峰 Python 教程](https://liaoxuefeng.com/books/python/introduction/index.html) | 中文最经典入门 | ✅ 主线（对照 JS 速读，**跳过爬虫/运维/图形界面章节**） |
| [菜鸟教程 Python3](https://www.runoob.com/python3/python3-tutorial.html) | 语法字典 | ✅ 查询用 |
| [官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/) | 权威但略枯燥 | 补充 |
| **对照学习法** | 搜 "Python for JavaScript developers" | 推荐：带 JS 映射学，速度×3 |

**重点章节**（其余可略）：数据类型、函数、切片、dict/set、**装饰器**、**生成器/yield**、`with` 上下文管理器、类和实例、模块与包、异常处理。

**验收**：`10-python-cli/` 写一个日志分析 CLI（读文件、dict 统计、f-string 输出、argparse 参数）。

## A2 · Python 工程化（5 天）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [uv 官方文档](https://docs.astral.sh/uv/) | 包管理主线，对照 README 的 pnpm 对照表 | ✅ 主线 |
| [Pydantic 文档](https://docs.pydantic.dev/latest/) | 数据校验（≈ zod），后端 + Agent 生态共同地基 | ✅ 主线 |
| [ruff 文档](https://docs.astral.sh/ruff/) | 格式化 + lint 二合一（≈ ESLint + Prettier） | ✅ 主线（配进 .vscode 即忘） |
| [Real Python](https://realpython.com/) | 英文最佳教程站，装饰器/asyncio 专题质量极高 | 推荐 |
| [pytest 文档](https://docs.pytest.org/) | 测试（到用时再查） | 选学 |

**验收**：给 A1 的 CLI 加类型注解 + Pydantic 模型 + pytest 单测 + ruff 检查通过。

## A3 · 异步编程（4 天）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [Real Python: Async IO in Python](https://realpython.com/async-io-python/) | 讲透事件循环/`await`/`gather` | ✅ 主线 |
| [httpx 文档](https://www.python-httpx.org/) | 异步 HTTP 客户端（≈ axios，但原生 async） | ✅ 主线 |
| 廖雪峰 asyncio 章节 | 中文对照理解 | 补充 |

**心智模型**：`async/await` 语法和 JS 几乎一致，`asyncio.gather()` ≈ `Promise.all()`，`Semaphore` ≈ `p-limit` 并发限流。**唯一要新学的是"事件循环是显式对象"**（`asyncio.run()` 创建它，JS 里它是隐形的且常驻）。

**验收**：并发抓取 N 个 URL / 批量上报脚本，带并发上限 + 超时 + 重试，对比串行版计时。

## A4 · FastAPI 后端（2 周）⭐ 阶段 A 重头戏

| 资源 | 定位 | 优先级 |
|---|---|---|
| [FastAPI 官方文档](https://fastapi.tiangolo.com/) | **文档质量天花板**，自带交互教程 | ✅ 主线（[中文版](https://fastapi.tiangolo.com/zh/) 也有） |
| [SQLModel 文档](https://sqlmodel.tiangolo.com/) | FastAPI 作者写的 ORM，Pydantic + SQLAlchemy 合一，**上手最快** | ✅ 主线（先它） |
| [SQLAlchemy 2.0 文档](https://docs.sqlalchemy.org/) | 生产级 ORM 事实标准 | ✅ 主线（SQLModel 之后补，只学 2.0 风格） |
| [Alembic 文档](https://alembic.sqlalchemy.org/) | 数据库迁移（≈ Prisma migrate） | ✅ 主线 |
| [redis-py 文档](https://redis.readthedocs.io/) | Redis 客户端，缓存三件套要用 | ✅ 主线 |
| [PyJWT 文档](https://pyjwt.readthedocs.io/) | JWT 鉴权（你做过登录态无感刷新，概念全通） | ✅ 主线 |
| [PostgreSQL 文档](https://www.postgresql.org/docs/) | 需要时查 | 选学（本地用 Docker 起） |
| [Docker 文档](https://docs.docker.com/) | 部署 + 本地起依赖 | ✅ 主线（`docker compose up` 起 PG/Redis） |

**必知概念**（对照 Node 生态）：

| FastAPI 世界 | Node 对照 |
|---|---|
| 路由装饰器 `@app.get()` | Express 路由 / NestJS `@Get()` |
| **依赖注入 Depends()** | Express 中间件（但类型安全、可复用） |
| Pydantic 请求体模型 | zod schema |
| `APIRouter` | Express Router |
| SQLModel / SQLAlchemy | Prisma / TypeORM |
| Alembic | Prisma migrate |
| uvicorn | node 进程本身（ASGI 服务器，≈ Node 的 http server） |

**缓存三件套（JD 点名"缓存方案设计"，必会）**：穿透（查不存在的 key → 布隆过滤器/空值缓存）、击穿（热点 key 过期瞬间 → 互斥锁/逻辑过期）、雪崩（大批 key 同时过期 → 随机 TTL）。

**验收**：`12-fastapi-rum-api/` 跑通 —— 上报接口 + 聚合查询 + Redis 缓存 + JWT 鉴权 + Alembic 迁移 + pytest 测试 + `docker compose up` 一键起。

---

# 阶段 B · LLM 与 Agent

## B1 · LLM API 基础（1 周）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [DeepSeek API 文档](https://api-docs.deepseek.com/) | 国内直连、便宜，本仓库默认接的它 | ✅ 主线（中文） |
| [OpenAI function calling 指南](https://platform.openai.com/docs/guides/function-calling) | 工具调用的标准范式，SDK 全兼容 | ✅ 主线 |
| [智谱 GLM 文档](https://open.bigmodel.cn/dev/api) | 国内备选 | 备选 |
| [通义百炼文档](https://help.aliyun.com/zh/model-studio/) | 国内备选 | 备选 |

**验收**：`20-llm-basics/` 跑通普通对话、流式、function calling、结构化输出（Pydantic 解析）。

## B2 · 裸 agent loop（4 天）⭐ 全程最值钱的一层

| 资源 | 定位 | 优先级 |
|---|---|---|
| [Anthropic《Building Effective Agents》](https://www.anthropic.com/engineering/building-effective-agents) | **Agent 设计第一文**，讲透 workflow vs agent、何时该用啥模式 | ✅ 必读（B2 开工前读一遍，B5 再读一遍） |

**验收**：不用任何框架，手写 ReAct 循环：模型 + 3 个工具（计算器 / 读文件 / HTTP 请求），自主完成多步任务。

## B3 · Agent 框架（2 周）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [OpenAI Agents SDK（Python）](https://openai.github.io/openai-agents-python/) | 最轻量，agents/handoffs/guardrails 概念最直观 | ✅ 第一周入门 |
| [LangGraph 文档](https://langchain-ai.github.io/langgraph/) | 生产事实标准：图状态机编排 | ✅ 第二周深入 |
| [LangChain Academy](https://academy.langchain.com/) | 免费官方课《Introduction to LangGraph》 | ✅ 配合 LangGraph |
| [DeepLearning.AI 短课](https://learn.deeplearning.ai/) | 免费 1-2 小时一门，Agents 系列全值得刷 | 推荐 |

**验收**：LangGraph 写带检查点（可中断恢复）的多步 Agent；能讲清"何时用框架 vs 裸写"。

## B4 · MCP（1 周）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [MCP 官方文档](https://modelcontextprotocol.io/) | 协议本质：Server / Client / Transport | ✅ 主线 |
| [FastMCP 文档](https://gofastmcp.com/) | Python 写 MCP Server 的事实标准，`@mcp.tool()` 即工具 | ✅ 主线 |
| [官方示例 Server 仓库](https://github.com/modelcontextprotocol/servers) | 看别人怎么暴露文件系统/GitHub | ✅ 精读 2-3 个 |

**验收**：把 `12-fastapi-rum-api/` 的查询能力封装成 MCP Server，用任意 MCP Client 实际调通。

## B5 · RAG + 评估 + 上线（1-2 周）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [LlamaIndex 文档](https://docs.llamaindex.ai/) | RAG 主线（数据接入→索引→检索） | ✅ 主线 |
| [LangSmith](https://smith.langchain.com/) | tracing + 评估平台（**从 B1 起就该接上**） | ✅ 工具 |
| [Hugging Face Learn](https://huggingface.co/learn/) | 想深入模型原理时再看 | 选学 |

**验收**：`12-fastapi-rum-api/` 长出 Text2SQL Agent（自然语言问性能问题 → 查库 → 回答），有 tracing、有评估报告、有 SSE 流式前端。

---

# 持续跟进（每天/每周刷）

| 渠道 | 内容 | 频率 |
|---|---|---|
| [Hugging Face 博客](https://huggingface.co/blog) | 开源模型与库的一手动态 | 每周 |
| GitHub Trending（Python + AI 筛选） | 新框架、爆款项目 | 每周 |
| X/Twitter：OpenAI、Anthropic、LangChain、HuggingFace 官号 | 发布第一现场 | 每天 5 分钟 |
| 中文：宝玉推特翻译、量子位 / 机器之心 | 不至于脱节 | 每天 5 分钟 |

# 三条使用纪律

1. **主线优先**：标 ✅ 的看完再碰其他的，收藏 ≠ 学会
2. **文档 > 视频课程 > 书**：这个领域变化太快，官方文档永远最新；视频课只用来省理解成本
3. **每阶段做完验收物再进下一个** —— A 阶段 2 个（CLI、API 服务）+ B 阶段 3 个（裸 agent、LangGraph 项目、MCP Server），加上贯穿项目，简历上是一个完整故事
