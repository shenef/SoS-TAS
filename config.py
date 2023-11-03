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
        with open(CONFIG_FILE_PATH, encoding="utf-8") as config_file:
            try:
                return yaml.load(config_file, Loader=Loader)
            except Exception:
                logger.error(f"Error: Failed to parse config file {CONFIG_FILE_PATH}")
                logger.exception()
                return {}
    except Exception:
        logger.info(f"Didn't find config file {CONFIG_FILE_PATH}, using default values for run.")
        return {}


_route_config: dict[str, bool] = {}


def open_route_config(path: str) -> bool:
    """
    Open a route config file and parse the yaml contents.

    Assign the global `_route_config` and return true if everything worked.
    """
    global _route_config
    try:
        with open(path, encoding="utf-8") as route_config:
            try:
                _route_config = yaml.load(route_config, Loader=Loader)
                return True
            except Exception:
                logger.error(f"Error: Failed to parse route config file {path}")
                logger.exception()
                return False
    except Exception:
        logger.warning(f"Didn't find route config file {path}")
        return False


def get_route_config() -> dict[str, bool]:
    """Return a handle to the global `_route_config`."""
    return _route_config


def set_route_config(route_config: dict[str, bool]) -> None:
    """Assign the global `_route_config`."""
    global _route_config
    _route_config = route_config
