from sqlalchemy import Column, Integer, String, Boolean, JSON, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    phone_number = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    user_external_reference_id = Column(UUID(as_uuid=True), unique=True, nullable=False)
    gender = Column(String, nullable=False)
    goal = Column(String, nullable=True)  
    height = Column(Float, nullable=True)  
    weight = Column(Float, nullable=True)  
    date_of_birth = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)

class DietPlan(Base):
    __tablename__ = "diet_plans"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    meals = Column(JSON, nullable=False)  # JSON field to store meal details
    nutrient_goals = Column(JSON, nullable=False)  # JSON field for nutrient goals
    restrictions = Column(JSON, nullable=True)  # JSON field for dietary restrictions
