import os
from flask import Flask, Request, jsonify
import base64
import msgpack

app = Flask(__name__)

# Use environment variables for configuration
port = int(os.environ.get("FLASK_PORT", 5000))

@app.route('/collectData', methods=['POST'])
def collect_data():
    try:
        encoded_data = Request.data
        if not encoded_data:
            return jsonify({"status": "error", "message": "Empty data payload."}), 400
        
        decoded_data = base64.b64decode(encoded_data)
        sensor_data = msgpack.unpackb(decoded_data, raw=False)

        # Placeholder for data processing
        print(sensor_data)

        return jsonify({"status": "success", "message": "Data received successfully."}), 200
    except (base64.binascii.Error, msgpack.exceptions.UnpackException):
        return jsonify({"status": "error", "message": "Invalid data format."}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=port)
