"""
Logger Module

Provides a centralized logging configuration
"""

import logging


def setup_logger(name: str = "multi_agent_rag"):
    """
    Configure and return logger

    :param name: Logger name
    :return: Logger instance
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if not logger.handlers:

        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger


# Global logger instance
logger = setup_logger()
