# Dockerfile for API Gateway

# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy API Gateway code
COPY api-gateway.py .

# Copy frontend directory
COPY frontend frontend

# Expose port 5000
EXPOSE 5000

# Run the API Gateway
CMD ["python", "api-gateway.py"]
