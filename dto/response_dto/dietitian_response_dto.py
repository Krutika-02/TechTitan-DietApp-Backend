from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class DietPlanResponse(BaseModel):
    id: int
    client_id: int
    title: str
    meals: List[Dict[str, str]]
    nutrient_goals: Dict[str, float]
    restrictions: Optional[List[str]]

    class Config:
        orm_mode = True

class DietitianDetailsResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    gender: str
    certificate: str
    clinic_name: float
    speecialization: float
    created_at: datetime
    updated_at: datetime
