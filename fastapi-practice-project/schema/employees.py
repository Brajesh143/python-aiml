from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str
    salary: float

class EmployeeResponse(BaseModel):
    pass