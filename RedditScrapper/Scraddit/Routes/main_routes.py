from flask import render_template
from . import main_bp  # Import the blueprint instance


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/about')
def about():
    return render_template('about.html')
