from datetime import datetime
from typing import Dict, List, Optional
from app.models.task import Task, TaskCreate, TaskUpdate, TaskStatus


class TasksStore:
    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self.counter = 0
    
    def get_tasks(self) -> List[Task]:
        return list(self.tasks.values())
    
    def get_task(self, task_id: int) -> Optional[Task]:
        return self.tasks.get(task_id)
    
    def create_task(self, task: TaskCreate) -> Task:
        self.counter += 1
        now = datetime.now()
        db_task = Task(
            id=self.counter,
            created_at=now,
            updated_at=now,
            **task.model_dump()
        )
        self.tasks[self.counter] = db_task
        return db_task
    
    def update_task(self, task_id: int, task_update: TaskUpdate) -> Optional[Task]:
        if task_id not in self.tasks:
            return None
        
        stored_task = self.tasks[task_id]
        update_data = task_update.model_dump(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(stored_task, field, value)
        
        stored_task.updated_at = datetime.now()
        return stored_task
    
    def delete_task(self, task_id: int) -> bool:
        if task_id not in self.tasks:
            return False
        
        del self.tasks[task_id]
        return True


tasks_store = TasksStore() 