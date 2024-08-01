from flask import Blueprint

# Create blueprint instances
main_bp = Blueprint('main', __name__)
download_bp = Blueprint('download', __name__)
logic_bp = Blueprint('logic', __name__)
delete_bp = Blueprint('delete', __name__)

from . import main_routes
from . import download_routes
from . import logic_routes
from . import delete_routes
