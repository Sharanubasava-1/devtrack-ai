from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='Todo') # Todo, In Progress, Done
    priority = db.Column(db.String(20), default='Medium') # Low, Medium, High
    deadline = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # AI Analysis Fields
    risk_level = db.Column(db.String(20), nullable=True) # Low, Medium, High
    complexity = db.Column(db.String(20), nullable=True) # Low, Medium, High
    ai_warning = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "deadline": self.deadline.isoformat() if self.deadline else None,
            "risk_level": self.risk_level,
            "complexity": self.complexity,
            "ai_warning": self.ai_warning
        }
