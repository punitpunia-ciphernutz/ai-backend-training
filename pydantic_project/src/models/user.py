from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None
    address: Optional[Address] = None

