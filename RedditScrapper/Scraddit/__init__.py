from flask import Flask, jsonify
from .Routes import main_bp, download_bp, logic_bp, delete_bp


def create_app(config_class='Config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    app.register_blueprint(download_bp, url_prefix='/download')  # Optional URL prefix
    app.register_blueprint(logic_bp, url_prefix='/logic')  # Optional URL prefix
    app.register_blueprint(main_bp, url_prefix='/main')  # Optional URL prefix


    return app
