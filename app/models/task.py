from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    status: TaskStatus = TaskStatus.TODO


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[TaskStatus] = None


class TaskInDB(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime


class Task(TaskInDB):
    class Config:
        from_attributes = True 