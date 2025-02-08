FROM python:3.9-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    gcc \
    libssl-dev \
    && pip install pandas sqlalchemy pymssql openpyxl

# Set the working directory
WORKDIR /app

# Copy the Python script and Excel file into the container
COPY ./automate.py /app/automate.py
COPY ./data.xlsx /app/data.xlsx

# Run the Python script
CMD ["python", "automate.py"]
