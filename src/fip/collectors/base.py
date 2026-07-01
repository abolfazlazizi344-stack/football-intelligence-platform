"""
Base collector class.
"""

from __future__ import annotations

from fip.api import APIClient


class BaseCollector:
    """
    Base class for all data collectors.
    """

    def __init__(self, client: APIClient | None = None):

        self.client = client or APIClient()