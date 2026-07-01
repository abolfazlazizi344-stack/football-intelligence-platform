import logging
from pathlib import Path

from fip.config.paths import LOGS_DIR
from fip.config import settings

LOGS_DIR.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("fip")
logger.setLevel(settings.log_level)

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOGS_DIR / "fip.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)