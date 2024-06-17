"""
Database Connection Setup
"""

import os
import sqlite3
from dotenv import load_dotenv

def get_database_connection():
    """
    Get a database connection based on the environment.

    Returns:
        sqlite3.Connection: SQLite connection object.
    """
    load_dotenv()
    environment = os.getenv("ENVIRONMENT")
    env_mapping = {"development": "DEV", "test": "TEST", "production": "PROD"}
    database_url = os.getenv(f"DATABASE_URL_{env_mapping.get(environment, '').upper()}")

    if database_url is None:
        raise ValueError("Invalid environment or database URL not set")

    conn = sqlite3.connect(database_url)
    return conn

# Example usage
if __name__ == "__main__":
    conn = get_database_connection()
    print("Connected to database:", conn)
    conn.close()
