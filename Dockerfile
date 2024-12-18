# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY Flask-Website/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir rasa

# Copy the rest of your application code
COPY . .

# Expose the port on which Rasa will run
EXPOSE 5005

# Define the command to run your application
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "5005"]
