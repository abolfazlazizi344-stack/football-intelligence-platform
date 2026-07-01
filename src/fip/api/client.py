"""
HTTP client for Football Intelligence Platform.
"""

from __future__ import annotations

import httpx

from fip.config import settings

from .retry import retry

from .exceptions import (
    AuthenticationError,
    NetworkError,
    ResourceNotFoundError,
    ServerError,
    RateLimitError,
)

from .rate_limiter import RateLimiter


class APIClient:
    """
    Base HTTP client.
    """

    BASE_URL = "https://v3.football.api-sports.io"

    TIMEOUT = 30

    def __init__(self):
        self.rate_limiter = RateLimiter()
        self.client = httpx.Client(
            timeout=self.TIMEOUT,
            headers={
                "x-apisports-key": settings.api_football_key,
            },
        )
    
    @retry()
    def get(self, endpoint: str, params: dict | None = None):

        url = f"{self.BASE_URL}{endpoint}"

        self.rate_limiter.wait()
        
        try:

            response = self.client.get(
                url,
                params=params,
            )

        except httpx.RequestError as exc:

            raise NetworkError(str(exc)) from exc

        self._raise_for_status(response)

        return response.json()

    def _raise_for_status(self, response: httpx.Response):

        if response.status_code == 401:
            raise AuthenticationError()

        if response.status_code == 404:
            raise ResourceNotFoundError()

        if response.status_code == 429:
            raise RateLimitError()

        if response.status_code >= 500:
            raise ServerError()