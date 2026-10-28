"""01 · 第一个 LLM API 调用

对照 JS：openai 的 Python SDK 和 Node 版几乎一一对应，
client.chat.completions.create ≈ await client.chat.completions.create(...)
区别只有两点：Python 不用 await（同步版），流式用 for 迭代而不是 for await。

运行：uv run 01-llm-basics/main.py
配置：cp .env.example .env 后填入你的 API key
"""

from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
import os

# 加载项目根目录的 .env（对标 Node 的 dotenv.config()）
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

api_key = os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL", "https://api.deepseek.com")  # 任何 OpenAI 兼容服务
model = os.getenv("MODEL", "deepseek-chat")

if not api_key:
    print("未配置 API key：请执行 cp .env.example .env 并填入 key")
    raise SystemExit(0)

client = OpenAI(api_key=api_key, base_url=base_url)

# ---- 1. 普通对话：一次请求一次响应 ----
resp = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "你是一个简洁的编程助教，回答不超过三句话。"},
        {"role": "user", "content": "用一句话解释什么是 function calling"},
    ],
)
print(resp.choices[0].message.content)

# ---- 2. 流式输出：对标 JS 的 SSE / for await ----
print("\n--- 流式 ---")
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "从 1 数到 5，每个数字占一行"}],
    stream=True,
)
for chunk in stream:  # Python 的异步迭代器，思维和 for await 完全一致
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()
