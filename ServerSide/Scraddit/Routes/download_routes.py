import traceback
from flask import send_file, abort
import os
from ..Backend.Path_Finder import get_path
from . import download_bp

# Path to the zip file
ZIP_DIR_PATH= get_path('zip')  # Ensure this path points to your zip file

def get_zip_file_path(directory_path):
    """Retrieve the path to the ZIP file in the given directory."""
    for filename in os.listdir(directory_path):
        if filename.endswith('.zip'):
            return os.path.join(directory_path, filename)
    return None
@download_bp.route('/download_all', methods=['GET'])
def download_all_files():
    print(f"ZIP_DIR_PATH: {ZIP_DIR_PATH}")
    try:
        # Find the ZIP file in the directory
        zip_file_path = get_zip_file_path(ZIP_DIR_PATH)
        if not zip_file_path or not os.path.isfile(zip_file_path):
            print(f"No ZIP file found in directory: {ZIP_DIR_PATH}")
            abort(500)  # Internal server error if no ZIP file is found

        # Get the original ZIP file name
        original_zip_filename = os.path.basename(zip_file_path)

        # Send the original ZIP file
        return send_file(zip_file_path, download_name=original_zip_filename, as_attachment=True)

    except Exception as e:
        # Handle any other exceptions
        print(f"Exception: {e}")
        traceback.print_exc()
        abort(500)  # Internal server error for unexpected issues