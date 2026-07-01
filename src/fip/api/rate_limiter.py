"""
Simple rate limiter for API requests.
"""

from __future__ import annotations

import time


class RateLimiter:
    """
    Limits the number of API requests per time window.
    """

    def __init__(
        self,
        max_requests: int = 100,
        period: int = 60,
    ):

        self.max_requests = max_requests
        self.period = period

        self.requests = []

    def wait(self) -> None:

        now = time.time()

        self.requests = [
            request
            for request in self.requests
            if now - request < self.period
        ]

        if len(self.requests) >= self.max_requests:

            sleep_time = self.period - (now - self.requests[0])

            if sleep_time > 0:
                time.sleep(sleep_time)

        self.requests.append(time.time())