import base64
import msgpack
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

# Mock function to simulate receiving encoded sensor data
def receive_sensor_data():
    # Simulate encoded sensor data (temperature and humidity values)
    sensor_data = {
        'temperature': np.random.normal(loc=20, scale=5, size=100),
        'humidity': np.random.normal(loc=50, scale=10, size=100)
    }
    # Encode the data using msgpack and base64 for simulation purposes
    encoded_data = base64.b64encode(msgpack.packb(sensor_data))
    return encoded_data

# Function to decode and unpack sensor data
def decode_and_unpack(data):
    decoded_data = base64.b64decode(data)
    unpacked_data = msgpack.unpackb(decoded_data, raw=False)
    return unpacked_data

# Function to train the Isolation Forest model
def train_isolation_forest(data):
    model = IsolationForest(n_estimators=100, contamination='auto', random_state=42)
    model.fit(data)
    return model

# Function to predict anomalies using the Isolation Forest model
def predict_anomalies(model, data):
    predictions = model.predict(data)
    # Mark anomalies with a boolean flag (True for anomalies, False for normal)
    data['is_anomaly'] = predictions == -1
    return data

# Main processing function
def process_sensor_data():
    encoded_data = receive_sensor_data()
    unpacked_data = decode_and_unpack(encoded_data)

    # Convert unpacked data to DataFrame for easier processing and modeling
    sensor_data_df = pd.DataFrame(unpacked_data)

    # Assuming your dataset is large enough and representative for training
    # For demonstration, using the same data for training and prediction
    model = train_isolation_forest(sensor_data_df)

    # Predict anomalies in the data
    processed_data = predict_anomalies(model, sensor_data_df)

    anomalies = processed_data[processed_data['is_anomaly']]
    print(f"Detected {len(anomalies)} anomalies")

process_sensor_data()