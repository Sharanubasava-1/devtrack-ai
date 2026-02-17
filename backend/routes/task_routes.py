from flask import Blueprint, request, jsonify
from models.task_model import db, Task
from schemas.task_schema import task_schema, tasks_schema
from services.ai_service import ai_service
from datetime import datetime

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description', '')
        deadline_str = data.get('deadline')
        
        deadline = None
        if deadline_str:
            try:
                deadline = datetime.fromisoformat(deadline_str.replace('Z', '+00:00'))
            except ValueError:
               pass # Handle invalid date format gracefully (or return error)

        # AI Analysis
        ai_result = ai_service.analyze_task(description, deadline)
        
        new_task = Task(
            title=title,
            description=description,
            deadline=deadline,
            risk_level=ai_result['risk_level'],
            complexity=ai_result['complexity'],
            ai_warning=ai_result['ai_warning']
        )
        
        db.session.add(new_task)
        db.session.commit()
        
        return task_schema.dump(new_task), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@task_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return tasks_schema.dump(tasks), 200

@task_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'status' in data:
        task.status = data['status']
    if 'priority' in data:
        task.priority = data['priority']
    if 'deadline' in data:
        # Update deadline logic
        try:
           task.deadline = datetime.fromisoformat(data['deadline'].replace('Z', '+00:00'))
        except:
           pass

    # Re-run AI analysis if description or deadline changed? 
    # For now, let's keep it simple or maybe only on create? 
    # Let's re-run if description is updated to keep it dynamic.
    if 'description' in data or 'deadline' in data:
         ai_result = ai_service.analyze_task(task.description, task.deadline)
         task.risk_level = ai_result['risk_level']
         task.complexity = ai_result['complexity']
         task.ai_warning = ai_result['ai_warning']

    db.session.commit()
    return task_schema.dump(task), 200

@task_bp.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200
