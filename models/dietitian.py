from pydantic import BaseModel, Field, constr, conlist
from datetime import date
from typing import List, Optional

class Meal(BaseModel):
    meal_type: constr(strip_whitespace=True, min_length=1)
    meal_name: constr(strip_whitespace=True, min_length=1)
    portion_size: constr(strip_whitespace=True, min_length=1)
    calories: int = Field(gt=0, description="Number of calories, must be greater than zero")
    ingredients: conlist(str, min_length=1)  # Use min_length instead of min_items
    instructions: constr(strip_whitespace=True, min_length=1)

class DailyPlan(BaseModel):
    day: constr(strip_whitespace=True, min_length=1)
    meals: conlist(Meal, min_length=1)  # Use min_length instead of min_items

class DietPlanRequest(BaseModel):
    dietitian_id: constr(strip_whitespace=True, min_length=1)
    client_id: constr(strip_whitespace=True, min_length=1)
    diet_plan_name: constr(strip_whitespace=True, min_length=1)
    start_date: date
    end_date: date
    plan_details: conlist(DailyPlan, min_length=1)  # Use min_length instead of min_items

class ModifyDietPlanRequest(BaseModel):
    diet_plan_id: constr(strip_whitespace=True, min_length=1)
    modifications: Optional[dict] = None

class DietPlanResponse(BaseModel):
    status: str
    diet_plan_id: Optional[str] = None 
    message: str
