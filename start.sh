#!/bin/bash
# Start FastAPI app on Railway

# Install dependencies (if not already installed)
pip install --upgrade pip
pip install -r app/requirements.txt

# Start the FastAPI app with uvicorn
# Railway sets the PORT environment variable automatically
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
