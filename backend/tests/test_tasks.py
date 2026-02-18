import pytest
from app import app
from models.task_model import db


# -----------------------
# Test Configuration
# -----------------------

@pytest.fixture
def client():
    """
    Creates a Flask test client with an isolated in-memory database.
    This ensures tests do not affect real application data.
    """
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()


# -----------------------
# Test: Create Task Success
# -----------------------

def test_create_task_success(client):

    response = client.post(
        "/api/tasks",
        json={
            "title": "Test Task",
            "description": "Implement backend API",
            "deadline": "2026-04-26T00:00:00"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Test Task"
    assert data["description"] == "Implement backend API"

    # Verify AI analysis fields exist
    assert "complexity" in data
    assert "risk_level" in data
    assert "ai_warning" in data


# -----------------------
# Test: Create Task Missing Title
# -----------------------

def test_create_task_missing_title(client):

    response = client.post(
        "/api/tasks",
        json={
            "description": "This should fail"
        }
    )

    assert response.status_code == 400


# -----------------------
# Test: Get Tasks
# -----------------------

def test_get_tasks(client):

    client.post(
        "/api/tasks",
        json={
            "title": "Fetch Test Task",
            "description": "Testing GET endpoint"
        }
    )

    response = client.get("/api/tasks")

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Fetch Test Task"


# -----------------------
# Test: Delete Task
# -----------------------

def test_delete_task(client):

    create_response = client.post(
        "/api/tasks",
        json={
            "title": "Delete Test",
            "description": "Testing DELETE endpoint"
        }
    )

    task_id = create_response.get_json()["id"]

    delete_response = client.delete(f"/api/tasks/{task_id}")

    assert delete_response.status_code == 200

    # Verify task removed
    get_response = client.get("/api/tasks")

    data = get_response.get_json()

    assert len(data) == 0


# -----------------------
# Test: AI Analysis High Risk
# -----------------------

def test_ai_analysis_high_risk(client):

    response = client.post(
        "/api/tasks",
        json={
            "title": "Payment Gateway",
            "description": "Integrate Stripe payment system"
        }
    )

    data = response.get_json()

    assert response.status_code == 201

    assert data["complexity"] in ["High", "Medium", "Low"]
    assert data["risk_level"] in ["High", "Medium", "Low"]

    # Payment should usually be high risk
    assert data["risk_level"] == "High"


# -----------------------
# Test: AI Analysis Low Risk
# -----------------------

def test_ai_analysis_low_risk(client):

    response = client.post(
        "/api/tasks",
        json={
            "title": "Update README",
            "description": "Fix typos in documentation"
        }
    )

    data = response.get_json()

    assert response.status_code == 201

    assert data["risk_level"] == "Low"