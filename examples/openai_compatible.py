"""
OpenAI SDK 兼容模式 — 零改动迁移

获取 API Key: https://share.acedata.cloud/r/1uNf1ozr78
"""

import os
from openai import OpenAI

# 方式一：直接用 OpenAI SDK，只需改 base_url 和 api_key
client = OpenAI(
    api_key=os.getenv("ACEDATA_API_KEY", "your_api_key_here"),
    base_url="https://api.acedata.cloud/v1",
)

# 就这么简单，后面跟 OpenAI SDK 用法完全一样
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "用 Python 写一个快速排序"},
    ],
    max_tokens=2048,
)

print(response.choices[0].message.content)

# 也支持 Claude / Gemini / DeepSeek / Grok 等模型，改 model 名即可
print("\n--- DeepSeek 模型 ---")
response2 = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "一句话解释什么是 RAG"}],
)
print(response2.choices[0].message.content)

# 图片生成也兼容
print("\n--- 图片生成 ---")
img = client.images.generate(
    model="flux-1-schnell",
    prompt="watercolor painting of Mount Fuji in spring",
    size="1024x1024",
)
print(f"图片地址: {img.data[0].url}")
