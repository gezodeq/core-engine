import os
import json
import logging
import datetime

from core_engine.config import Config

logger = logging.getLogger(__name__)

def get_current_date():
    return datetime.date.today().strftime("%Y-%m-%d")

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def load_config(config_file_path):
    try:
        with open(config_file_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        logger.error(f"Config file not found at: {config_file_path}")
        return None
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in config file: {config_file_path}")
        return None

def save_config(config, config_file_path):
    try:
        with open(config_file_path, 'w') as config_file:
            json.dump(config, config_file, indent=4)
    except Exception as e:
        logger.error(f"Failed to save config: {e}")

def get_config_value(config, key):
    return config.get(key)

def get_config_section(config, section):
    return config.get(section, {})

def create_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
    except Exception as e:
        logger.error(f"Failed to create directory: {e}")

def get_absolute_path(relative_path):
    return os.path.abspath(relative_path)

def get_config_path():
    return os.path.join(Config.BASE_DIR, 'config.json')