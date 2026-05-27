from pydantic import BaseModel

class TaskRequest(BaseModel):
    title: str
    completed: bool = False

class TaskResponse(TaskRequest):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True  