from src.api.task_api import create_task

task_data = {
    "title": "Learn Clean Architecture",
    "completed": False,
    "description": "Practice backend structure"
}

create_task(task_data)