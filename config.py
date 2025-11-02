import os
from pathlib import Path

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        base_dir = Path(__file__).parent
        self.SQLALCHEMY_DATABASE_URI = f"sqlite:///{base_dir / 'todos.db'}"
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')