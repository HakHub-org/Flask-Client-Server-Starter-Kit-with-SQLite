"""
Database Initialization Script
"""

import os
import sqlite3
from dotenv import load_dotenv

def initialize_database():
    """
    Initialize the database and create the required tables.
    """
    load_dotenv()

    env = os.getenv("ENVIRONMENT")
    env_mapping = {"development": "DEV", "test": "TEST", "production": "PROD"}
    db_url = os.getenv(f"DATABASE_URL_{env_mapping.get(env, '').upper()}")

    if db_url is None:
        raise ValueError("Invalid environment or database URL not set")

    connection = sqlite3.connect(db_url)
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (post_id) REFERENCES posts (id),
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

    connection.commit()
    connection.close()
    print("Database initialized and tables created successfully.")

if __name__ == "__main__":
    initialize_database()
