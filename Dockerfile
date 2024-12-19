FROM python:3.9-slim-buster  

WORKDIR /app

# Install system dependencies and clean up apt cache
RUN apt-get update 
# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt 

# Copy your application code
COPY . /app 
WORKDIR /app

RUN apt-get update


# Set the entrypoint
CMD ["python3", "app.py"]