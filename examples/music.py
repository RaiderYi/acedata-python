"""
AI 音乐生成示例 (Suno)

支持模型: chirp-v5-5, chirp-v4-5, chirp-v4 等
获取 API Key: https://share.acedata.cloud/r/1uNf1ozr78
"""

import os
from acedata import AceDataClient

API_KEY = os.getenv("ACEDATA_API_KEY", "your_api_key_here")

client = AceDataClient(api_key=API_KEY)

# 灵感模式 — 只需给一句话描述
result = client.music(
    prompt="An upbeat jazz song about walking through autumn leaves in the park",
    model="chirp-v5-5",
    custom=False,
)
print("灵感模式结果:")
print(f"  任务 ID: {result.get('id', '')}")
print(f"  状态: {result.get('status', '')}")

# 自定义模式 — 指定标题、风格、歌词
print("\n--- 自定义模式 ---")
custom_result = client.music(
    model="chirp-v5-5",
    custom=True,
    title="Neon Dreams",
    style="synthwave, retro 80s, dreamy",
    lyric="""[Verse]
Walking through the neon lights
City never sleeps tonight
[Chorus]
We are the dreamers of the night
Dancing in the electric light""",
)
print(f"  任务 ID: {custom_result.get('id', '')}")

# 查询结果
if custom_result.get("id"):
    import time
    print("\n等待生成（约 30-60 秒）...")
    time.sleep(30)
    feed = client._request("GET", f"/feed/{custom_result['id']}")
    for clip in feed.get("clips", []):
        print(f"  歌曲: {clip.get('title', '')}")
        print(f"  音频: {clip.get('audio_url', '')}")
        print(f"  封面: {clip.get('image_url', '')}")
