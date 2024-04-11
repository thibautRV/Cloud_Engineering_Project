from sqlalchemy import create_engine, text, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database connection details
HOST = 'localhost'
PORT = '5432'
DATABASE = 'Numeric Farm'
USER = 'postgres'
PASSWORD = 'datasql78$'

# Create the SQLAlchemy connection string
DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
Base = declarative_base()

class SensorData(Base):
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True)
    sensor_id = Column(String)
    plant_id = Column(Integer)
    sensor_version = Column(String)
    measure_type = Column(String)
    measure_value = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def add_sensor_data(sensor_id, plant_id, sensor_version, measure_type, measure_value):
    session = Session()
    new_data = SensorData(sensor_id=sensor_id, plant_id=plant_id, sensor_version=sensor_version,
                          measure_type=measure_type, measure_value=measure_value)
    session.add(new_data)
    session.commit()
    session.close()

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