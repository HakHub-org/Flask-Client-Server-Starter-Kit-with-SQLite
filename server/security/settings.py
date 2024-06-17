"""
Security Settings
"""

from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

if os.getenv("HTTPS_ENABLED") == "true":
    # Configure HTTPS settings here
    pass

cors = CORS(app, resources={r"/*": {"origins": os.getenv("ALLOWED_ORIGINS").split(",")}})
