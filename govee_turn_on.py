import os
import json
import requests

# Grab API Key from environment variable and set MAC Address
api_key = os.environ['GOVEE_API_KEY']
device_mac = os.environ['DEVICE_MAC_ADDRESS']
device_model = os.environ['DEVICE_MODEL']

# Set the URL for the Govee API endpoint
url = f'https://developer-api.govee.com/v1/devices/control'

# Set the headers for the request
headers = {
    "Govee-API-Key": api_key,
    "Content-Type": "application/json"
}

payload = {
        "device": device_mac,
        "model": device_model,
        "cmd": {
            "name": "turn",
            "value": "on"
        }
    }

try:
    # Make the API request to turn on the lamp
    response = requests.put(url, json=payload, headers=headers)
    response.raise_for_status()
    # Check if the request was successful
    if response.ok:
        print('Lamp turned on successfully.')
except requests.exceptions.HTTPError as err:
    print(f'HTTP error occurred: {err}')
except requests.exceptions.RequestException as err:
    print(f'Other error occurred: {err}')
