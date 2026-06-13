class AgentInboxError(Exception):
    """Base error for AgentInbox API."""

    def __init__(self, message: str, code: str = "unknown"):
        super().__init__(message)
        self.code = code
        self.message = message


class UnauthorizedError(AgentInboxError):
    """Invalid API key or unauthorized access."""

    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, "unauthorized")


class RateLimitError(AgentInboxError):
    """Rate limit exceeded."""

    def __init__(self, message: str = "Rate limit exceeded", retry_after: int = 0):
        super().__init__(message, "rate_limited")
        self.retry_after = retry_after


class QuotaExceededError(AgentInboxError):
    """Plan quota exceeded."""

    def __init__(self, message: str = "Quota exceeded", limit: int = 0):
        super().__init__(message, "quota_exceeded")
        self.limit = limit


class NotFoundError(AgentInboxError):
    """Resource not found."""

    def __init__(self, message: str = "Not found"):
        super().__init__(message, "not_found")


class InvalidRequestError(AgentInboxError):
    """Invalid request parameters."""

    def __init__(self, message: str = "Invalid request"):
        super().__init__(message, "invalid_request")
