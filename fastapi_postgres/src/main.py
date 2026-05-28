from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.connection import (engine, session_local, Base)

from src.database.models import Task

from src.schemas.task_schema import (TaskRequest,TaskResponse)

app = FastAPI()

# Create tables on startup

@app.on_event("startup")
async def startup():

    await create_tables()


#create tabels

async def create_tables():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )

# Dependency to get DB session
async def get_db():
    async with session_local() as db:
        yield db


#create task

@app.post("/tasks", response_model=TaskResponse)
async def create_task(
    task: TaskRequest,
    db: AsyncSession = Depends(get_db)
):
    new_task = Task(
        title = task.title,
        completed = task.completed
    )

    db.add(new_task)

    await db.commit()

    await db.refresh(new_task)

    return new_task

#read all tasks
@app.get("/tasks", response_model=list[TaskResponse])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task))
    return result.scalars().all()

#update task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, updated_task: TaskRequest, db: AsyncSession = Depends(get_db)):
    
    result = await db.execute(select(task).filter(task.id == task_id))
    task = result.scalar_one_or_none()

    # check if task exists
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    #update task
    task.title = updated_task.title
    task.completed = updated_task.completed

    await db.commit()
    await db.refresh(task)

    return task

#delete task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Task).filter(Task.id == task_id))
    task = result.scalar_one_or_none()

    # check if task exists
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    await db.delete(task)
    await db.commit()

    return {"detail": "Task deleted successfully"}








