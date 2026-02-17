import sys
import os

# Add backend directory to sys.path
sys.path.append(os.getcwd())

from app import app, db
from models.task_model import Task
from services.ai_service import ai_service

def verify():
    print("Verifying DevTrack AI Setup...")
    
    with app.app_context():
        # 1. Create Tables
        db.create_all()
        print("✅ Database tables created.")

        # 2. Test AI Service
        description = "Build payment system for the new e-commerce platform"
        ai_result = ai_service.analyze_task(description)
        
        if ai_result['risk_level'] == 'High':
            print(f"✅ AI Service correctly identified High Risk for: '{description}'")
        else:
            print(f"❌ AI Service FAILED. Expected High Risk, got {ai_result['risk_level']}")
            return

        if ai_result['complexity'] == 'High': # 'system' keyword
             print(f"✅ AI Service correctly identified High Complexity.")
        else:
             print(f"❌ AI Service FAILED. Expected High Complexity, got {ai_result['complexity']}")

        # 3. Test Database Insertion
        new_task = Task(
            title="Test Task",
            description=description,
            risk_level=ai_result['risk_level'],
            complexity=ai_result['complexity'],
            ai_warning=ai_result['ai_warning']
        )
        db.session.add(new_task)
        db.session.commit()
        
        saved_task = Task.query.first()
        if saved_task and saved_task.title == "Test Task":
            print("✅ Task successfully saved to SQLite database.")
        else:
            print("❌ Database save failed.")
            return

        print("\n🎉 Verification Successful! The backend and AI service are operational.")

if __name__ == "__main__":
    verify()
