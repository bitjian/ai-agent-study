# AI Agent 学习工作空间（Python · Agent 工程师路线）

> 目标：8 周兼职达到 Agent 开发求职能力；3-4 周出第一个能跑的 Agent。
> 前置优势：JS/Node 全栈 + React 流式经验（Agent UI 层、SSE 是明确加分项）。
> 姊妹仓库：`~/bitjian/go-study`（Go 路线暂停，环境保留）。

## 六层技能栈进度（从底往上，别跳层）

| 层 | 内容 | 验收物 | 状态 |
|---|---|---|---|
| L1 | Python 语法（对照 JS 速成，跳过爬虫/运维） | CLI 小工具 | ⬜ |
| L2 | uv / 类型注解 / Pydantic / asyncio / pytest | 给 CLI 补类型+单测 | ⬜ |
| L3 | LLM API：function calling、流式、结构化输出；**手写裸 agent loop** | 不用框架的 ReAct 小 Agent | ⬜ |
| L4 | 框架：OpenAI Agents SDK 入门 → **LangGraph** 深入 | 带状态、可恢复的多步 Agent | ⬜ |
| L5 | MCP：FastMCP 写 Server、Client 调用、权限收敛 | 自研 MCP Server（可开源） | ⬜ |
| L6 | RAG、评估（LLM-as-a-Judge）、tracing、FastAPI 部署 | Agent 上线 + 评估报告 | ⬜ |

## 目录

- `glossary.md` — **术语对照手册**（Python/Agent 生态 ↔ JS/Node，常查常新）
- `resources.md` — **学习资源库**（按六层组织，链接已实测可访问）
- `01-llm-basics/` — 第一个 LLM 调用 + 流式（L3 热身，先跑通感知一下）

## 命令速查（uv 对标 pnpm）

```bash
uv run <script.py>        # 运行（自动处理 venv，对标 pnpm exec）
uv add <pkg>              # 加依赖（对标 pnpm add）
uv remove <pkg>           # 删依赖
uv sync                   # 按 lockfile 装依赖（对标 pnpm i）
uv python pin 3.13        # 锁定 Python 版本（对标 engines）
uv tool install <tool>    # 全局 CLI 工具（对标 npx/globals）
```

国内加速：装包慢时加 `UV_DEFAULT_INDEX=https://pypi.tuna.tsinghua.edu.cn/simple`（本项目依赖已按此装好）。

## LLM 接入

`cp .env.example .env` 填 key。默认 DeepSeek（国内直连、便宜），任何 OpenAI 兼容服务改 `BASE_URL`/`MODEL` 即可（通义/智谱/OpenAI 模板都写在 `.env.example` 里）。

## 学习资源

| 资源 | 用途 |
|---|---|
| 廖雪峰 Python 教程 / 菜鸟教程 Python3 | L1 语法速成（中文） |
| Anthropic《Building Effective Agents》 | L3 必读，Agent 设计第一文 |
| OpenAI Agents SDK 文档 → LangGraph 官方教程 | L4 主线 |
| [FastMCP 文档（gofastmcp.com）](https://gofastmcp.com) | L5 写 MCP Server |
| 各框架 tracing（LangSmith / OTel） | 从 L3 起就开着 |

## 避坑（真实教训）

- 先手写裸 agent loop 再上框架，否则调试框架魔法会怀疑人生
- 别框架跳跃：一个框架 3 个项目 > 六个框架各跑 demo
- AutoGen 已归档，网上老教程别跟
- 单 Agent 先行，第一天就算 token 成本、开 tracing
