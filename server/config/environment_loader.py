"""
Environment Loader
"""

import os
from dotenv import load_dotenv

def load_environment_variables():
    """
    Load environment variables from a .env file.
    """
    load_dotenv()
    print("Environment variables loaded.")
