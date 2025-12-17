# utils.py

import os
import logging
from typing import Any, Callable, Dict, List, Optional, Tuple

def get_absolute_path(relative_path: str) -> str:
    """Get the absolute path of a file or directory.

    Args:
        relative_path (str): The relative path.

    Returns:
        str: The absolute path.
    """
    return os.path.abspath(relative_path)

def get_current_directory() -> str:
    """Get the current working directory.

    Returns:
        str: The current working directory.
    """
    return os.getcwd()

def get_directory_size(directory: str) -> int:
    """Get the size of a directory in bytes.

    Args:
        directory (str): The path to the directory.

    Returns:
        int: The size of the directory in bytes.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def configure_logging(log_level: int = logging.INFO) -> None:
    """Configure logging.

    Args:
        log_level (int, optional): The log level. Defaults to logging.INFO.
    """
    logging.basicConfig(level=log_level, format='%(asctime)s %(levelname)s: %(message)s')

def format_exception(exc: Exception) -> str:
    """Format an exception as a string.

    Args:
        exc (Exception): The exception.

    Returns:
        str: The formatted exception.
    """
    return f"Exception: {exc.__class__.__name__} - {str(exc)}"

def is_list_empty(lst: List[Any]) -> bool:
    """Check if a list is empty.

    Args:
        lst (List[Any]): The list.

    Returns:
        bool: Whether the list is empty.
    """
    return len(lst) == 0

def is_dict_empty(dictionary: Dict[Any, Any]) -> bool:
    """Check if a dictionary is empty.

    Args:
        dictionary (Dict[Any, Any]): The dictionary.

    Returns:
        bool: Whether the dictionary is empty.
    """
    return len(dictionary) == 0