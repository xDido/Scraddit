import os
from datetime import timedelta


class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_PERMANENT = True
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)  # Set session lifetime
    DEBUG = False
    TESTING = False
    LOGGING_LEVEL = 'WARNING'


