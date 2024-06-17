"""
Logging Configuration
"""

import logging
import os

def setup_logging(env):
    """
    Set up logging configuration based on the environment.

    Args:
        env (str): The current environment ('development', 'testing', 'production').
    """
    logging_config = {
        "development": {
            "level": "DEBUG",
            "file": "logs/dev.log"
        },
        "testing": {
            "level": "INFO",
            "file": "logs/test.log"
        },
        "production": {
            "level": "WARNING",
            "file": "logs/prod.log"
        }
    }

    log_config = logging_config[env]
    logging.basicConfig(filename=log_config["file"], level=getattr(logging, log_config["level"]))

# Setup logging
current_env = os.getenv("ENVIRONMENT")  # Should be set in .env
setup_logging(current_env)
