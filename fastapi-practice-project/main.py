import asyncio
from database import engine, Base, get_db
from pydantic import BaseModel, Field
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from model.employees import Employee
from model.users import User
from schema.users import LoginRequest, TokenResponse
from auth.jwt import create_access_token
from dependencies.auth import get_current_user, require_admin

Base.metadata.create_all(bind=engine)

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    quantity: int

class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str
    salary: float

class UserCreate(BaseModel):
    email: str
    password: str

# @app.get("/products")
# async def get_products():
#     await asyncio.sleep(2)
#     return [
#         Product(name="Product 1", price=10.99, quantity=5),
#         Product(name="Product 2", price=19.99, quantity=3),
#         Product(name="Product 3", price=5.99, quantity=10),
#     ]

users = {
    "admin@test.com": {
        "id": 101,
        "email": "admin@test.com",
        "password": "secret",
        "role": "admin"
    },
    "manager@test.com": {
        "id": 102,
        "email": "manager@test.com",
        "password": "secret",
        "role": "manager"
    },
    "employee@test.com": {
        "id": 103,
        "email": "employee@test.com",
        "password": "secret",
        "role": "employee"
    }
}

@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):

    employees = db.query(Employee).all()

    return employees

@app.post("/employees")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    new_employee = Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        salary=employee.salary
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return {
        "message": "Employee created successfully",
        "employee": {
            "id": new_employee.id,
            "name": new_employee.name,
            "email": new_employee.email,
            "department": new_employee.department,
            "salary": new_employee.salary
        }
    }


@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    current_user=Depends(require_admin)
):

    return {
        "message": f"Employee {employee_id} deleted"
    }

app.post("/users")
def create_user(
    user: UserCreate, 
    db: Session = Depends(get_db())
):

    new_user = User(
            email=user.email,
            password=user.password
        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "message": "User created successfully",
        "employee": {
            "id": new_user.id
        }
    }

@app.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):

    user = users.get(request.email)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if user["password"] != request.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        user_id=user["id"],
        role=user["role"]
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.get("/profile")
def get_profile(
    current_user=Depends(get_current_user)
):

    return {
        "message": "You are authenticated",
        "user": current_user
    }


# async def get_user():
#     await asyncio.sleep(2)
#     return "user"

# async def get_orders():
#     await asyncio.sleep(2)
#     return "orders"

# async def main():
#     user = await get_user()
#     orders = await get_orders()
#     print(user)
#     print(orders)

# asyncio.run(main())