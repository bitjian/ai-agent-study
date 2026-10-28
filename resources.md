# 学习资源库：Python → AI Agent 工程师

> 使用规则：**只看当前层.getResource，别囤积**。每层给"主线"（必学）和"补充"（选学）。
> 链接均于 2026-10-28 实测可访问 ✅

## L1 · Python 语法速成（3-5 天）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [廖雪峰 Python 教程](https://liaoxuefeng.com) | 中文最经典入门，Python3 全套 | ✅ 主线（对照 JS 速读，跳过爬虫/运维章节） |
| [菜鸟教程 Python3](https://www.runoob.com/python3/python3-tutorial.html) | 当字典查语法 | ✅ 查询用 |
| [官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/) | 官方，权威但略枯燥 | 补充 |
| **对照学习法** | 搜 "Python for JavaScript developers" 类对照文章 | 推荐：带着 JS 映射学，速度×3 |

**验收**：`cli` 目录写一个日志分析 CLI（读文件、dict 统计、f-string 输出）。

## L2 · Python 工程化（1 周）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [uv 官方文档](https://docs.astral.sh/uv/) | 包管理主线，对照 README 里的 pnpm 对照表看 | ✅ 主线 |
| [Pydantic 文档](https://docs.pydantic.dev/latest/) | 数据校验（= zod），Agent 生态地基 | ✅ 主线 |
| [Real Python](https://realpython.com/) | 英文最佳教程站（asyncio、装饰器专题质量极高） | 推荐（403 是反爬，浏览器可开） |
| pytest 官方文档 | 测试（到用时再查） | 选学 |

**验收**：给 L1 的 CLI 加类型注解 + Pydantic 模型 + pytest 单测。

## L3 · LLM API 与裸 Agent（1 周）⭐ 最重要的一层

| 资源 | 定位 | 优先级 |
|---|---|---|
| [DeepSeek API 文档](https://api-docs.deepseek.com/) | 国内直连、便宜，本仓库默认接的它 | ✅ 主线（中文） |
| [智谱 GLM API 文档](https://open.bigmodel.cn/dev/api) | 国内备选 | 备选 |
| [通义百炼文档](https://help.aliyun.com/zh/model-studio/) | 国内备选（qwen 系列） | 备选 |
| [OpenAI function calling 指南](https://platform.openai.com/docs/guides/function-calling) | 工具调用的标准范式（SDK 全兼容） | ✅ 主线 |
| [Anthropic《Building Effective Agents》](https://www.anthropic.com/engineering/building-effective-agents) | **Agent 设计第一文**，讲透 workflow vs agent、何时该用啥模式 | ✅ 必读（L3 开工前读一遍，L6 再读一遍） |

**验收**：`agent-loop/` 不用任何框架，手写 ReAct 循环：模型 + 3 个工具（计算器/读文件/HTTP 请求）自主完成多步任务。

## L4 · Agent 框架（2 周）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [OpenAI Agents SDK（Python）](https://openai.github.io/openai-agents-python/) | 最轻量，agents/handoffs/guardrails 概念最直观 | ✅ 第一周入门 |
| [LangGraph 文档](https://langchain-ai.github.io/langgraph/) | 生产事实标准：图状态机编排 | ✅ 第二周深入 |
| [LangChain Academy](https://academy.langchain.com/) | 免费官方课程《Introduction to LangGraph》 | ✅ 配合 LangGraph |
| [DeepLearning.AI 短课](https://learn.deeplearning.ai/) | 免费、1-2 小时一门：Agents 系列课全值得刷 | 推荐 |

**验收**：LangGraph 写一个带检查点（可中断恢复）的多步 Agent；能讲清"何时该用框架 vs 裸写"。

## L5 · MCP（1 周）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [MCP 官方文档](https://modelcontextprotocol.io/) | 协议本质：Server/Client/Transport 三概念 | ✅ 主线 |
| [FastMCP 文档](https://gofastmcp.com/) | Python 写 MCP Server 的事实标准，`@mcp.tool()` 即工具 | ✅ 主线 |
| [官方示例 Server 仓库](https://github.com/modelcontextprotocol/servers) | 看别人怎么暴露文件系统/GitHub 等工具 | ✅ 精读 2-3 个 |

**验收**：把自己的一个常用 API 封装成 MCP Server，用 Claude/任意 MCP Client 实际调用成功。

## L6 · 进阶与上线（1-2 周）

| 资源 | 定位 | 优先级 |
|---|---|---|
| [FastAPI 官方文档](https://fastapi.tiangolo.com/) | 质量天花板级教程，Agent 服务出口 | ✅ 主线 |
| [LlamaIndex 文档](https://docs.llamaindex.ai/) | RAG 主线（数据接入→索引→检索） | ✅ 主线 |
| [LangSmith](https://smith.langchain.com/) | tracing + 评估平台（从 L3 起就接上） | ✅ 工具 |
| [Hugging Face Learn](https://huggingface.co/learn/) | 想深入模型原理时再看 | 选学 |

**验收**：完整 Agent（RAG + 工具 + 流式）经 FastAPI 上线，有 tracing 和评估报告。

## 持续跟进（每天/每周刷）

| 渠道 | 内容 | 频率 |
|---|---|---|
| [Hugging Face 博客](https://huggingface.co/blog) | 开源模型与库的一手动态 | 每周 |
| GitHub Trending（Python + AI 筛选） | 新框架、爆款项目 | 每周 |
| X/Twitter：关注 OpenAI、Anthropic、LangChain、HuggingFace 官号 | 发布第一现场 | 每天 5 分钟 |
| 中文：宝玉（推特征翻译）、量子位/机器之心 | 不至于脱节 | 每天 5 分钟 |

## 三条使用纪律

1. **主线优先**：标 ✅ 的看完再碰其他的，收藏 ≠ 学会
2. **文档 > 视频课程 > 书**：这个领域变化太快，官方文档永远最新；视频课只用来省理解成本（如 LangGraph Academy）
3. **每层做完验收物再进下一层**，验收物就是你的简历项目，学完 8 周你手里会有 4 个可展示的 repo
