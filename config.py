"""Opens the config.yaml file and parses it into a dict."""

import logging

import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

logger = logging.getLogger(__name__)

CONFIG_FILE_PATH = "config.yaml"


def open_config() -> dict:
    """Open the config file and parse the yaml contents."""
    try:
        with open(CONFIG_FILE_PATH) as config_file:
            try:
                return yaml.load(config_file, Loader=Loader)
            except Exception:
                logger.error(f"Error: Failed to parse config file {CONFIG_FILE_PATH}")
                logger.exception()
                return {}
    except Exception:
        logger.info(
            f"Didn't find config file {CONFIG_FILE_PATH}, using default values for run."
        )
        return {}
