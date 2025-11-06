#!/bin/bash
set -e

# Move to app directory
cd /app

# Upgrade pip (simple)
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Start FastAPI app
uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
