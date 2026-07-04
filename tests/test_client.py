"""
单元测试 — AceData Python SDK

不需要真实 API Key，测试客户端逻辑、异常处理、参数构造。
"""

import pytest
from acedata import AceDataClient, AceDataError, AuthenticationError, RateLimitError
from acedata.client import DEFAULT_BASE_URL
from acedata.exceptions import RateLimitError as RLE


class TestClientInit:
    """客户端初始化测试"""

    def test_init_with_valid_key(self):
        client = AceDataClient(api_key="test_key_123")
        assert client.api_key == "test_key_123"
        assert client.base_url == DEFAULT_BASE_URL

    def test_init_with_custom_base_url(self):
        client = AceDataClient(api_key="test_key", base_url="https://custom.api.com/v1/")
        assert client.base_url == "https://custom.api.com/v1"

    def test_init_empty_key_raises(self):
        with pytest.raises(AuthenticationError):
            AceDataClient(api_key="")

    def test_init_none_key_raises(self):
        with pytest.raises(AuthenticationError):
            AceDataClient(api_key=None)

    def test_default_timeout(self):
        client = AceDataClient(api_key="test")
        assert client.timeout == 120

    def test_custom_timeout(self):
        client = AceDataClient(api_key="test", timeout=30)
        assert client.timeout == 30

    def test_max_retries(self):
        client = AceDataClient(api_key="test", max_retries=5)
        assert client.max_retries == 5


class TestOpenAICompat:
    """OpenAI 兼容性测试"""

    def test_openai_base_url(self):
        client = AceDataClient(api_key="test")
        assert client.openai_base_url == DEFAULT_BASE_URL

    def test_openai_base_url_equals_client_base_url(self):
        client = AceDataClient(api_key="test", base_url="https://custom.api.com/v1")
        assert client.openai_base_url == "https://custom.api.com/v1"


class TestExceptions:
    """异常类测试"""

    def test_acedata_error_is_exception(self):
        err = AceDataError("test error")
        assert isinstance(err, Exception)
        assert str(err) == "test error"

    def test_auth_error_inherits(self):
        err = AuthenticationError("bad key")
        assert isinstance(err, AceDataError)
        assert isinstance(err, Exception)

    def test_rate_limit_error_with_retry(self):
        err = RateLimitError("too fast", retry_after=60)
        assert isinstance(err, AceDataError)
        assert err.retry_after == 60

    def test_rate_limit_error_without_retry(self):
        err = RateLimitError("too fast")
        assert err.retry_after is None
