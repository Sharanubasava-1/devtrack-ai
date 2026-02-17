# DevTrack AI

DevTrack AI is a developer task tracker that uses AI to detect risk levels and complexity in task descriptions.

## Features
- **Task Management**: Create, update, delete tasks.
- **AI Analysis**: Automatically detects Risk (High/Medium/Low) and Complexity based on task descriptions.
- **Modern UI**: Clean, dark-mode inspired interface.

## Tech Stack
- **Backend**: Python, Flask, SQLAlchemy, SQLite
- **Frontend**: React, Vite
- **AI**: Rule-based analysis (extensible to OpenAI)

## Setup
### Backend
1. Navigate to `backend`:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python app.py
   ```

### Frontend
1. Navigate to `frontend`:
   ```bash
   cd frontend
   ```
2. Install dependencies (if not using docker):
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

## API Endpoints
- `GET /api/tasks`: List all tasks.
- `POST /api/tasks`: Create a new task.
- `DELETE /api/tasks/<id>`: Delete a task.
