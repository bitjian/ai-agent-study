# 术语对照手册：Python / Agent 生态 ↔ JS/Node 生态

> 用法：学到一个新词就来这查它的"JS 翻译"。持续补充，按层分组。

## 一、包管理与工具链

| Python 世界 | 是什么 | JS/Node 对照 |
|---|---|---|
| **uv** | Rust 写的全能包管理器（事实标准） | pnpm |
| **pip** | 老牌装包工具（被 uv 取代中） | npm（老旧版） |
| **venv / 虚拟环境** | 项目独立的依赖目录，避免全局污染 | `node_modules/` 的隔离思想 |
| **pyproject.toml** | 项目声明文件（依赖、元数据、工具配置） | package.json |
| **uv.lock** | 精确锁版本，保证可复现 | pnpm-lock.yaml |
| **uvx / pipx** | 临时运行 CLI 工具不装全局 | npx |
| **PyPI** | Python 官方包仓库 | npm registry |
| **镜像源**（清华/阿里） | 国内加速下载 | taobao registry / npmmirror |
| **wheels / sdist** | 预编译包 / 源码包 | npm 里没直接对应（类似 prebuilt binary） |

## 二、语言核心（对照 JS 语法）

| Python | 是什么 | JS/Node 对照 | 记忆点 |
|---|---|---|---|
| **list** `[1,2]` | 有序可变数组 | Array | 通用容器 |
| **dict** `{"a":1}` | 键值对 | Object / Map | 最常用，JSON 天然互转 |
| **tuple** `(1,2)` | 不可变数组 | 只读数组 | 函数多返回值 `return a, b` 就是 tuple |
| **set** `{1,2}` | 去重集合 | Set | 交集并集直接用运算符 |
| **None** | 空值 | null / undefined 合体 | 判断用 `is None` |
| **f-string** `f"{x}"` | 字符串插值 | 模板字符串 `` `${x}` `` | 优先用它 |
| **切片** `a[1:3]`、`a[::-1]` | 子数组 / 反转 | `slice()` / `reverse()` | 切片是语言级语法 |
| **解构** `a, b = b, a` | 多变量赋值/交换 | 数组解构 | 交换变量一行搞定 |
| **装饰器** `@decorator` | 包装函数/方法，加行为 | 高阶函数 + `@decorator` 语法糖（实验性） | Agent 框架里 `@tool`、`@mcp.tool()` 全靠它 |
| **生成器** `yield` | 惰性逐个产出值 | generator 函数（function* + yield） | 流式处理的核心 |
| **上下文管理器** `with open(f)` | 自动清理资源 | 没有直接对应（≈ try-finally 的语法糖） | `with` = 自动 close |
| ***args / \*\*kwargs** | 可变参数 / 关键字参数 | rest 参数 / 展开传参 | `f(*list)` ≈ `f(...list)` |
| **类型注解** `def f(x: int) -> str` | 标类型，运行时不强制 | TypeScript（但 TS 会编译期查，Python 默认只标注） | 配 mypy/pyright 才有 TS 体验 |
| **dataclass / Pydantic BaseModel** | 声明式数据结构 + 校验 | zod schema / class | Pydantic ≈ zod，Agent 生态基石 |
| **异常** `try/except/raise/finally` | 错误处理 | try/catch/throw/finally | 几乎一一对应 |
| **模块导入** `import x` / `from x import y` | 导入 | import / 具名导入 | 区别：文件即模块，无需 export 关键字 |

## 三、异步编程（思维完全一致，换套关键词）

| Python | JS/Node 对照 | 记忆点 |
|---|---|---|
| `async def` | `async function` | 一样 |
| `await` | `await` | 一样 |
| **asyncio**（事件循环） | Node 事件循环 / libuv | 单线程协作式并发 |
| `asyncio.gather(*tasks)` | `Promise.all([...])` | 并发跑一批 |
| `asyncio.create_task(coro)` | 不 await 的 promise 启动 | 后台先跑着 |
| `asyncio.Semaphore` / `gather` 限流 | p-limit / 并发池 | 控并发数 |
| `async for` / `async with` | `for await` | 异步迭代 |
| 同步库阻塞问题 | —— | Python 大量老库是同步的，Agent 代码注意用异步版（如 `httpx.AsyncClient` vs `requests`） |

