# src/utils/logger.py
import logging
import sys

_CONFIGURED = False


def _configure_root():
    global _CONFIGURED
    if _CONFIGURED:
        return
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
        stream=sys.stdout,
    )
    _CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    """Return a module-level logger with a consistent format."""
    _configure_root()
    return logging.getLogger(name)
