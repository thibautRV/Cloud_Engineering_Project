from sqlalchemy import create_engine, Column, Integer, String, DateTime, JSON
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus
import os
from datetime import datetime
from contextlib import contextmanager

import time
import psycopg2
from psycopg2 import OperationalError
from flask import Flask, jsonify, request

# Encoding all parts of the URI that could potentially contain special characters
USER = quote_plus(os.getenv('POSTGRES_USER', 'postgres'))
PASSWORD = quote_plus(os.getenv('POSTGRES_PASSWORD', 'datasql'))
HOST = quote_plus(os.getenv('POSTGRES_HOST', 'database'))
PORT = quote_plus(os.getenv('POSTGRES_PORT', '5432'))
DATABASE = quote_plus(os.getenv('POSTGRES_DB', 'NumericFarm'))

DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
#"postgresql://postgres:datasql@database:5432/NumericFarm"


# Declare the base
Base = declarative_base()

# Define the SensorData model
class SensorData(Base):
    __tablename__ = 'sensor_data'
    reading_id = Column(Integer, primary_key=True)
    sensor_id = Column(String)
    sensor_version = Column(String)
    plant_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    measures = Column(JSON)  # Assuming measures is intended to be stored as a JSON-like structure
    
# Initialize the engine with the database URI
engine = create_engine(DATABASE_URI, echo=True)  # Set echo=True for debug

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Database error occurred: {e}")
        raise
    finally:
        session.close()

def healthcheck_logic():
    conn = None
    while not conn:
        try:
            conn = psycopg2.connect(
                dbname="NumericFarm",
                user="postgres",
                password="datasql",
                host="database"
            )
            print("Database connection successful")
        except OperationalError as e:
            print(e)
            time.sleep(5)
    return True

def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db()

    return app

app = create_app()

@app.route('/health', methods=['GET'])
def healthcheck():
    if healthcheck_logic():
        return jsonify({"status": "healthy"}), 200
    else:
        return jsonify({"status": "unhealthy"}), 500

@app.route('/add_sensor_data', methods=['POST'])
def add_sensor_data():
    data = request.json
    with session_scope() as session:
        new_data = SensorData(
                sensor_id=data["sensor_id"],
                sensor_version=data["sensor_version"],
                plant_id=data["plant_id"],
                timestamp=data["time"],
                measures=data["measures"]
                )
        session.add(new_data)
    return jsonify({"message": "Data added successfully"}), 201

@app.route('/del_sensor_data', methods=['DELETE'])
def delete_sensor_data(id):
    with session_scope() as session:
        data = session.query(SensorData).filter(SensorData.id == id).first()
        if data:
            session.delete(data)
            session.commit()
            return jsonify({"message": "Data deleted successfully"}), 200
        else:
            return jsonify({"error": "Data not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=1000)
    