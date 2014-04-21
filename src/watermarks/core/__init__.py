import logging


def setup_logger(log_level=None):
    log_level = log_level or logging.INFO
    logger = logging.getLogger()
    logger.setLevel(log_level)
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)
