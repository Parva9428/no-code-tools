# No-Code Tools Directory

A modern directory of no-code tools built with Flask, FastAPI, and Next.js, featuring a dark/light theme toggle.

## Project Structure

```
no-code-tools/
├── backend/
│   ├── flask_app/         # Flask backend
│   └── fastapi_app/      # FastAPI backend
└── frontend/            # Next.js frontend
```

## Setup Instructions

1. Install backend dependencies:
```bash
cd backend/flask_app
pip install -r requirements.txt

cd ../fastapi_app
pip install -r requirements.txt
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Run the applications:
- Flask backend: `python flask_app/app.py`
- FastAPI backend: `uvicorn fastapi_app.main:app --reload`
- Frontend: `npm run dev`

## Features
- Modern, responsive UI
- Dark/Light theme toggle
- Tool categories and filtering
- Search functionality
- Tool ratings and reviews
