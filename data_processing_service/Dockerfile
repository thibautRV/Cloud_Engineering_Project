# Use an official Python runtime as a base image
FROM python:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/data_processing_service/requirements.txt

# Make port 1000 available to the world outside this container
EXPOSE 1000

# Set the PYTHONPATH to include the working directory
#ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/data_processing_service/"

# Run database_connection.py when the container launches
CMD ["python", "/usr/src/app/data_processing_service/database_connection.py"]
