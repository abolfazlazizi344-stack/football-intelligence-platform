"""
Retry utilities for API requests.
"""

from __future__ import annotations

import time
from functools import wraps

import httpx

from .exceptions import NetworkError, ServerError


def retry(
    retries: int = 3,
    delay: float = 1.0,
):
    """
    Retry decorator for transient failures.
    """

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            last_exception = None

            for attempt in range(retries):

                try:

                    return func(*args, **kwargs)

                except (
                    httpx.RequestError,
                    NetworkError,
                    ServerError,
                ) as exc:

                    last_exception = exc

                    if attempt < retries - 1:

                        time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator