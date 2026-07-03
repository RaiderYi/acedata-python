"""
AceData Cloud Python SDK
========================
统一接口访问 GPT / Claude / Gemini / Suno / Midjourney / Veo 等 AI 服务。

先获取 API Key: https://share.acedata.cloud/r/1uNf1ozr78
"""

from .client import AceDataClient
from .exceptions import AceDataError, AuthenticationError, RateLimitError

__version__ = "1.0.0"
__all__ = ["AceDataClient", "AceDataError", "AuthenticationError", "RateLimitError"]
