from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus
import os
from datetime import datetime
from contextlib import contextmanager

# Encoding all parts of the URI that could potentially contain special characters
USER = quote_plus(os.getenv('POSTGRES_USER', 'postgres'))
PASSWORD = quote_plus(os.getenv('POSTGRES_PASSWORD', 'datasql'))
HOST = quote_plus(os.getenv('POSTGRES_HOST', 'database'))
PORT = quote_plus(os.getenv('POSTGRES_PORT', '5432'))
DATABASE = quote_plus(os.getenv('POSTGRES_DB', 'NumericFarm'))

DATABASE_URI = "postgresql://postgres:datasql@database:5432/NumericFarm"
#f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

Base = declarative_base()

class SensorData(Base):
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True)
    sensor_id = Column(String)
    plant_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)

engine = create_engine(DATABASE_URI)
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

def add_sensor_data(sensor_id, plant_id):#, sensor_version, measure_type, measure_value):
    with session_scope() as session:
        new_data = SensorData(sensor_id=sensor_id, plant_id=plant_id)#, sensor_version=sensor_version,
                            #measure_type=measure_type, measure_value=measure_value)
        session.add(new_data)

def delete_sensor_data(id):
    session = Session()
    data = session.query(SensorData).filter(SensorData.id == id).first()
    if data:
        session.delete(data)
        session.commit()
    session.close()

# Initialiser la base de données au premier lancement
import time
import psycopg2
from psycopg2 import OperationalError

if __name__ == "__main__":
    #init_db()
    def create_conn():
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
        return conn

    conn = create_conn()