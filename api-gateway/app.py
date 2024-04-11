import os
from flask import Flask, request, jsonify  # Note that it should be 'request' with lowercase 'r'
from data_processing_service.database_connection import add_sensor_data
import base64
import msgpack

app = Flask(__name__)

# Use environment variables for configuration
port = int(os.environ.get("FLASK_PORT", 5000))

@app.route('/collectData', methods=['POST'])
def collect_data():
    try:
        # Get raw data from the POST request body
        encoded_data = request.data  # Use 'request' with lowercase 'r'
        if not encoded_data:
            return jsonify({"status": "error", "message": "Empty data payload."}), 400
        
        # Decode data from base64
        decoded_data = base64.b64decode(encoded_data)
        # Unpack data from msgpack
        sensor_data = msgpack.unpackb(decoded_data, raw=False)

        # Here we assume that sensor_data is a dictionary that contains all the necessary fields.
        # You need to adapt this part to match the structure of your actual sensor data.
        add_sensor_data(
            sensor_id=sensor_data['sensor_id'],
            plant_id=sensor_data['plant_id'],
            sensor_version=sensor_data['sensor_version'],
            measure_type=sensor_data['measure_type'],
            measure_value=sensor_data['measure_value']
        )

        return jsonify({"status": "success", "message": "Data received and stored successfully."}), 200
    except (base64.binascii.Error, msgpack.exceptions.UnpackException):
        return jsonify({"status": "error", "message": "Invalid data format."}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)