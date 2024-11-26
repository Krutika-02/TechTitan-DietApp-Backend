from pydantic import BaseModel
from datetime import date
from typing import Optional

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

class UserResponseDTO(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    gender: str
    goal: str
    height: float
    weight: float
    date_of_birth: date
    is_active: bool

    class Config:
        orm_mode = True  # Enables direct mapping from SQLAlchemy models
