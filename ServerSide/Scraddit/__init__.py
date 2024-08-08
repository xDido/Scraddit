from flask import Flask, session
from .Routes import main_bp, download_bp, logic_bp, delete_bp, session_bp
from flask_session import Session
from .config import DevelopmentConfig
from .config import ProductionConfig


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    Session(app)
    # Register blueprints
    app.register_blueprint(download_bp, url_prefix='/api/download')
    app.register_blueprint(logic_bp, url_prefix='/api/logic')
    app.register_blueprint(main_bp)
    app.register_blueprint(delete_bp, url_prefix='/api/delete')
    app.register_blueprint(session_bp, url_prefix='/api/session')

    return app
