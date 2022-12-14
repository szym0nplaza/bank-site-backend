from config.event_bus import event_bus
from config.logger import LogConfig
from logging.config import dictConfig


log_config = LogConfig()
dictConfig(log_config.__dict__)