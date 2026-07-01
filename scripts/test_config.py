from fip.config import (
    settings,
    PROJECT_ROOT,
    DATA_DIR,
    DOCS_DIR,
    LOGS_DIR,
)

print("=" * 50)
print("Football Intelligence Platform")
print("Configuration Test")
print("=" * 50)

print(f"Project Root : {PROJECT_ROOT}")
print(f"Data Folder  : {DATA_DIR}")
print(f"Docs Folder  : {DOCS_DIR}")
print(f"Logs Folder  : {LOGS_DIR}")

print()

print(f"Log Level    : {settings.log_level}")
print(f"API Key Set? : {'Yes' if settings.api_football_key else 'No'}")