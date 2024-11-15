FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app ./app

# Set default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
