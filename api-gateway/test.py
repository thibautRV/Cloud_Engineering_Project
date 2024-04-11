import requests
import base64
import msgpack

# Replace this dictionary with your actual sensor data
sensor_data = {
    'sensor_id': '123',
    'plant_id': '456',
    'sensor_version': '1.0',
    'measure_type': 'temperature',
    'measure_value': 23.5
}

# Encode and pack data
packed_data = msgpack.packb(sensor_data)
encoded_data = base64.b64encode(packed_data)

# Send POST request
response = requests.post('http://localhost:5000/collectData', data=encoded_data)
print(response.text)
