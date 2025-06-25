# File: /mangadex-api/mangadex-api/src/mangadex/utils/exceptions.py

class APIError(Exception):
    """Generic exception for API errors."""
    pass

class MangaDexAPIError(Exception):
    """Base class for all MangaDex API exceptions."""
    pass

class AuthenticationError(MangaDexAPIError):
    """Exception raised for authentication errors."""
    pass

class NotFoundError(MangaDexAPIError):
    """Exception raised when a resource is not found."""
    pass

class BadRequestError(MangaDexAPIError):
    """Exception raised for bad requests."""
    pass

class ForbiddenError(MangaDexAPIError):
    """Exception raised for forbidden actions."""
    pass

class RateLimitError(MangaDexAPIError):
    """Exception raised when the rate limit is exceeded."""
    pass

class ServerError(MangaDexAPIError):
    """Exception raised for server errors."""
    pass

class InvalidResponseError(MangaDexAPIError):
    """Exception raised for invalid responses from the API."""
    pass