<div align="center">

<h1>🚀 AceData Python SDK</h1>

**一个 API Key，访问所有 AI 服务** — GPT / Claude / Gemini / DeepSeek / Grok / Suno / Midjourney / Veo / Kling

中文 | [English](./README_EN.md)

</div>

## ✨ 为什么用 AceData Cloud

- **统一接口**：一个 Key、一个 Base URL，调用 50+ 模型
- **按量付费**：无需订阅，用多少付多少，比官方便宜
- **OpenAI 兼容**：直接换 `base_url` 即可迁移，零改动
- **全模态覆盖**：对话、图片、音乐、视频、嵌入向量
- **高可用**：全球 CDN 加速，99.9% 可用性

## 🔑 获取 API Key

> **第一步**：前往 AceData Cloud 注册并获取 API Key
>
> 👉 **[点击注册获取 Key](https://share.acedata.cloud/r/1uNf1ozr78)**

注册后在 [控制台](https://platform.acedata.cloud/console) 复制你的 API Key。

## 📦 安装

```bash
pip install -e .
# 或直接安装依赖
pip install requests
```

## 🚀 快速开始

```python
from acedata import AceDataClient

# 获取 Key: https://share.acedata.cloud/r/1uNf1ozr78
client = AceDataClient(api_key="your_api_key")

# AI 对话
response = client.chat(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "你好"}],
)
print(response["choices"][0]["message"]["content"])
```

## 🔧 OpenAI SDK 兼容（零改动迁移）

已有 OpenAI 项目？只需改两行：

```python
from openai import OpenAI

client = OpenAI(
    api_key="your_acedata_key",          # ← 换成 AceData Key
    base_url="https://api.acedata.cloud/v1",  # ← 换成 AceData URL
)

# 后面完全一样
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello!"}],
)
```

## 📖 功能一览

### AI 对话

支持 `gpt-4o` / `gpt-4o-mini` / `claude-3.5-sonnet` / `gemini-2.0-flash` / `deepseek-chat` / `grok-2` 等

```python
# 普通对话
response = client.chat(model="gpt-4o", messages=[...])

# 流式对话
for token in client.chat_stream(model="gpt-4o", messages=[...]):
    print(token, end="", flush=True)
```

### AI 图片生成

支持 `flux-1-schnell` / `flux-1-dev` / `midjourney` / `seedream` 等

```python
result = client.image(
    model="flux-1-schnell",
    prompt="a cute cat in watercolor style",
    size="1024x1024",
)
print(result["data"][0]["url"])
```

### AI 音乐生成 (Suno)

支持 `chirp-v5-5` / `chirp-v4-5` / `chirp-v4` 等

```python
# 灵感模式
song = client.music(prompt="A jazz song about autumn rain")

# 自定义模式（指定歌词、风格、标题）
song = client.music(
    custom=True,
    title="Neon Dreams",
    style="synthwave, retro 80s",
    lyric="[Verse]\nWalking through neon lights...",
)
```

### AI 视频生成

支持 `veo-3` / `sora` / `kling` / `luma` / `hailuo` / `seedance` 等

```python
video = client.video(
    model="veo-3",
    prompt="sunset over the ocean, cinematic",
    duration=5,
)
```

### 文本嵌入

```python
embedding = client.embeddings(
    model="text-embedding-3-large",
    input="这是一段需要向量化的文本",
)
```

## 🌐 可用模型（部分）

| 类型 | 模型 | 说明 |
|------|------|------|
| 对话 | gpt-4o, gpt-4o-mini | OpenAI 旗舰 |
| 对话 | claude-3.5-sonnet, claude-3-opus | Anthropic |
| 对话 | gemini-2.0-flash, gemini-2.0-pro | Google |
| 对话 | deepseek-chat, deepseek-reasoner | DeepSeek |
| 对话 | grok-2 | xAI |
| 图片 | flux-1-schnell, flux-1-dev | FLUX 系列 |
| 图片 | midjourney | Midjourney |
| 图片 | seedream | 字节跳动 |
| 音乐 | chirp-v5-5, chirp-v4-5 | Suno |
| 视频 | veo-3 | Google Veo |
| 视频 | sora | OpenAI Sora |
| 视频 | kling | 快手可灵 |
| 视频 | luma, hailuo, seedance | 其他视频模型 |

> 完整模型列表请查看 [模型页面](https://platform.acedata.cloud/models)

## 💰 定价

按量付费，无需订阅。比官方 API 价格更优。

持有 $ACE 代币还可解锁最高 20% 折扣。

> 注册即送免费额度：👉 [点击注册](https://share.acedata.cloud/r/1uNf1ozr78)

## 📚 更多

- [完整 API 文档](https://platform.acedata.cloud/docs)
- [SDK 仓库](https://github.com/AceDataCloud)
- [Nexior 开源 UI](https://github.com/AceDataCloud/Nexior)
- [Studio 在线体验](https://studio.acedata.cloud)
- [MCP 服务器](https://github.com/AceDataCloud)

## 📂 项目结构

```
acedata-python/
├── acedata/
│   ├── __init__.py      # 包入口
│   ├── client.py        # 核心客户端
│   └── exceptions.py    # 异常定义
├── examples/
│   ├── chat.py          # 对话示例
│   ├── image.py         # 图片生成示例
│   ├── music.py         # 音乐生成示例
│   ├── video.py         # 视频生成示例
│   └── openai_compatible.py  # OpenAI 兼容示例
├── .env.example
├── requirements.txt
├── pyproject.toml
└── LICENSE
```

## 📄 License

[MIT](./LICENSE)

---

<div align="center">

**Powered by [AceData Cloud](https://platform.acedata.cloud)**

[注册](https://share.acedata.cloud/r/1uNf1ozr78) · [文档](https://platform.acedata.cloud/docs) · [Studio](https://studio.acedata.cloud)

</div>
