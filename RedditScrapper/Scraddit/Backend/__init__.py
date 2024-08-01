# Script.py
from .Logging_Handler import setup_logging, delete_log_files
from .Compressing_Handler import compress_files, delete_zip_files
import os

from .Praw_Handler import collect_subreddit_data, create_reddit_object, choose_subreddit
from .Path_Finder import get_path
from .JSON_Handler import delete_json_files


def main():
    log_directory = get_path('Logs')
    logger = setup_logging(log_directory)

    # Create a Reddit object
    reddit = create_reddit_object()

    # Choose a subreddit
    subreddit_name = 'Egypt'  # Example subreddit
    subreddit = choose_subreddit(reddit, subreddit_name)
    collect_subreddit_data(subreddit, logger, 'new')
    compress_files(log_directory, subreddit_name)


if __name__ == "__main__":
    delete_log_files()
    delete_zip_files()
    delete_json_files()
