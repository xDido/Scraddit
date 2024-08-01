import os


class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    COSMOS_DB_ENDPOINT = os.getenv('COSMOS_DB_ENDPOINT', 'your_cosmos_db_endpoint')
    COSMOS_DB_KEY = os.getenv('COSMOS_DB_KEY', 'your_cosmos_db_key')
    COSMOS_DB_DATABASE = os.getenv('COSMOS_DB_DATABASE', 'your_database_name')
    DEBUG = False
    TESTING = False
    LOGGING_LEVEL = 'WARNING'


class DevelopmentConfig(Config):
    """Configuration for development."""
    DEBUG = True
    LOGGING_LEVEL = 'DEBUG'


class TestingConfig(Config):
    """Configuration for testing."""
    TESTING = True
    LOGGING_LEVEL = 'ERROR'


class ProductionConfig(Config):
    """Configuration for production."""
    SECRET_KEY = os.getenv('SECRET_KEY')
    COSMOS_DB_ENDPOINT = os.getenv('COSMOS_DB_ENDPOINT')
    COSMOS_DB_KEY = os.getenv('COSMOS_DB_KEY')
    COSMOS_DB_DATABASE = os.getenv('COSMOS_DB_DATABASE')
    LOGGING_LEVEL = 'WARNING'
