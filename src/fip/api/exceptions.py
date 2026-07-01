"""
Custom exceptions for Football Intelligence Platform API layer.
"""


class APIError(Exception):
    """Base exception for API-related errors."""


class AuthenticationError(APIError):
    """Raised when API authentication fails."""


class AuthorizationError(APIError):
    """Raised when access to a resource is forbidden."""


class ResourceNotFoundError(APIError):
    """Raised when the requested resource does not exist."""


class RateLimitError(APIError):
    """Raised when the API rate limit has been exceeded."""


class ServerError(APIError):
    """Raised when the remote server returns a 5xx error."""


class NetworkError(APIError):
    """Raised when the request cannot reach the server."""


class InvalidResponseError(APIError):
    """Raised when the API returns an invalid response."""