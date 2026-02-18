import pytest
import sys
import os

# Add the parent directory to the path so we can import app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from models.task_model import Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_get_tasks_empty(client):
    """Test getting tasks when none exist."""
    rv = client.get('/api/tasks')
    assert rv.status_code == 200
    assert rv.get_json() == []

def test_create_task(client):
    """Test creating a new task."""
    rv = client.post('/api/tasks', json={
        'title': 'Test Task',
        'description': 'This is a test task description.'
    })
    assert rv.status_code == 201
    json_data = rv.get_json()
    assert json_data['title'] == 'Test Task'
    assert 'id' in json_data

def test_create_task_invalid(client):
    """Test creating a task with missing fields."""
    rv = client.post('/api/tasks', json={
        'title': 'Incomplete Task'
    })
    assert rv.status_code == 400

def test_ai_risk_analysis(client):
    """Test that risk analysis is performed on creation."""
    rv = client.post('/api/tasks', json={
        'title': 'Risky Task',
        'description': 'Integration with payment gateway and critical security systems.'
    })
    assert rv.status_code == 201
    json_data = rv.get_json()
    # Based on keywords, this might be Medium or High, but definitely not None
    assert json_data.get('risk_level') in ['Medium', 'High']
