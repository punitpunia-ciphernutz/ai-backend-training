import json
from src.schemas.task_schema import Task
from src.utils.logger import logger

TASK_FILE = "data/tasks.json"


def save_task(task: Task):
    task_data = task.model_dump()

    try:
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)

    except:
        tasks = []

    tasks.append(task_data)

    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

    logger.info(f"Task saved: {task.title}")