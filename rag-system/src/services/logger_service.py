import logging as LOGGER

# Configure the logging system
LOGGER.basicConfig(
    level=LOGGER.INFO,  # Tells it to capture INFO, WARNING, ERROR, etc.
    format="%(asctime)s - %(levelname)s - %(message)s"  # Makes it look clean
)