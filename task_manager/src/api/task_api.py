from src.schemas.task_schema import Task
from src.services.task_service import save_task


def create_task(data):
    task = Task(**data)

    save_task(task)

    print("Task created successfully")