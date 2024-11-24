from typing import List
from pydantic import BaseModel, Field

class RequestDTO(BaseModel):
    age: int
    health_conditions: str
    activity_level: str
    preferences: str
    height: float
    weight: float

class IngredientOptimizationRequestDTO(BaseModel):
    ingredients: List[str] = Field(..., description="List of available ingredients")
    dietary_preferences: str = Field(..., description="Dietary preferences (e.g., vegetarian, vegan)")
    health_goals: str = Field(..., description="Health goals (e.g., weight loss, muscle gain)")
    calorie_limit: int = Field(..., description="Calorie limit for the recipes")