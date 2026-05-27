from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import session

from src.database.connection import (engine, session_local, Base)

from src.database.models import Task

from src.schemas.task_schema import (TaskRequest,TaskResponse)

app = FastAPI()

#create tabels

Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

#create task

@app.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskRequest,
    db: session = Depends(get_db)
):
    new_task = Task(
        title = task.title,
        completed = task.completed
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return new_task

#read all tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: session = Depends(get_db)):
    return db.query(Task).all()

#update task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskRequest, db: session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    # check if task exists
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    #update task
    task.title = updated_task.title
    task.completed = updated_task.completed

    db.commit()
    db.refresh(task)

    return task

#delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    # check if task exists
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()

    return {"detail": "Task deleted successfully"}








