import requests
import time
import random
import os
import logging

# Configuration through environment variables
API_ENDPOINT = os.getenv('API_ENDPOINT', 'http://api-gateway:5000/api/sensors')
FREQUENCY_SECONDS = int(os.getenv('FREQUENCY_SECONDS', '60'))
TEMPERATURE_RANGE = eval(os.getenv('TEMPERATURE_RANGE', '(20, 30)'))
HUMIDITY_RANGE = eval(os.getenv('HUMIDITY_RANGE', '(30, 60)'))

# Setup logging
logging.basicConfig(level=logging.INFO)

def generate_sensor_data():
    return {
        'temperature': random.uniform(*TEMPERATURE_RANGE),
        'humidity': random.uniform(*HUMIDITY_RANGE),
        # ... other sensor data ...
    }

def send_data_to_api(data):
    try:
        response = requests.post(API_ENDPOINT, json=data)
        response.raise_for_status()  # Raises an exception for HTTP errors
        logging.info(f"Data sent successfully: {data}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send data: {e}")

def simulate_sensor_data():
    while True:
        data = generate_sensor_data()
        send_data_to_api(data)
        time.sleep(FREQUENCY_SECONDS)

if __name__ == "__main__":
    simulate_sensor_data()
