<div align="center">

<h1>🚀 AceData Python SDK</h1>

**一个 API Key，访问所有 AI 服务** — GPT / Claude / Gemini / DeepSeek / Grok / Suno / Midjourney / Veo / Kling

[![CI](https://github.com/RaiderYi/acedata-python/actions/workflows/ci.yml/badge.svg)](https://github.com/RaiderYi/acedata-python/actions)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-13%20passed-brightgreen.svg)](https://github.com/RaiderYi/acedata-python/tree/main/tests)
[![Stars](https://img.shields.io/github/stars/RaiderYi/acedata-python?style=social)](https://github.com/RaiderYi/acedata-python)

中文 | [English](./README_EN.md)

</div>

---

## 📑 目录

- [为什么选择 AceData Cloud](#-为什么用-acedata-cloud)
- [与官方 API 对比](#-与官方-api-对比)
- [获取 API Key](#-获取-api-key)
- [安装](#-安装)
- [快速开始](#-快速开始)
- [OpenAI SDK 兼容](#-openai-sdk-兼容零改动迁移)
- [功能一览](#-功能一览)
- [可用模型](#-可用模型部分)
- [错误处理](#-错误处理)
- [项目结构](#-项目结构)

---

## ✨ 为什么用 AceData Cloud

- **统一接口**：一个 Key、一个 Base URL，调用 50+ 模型
- **按量付费**：无需订阅，用多少付多少，比官方便宜
- **OpenAI 兼容**：直接换 `base_url` 即可迁移，零改动
- **全模态覆盖**：对话、图片、音乐、视频、嵌入向量
- **高可用**：全球 CDN 加速，99.9% 可用性
- **支持 BYOK**：自带 Key 也能用，不消耗平台 Credit

## 📊 与官方 API 对比

| 特性 | OpenAI 官方 API | AceData Cloud |
|------|:---:|:---:|
| 模型数量 | 仅 OpenAI 系列 | 50+ 模型（GPT/Claude/Gemini/...） |
| 计费方式 | 需订阅 + 绑卡 | 按量付费，无需绑卡 |
| 中国可用性 | 需代理 | 全球可用，中国直连 |
| 多模态 | 仅 OpenAI 模型 | 跨厂商全模态 |
| 迁移成本 | — | 零改动（OpenAI 兼容） |
| 价格 | 官方定价 | 更优（持有 $ACE 再省 20%） |

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

支持 `gpt-4o` / `gpt-4o-mini` / `claude-3.5-sonnet` / `gemini-2.0-flash` / `deepseek-chat` / `grok-2` / `glm-4` 等

```python
# 普通对话
response = client.chat(model="gpt-4o", messages=[...])

# 流式对话
for token in client.chat_stream(model="gpt-4o", messages=[...]):
    print(token, end="", flush=True)
```

<details>
<summary>多模型切换示例</summary>

```python
models = ["gpt-4o-mini", "claude-3.5-sonnet", "gemini-2.0-flash", "deepseek-chat"]

for model in models:
    response = client.chat(
        model=model,
        messages=[{"role": "user", "content": "一句话介绍你自己"}],
        max_tokens=100,
    )
    print(f"[{model}] {response['choices'][0]['message']['content']}")
```

</details>

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

支持 `chirp-v5-5` / `chirp-v4-5` 等

```python
# 灵感模式
song = client.music(prompt="A jazz song about autumn rain")

# 自定义模式（歌词+风格+标题）
song = client.music(
    custom=True, title="Neon Dreams", style="synthwave",
    lyric="[Verse]\nWalking through neon lights...",
)
```

### AI 视频生成

支持 `veo-3` / `sora` / `kling` / `luma` / `hailuo` 等

```python
video = client.video(model="veo-3", prompt="sunset over the ocean, cinematic", duration=5)
```

### 文本嵌入

```python
embedding = client.embeddings(
    model="text-embedding-3-large",
    input="需要向量化的文本",
)
```

## 🌐 可用模型（部分）

| 类型 | 模型 | 厂商 |
|------|------|------|
| 对话 | gpt-4o, gpt-4o-mini, gpt-4-turbo | OpenAI |
| 对话 | claude-3.5-sonnet, claude-3-opus | Anthropic |
| 对话 | gemini-2.0-flash, gemini-2.0-pro | Google |
| 对话 | deepseek-chat, deepseek-reasoner | DeepSeek |
| 对话 | grok-2 | xAI |
| 对话 | glm-4, glm-4-flash | 智谱AI |
| 对话 | moonshot-v1-8k | 月之暗面 |
| 图片 | flux-1-schnell, flux-1-dev | Black Forest Labs |
| 图片 | midjourney | Midjourney |
| 图片 | seedream | 字节跳动 |
| 音乐 | chirp-v5-5, chirp-v4-5 | Suno |
| 视频 | veo-3 | Google Veo |
| 视频 | sora | OpenAI Sora |
| 视频 | kling | 快手可灵 |
| 视频 | luma, hailuo, seedance | Luma / MiniMax / 字节 |

> 完整模型列表请查看 [模型页面](https://platform.acedata.cloud/models)

## 🛡️ 错误处理

```python
from acedata import AceDataClient, AuthenticationError, RateLimitError

try:
    response = client.chat(model="gpt-4o", messages=[...])
except AuthenticationError:
    print("API Key 无效，请检查")
except RateLimitError as e:
    print(f"请求太快，{e.retry_after}秒后重试")
```

## 💰 定价

按量付费，无需订阅。比官方 API 价格更优。

持有 $ACE 代币还可解锁最高 20% 折扣。

> 注册即送免费额度：👉 [点击注册](https://share.acedata.cloud/r/1uNf1ozr78)

## 📂 项目结构

```
acedata-python/
├── acedata/
│   ├── __init__.py      # 包入口
│   ├── client.py        # 核心客户端（对话/图片/音乐/视频）
│   └── exceptions.py    # 异常定义
├── examples/
│   ├── chat.py                # 对话示例
│   ├── image.py               # 图片生成示例
│   ├── music.py               # 音乐生成示例
│   ├── video.py               # 视频生成示例
│   └── openai_compatible.py   # OpenAI 兼容示例
├── tests/
│   └── test_client.py   # 单元测试（13 tests）
├── .github/workflows/
│   └── ci.yml           # GitHub Actions CI
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── pyproject.toml
```

## 📄 License

[MIT](./LICENSE)

---

<div align="center">

**Powered by [AceData Cloud](https://platform.acedata.cloud)**

[注册获取Key](https://share.acedata.cloud/r/1uNf1ozr78) · [文档](https://platform.acedata.cloud/docs) · [在线体验](https://studio.acedata.cloud) · [开源UI](https://github.com/AceDataCloud/Nexior)

⭐ 如果这个项目对你有帮助，请给个 Star！

</div>
