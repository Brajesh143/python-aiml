from fastapi import APIRouter, Depends, HTTPException
from schema.users import LoginRequest, TokenResponse
from database import get_db
from sqlalchemy.orm import Session
from auth.security import verify_password
from dependencies.auth import get_current_user
from model.users import User
from auth.jwt import create_access_token
from sqlalchemy import select

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login", response_model=TokenResponse)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.execute(
        select(User).where(User.email == request.email)
    ).scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(request.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        user_id=user.id,
        role=user.role
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/profile")
def get_profile(
    current_user=Depends(get_current_user)
):

    return {
        "message": "You are authenticated",
        "user": current_user
    }