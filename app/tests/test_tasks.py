import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.task import TaskStatus

client = TestClient(app)


def test_create_task():
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "status": TaskStatus.TODO
    }
    
    response = client.post("/api/v1/tasks/", json=task_data)
    assert response.status_code == 201
    
    created_task = response.json()
    assert created_task["title"] == task_data["title"]
    assert created_task["description"] == task_data["description"]
    assert created_task["status"] == task_data["status"]
    assert "id" in created_task
    assert "created_at" in created_task
    assert "updated_at" in created_task


def test_get_tasks():
    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task():
    # First create a task
    task_data = {"title": "Get Test Task"}
    create_response = client.post("/api/v1/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Now retrieve it
    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == task_data["title"]


def test_update_task():
    # First create a task
    task_data = {"title": "Update Test Task"}
    create_response = client.post("/api/v1/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Now update it
    update_data = {"status": TaskStatus.DONE}
    response = client.patch(f"/api/v1/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == task_data["title"]
    assert response.json()["status"] == update_data["status"]


def test_delete_task():
    # First create a task
    task_data = {"title": "Delete Test Task"}
    create_response = client.post("/api/v1/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Delete it
    response = client.delete(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 204
    
    # Verify it's gone
    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 404 