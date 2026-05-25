from fastapi import FastAPI, HTTPException
from src.schemas.task_schema import TaskRequest, TaskResponse

app = FastAPI()

tasks = []
task_counter = 1


# CREATE Task
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskRequest):

    global task_counter

    new_task = {
        "id": task_counter,
        "title": task.title,
        "completed": task.completed,
        "description": task.description
    }

    tasks.append(new_task)

    task_counter += 1

    return new_task


# READ All Tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks


# READ Single Task
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# UPDATE Task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskRequest):

    for task in tasks:

        if task["id"] == task_id:

            task["title"] = updated_task.title
            task["completed"] = updated_task.completed
            task["description"] = updated_task.description

            return task

    raise HTTPException(status_code=404, detail="Task not found")


# DELETE Task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:

            deleted_task = tasks.pop(index)

            return {
                "message": "Task deleted",
                "task": deleted_task
            }

    raise HTTPException(status_code=404, detail="Task not found")