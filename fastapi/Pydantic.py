from Pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    city: str
    age: int
    gender: str
    medical_history: List[str]