from fastapi import APIRouter, FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from custom_utilities.database import SessionLocal
from services.user_management.user_management import register_user
from models.user_management import User
from dto.request_dto.user_request_models import RegisterRequest,LoginRequest
from dto.response_dto.user_response_dto import LoginResponse
from custom_utilities.auth import verify_password, create_access_token, role_required
from datetime import timedelta

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
        data={"sub": user.email, "role": user.role},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }

@router.get("/user/{user_id}")
def get_user(user_id: int, user: dict = Depends(role_required(["dietitian", "client"]))):
    # Logic to fetch user details
    return {"user_id": user_id, "role": user["role"]}

@router.get("/users", dependencies=[Depends(role_required(["dietitian"]))])
def get_all_users():
    # Only dietitians can access this endpoint
    return {"message": "List of all users"}

@router.put("/user/{user_id}")
def update_user(
    user_id: int,
    user_update: dict,
    user: dict = Depends(role_required(["client", "dietitian"])),
):
    # Both roles can update users, but logic can restrict specific conditions
    return {"user_id": user_id, "updated": user_update}
