from fastapi import FastAPI, Depends, HTTPException

from src.auth.auth_handler import (create_access_token)

from src.auth.auth_handler import verify_token

from src.schemas.auth_schema import LoginRequest

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.orm import session

from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.connection import (engine, session_local, Base)

from src.database.models import Task

from src.schemas.task_schema import (TaskRequest, TaskResponse)

from fastapi import (UploadFile, File)

import os

from fastapi import (UploadFile, File)

import uuid


app = FastAPI()

# create a fake user for authentication

fake_user = {
    "username": "admin",
    "password": "admin123"
}

# Security Scheme

security = HTTPBearer()

# Add Current User Dependency


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    payload = verify_token(token)

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload


# login endpoint

@app.post("/login")
async def login(user: LoginRequest):

    # verify user credentials
    if (
        user.username != fake_user["username"] or
        user.password != fake_user["password"]
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # generate JWT token

    access_token = create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}

# Protected route


@app.get("/protected")
async def protected_route(user=Depends(get_current_user)):
    return {
        "message": "Protected route accessed",
        "user": user
    }

# Create tables on startup


@app.on_event("startup")
async def startup():

    await create_tables()

# file types allowed for upload
ALLOWED_FILE_TYPES = [
    "image/jpeg",
    "image/png",
    "application/pdf"
]

MAX_FILE_SIZE = 5 * 1024 * 1024
# create tabels


async def create_tables():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )

# Dependency to get DB session


async def get_db():
    async with session_local() as db:
        yield db


# create task

@app.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskRequest, db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    new_task = Task(
        title=task.title,
        completed=task.completed
    )

    db.add(new_task)

    await db.commit()

    await db.refresh(new_task)

    return new_task

# read all tasks


@app.get("/tasks", response_model=list[TaskResponse])
async def get_tasks(db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    result = await db.execute(select(Task))
    return result.scalars().all()

# update task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, updated_task: TaskRequest, db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):

    result = await db.execute(select(task).filter(task.id == task_id))
    task = result.scalar_one_or_none()

    # check if task exists
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # update task
    task.title = updated_task.title
    task.completed = updated_task.completed

    await db.commit()
    await db.refresh(task)

    return task

# delete task


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):

    result = await db.execute(select(Task).filter(Task.id == task_id))
    task = result.scalar_one_or_none()

    # check if task exists
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    await db.delete(task)
    await db.commit()

    return {"detail": "Task deleted successfully"}


# file upload endpoint
@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    # Validate MIME type
    if file.content_type not in ALLOWED_FILE_TYPES:

        raise HTTPException(
            status_code=400,
            detail="Invalid file type"
        )

    # Read file content
    content = await file.read()

    # Validate file size
    if len(content) > MAX_FILE_SIZE:

        raise HTTPException(
            status_code=400,
            detail="File too large"
        )

    # Create uploads directory
    os.makedirs(
        "storage/uploads",
        exist_ok=True
    )

    # Generate safe unique filename

    unique_filename = (
        f"{uuid.uuid4()}.{file_extension}"
    )

    # Safe file path
    file_path = (
        f"storage/uploads/{unique_filename}"
    )

    # Store file locally
    with open(file_path, "wb") as buffer:

        buffer.write(content)

    return {
        "message": "File uploaded successfully",
        "original_filename": file.filename,
        "stored_filename": unique_filename,
        "content_type": file.content_type,
        "size": len(content)
    }
