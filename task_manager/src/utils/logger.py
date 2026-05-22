import logging
from src.config.settings import LOG_LEVEL

logging.basicConfig(
    filename="logs/app.log",
    level=LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger()