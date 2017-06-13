class Error(Exception):
    """Abstract Exception class."""

    def __init__(self, message):
        self.message = message


class APIError(Error):
    """Abstract API error class."""
    def __init__(self, code):
        self.code = code


class InvalidMSISDNError(Error):
    """Invalid msisdn error class."""
    pass


class DailyQuotaExceededError(APIError):
    """Daily quota exceeded."""
    pass


class UpstreamQuotaExceededError(APIError):
    """Upstream quota exceeded."""
    pass


class FatalError(APIError):
    """Internal fatal error."""
    pass


class AuthenticationError(Error):
    """Authentication failure."""
    pass


class DataValidationError(APIError):
    """Data validation failed."""
    pass


class NoSufficientCreditsError(APIError):
    """No sufficient credits."""
    pass


class UpstreamCreditsNotAvailable(APIError):
    """Upstream credits not available."""
    pass


class MaximumBatchExceededError(APIError):
    """Maximum batch size exceeded."""
    pass


class UnavailableError(APIError):
    """Temporarily unavailable."""
    pass
