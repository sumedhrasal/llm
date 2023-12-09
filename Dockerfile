# Use the official Python 3.10 base image
FROM python:3.10

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Flask will run on
EXPOSE 8081

# Define the command to run the Flask application
# CMD ["flask", "run", "--host", "0.0.0.0"]
CMD ["python", "run_api.py"]
