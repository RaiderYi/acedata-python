"""AceData Cloud SDK 异常定义"""


class AceDataError(Exception):
    """基础异常"""

    pass


class AuthenticationError(AceDataError):
    """API Key 无效或过期"""

    pass


class RateLimitError(AceDataError):
    """请求频率超限"""

    def __init__(self, message, retry_after=None):
        super().__init__(message)
        self.retry_after = retry_after
