# Base Python image
FROM python:3.9-slim-buster

# Main dir
WORKDIR /central

# Copies requirements to docker container (/app)
COPY requirements.txt ./

# Requirements installation
RUN pip install --no-cache-dir -r requirements.txt

# Copies dirs to docker container (/app)
# FIX THIS
COPY . . 

# Port 
EXPOSE 8000

# Run this command
CMD ["python", "manage.py", "runserver", "0:8000"]
