class Error(Exception):
    """
    Abstract Exception class.
    """
    def __init__(self, message):
        self.message = message


class APIError(Error):
    def __init__(self, code):
        self.code = code


class InvalidMSISDNError(Error):
    pass


class DailyQuotaExceededError(APIError):
    pass


class UpstreamQuotaExceededError(APIError):
    pass


class FatalError(APIError):
    pass


class AuthenticationError(Error):
    pass


class DataValidationError(APIError):
    pass


class NoSufficientCreditsError(APIError):
    pass


class UpstreamCreditsNotAvailable(APIError):
    pass


class MaximumBatchExceededError(APIError):
    pass


class UnavailableError(APIError):
    pass
