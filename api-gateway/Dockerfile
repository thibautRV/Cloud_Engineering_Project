# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/api-gateway/requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for the Flask application
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the PYTHONPATH to include the working directory
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

# Command to run the Flask application
CMD ["flask", "run"]
