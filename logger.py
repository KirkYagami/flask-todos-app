import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._setup_logger()
        return cls._instance

    def _setup_logger(self):
        self.logger = logging.getLogger('TodoApp')
        self.logger.setLevel(logging.INFO)

        # Avoid duplicate handlers
        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )

            # Console handler
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

            # File handler (rotating)
            log_dir = Path(__file__).parent / 'logs'
            log_dir.mkdir(exist_ok=True)
            fh = RotatingFileHandler(
                log_dir / 'app.log',
                maxBytes=10_000_000,
                backupCount=5
            )
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger