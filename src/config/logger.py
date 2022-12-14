import logging, os
from pydantic import BaseModel
from logging.config import dictConfig


class LogConfig(BaseModel):
    """Logging configuration [console - always, file - only for errors]"""

    LOG_FORMAT: str = "%(levelprefix)s [%(asctime)s] | %(filename)s: %(message)s"
    FILE_LOG_FORMAT: str = "%(levelname)s: [%(asctime)s] %(name)s | %(message)s"
    LOG_FILENAME: str = "logs/bankapp.err.log"
    LOG_LEVEL: str = "INFO"
    os.makedirs(os.path.dirname(LOG_FILENAME), exist_ok=True)

    # Logger config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "console": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "file": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": FILE_LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    }
    handlers = {
        "console": {
            "formatter": "console",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": LOG_LEVEL
        },
        "file": {
            "formatter": "file",
            "class": "logging.FileHandler",
            "level": "ERROR",
            "filename": LOG_FILENAME
        },
    }
    loggers = {
        "BankAppLogger": {"handlers": ["console", "file"], "level": LOG_LEVEL},
    }

logger = logging.getLogger("BankAppLogger")