## 四、工程化与质量

| Python | JS/Node 对照 | 说明 |
|---|---|---|
| **ruff** | ESLint + Prettier 合体（同一家出的，极快） | lint + format 一个工具 |
| **pyright / mypy** | tsc（类型检查） | VS Code 默认用 pyright |
| **pytest** | vitest / jest | 测试框架，`assert` 风格更直白 |
| **python-dotenv** | dotenv | 一模一样 |
| **REPL** `python` / `uv run python` | `node` 交互式 | 探索 API 神器 |
| **GIL** | —— | 全局锁：同一进程多线程不能并行跑 Python 字节码；并发用 asyncio 或多进程（Node 同学可理解为"永远单线程"的强约束版） |

## 五、LLM API 层

| 术语 | 是什么 | JS 对照/备注 |
|---|---|---|
| **chat completions** | 对话补全接口（消息数组进出） | openai SDK 的 Node/Python 版同名方法 |
| **token** | 模型计费与长度单位，≈0.75 个英文单词 / 0.5 个汉字 | 无对应，但直接决定成本和上限 |
| **context window（上下文窗口）** | 模型一次能"看见"的最大 token 数 | 超了就报错或要裁剪——前端同学可类比"内存限制" |
| **system prompt** | 设定角色与规则的最高优先级消息 | `messages[0].role === "system"` |
| **多轮对话** | 把历史 messages 原样传回，模型才"记得" | 模型无状态，记忆全靠你带上下文 |
| **function calling / tool use** | 模型输出"我要调某函数+参数 JSON"，你执行后把结果喂回去 | 这是 Agent 的发动机 |
| **结构化输出** | 强制模型按 JSON Schema 返回（配 Pydantic 校验） | zod parse 的 AI 版 |
| **流式输出（SSE）** | token 逐段返回 | 你熟的 SSE，`for chunk in stream` ≈ `for await` |
| **embedding** | 文本 → 向量，语义相近则向量相近 | RAG 的地基 |
| **temperature / top_p** | 随机度旋钮：低=稳定，高=发散 | 无对应，记住 0~2 即可 |

## 六、Agent 层（新概念居多，无 JS 对应）

| 术语 | 一句话解释 |
|---|---|
| **agent loop（Agent 循环）** | 核心中的核心：模型思考 → 调工具 → 读结果 → 再思考 → …直到任务完成。先手写一遍再上框架 |
| **ReAct** | 经典循环模式：Reason（想）+ Act（做）交替进行 |
| **Plan-and-Execute** | 先列计划再逐步执行，适合长任务 |
| **工具（tool）** | 暴露给模型的能力：一个带 schema 的函数（查库、调 API、读写文件） |
| **LangGraph** | 生产级 Agent 编排框架：Agent = 图（节点=动作，边=流转），对标前端状态机的思维 |
| **OpenAI Agents SDK** | 轻量 Agent 框架，入门最简单 |
| **handoff（交接）** | 多 Agent 协作模式：A 干不下去了把控制权交给 B |
| **记忆（memory）** | 短期=对话内上下文；长期=存库按需检索 |
| **RAG（检索增强生成）** | 先从知识库检索相关片段，塞进上下文再让模型回答——"开卷考试" |
| **向量库**（FAISS/Qdrant/Milvus） | 存 embedding、按语义相似度检索的数据库 |
| **MCP（Model Context Protocol）** | Agent 连接外部工具的开放标准；**MCP Server**=暴露工具的服务，**MCP Client**=Agent 侧的连接器。类比：MCP 之于 Agent ≈ REST 之于 Web |
| **FastMCP** | Python 写 MCP Server 最流行的库，`@mcp.tool()` 装饰器即工具 |
| **guardrails（护栏）** | 限制 Agent 能做什么：权限收敛、输入校验、输出审查 |
| **human-in-the-loop** | 关键操作前插入人工审批 |
| **多 Agent（multi-agent）** | 多个 Agent 分工协作（别急着学，单 Agent 先跑通） |
| **tracing / 可观测** | 记录 Agent 每步做了什么（LangSmith/OTel），调试全靠它 |
| **评估（evals）** | 量化 Agent 好不好用：**LLM-as-a-Judge**=让另一个模型当裁判 |
| **幻觉（hallucination）** | 模型一本正经地编造事实；RAG/工具调用是主要解法 |
| **prompt injection（提示注入）** | 用户/数据里藏指令劫持 Agent——Agent 时代的"XSS"，安全面试常考 |

