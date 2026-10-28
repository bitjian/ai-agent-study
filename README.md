# AI Agent 学习工作空间（Python 后端 → Agent 两阶段路线）

> 目标：**先补齐 Python 后端能力，再做 Agent**。总计 8-10 周兼职（每天 1.5-2h）。
> 前置优势：JS/Node 全栈 + React 流式经验（Agent UI 层、SSE 是明确加分项）。
> 姊妹仓库：`~/bitjian/go-study`（Go 路线暂停，环境保留）。

## 为什么改成两阶段（2026-10-28 调整）

Agent 服务的本质**就是一个后端服务**：HTTP 接口、SSE 流式输出、鉴权、限流、日志、数据库、Docker 部署——这些全在后端，一个都躲不掉。
先补后端，再做 Agent 时你只需要在**已经跑通的服务上长出一个 LLM 大脑**，而不用同时面对"Python 语法 + 异步 + FastAPI + LLM + 框架"五座大山。

三条硬理由：

1. **FastAPI 是 Agent 的标准出口** —— 你最终交付的 Agent 就是 `/v1/chat` 这种接口，先会写接口，Agent 阶段只专注 LLM 部分
2. **贯穿项目不重写** —— 后端骨架直接长成 Agent 产品，简历上是一个完整故事，而不是两个互不相干的 demo
3. **对齐 JD** —— 目标岗位要求"后端为重点、Go/Python 写服务、数据库/缓存/消息队列方案设计"，阶段 A 正好逐条命中

## 阶段 A · Python + 后端工程（4-5 周）

| # | 主题 | 学什么 | 验收物 | 状态 |
|---|---|---|---|---|
| A1 | **Python 语法**（5-7 天） | 对照 JS：dict/list/切片、f-string、装饰器、`with`、异常、类 | `10-python-cli/` 日志分析 CLI | ⬜ |
| A2 | **工程化**（5 天） | uv、类型注解、Pydantic（≈zod）、pytest、ruff | 给 CLI 补类型 + 单测 | ⬜ |
| A3 | **异步编程**（4 天） | asyncio / `gather` / Semaphore、httpx；对照 `Promise.all` | 并发批量上报脚本 | ⬜ |
| A4 | **FastAPI 后端**（2 周） | 路由、依赖注入、中间件、JWT 鉴权、SQLModel/SQLAlchemy、Alembic 迁移、Redis 缓存、Docker | `12-fastapi-rum-api/` 可跑的服务 | ⬜ |

**A 阶段终点**：一个完整的 REST 服务——能收数据、落库、查接口、有鉴权、有缓存、有测试、`docker compose up` 能起。

### 贯穿项目：`12-fastapi-rum-api/`（RUM 性能数据服务）

选它是因为你手上就有业务素材（RUM 性能监控），面试时能讲真实场景：

```
POST /v1/rum/report      接收前端性能上报（Pydantic 校验）
GET  /v1/rum/stats       聚合查询（LCP/CLS 分位数、按页面/地区）
GET  /v1/rum/slow-pages  慢页面 Top N
      → Redis 缓存热点查询 → PostgreSQL/MySQL 落库 → Alembic 管迁移
```

阶段 B 时，在这个服务上加一层 LLM：**自然语言提问 → Text2SQL → 查库 → 回答**，直接进化成「RUM 性能分析助手」。一个仓库两段故事。

## 阶段 B · LLM 与 Agent（4-5 周）

| # | 主题 | 学什么 | 验收物 | 状态 |
|---|---|---|---|---|
| B1 | **LLM API**（1 周） | chat completions、function calling、流式 SSE、结构化输出、token 成本 | `20-llm-basics/` | ⬜ |
| B2 | **裸 agent loop**（4 天）⭐ | 不用框架手写 ReAct：思考→调工具→读结果→再思考 | 自主多步任务的 Agent | ⬜ |
| B3 | **框架**（2 周） | OpenAI Agents SDK 入门 → **LangGraph** 深入（图状态机） | 带检查点、可恢复的 Agent | ⬜ |
| B4 | **MCP**（1 周） | FastMCP 写 Server、Client 调用、权限收敛 | 自研 MCP Server（可开源） | ⬜ |
| B5 | **RAG + 评估 + 上线**（1-2 周） | embedding/向量库、LLM-as-a-Judge、LangSmith tracing、挂到 A 阶段的 FastAPI | Agent 上线 + 评估报告 | ⬜ |

**B 阶段终点**：`12-fastapi-rum-api/` 里长出一个能对话的 Agent，有 tracing、有评估、有前端流式界面（你的强项）。

## 目录

| 路径 | 阶段 | 内容 |
|---|---|---|
| `glossary.md` | 全程 | 术语对照手册（Python/后端/Agent ↔ JS/Node），含**运行时与执行模型**一节 |
| `resources.md` | 全程 | 学习资源库（按 A/B 两阶段组织，链接已实测） |
| `10-python-cli/` | A1-A2 | 语法练习 + CLI 小工具 |
| `11-async-http/` | A3 | asyncio + httpx 并发 |
| `12-fastapi-rum-api/` | A4 → B5 | **贯穿项目**：后端服务 → 长成 Agent |
| `20-llm-basics/` | B1 | 第一个 LLM 调用 + 流式 |
| `python/` | — | 随手练习（hello.py 等） |

## 命令速查（uv 对标 pnpm）

```bash
uv run <script.py>        # 运行（自动处理 venv，对标 pnpm exec）
uv add <pkg>              # 加依赖（对标 pnpm add）
uv remove <pkg>           # 删依赖
uv sync                   # 按 lockfile 装依赖（对标 pnpm i）
uv python pin 3.13        # 锁定 Python 版本（对标 engines）
uv tool install <tool>    # 全局 CLI 工具（对标 npx/globals）
```

A4 会用到的后端命令：

```bash
uv run uvicorn app.main:app --reload    # 起 FastAPI（对标 next dev）
uv run pytest                           # 跑测试
uv run alembic revision --autogenerate -m "xxx" && uv run alembic upgrade head   # 迁移
docker compose up -d                    # 起 Postgres + Redis
```

国内加速：装包慢时加 `UV_DEFAULT_INDEX=https://pypi.tuna.tsinghua.edu.cn/simple`（本项目依赖已按此装好）。

## LLM 接入（阶段 B 再用，现在不用管）

`cp .env.example .env` 填 key。默认 DeepSeek（国内直连、便宜），任何 OpenAI 兼容服务改 `BASE_URL`/`MODEL` 即可。

## 避坑

**阶段 A**
- 别用 `requests`，用 `httpx`（原生支持 async，Agent/后端生态都是它）
- 装包一律 `uv add`，别用 `pip install`（venv 混乱的头号原因）
- SQLAlchemy **直接学 2.0 风格**（`Mapped[]` + `session.execute(select(...))`），网上 1.x 的老写法满地都是
- 类型注解从 A1 就写，别等补——Python 没类型等于 JS 没 TS，重构时你会想死

**阶段 B**
- 先手写裸 agent loop 再上框架，否则调试框架魔法会怀疑人生
- 别框架跳跃：一个框架 3 个项目 > 六个框架各跑 demo
- AutoGen 已归档，网上老教程别跟
- 单 Agent 先行，第一天就开 tracing、算 token 成本
