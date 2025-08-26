# Base image
FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Install system dependencies (optional: helps pdfplumber & others)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    poppler-utils \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements first (to use cache if code changes but requirements don’t)
COPY app/requirements.txt .

# Install Python dependencies
# ✅ en_core_web_sm is installed directly from wheel (faster, no "python -m spacy download")
RUN pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir \
    https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl

# Copy app code (this will invalidate cache only if code changes)
COPY app /app/app

# Expose FastAPI port
EXPOSE 8000

# Start API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]



