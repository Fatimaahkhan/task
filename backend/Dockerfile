# Use Python 3.9 as base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port 5000
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
