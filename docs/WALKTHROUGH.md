# DevTrack AI - Submission Walkthrough

## 1. System Structure
The project follows a clean separation of concerns:
- **`backend/`**: Flask-based REST API handling business logic, database interactions, and AI analysis.
    - **`routes/`**: API endpoint definitions.
    - **`services/`**: Core logic including the `AIService`.
    - **`schemas/`**: Data validation using Marshmallow.
    - **`models/`**: Database models (SQLAlchemy).
- **`frontend/`**: React application (Vite) for the user interface.
- **`ai-guidance/`**: Documentation and rules for AI agents, ensuring safe and predictable code generation and behavior.

This structure ensures that the API, UI, and AI logic are decoupled, making the system easier to maintain and scale.

## 2. AI Usage & Strategy
AI is used to enhance task management by automatically analyzing task descriptions for **Risk** and **Complexity**.

- **Current Implementation**: A robust rule-based engine simulates the AI's decision-making process. This ensures deterministic behavior and allows for easy testing without incurring API costs or latency during development.
- **Constraint Enforcement**: The `ai-guidance` directory contains strict rules (`prompting-rules.md`, `agents.md`) that define how an actual LLM would be prompted. This includes:
    - **JSON-only output**: Preventing parsing errors.
    - **Read-only analysis**: The AI cannot modify the state directly; it can only suggest values.
    - **Fallback mechanisms**: The system handles cases where the AI might fail or return invalid data.

## 3. Risk Mitigation
- **Input Validation**: usage of `marshmallow` schemas in the backend ensures that all incoming data is validated before processing.
- **Safe Defaults**: If the AI analysis (or rule-based engine) fails or returns uncertainty, the system defaults to "Medium" risk/complexity to prompt human review.
- **No Direct Execution**: The AI analysis is purely informational. It does not trigger automated deployments or destructive actions.

## 4. Extension Approach
To extend this system (e.g., adding real LLM support):
1.  **Modify `backend/services/ai_service.py`**: Replace the rule-based logic with an API call to OpenAI (or similar).
2.  **Use System Prompts**: Inject the content from `ai-guidance/prompting-rules.md` as the system message to the LLM.
3.  **Keep Validation**: The existing JSON validation logic in the service layer would remain to ensure the LLM's output conforms to the schema.
