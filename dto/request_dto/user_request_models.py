from typing import Optional, Literal
from datetime import date
from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    password: str
    gender: Literal["Male", "Female", "Other"]  # Restrict values to valid options
    goal: str
    height: float  
    weight: float
    date_of_birth: date
    user_external_reference_id: str

class LoginRequest(BaseModel):
    email: str
    password: str

class UpdateUserProfileRequest(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
