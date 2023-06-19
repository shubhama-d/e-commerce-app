FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .
# Expose the port on which the frontend service will run
EXPOSE 5000
# Set the entrypoint command to run the WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.wsgi:app"]