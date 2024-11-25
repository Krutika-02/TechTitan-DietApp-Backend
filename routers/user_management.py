from datetime import timedelta
from typing import List
from fastapi import APIRouter, FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from custom_utilities.database import get_db
from custom_utilities.auth import verify_token
from services.user_management.user_management import register_user, UserService
from models.user_management import User
from dto.request_dto.user_request_models import RegisterRequest,LoginRequest, UserRequestDTO
from dto.response_dto.user_response_dto import LoginResponse, UserResponseDTO
from custom_utilities.auth import verify_password, create_access_token

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

app = FastAPI()

@router.post("/register")
def register(register_request: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == register_request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user = register_user(db, register_request.dict())
    return {"message": "User registered successfully", "user_id": user.id}

@router.post("/login", response_model=LoginResponse)
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(User).filter(User.email == login_request.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Verify password
    if not verify_password(login_request.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Create access token
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }

@router.get("/{user_id}", response_model=UserResponseDTO)
def get_user_details(user_id: int, db: Session = Depends(get_db),token_payload: dict = Depends(verify_token)):
    user_details = UserService.get_user_details(db, user_id)
    if not user_details:
        raise HTTPException(status_code=404, detail="User not found")
    return user_details

@router.get("/", response_model=List[UserResponseDTO])
def get_all_user_details(db: Session = Depends(get_db),token_payload: dict = Depends(verify_token)):
    user_details = UserService.get_all_user_details(db)
    if not user_details:
        raise HTTPException(status_code=404, detail="No users found")
    return user_details  # Directly return the list of UserResponseDTO objects
