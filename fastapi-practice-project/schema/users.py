from pydantic import BaseModel
from typing import TypedDict

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str
    isActive: bool

class UserResponse(BaseModel):
    name: str
    email: str
    role: str
    isActive: bool

class LoginRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str