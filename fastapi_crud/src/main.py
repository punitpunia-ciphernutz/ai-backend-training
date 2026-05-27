import time
from fastapi import FastAPI, HTTPException, Request , BackgroundTasks
from fastapi.responses import JSONResponse
from src.schemas.task_schema import TaskRequest, TaskResponse

app = FastAPI()

# email function to simulate sending email in background

def send_email(email: str):

    print(f"Sending email to {email}...")

    time.sleep(5)

    print("Email sent successfully")

# Add route for email sending

@app.post("/send-email")
async def send_email_api(email: str, background_tasks: BackgroundTasks):

    background_tasks.add_task(send_email, email)

    return {
        "message": "Email is being sent in background"
    }

# Gloable exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        satus_code=500,
        content={
            "success": False,
            "error": {
                "message": "Internal server error",
                "Status code": 500
            }
        }
    )

# Global HTTP Exception Handler for specific HTTP errors like 404, 400, etc
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "message": exc.detail,
                "status_code": exc.status_code
            }
        }
    )

tasks = []
task_counter = 1

#middleware to log request details
@app.middleware("http")
async def log_requests(request: Request, call_next):
    
    #before request
    start_time = time.time()
    print(f"Request: {request.method} {request.url}")

    # forward request to the route
    response = await call_next(request)

    #after request
    process_time = time.time() - start_time
    print(f"Processed in {process_time:.4f} sec")
    
    #add custom header to response
    response.headers["X-Process-Time"] = str(process_time)

    return response


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