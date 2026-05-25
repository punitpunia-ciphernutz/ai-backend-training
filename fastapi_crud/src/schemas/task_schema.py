from pydantic import BaseModel
from typing import Optional


#req model

class TaskRequest(BaseModel):
    title: str
    completed: bool = False
    description: Optional[str] = None

#response model
class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool

