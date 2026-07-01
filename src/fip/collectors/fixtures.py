"""
Fixture collector.
"""

from __future__ import annotations

from .base import BaseCollector


class FixtureCollector(BaseCollector):
    """
    Collects fixture data from API-Football.
    """

    ENDPOINT = "/fixtures"

    def get_fixtures(
        self,
        league: int,
        season: int,
    ) -> dict:

        params = {
            "league": league,
            "season": season,
        }

        return self.client.get(
            self.ENDPOINT,
            params=params,
        )