from flask import Blueprint, send_file, abort
import zipfile
import os
import io
from ..Backend.Path_Finder import get_path
from . import download_bp

# Path to the zip file
ZIP_FILE_PATH = get_path('zip') # Change this to your zip file path


@download_bp.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        # Ensure the filename is safe and valid
        if '..' in filename or filename.startswith('/'):
            abort(400)  # Bad request if the filename is unsafe

        # Check if the zip file exists
        if not os.path.isfile(ZIP_FILE_PATH):
            abort(500)  # Internal server error if the zip file does not exist

        # Open the zip file and look for the file
        with zipfile.ZipFile(ZIP_FILE_PATH, 'r') as zipf:
            if filename not in zipf.namelist():
                abort(404)  # File not found in the zip archive

            # Extract the file from the zip archive into memory
            file_data = zipf.read(filename)
            # Create a BytesIO stream to serve the file
            file_stream = io.BytesIO(file_data)
            return send_file(file_stream, attachment_filename=filename, as_attachment=True)

    except Exception as e:
        # Handle any other exceptions
        print(e)
        abort(500)  # Internal server error for unexpected issues
