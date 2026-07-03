"""
快速体验 — AI 对话

获取 API Key: https://share.acedata.cloud/r/1uNf1ozr78
"""

import os
from acedata import AceDataClient

# 从环境变量读取 Key（推荐）或直接填入
API_KEY = os.getenv("ACEDATA_API_KEY", "your_api_key_here")

client = AceDataClient(api_key=API_KEY)

# 对话
response = client.chat(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "你是一个有帮助的助手"},
        {"role": "user", "content": "用三句话介绍量子计算"},
    ],
)

print(response["choices"][0]["message"]["content"])

# 流式对话
print("\n--- 流式输出 ---")
for token in client.chat_stream(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "写一首关于秋天的俳句"}],
):
    print(token, end="", flush=True)
print()
