from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database connection details
HOST = 'localhost'
PORT = '5432'
DATABASE = 'Numeric Farm'
USER = 'postgres'
PASSWORD = 'datasql78$'

# Create the SQLAlchemy connection string
DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'


def verify_connection(uri):
    try:
        # Create an engine instance
        engine = create_engine(uri, echo=True)  # `echo=True` enables SQL logging
        
        # Connect to the database by creating a session
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Execute a query to fetch the PostgreSQL version
        # Use the text() function to wrap your SQL command
        result = session.execute(text("SELECT version();"))
        
        # Fetch and print the result
        version = result.fetchone()
        print("Connected to PostgreSQL version:", version[0])
        
        # Close the session
        session.close()
        
    except SQLAlchemyError as e:
        print("Failed to connect to the database.")
        print(e)

# Call the function with your DATABASE_URI
verify_connection(DATABASE_URI)
