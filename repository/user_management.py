from typing import Optional,List
from sqlalchemy.orm import Session
from models.user_management import User

class UserRepository:
    @staticmethod
    def fetch_user_details(db: Session, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def fetch_all_user_details(db: Session) -> List[User]:
        return db.query(User).all()
