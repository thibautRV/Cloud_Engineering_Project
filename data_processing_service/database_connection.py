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

DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

print("Database URI:", DATABASE_URI)  # Debug print to check the URI

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

if __name__ == "__main__":
    init_db()
