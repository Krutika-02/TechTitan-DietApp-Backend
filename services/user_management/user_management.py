import uuid
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from models.user_management import User
from custom_utilities.auth import hash_password
from repository.user_management import UserRepository
from dto.response_dto.user_response_dto import UserResponseDTO

def register_user(db: Session, user_data: dict):
    hashed_password = hash_password(user_data["password"])
    new_user = User(
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        email=user_data["email"],
        phone_number=user_data["phone_number"],
        hashed_password=hashed_password,
        gender=user_data["gender"],
        goal=user_data.get("goal", None), 
        height=user_data.get("height", None),  
        weight=user_data.get("weight", None),  
        date_of_birth=user_data.get("date_of_birth", None),
        user_external_reference_id=str(uuid.uuid4())
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

class UserService:

    @staticmethod
    def get_user_details(db: Session, user_id: int) -> UserResponseDTO:
        return UserRepository.fetch_user_details(db, user_id)

    @staticmethod
    def get_all_user_details(db: Session) -> List[UserResponseDTO]:
        users = UserRepository.fetch_all_user_details(db)
        return [
            UserResponseDTO(
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                phone_number=user.phone_number,
                gender=user.gender,
                goal=user.goal,
                height=user.height,
                weight=user.weight,
                date_of_birth=user.date_of_birth,
                is_active=user.is_active,
            )
            for user in users
        ]