## 七、Web 与部署层

| Python | JS/Node 对照 | 说明 |
|---|---|---|
| **FastAPI** | Express / Fastify（但自带类型校验+自动文档） | Agent 服务出口标配，原生支持 async |
| **Uvicorn** | Node 进程本身（ASGI 服务器） | 跑 FastAPI 的服务器 |
| **Pydantic 做请求校验** | zod + Express 中间件 | FastAPI 里声明即校验 |
| **Docker** | 一样 | Agent 上线标配，你 Go 学的 Docker 知识直接复用 |
| **SSE / WebSocket** | 一样 | Agent 流式输出的传输层，你的前端强项 |

## 八、运行时与执行模型（底层认知）

**核心校正：`python` 命令 ↔ `node` 命令（同层）；`PVM` ↔ `V8`（同层）。** 把 V8 和「Python 解释器」并列是错了一层。

| 概念 | 是什么 | JS/Node 对照 | 说明 |
|---|---|---|---|
| **语言规范** | 纸面标准，不是软件 | ECMAScript 规范 | Python 语言规范；都可有多种实现 |
| **CPython** | Python 的官方实现（用 C 写的），就是 `python` 命令 | **Node.js 运行时** | 既是引擎又是运行时：含 PVM + 标准库 + GC + GIL |
| **PVM（Python 虚拟机）** | 逐条解释字节码的 C 循环（`ceval.c`） | **V8 引擎** | 只是执行引擎，不是完整运行时 |
| **字节码（.pyc）** | 源码编译后的虚拟机指令，缓存在 `__pycache__/` | V8 的 Ignition 字节码 | **Python 是栈式**（push/pop），**V8 是寄存器式**（`Star r22`） |
| **AST** | 语法树 | 一样 | 两者前两步（源码→AST→字节码）几乎相同 |
| **TurboFan** | 不存在于 CPython | V8 的 JIT 编译器 | 热点函数被编译成**真机器码**，这是 V8 快一个量级的原因 |
| **PyPy** | 带 JIT 的 Python 实现 | 类似 V8 的思路 | 纯计算能快 5-10 倍，但生态兼容性不如 CPython |
| **GIL（全局解释器锁）** | 同一进程内只允许一个线程执行字节码 | 对照：Node 单线程事件循环 | CPU 密集用**多进程**绕开（`ProcessPoolExecutor`），不是多线程 |
| **libuv** | 不存在于 CPython | Node 的异步 IO 底层库 | Python 对应 asyncio（单线程事件循环，同思路） |

### 执行流水线分叉点

```
Python:  .py → AST → .pyc 字节码 → PVM 逐条解释 ──────────→ CPU（全程无机器码）
JS:      .js → AST → Ignition 字节码 → TurboFan JIT 机器码 → CPU
```

本机实测（1 亿次整数累加，M 系 Mac）：Python 3.13 耗时 4.24s，Node 22 耗时 0.55s，约 8 倍差距。

**对 Agent 开发的影响：几乎为零。** 瓶颈是 LLM API 的网络等待（秒级），解释器差异（毫秒级）完全淹没。重计算由 numpy/向量库等 C 扩展承担。

### 可复现的验证命令

```bash
# Python 字节码
python -c "import dis; dis.dis(lambda a, b: a + b)"
python -c "import sys; print(sys.implementation, sys._is_gil_enabled())"

# V8 字节码与 JIT
node --print-bytecode -e "function add(a,b){return a+b}; add(1,2)"
node --trace-opt -e "function add(a,b){return a+b}; for(let i=0;i<2e5;i++) add(i,1)"
```

## 使用建议

1. 每天学到新词，回来补一行——这份表就是你的"外语词典"
2. 优先记**第五、六节**：那是 Agent 岗面试的高频词
3. 发现某个词理解模糊时，最好的验证方式是去 `01-llm-basics/` 写个 10 行的小实验
