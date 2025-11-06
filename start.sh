#!/bin/bash

# Upgrade pip
python -m ensurepip --upgrade
python -m pip install --upgrade pip

# Install dependencies
python -m pip install -r app/requirements.txt

# Start the FastAPI app
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
