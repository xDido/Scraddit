import os
from datetime import timedelta


class Config:
    """Base configuration."""


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)  # Set session lifetime
    SESSION_PERMANENT = True
    SESSION_TYPE = 'filesystem'


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)  # Set session lifetime
    SESSION_PERMANENT = True
    SESSION_TYPE = 'filesystem'
