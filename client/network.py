# client/network.py

import requests

def get_server_data(url):
    response = requests.get(url)
    return response.json()
