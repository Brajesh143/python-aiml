from schema.users import UserCreate, UserResponse
from fastapi import Depends, APIRouter
from database import get_db
from sqlalchemy.orm import Session
from model.users import User
from auth.security import hash_password

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = User(
            name=user.name,
            email=user.email,
            password=hash_password(user.password),
            role=user.role,
            isActive=1
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

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()

    return users