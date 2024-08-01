import logging
import os
from datetime import datetime
from .Path_Finder import get_path

def setup_logging(log_directory: str = None):
    """
    Set up logging to two separate files: one for DEBUG and one for INFO level logs.
    Both files will include timestamps in their filenames.

    :param log_directory: Directory where log files will be stored
    :return: Logger object
    """
    if log_directory is None:

        log_directory = get_path('Logs')

    # Create the log directory if it doesn't exist
    os.makedirs(log_directory, exist_ok=True)

    # Generate a timestamp for the log filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    debug_filename = f"reddit_scraper_DEBUG_{timestamp}.log"
    info_filename = f"reddit_scraper_INFO_{timestamp}.log"
    debug_filepath = os.path.join(log_directory, debug_filename)
    info_filepath = os.path.join(log_directory, info_filename)

    # Create a logger
    logger = logging.getLogger('reddit_scraper')
    logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all levels

    # Create formatters
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create and set up the DEBUG file handler
    debug_handler = logging.FileHandler(debug_filepath, encoding='utf-8')
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)

    # Create and set up the INFO file handler
    info_handler = logging.FileHandler(info_filepath, encoding='utf-8')
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(debug_handler)
    logger.addHandler(info_handler)

    logger.info(f"Logging initiated. DEBUG log file: {debug_filepath}")
    logger.info(f"Logging initiated. INFO log file: {info_filepath}")
    return logger


def delete_log_files(log_directory: str = None):
    """
    Delete all log files in the specified directory.

    :param log_directory: Directory where log files are stored
    :return: Number of files deleted
    """
    if log_directory is None:
        log_directory = get_path('Logs')

    deleted_count = 0

    # Ensure the directory exists
    if not os.path.exists(log_directory):
        logging.warning(f"Log directory does not exist: {log_directory}")
        return deleted_count

    # Iterate over all files in the directory
    for filename in os.listdir(log_directory):
        if filename.endswith('.log'):
            file_path = os.path.join(log_directory, filename)
            try:
                os.remove(file_path)
                deleted_count += 1
                logging.info(f"Deleted log file: {file_path}")
            except Exception as e:
                logging.error(f"Error deleting {file_path}: {str(e)}")

    logging.info(f"Cleanup complete. Deleted {deleted_count} log files.")
    return deleted_count
