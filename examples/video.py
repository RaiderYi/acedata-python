"""
AI 视频生成示例

支持模型: veo-3, sora, kling, luma, hailuo, seedance 等
获取 API Key: https://share.acedata.cloud/r/1uNf1ozr78
"""

import os
from acedata import AceDataClient

API_KEY = os.getenv("ACEDATA_API_KEY", "your_api_key_here")

client = AceDataClient(api_key=API_KEY)

# Veo 3 — Google 最新视频生成
result = client.video(
    model="veo-3",
    prompt="A cinematic drone shot over a misty mountain range at sunrise, golden light breaking through clouds",
    duration=5,
)
print("Veo 3 结果:")
print(f"  任务 ID: {result.get('id', '')}")
print(f"  状态: {result.get('status', '')}")

# Kling — 快速生成
print("\n--- Kling 视频 ---")
kling = client.video(
    model="kling",
    prompt="A koi fish swimming in a pond with lotus flowers, slow motion, underwater camera",
    duration=5,
)
print(f"  任务 ID: {kling.get('id', '')}")

# 查询结果（视频生成需要等待）
import time

task_id = result.get("id")
if task_id:
    print("\n等待生成中（视频生成约需 1-3 分钟）...")
    for _ in range(6):
        time.sleep(30)
        feed = client._request("GET", f"/videos/{task_id}")
        status = feed.get("status", "")
        print(f"  状态: {status}")
        if status in ("succeeded", "completed"):
            video_url = feed.get("url", "") or feed.get("video_url", "")
            print(f"  视频地址: {video_url}")
            break
