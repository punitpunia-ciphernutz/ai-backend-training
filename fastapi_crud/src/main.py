from fastapi import FastAPI
from src.schemas.task_schema import Task

app = FastAPI()

# In-memory storage
tasks = []


# CREATE Task
@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {
        "message": "Task created",
        "task": task
    }


# READ All Tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# READ Single Task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task.id == task_id:
            return task

    return {"error": "Task not found"}


# UPDATE Task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    for index, task in enumerate(tasks):

        if task.id == task_id:
            tasks[index] = updated_task

            return {
                "message": "Task updated",
                "task": updated_task
            }

    return {"error": "Task not found"}


# DELETE Task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for index, task in enumerate(tasks):

        if task.id == task_id:
            deleted_task = tasks.pop(index)

            return {
                "message": "Task deleted",
                "task": deleted_task
            }

    return {"error": "Task not found"}