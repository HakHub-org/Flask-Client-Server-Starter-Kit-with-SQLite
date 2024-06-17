"""
Main Application Entrypoint
"""

import os
import sys
from flask import Flask, jsonify
from dotenv import load_dotenv

# Add the directory containing the 'config' module to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'config'))

from environment_loader import load_environment_variables
from logging_config import setup_logging

def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()
    load_environment_variables()

    # Setup logging
    current_env = os.getenv("ENVIRONMENT")
    setup_logging(current_env)

    @app.route('/ping', methods=['GET'])
    def ping():
        return jsonify({'message': 'pong'}), 200

    # Import and register blueprints (routes)
    from modules.routes import api_bp
    app.register_blueprint(api_bp)

    return app

def main():
    """
    Main entry point for the application.
    """
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=os.getenv("DEBUG_MODE") == "true")

if __name__ == "__main__":
    main()
