import sys
from config.logger import LogConfig
from logging.config import dictConfig

if not hasattr(sys, '_called_from_test'):
    from config.event_bus import event_bus


log_config = LogConfig()
dictConfig(log_config.__dict__)