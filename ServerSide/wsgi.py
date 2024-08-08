from Scraddit import create_app  # Replace with the actual import path
from waitress import serve
import os

# Create an application instance
app = create_app()

if __name__ == "__main__":
    # Determine the server mode
    serve(app, host='0.0.0.0', port=8080)  # Waitress for production
