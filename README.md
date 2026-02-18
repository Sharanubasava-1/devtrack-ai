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

## Key Technical Decisions

### Architecture
- **Monorepo Structure**: Kept backend and frontend in a single repository for simplicity and easier development coordination.
- **Flask over Django**: Chosen for its lightweight nature and flexibility, allowing for a focused API implementation without unnecessary boilerplate.
- **Vite for Frontend**: Selected for its fast build times and modern development experience compared to Create React App.

### AI Integration
- **Rule-Based Fallback**: The system uses a rule-based approach for risk analysis as a default. This ensures the application remains functional even without an external AI service or API keys.
- **Structured JSON Output**: AI agents (simulated or real) are constrained to return strict JSON to ensure predictable parsing and system stability.

### Data Validation
- **Marshmallow Schemas**: Used for backend validation to enforce data integrity and prevent invalid states before they reach the database.
- **Prop Types**: (Implied/Recommended) used in frontend for component interface safety.

## Trade-offs
- **SQLite Database**: Used for simplicity and zero-configuration setup. While not suitable for high-concurrency production environments, it is sufficient for this assessment and easy to migrate to PostgreSQL.
- **No User Authentication**: Omitted to focus on the core task management and AI analysis features, keeping the scope manageable for the assessment.

## Future Improvements
- **True AI Integration**: Connect to OpenAI or a local LLM for more nuanced task analysis.
- **Task Dependencies**: Implement a DAG (Directed Acyclic Graph) for complex task dependencies.
- **User Accounts**: Add authentication and authorization for multi-user support.

