from sqlalchemy.orm import Session
from models.user_management import UserInfo, DietitianDetails, ClientDetails

def create_user(session, user_info: UserInfo):
    session.add(user_info)
    session.commit()
    session.refresh(user_info)
    return user_info

def get_user_by_email(db: Session, email: str):
    return db.query(UserInfo).filter(UserInfo.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(UserInfo).filter(UserInfo.user_id == user_id).first()

# Additional methods to work with user roles, dietitian, and client details

def create_dietitian_details(db: Session, dietitian_details: DietitianDetails):
    db.add(dietitian_details)
    db.commit()
    db.refresh(dietitian_details)
    return dietitian_details

def create_client_details(db: Session, client_details: ClientDetails):
    db.add(client_details)
    db.commit()
    db.refresh(client_details)
    return client_details

def get_dietitian_by_user_id(db: Session, user_id: int):
    return db.query(DietitianDetails).filter(DietitianDetails.user_id == user_id).first()

def get_client_by_user_id(db: Session, user_id: int):
    return db.query(ClientDetails).filter(ClientDetails.user_id == user_id).first()
