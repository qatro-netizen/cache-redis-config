import redis
import json
import os
from typing import Optional, Dict, Any

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file.

    Args:
        config_path: The path to the JSON configuration file.

    Returns:
        A dictionary containing the configuration.

    Raises:
        FileNotFoundError: If the configuration file is not found.
        json.JSONDecodeError: If the configuration file is not valid JSON.
    """
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in configuration file: {config_path} - {e}", e.doc, e.pos)


def get_redis_connection(config: Dict[str, Any]) -> redis.Redis:
    """
    Establishes a connection to Redis using the provided configuration.

    Args:
        config: A dictionary containing Redis connection parameters.
               Expected keys: 'host', 'port', 'db', 'password' (optional), other redis options.

    Returns:
        A Redis connection object.

    Raises:
        redis.exceptions.ConnectionError: If a connection to Redis cannot be established.
    """
    try:
        redis_config = {
            'host': config['host'],
            'port': config['port'],
            'db': config['db']
        }

        if 'password' in config and config['password']:
            redis_config['password'] = config['password']

        # Add any other redis options from the config
        for key, value in config.items():
            if key not in ['host', 'port', 'db', 'password']:
                redis_config[key] = value

        r = redis.Redis(**redis_config)
        r.ping()  # Verify connection
        return r
    except redis.exceptions.ConnectionError as e:
        raise redis.exceptions.ConnectionError(f"Failed to connect to Redis: {e}")


def get_environment_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """
    Retrieves an environment variable.

    Args:
        key: The name of the environment variable.
        default: The default value to return if the environment variable is not set.

    Returns:
        The value of the environment variable, or the default value if it is not set.
    """
    return os.environ.get(key, default)