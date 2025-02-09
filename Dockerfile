# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory into the container
COPY . /app

# Create logs directory
RUN mkdir -p /app/logs

# Install dependencies
RUN apt-get update && apt-get install -y \
    unixodbc-dev gcc libssl-dev \
    && pip install --no-cache-dir pandas sqlalchemy pymssql openpyxl lxml pyfiglet colorama

# Expose port 1433 for SQL Server connection (if needed)
EXPOSE 1433

# Run the main script when the container starts
CMD ["python", "automate.py"]
