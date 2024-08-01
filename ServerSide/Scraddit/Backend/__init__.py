from .Logging_Handler import setup_logging, delete_log_files
from .Compressing_Handler import compress_files, delete_zip_files
from .Praw_Handler import collect_subreddit_data, create_reddit_object, choose_subreddit
from .Path_Finder import get_path
from .JSON_Handler import delete_json_files

def main():
    print("main")
