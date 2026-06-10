import logging

logger = logging.getLogger("ai_assistant")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler = logging.FileHandler("app.log")

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

if not logger.handlers:
    logger.addHandler(file_handler)