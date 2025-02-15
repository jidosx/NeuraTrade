import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_info(message):
    logger.info(message)
