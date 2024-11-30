# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy Python files
COPY app.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "app.py"]
