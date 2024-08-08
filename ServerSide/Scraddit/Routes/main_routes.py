from flask import render_template
from . import main_bp  # Import the blueprint instance


@main_bp.route('/', methods=['GET'])
def index():
    return 'Hello, World with waittestsdasdasdress!!!'


@main_bp.route('/about')
def about():
    return render_template('about.html')
