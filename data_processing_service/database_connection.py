from sqlalchemy import create_engine, text, Column, Integer, String, Float, DateTime
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import os
from contextlib import contextmanager


# Environment variables should be set in your Docker container or environment configuration
HOST = os.getenv('POSTGRES_HOST', 'database')
PORT = os.getenv('POSTGRES_PORT', '5432')
DATABASE = os.getenv('POSTGRES_DB', 'NumericFarm')
USER = os.getenv('POSTGRES_USER', 'postgres')
PASSWORD = os.getenv('POSTGRES_PASSWORD', 'datasql78$')

# Create the SQLAlchemy connection string
DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

Base = declarative_base()

class SensorData(Base):
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True)
    sensor_id = Column(String)
    plant_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.now(datetime.UTC))

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
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
if __name__ == "__main__":
    init_db()
