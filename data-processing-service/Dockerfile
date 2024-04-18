# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/data_processing_service/requirements.txt

# Run database_connection.py when the container launches
CMD ["python", "database_connection.py"]
