# dto/response_dto/ingredient_optimization_response_dto.py
from pydantic import BaseModel, Field
from typing import List, Dict

class ResponseDTO(BaseModel):
    bmi: float
    diet_plan: str

class RecipeDTO(BaseModel):
    name: str = Field(..., description="Name of the recipe")
    ingredients: List[str] = Field(..., description="List of ingredients used in the recipe")
    instructions: str = Field(..., description="Step-by-step cooking instructions")
    nutrition_info: Dict[str, str] = Field(..., description="Nutritional breakdown (calories, protein, carbs, fats)")

class IngredientOptimizationResponseDTO(BaseModel):
    recipes: List[RecipeDTO] = Field(..., description="List of optimized recipes")
