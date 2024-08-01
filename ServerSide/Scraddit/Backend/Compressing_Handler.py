import os
import zipfile
import datetime
from .Path_Finder import get_path

def compress_files(src_folder: str, sub_name: str):
    """
    Compress all files from the specified source folder into a single zip file named after the JSON file.

    :param src_folder: Path to the folder to compress
    :param sub_name: Name to use for the zip file
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{sub_name}_{timestamp}"
    zip_name = f'{filename}.zip'

    data_directory = get_path('zip')

    zip_path = os.path.join(data_directory, zip_name)

    # Create the zip file and add files from the specified folder
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(src_folder):
            for file in files:
                file_path = os.path.join(root, file)
                # Create a relative path for the file in the zip archive
                relative_path = os.path.relpath(file_path, start=src_folder)
                zipf.write(file_path, relative_path)

    print(f'Files have been compressed into {zip_path}')


def delete_zip_files():
    """
    Delete all zip files in the specified directory.
    """
    backend_directory = os.path.dirname(__file__)
    project_root = os.path.dirname(backend_directory)
    data_directory = os.path.join(project_root, 'zip')

    for file in os.listdir(data_directory):
        if file.endswith('.zip'):
            file_path = os.path.join(data_directory, file)
            os.remove(file_path)
            print(f'{file} has been deleted')
