from typing import List, Dict, Optional
from pydantic import BaseModel

class DietPlanCreate(BaseModel):
    client_id: int
    title: str
    meals: List[Dict[str, str]]  # e.g., [{"time": "08:00 AM", "items": ["Oatmeal"], "portionSize": "1 bowl"}]
    nutrient_goals: Dict[str, float]  # e.g., {"calories": 2000, "protein": 150, "carbs": 250, "fat": 70}
    restrictions: Optional[List[str]]