import pandas as pd
from sqlalchemy import create_engine

# Connexion à la base de données
engine = create_engine('postgresql://admin:securepass@db:5432/sensordata')

def detect_anomalies():
    # Charger les dernières données des capteurs
    query = "SELECT sensor_id, timestamp, temperature, humidity FROM sensor_data ORDER BY timestamp DESC LIMIT 100"
    data = pd.read_sql(query, engine)

    # Définir les seuils d'anomalie
    temp_threshold = 30  # Température en degrés Celsius
    humidity_threshold = 80  # Humidité en pourcentage

    # Détecter les anomalies
    data['temp_anomaly'] = data['temperature'] > temp_threshold
    data['humidity_anomaly'] = data['humidity'] > humidity_threshold

    # Afficher les anomalies détectées
    anomalies = data[(data['temp_anomaly']) | (data['humidity_anomaly'])]
    print(anomalies)

if __name__ == '__main__':
    detect_anomalies()
