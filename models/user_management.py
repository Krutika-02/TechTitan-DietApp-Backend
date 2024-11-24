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

# from datetime import datetime, timezone
# from sqlalchemy import (
#     Column,
#     Integer,
#     String,
#     Boolean,
#     ForeignKey,
#     DateTime,
#     Text,
#     BigInteger,
# )
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.types import Enum

# Base = declarative_base()

# # User Info Model
# class UserInfo(Base):
#     __tablename__ = "user_info"

#     user_id = Column(Integer, primary_key=True)
#     first_name = Column(String(50), nullable=False)
#     last_name = Column(String(50), nullable=False)
#     email = Column(String(100), nullable=False, unique=True)
#     phone_number = Column(String(15), nullable=False, unique=True)
#     password = Column(String(255), nullable=False)  # Hashed password storage
#     gender = Column(Enum("Male", "Female", "Other", name="gender_enum"), nullable=False)
#     role = Column(String(20), nullable=False)  # "Dietitian" or "Client"
#     user_external_reference_id = Column(UUID(as_uuid=True), unique=True, nullable=False)
#     created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
#     updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
#     is_active = Column(Boolean, default=True)

#     # Relationships
#     user_logins = relationship("UserLogin", back_populates="user_info")
#     user_roles = relationship("UserRole", back_populates="user_info")
#     dietitian_details = relationship("DietitianDetails", back_populates="user_info", uselist=False)
#     client_details = relationship(
#         "ClientDetails",
#         back_populates="user_info",
#         foreign_keys="[ClientDetails.user_id]",  # Explicit foreign key
#         uselist=False
#     )


# # User Login Model
# class UserLogin(Base):
#     __tablename__ = "user_login"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("user_info.user_id"))
#     email = Column(String(100), nullable=True)
#     otp = Column(BigInteger, nullable=True)
#     otp_created_at = Column(DateTime, nullable=True)
#     access_token = Column(String(200), nullable=True)
#     created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
#     updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
#     user_external_reference_id = Column(UUID(as_uuid=True), unique=True, nullable=False)
#     is_active = Column(Boolean, default=True)

#     # Relationships
#     user_info = relationship("UserInfo", back_populates="user_logins")


# # Roles Model
# class Role(Base):
#     __tablename__ = "roles"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     role_name = Column(String(50), unique=True, nullable=False)  # e.g., "Dietitian", "Client"
#     created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
#     updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
#     is_active = Column(Boolean, default=True)

#     # Relationships
#     users = relationship("UserRole", back_populates="role")


# # User Roles Model
# class UserRole(Base):
#     __tablename__ = "user_roles"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("user_info.user_id"))
#     role_id = Column(Integer, ForeignKey("roles.id"))
#     created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
#     updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
#     is_active = Column(Boolean, default=True)

#     # Relationships
#     user_info = relationship("UserInfo", back_populates="user_roles")
#     role = relationship("Role", back_populates="users")


# # Dietitian Details Model
# class DietitianDetails(Base):
#     __tablename__ = "dietitian_details"

#     dietitian_id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("user_info.user_id"))
#     specialization = Column(String(255), nullable=False)
#     clinic_name = Column(String(255), nullable=True)
#     certifications = Column(Text, nullable=True)
#     created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
#     updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

#     # Relationships
#     user_info = relationship("UserInfo", back_populates="dietitian_details", uselist=False)

# # Client Details Model
# class ClientDetails(Base):
#     __tablename__ = "client_details"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("user_info.user_id"))
#     height = Column(Integer, nullable=True)  # Height in cm
#     weight = Column(Integer, nullable=True)  # Weight in kg
#     gender = Column(String(10), nullable=False)  # "Male", "Female", or "Other"
#     health_goals = Column(String(200), nullable=True)  # e.g., "Weight Loss"
#     food_preferences = Column(String(100), nullable=True)  # e.g., "Vegetarian"
#     dietitian_id = Column(Integer, ForeignKey("user_info.user_id"))  # Linked dietitian ID

#     created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
#     updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
#     is_active = Column(Boolean, default=True)

#     # Relationships
#     user_info = relationship(
#         "UserInfo",
#         back_populates="client_details",
#         foreign_keys="[ClientDetails.user_id]"  # Explicit foreign key for user_id
#     )
#     dietitian = relationship(
#         "UserInfo",
#         foreign_keys=[dietitian_id],  # Explicitly reference dietitian_id
#         backref="clients"  # Optional: to access clients from the dietitian's side
#     )
