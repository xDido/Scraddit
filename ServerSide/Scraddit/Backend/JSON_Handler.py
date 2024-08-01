import json
import os
import datetime
from .Path_Finder import get_path


def export_to_json(data, subreddit_name):
    """
    Export collected Reddit data to a JSON file.
    :param data: List of dictionaries containing post and comment data
    :param subreddit_name: Name of the subreddit (used for filename)
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"r_{subreddit_name}_{timestamp}.json"

    data_directory = get_path('Logs')

    os.makedirs(data_directory, exist_ok=True)

    file_path = os.path.join(data_directory, filename)

    with open(file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=2)

    print(f"Data exported to {file_path}")


def delete_json_files():
    """
    Delete all JSON files in the specified directory.
    """
    data_directory = get_path('Logs')

    for file in os.listdir(data_directory):
        if file.endswith('.json'):
            file_path = os.path.join(data_directory, file)
            os.remove(file_path)
            print(f'{file} has been deleted')
