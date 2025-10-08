# HarshaOS Local Development Guide

## Prerequisites
- Python 3.11
- Node.js 18+
- npm
- (Optional) Ollama runtime for local LLM models

## Backend setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/db/db_init.py
python backend/main.py
```

The API listens on `http://localhost:9080`.

## Frontend setup
```bash
cd ui
npm install
npm start
```

An Electron window will open after Vite finishes compiling.

## Environment variables
Create a `.env` file based on `.env.example` to override configuration such as IMAP credentials or Ollama paths.
