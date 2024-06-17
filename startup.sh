#!/bin/bash

# Activate server virtual environment
source server_venv/bin/activate
pip install -r server/requirements.txt
deactivate

# Activate client virtual environment
source client_venv/bin/activate
pip install -r client/requirements.txt
deactivate

echo "Setup complete. Use the following commands to run the server and client:"
echo "source server_venv/bin/activate; python server/app.py"
echo "source client_venv/bin/activate; python client/main.py"
