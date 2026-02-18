from flask import Blueprint, request, jsonify
from models.task_model import db, Task
from schemas.task_schema import task_schema, tasks_schema
from datetime import datetime

task_bp = Blueprint('task_bp', __name__)


# -----------------------
# AI Analysis Function
# -----------------------
def analyze_task(title, description):
    text_to_analyze = (title or "") + " " + (description or "")
    text = text_to_analyze.lower()

    if not text.strip():
        return "Low", "Low", "No content to analyze."

    # Complexity Keywords
    high_complexity_keywords = [
        "ai", "machine learning", "neural network", "payment", 
        "authentication", "security", "encryption", "blockchain",
        "microservices", "infrastructure"
    ]
    medium_complexity_keywords = [
        "api", "database", "backend", "frontend", "integration", 
        "migration", "testing", "deploy", "pipeline"
    ]

    # Risk Keywords
    high_risk_keywords = [
        "payment", "financial", "security", "auth", "authentication",
        "password", "secret", "key", "token", "credential", "login",
        "signup", "register", "admin", "production", "db drop"
    ]
    medium_risk_keywords = [
        "data", "user", "api", "database", "migration", "privacy"
    ]

    # Complexity Logic
    if any(word in text for word in high_complexity_keywords):
        complexity = "High"
    elif any(word in text for word in medium_complexity_keywords):
        complexity = "Medium"
    else:
        complexity = "Low"

    # Risk Logic
    if any(word in text for word in high_risk_keywords):
        risk = "High"
    elif any(word in text for word in medium_risk_keywords):
        risk = "Medium"
    else:
        risk = "Low"

    # Warning Generation
    if risk == "High":
        warning = "CRITICAL: This task involves sensitive security or financial components. Review carefully."
    elif complexity == "High":
        warning = "Complex task detected. Ensure proper planning and testing."
    else:
        warning = "No major risks detected."

    return complexity, risk, warning


# -----------------------
# GET all tasks
# -----------------------
@task_bp.route('', methods=['GET'])
def get_tasks():
    try:
        tasks = Task.query.order_by(Task.id.desc()).all()
        return jsonify([task.to_dict() for task in tasks]), 200
    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# -----------------------
# CREATE new task
# -----------------------
@task_bp.route('', methods=['POST'])
def create_task():
    try:
        data = request.get_json()

        title = data.get('title')
        description = data.get('description')
        deadline_str = data.get('deadline')

        if not title:
            return jsonify({"error": "Title is required"}), 400

        deadline = None
        if deadline_str:
            deadline = datetime.fromisoformat(deadline_str.replace('Z', ''))

        # AI Analysis
        complexity, risk_level, ai_warning = analyze_task(title, description)

        new_task = Task(
            title=title,
            description=description,
            deadline=deadline,
            complexity=complexity,
            risk_level=risk_level,
            ai_warning=ai_warning
        )

        db.session.add(new_task)
        db.session.commit()

        return jsonify(new_task.to_dict()), 201

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# -----------------------
# DELETE task
# -----------------------
@task_bp.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted"}), 200
    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500
