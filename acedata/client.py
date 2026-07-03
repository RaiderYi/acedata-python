"""
AceData Cloud Python SDK — 核心客户端

统一接口调用 GPT / Claude / Gemini / DeepSeek / Suno / Midjourney 等服务。
兼容 OpenAI SDK 格式，可直接替换 base_url 使用。

获取 API Key: https://share.acedata.cloud/r/1uNf1ozr78
文档: https://platform.acedata.cloud/docs
"""

import json
import time
import requests
from typing import Optional, List, Dict, Any, Iterator, Union
from .exceptions import AceDataError, AuthenticationError, RateLimitError

DEFAULT_BASE_URL = "https://api.acedata.cloud/v1"


class AceDataClient:
    """
    AceData Cloud 统一 API 客户端

    用法:
        client = AceDataClient(api_key="your_key")
        response = client.chat(model="gpt-4o", messages=[...])
        image = client.image(model="flux-1", prompt="a cat")
        song = client.music(prompt="jazz piano", custom=True)

    获取 Key: https://share.acedata.cloud/r/1uNf1ozr78
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: int = 120,
        max_retries: int = 3,
    ):
        if not api_key:
            raise AuthenticationError(
                "API Key 不能为空。前往 https://share.acedata.cloud/r/1uNf1ozr78 获取"
            )
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self._session = requests.Session()
        self._session.headers.update(
            {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
        )

    # ── 内部请求 ──────────────────────────────────────────

    def _request(
        self,
        method: str,
        path: str,
        json_body: Optional[dict] = None,
        stream: bool = False,
    ) -> Union[dict, Iterator[bytes]]:
        url = f"{self.base_url}{path}"
        last_error = None

        for attempt in range(self.max_retries):
            try:
                resp = self._session.request(
                    method=method,
                    url=url,
                    json=json_body,
                    timeout=self.timeout,
                    stream=stream,
                )

                if resp.status_code == 401:
                    raise AuthenticationError(
                        "API Key 无效或过期。前往 https://share.acedata.cloud/r/1uNf1ozr78 重新获取"
                    )
                if resp.status_code == 429:
                    retry_after = resp.headers.get("Retry-After")
                    raise RateLimitError(
                        "请求频率超限，请稍后重试", retry_after=int(retry_after) if retry_after else None
                    )
                if resp.status_code >= 500 and attempt < self.max_retries - 1:
                    last_error = AceDataError(f"服务端错误 {resp.status_code}，第 {attempt+1} 次重试")
                    time.sleep(2 ** (attempt + 1))
                    continue

                if stream:
                    return resp.iter_lines()

                resp.raise_for_status()
                return resp.json()

            except (requests.ConnectionError, requests.Timeout) as e:
                last_error = AceDataError(f"网络错误: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** (attempt + 1))
                    continue
                raise

        raise last_error or AceDataError("未知错误")

    # ── 对话 ──────────────────────────────────────────────

    def chat(
        self,
        model: str = "gpt-4o-mini",
        messages: List[Dict[str, str]] = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ) -> dict:
        """
        AI 对话（兼容 OpenAI 格式）

        支持模型: gpt-4o, gpt-4o-mini, claude-3.5-sonnet,
                  gemini-2.0-flash, deepseek-chat, grok-2 等

        >>> client.chat(model="gpt-4o", messages=[{"role":"user","content":"你好"}])
        """
        body = {
            "model": model,
            "messages": messages or [],
            "temperature": temperature,
            "max_tokens": max_tokens,
            **kwargs,
        }
        return self._request("POST", "/chat/completions", json_body=body)

    def chat_stream(
        self,
        model: str = "gpt-4o-mini",
        messages: List[Dict[str, str]] = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ) -> Iterator[str]:
        """流式对话，逐 token 返回"""
        body = {
            "model": model,
            "messages": messages or [],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True,
            **kwargs,
        }
        lines = self._request("POST", "/chat/completions", json_body=body, stream=True)
        for line in lines:
            if line:
                line_str = line.decode("utf-8") if isinstance(line, bytes) else line
                if line_str.startswith("data: "):
                    data = line_str[6:]
                    if data == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                        delta = chunk["choices"][0].get("delta", {})
                        if delta.get("content"):
                            yield delta["content"]
                    except json.JSONDecodeError:
                        continue

    # ── 图片生成 ──────────────────────────────────────────

    def image(
        self,
        model: str = "flux-1-schnell",
        prompt: str = "",
        size: str = "1024x1024",
        n: int = 1,
        **kwargs,
    ) -> dict:
        """
        AI 图片生成

        支持模型: flux-1-schnell, flux-1-dev, midjourney, seedream 等

        >>> client.image(model="flux-1-schnell", prompt="a cute cat", size="1024x1024")
        """
        body = {"model": model, "prompt": prompt, "size": size, "n": n, **kwargs}
        return self._request("POST", "/images/generations", json_body=body)

    # ── 音乐生成 (Suno) ──────────────────────────────────

    def music(
        self,
        prompt: str = "",
        model: str = "chirp-v5-5",
        custom: bool = False,
        title: str = "",
        style: str = "",
        lyric: str = "",
        **kwargs,
    ) -> dict:
        """
        AI 音乐生成 (Suno)

        灵感模式:
        >>> client.music(prompt="A jazz song about autumn rain")

        自定义模式:
        >>> client.music(custom=True, title="My Song", style="pop", lyric="[Verse]...")
        """
        body = {
            "model": model,
            "prompt": prompt,
            "custom": custom,
            **kwargs,
        }
        if custom:
            body.update({"title": title, "style": style, "lyric": lyric})
        return self._request("POST", "/audios", json_body=body)

    # ── 视频生成 ──────────────────────────────────────────

    def video(
        self,
        model: str = "veo-3",
        prompt: str = "",
        duration: int = 5,
        **kwargs,
    ) -> dict:
        """
        AI 视频生成

        支持模型: veo-3, sora, kling, luma, hailuo, seedance 等

        >>> client.video(model="veo-3", prompt="sunset over the ocean", duration=5)
        """
        body = {"model": model, "prompt": prompt, "duration": duration, **kwargs}
        return self._request("POST", "/videos/generations", json_body=body)

    # ── 嵌入向量 ──────────────────────────────────────────

    def embeddings(
        self,
        model: str = "text-embedding-3-large",
        input: str = "",
        **kwargs,
    ) -> dict:
        """文本嵌入向量"""
        body = {"model": model, "input": input, **kwargs}
        return self._request("POST", "/embeddings", json_body=body)

    # ── 工具 ──────────────────────────────────────────────

    def list_models(self) -> dict:
        """列出所有可用模型"""
        return self._request("GET", "/models")

    def balance(self) -> dict:
        """查询账户余额"""
        return self._request("GET", "/credits/balance")

    # ── OpenAI SDK 兼容 ──────────────────────────────────

    @property
    def openai_base_url(self) -> str:
        """
        返回可用于 OpenAI SDK 的 base_url

        >>> from openai import OpenAI
        >>> client = OpenAI(api_key="your_key", base_url=acedata.openai_base_url)
        """
        return self.base_url
