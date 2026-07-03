"""
AI 图片生成示例

支持模型: flux-1-schnell, flux-1-dev, midjourney, seedream 等
获取 API Key: https://share.acedata.cloud/r/1uNf1ozr78
"""

import os
from acedata import AceDataClient

API_KEY = os.getenv("ACEDATA_API_KEY", "your_api_key_here")

client = AceDataClient(api_key=API_KEY)

# FLUX 快速出图
result = client.image(
    model="flux-1-schnell",
    prompt="a cute orange cat sitting on a windowsill, warm sunlight, photorealistic",
    size="1024x1024",
)

# 打印图片 URL
for item in result.get("data", []):
    url = item.get("url", "")
    print(f"图片 URL: {url}")

# 批量生成 (n=4)
print("\n--- 批量生成 4 张 ---")
batch = client.image(
    model="flux-1-dev",
    prompt="cyberpunk city at night, neon lights, rain reflections",
    size="1024x1024",
    n=4,
)
for i, item in enumerate(batch.get("data", [])):
    print(f"  图 {i+1}: {item.get('url', '')}")
