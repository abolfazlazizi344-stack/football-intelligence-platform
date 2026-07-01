from pathlib import Path

# --------------------------------------------------
# Project Root
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[3]

# --------------------------------------------------
# Data Directories
# --------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
FEATURES_DATA_DIR = DATA_DIR / "features"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

# --------------------------------------------------
# Documentation
# --------------------------------------------------

DOCS_DIR = PROJECT_ROOT / "docs"

# --------------------------------------------------
# Project Resources
# --------------------------------------------------

LOGS_DIR = PROJECT_ROOT / "logs"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
TESTS_DIR = PROJECT_ROOT / "tests"

# --------------------------------------------------
# Helper
# --------------------------------------------------

ALL_DIRECTORIES = [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    FEATURES_DATA_DIR,
    EXTERNAL_DATA_DIR,
    DOCS_DIR,
    LOGS_DIR,
    NOTEBOOKS_DIR,
    SCRIPTS_DIR,
    TESTS_DIR,
]


def create_project_directories() -> None:
    """
    Create all required project directories if they do not already exist.
    """
    for directory in ALL_DIRECTORIES:
        directory.mkdir(parents=True, exist_ok=True)