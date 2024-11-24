from pydantic import BaseModel
from typing import List, Dict, Optional

class DietPlanResponse(BaseModel):
    id: int
    client_id: int
    title: str
    meals: List[Dict[str, str]]
    nutrient_goals: Dict[str, float]
    restrictions: Optional[List[str]]

    class Config:
        orm_mode = True