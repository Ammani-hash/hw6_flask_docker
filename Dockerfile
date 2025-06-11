# Use Python as base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy everything into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask uses
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
