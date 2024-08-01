from flask import Flask, session
from .Routes import main_bp, download_bp, logic_bp, delete_bp, session_bp
from flask_session import Session
from .config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    Session(app)
    # Register blueprints
    app.register_blueprint(download_bp, url_prefix='/download')
    app.register_blueprint(logic_bp, url_prefix='/logic')
    app.register_blueprint(main_bp, url_prefix='/main')
    app.register_blueprint(delete_bp, url_prefix='/delete')
    app.register_blueprint(session_bp, url_prefix='/session')

    return app
