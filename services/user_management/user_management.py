from sqlalchemy.orm import Session
from models.user_management import User
from custom_utilities.auth import hash_password
import uuid

def register_user(db: Session, user_data: dict):
    hashed_password = hash_password(user_data["password"])
    new_user = User(
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        email=user_data["email"],
        phone_number=user_data["phone_number"],
        hashed_password=hashed_password,
        gender=user_data["gender"],
        role=user_data["role"],
        user_external_reference_id=str(uuid.uuid4())
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
