from fip.collectors import FixtureCollector

collector = FixtureCollector()

response = collector.get_fixtures(
    league=1,
    season=2022,
)

print("=" * 50)
print("API Request Successful")
print("=" * 50)

print(response.keys())