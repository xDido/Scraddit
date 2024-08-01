import os


def get_path(subdirectory: str) -> str:
    """
    Returns the absolute path to a subdirectory within the project directory.

    :param subdirectory: Name of the subdirectory to locate
    :return: Absolute path to the subdirectory
    """
    backend_directory = os.path.dirname(__file__)  # Get the directory of the current script
    project_root = os.path.dirname(backend_directory)  # Go one level up to the project root
    target_path = os.path.join(project_root, subdirectory)  # Join the project root with the subdirectory

    return target_path

