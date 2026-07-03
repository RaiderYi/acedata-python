<div align="center">

<h1>🚀 AceData Python SDK</h1>

**One API Key for all AI services** — GPT / Claude / Gemini / DeepSeek / Grok / Suno / Midjourney / Veo / Kling

[中文](./README.md) | English

</div>

## ✨ Why AceData Cloud

- **Unified API**: One key, one base URL, 50+ models
- **Pay-as-you-go**: No subscription, cheaper than official
- **OpenAI Compatible**: Just change `base_url`, zero code change
- **All Modalities**: Chat, Image, Music, Video, Embeddings
- **High Availability**: Global CDN, 99.9% uptime

## 🔑 Get Your API Key

> **Step 1**: Register on AceData Cloud and get your API Key
>
> 👉 **[Register & Get Key](https://share.acedata.cloud/r/1uNf1ozr78)**

Copy your API Key from the [Console](https://platform.acedata.cloud/console).

## 📦 Installation

```bash
pip install -e .
# or just install the dependency
pip install requests
```

## 🚀 Quick Start

```python
from acedata import AceDataClient

# Get key: https://share.acedata.cloud/r/1uNf1ozr78
client = AceDataClient(api_key="your_api_key")

# AI Chat
response = client.chat(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response["choices"][0]["message"]["content"])
```

## 🔧 OpenAI SDK Compatible

Already using OpenAI SDK? Just change two lines:

```python
from openai import OpenAI

client = OpenAI(
    api_key="your_acedata_key",              # ← AceData Key
    base_url="https://api.acedata.cloud/v1", # ← AceData URL
)

# Everything else stays the same
```

## 📖 Features

| Feature | Models | Example |
|---------|--------|---------|
| Chat | gpt-4o, claude-3.5, gemini-2.0, deepseek, grok | `examples/chat.py` |
| Image | flux-1, midjourney, seedream | `examples/image.py` |
| Music | chirp-v5-5 (Suno) | `examples/music.py` |
| Video | veo-3, sora, kling, luma | `examples/video.py` |
| Embeddings | text-embedding-3-large | — |

## 📚 Resources

- [API Docs](https://platform.acedata.cloud/docs)
- [Nexior Open Source UI](https://github.com/AceDataCloud/Nexior)
- [Studio](https://studio.acedata.cloud)
- [All Models](https://platform.acedata.cloud/models)

## 📄 License

[MIT](./LICENSE)

---

<div align="center">

**Powered by [AceData Cloud](https://platform.acedata.cloud)**

[Register](https://share.acedata.cloud/r/1uNf1ozr78) · [Docs](https://platform.acedata.cloud/docs) · [Studio](https://studio.acedata.cloud)

</div>
