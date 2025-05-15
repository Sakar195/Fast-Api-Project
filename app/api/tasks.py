from fastapi import APIRouter, HTTPException, status
from typing import List

from app.models.task import Task, TaskCreate, TaskUpdate
from app.core.tasks_store import tasks_store

router = APIRouter()


@router.get("/", response_model=List[Task])
async def get_tasks():
    """
    Get all tasks
    """
    return tasks_store.get_tasks()


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    """
    Create a new task
    """
    return tasks_store.create_task(task)


@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """
    Get a specific task by ID
    """
    task = tasks_store.get_task(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return task


@router.patch("/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    """
    Update a task by ID
    """
    updated_task = tasks_store.update_task(task_id, task_update)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return updated_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    """
    Delete a task by ID
    """
    success = tasks_store.delete_task(task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return None 