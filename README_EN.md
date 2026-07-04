<div align="center">

<h1>🚀 AceData Python SDK</h1>

**One API Key for all AI services** — GPT / Claude / Gemini / DeepSeek / Grok / Suno / Midjourney / Veo / Kling

[![CI](https://github.com/RaiderYi/acedata-python/actions/workflows/ci.yml/badge.svg)](https://github.com/RaiderYi/acedata-python/actions)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-13%20passed-brightgreen.svg)](https://github.com/RaiderYi/acedata-python/tree/main/tests)
[![Stars](https://img.shields.io/github/stars/RaiderYi/acedata-python?style=social)](https://github.com/RaiderYi/acedata-python)

[中文](./README.md) | English

</div>

---

## ✨ Why AceData Cloud

- **Unified API**: One key, one base URL, 50+ models
- **Pay-as-you-go**: No subscription, cheaper than official
- **OpenAI Compatible**: Just change `base_url`, zero code change
- **All Modalities**: Chat, Image, Music, Video, Embeddings
- **High Availability**: Global CDN, 99.9% uptime
- **BYOK Support**: Bring your own keys, no platform credits consumed

## 📊 vs Official APIs

| Feature | OpenAI Official | AceData Cloud |
|---------|:---:|:---:|
| Models | OpenAI only | 50+ models (GPT/Claude/Gemini/...) |
| Billing | Subscription + card | Pay-as-you-go, no card needed |
| China Access | Requires VPN | Direct access worldwide |
| Multi-modal | OpenAI only | Cross-vendor all modalities |
| Migration | — | Zero change (OpenAI compatible) |

## 🔑 Get Your API Key

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

client = AceDataClient(api_key="your_api_key")

response = client.chat(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response["choices"][0]["message"]["content"])
```

## 🔧 OpenAI SDK Compatible

```python
from openai import OpenAI

client = OpenAI(
    api_key="your_acedata_key",
    base_url="https://api.acedata.cloud/v1",
)

# Everything else stays the same
```

## 📖 Features

| Feature | Models | Example |
|---------|--------|---------|
| Chat | gpt-4o, claude-3.5, gemini-2.0, deepseek, grok, glm-4 | `examples/chat.py` |
| Image | flux-1, midjourney, seedream | `examples/image.py` |
| Music | chirp-v5-5 (Suno) | `examples/music.py` |
| Video | veo-3, sora, kling, luma | `examples/video.py` |
| Embeddings | text-embedding-3-large | — |
| Error Handling | AuthError, RateLimitError | `tests/test_client.py` |

## 🛡️ Error Handling

```python
from acedata import AuthenticationError, RateLimitError

try:
    response = client.chat(model="gpt-4o", messages=[...])
except AuthenticationError:
    print("Invalid API Key")
except RateLimitError as e:
    print(f"Rate limited, retry after {e.retry_after}s")
```

## 📚 Resources

- [API Docs](https://platform.acedata.cloud/docs)
- [All Models](https://platform.acedata.cloud/models)
- [Nexior Open Source UI](https://github.com/AceDataCloud/Nexior)
- [Studio](https://studio.acedata.cloud)
- [MCP Servers](https://github.com/AceDataCloud)

## 📄 License

[MIT](./LICENSE)

---

<div align="center">

**Powered by [AceData Cloud](https://platform.acedata.cloud)**

[Register](https://share.acedata.cloud/r/1uNf1ozr78) · [Docs](https://platform.acedata.cloud/docs) · [Studio](https://studio.acedata.cloud)

⭐ Star this repo if it helped!

</div>
