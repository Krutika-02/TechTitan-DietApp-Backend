from uuid import uuid4
from datetime import date
from models.dietitian import DietPlanRequest, DietPlanResponse, ModifyDietPlanRequest
from repository.diet_plan_repository import find_diet_plan, update_diet_plan

# Simulated database
database = []

# Helper function to validate date range
def validate_date_range(start_date: date, end_date: date):
    if end_date < start_date:
        raise ValueError("End date must be greater than or equal to start date")

# Service function to create a diet plan
def create_diet_plan_service(diet_plan: DietPlanRequest) -> DietPlanResponse:
    # Validate date range
    validate_date_range(diet_plan.start_date, diet_plan.end_date)

    # Simulate creating a unique ID and saving to a database
    diet_plan_id = f"plan_{uuid4().hex}"
    database.append({
        "diet_plan_id": diet_plan_id,
        **diet_plan.dict()
    })

    # Return a success response
    return DietPlanResponse(
        status="success",
        diet_plan_id=diet_plan_id,
        message="Diet plan created successfully."
    )

def modify_diet_plan_service(request: ModifyDietPlanRequest) -> DietPlanResponse:
    # Validate if the diet plan exists
    diet_plan = find_diet_plan(request.diet_plan_id)
    if not diet_plan:
        return DietPlanResponse(
            status="failure",
            message="Diet plan not found."
        )
    
    # Attempt to update the diet plan
    success = update_diet_plan(request.diet_plan_id, request.modifications)
    if not success:
        return DietPlanResponse(
            status="failure",
            message="Failed to update the diet plan."
        )
    
    return DietPlanResponse(
        status="success",
        message="Diet plan updated successfully."
    )
