from fastapi import FastAPI, APIRouter, HTTPException
from models.dietitian import DietPlanRequest, DietPlanResponse, ModifyDietPlanRequest
from services.diet_plan_service.diet_plan_service import create_diet_plan_service, modify_diet_plan_service

# Create router instance
router = APIRouter()

app = FastAPI()

# API endpoint to create a diet plan
@router.post("/create", response_model=DietPlanResponse)
def create_diet_plan(diet_plan: DietPlanRequest):
    try:
        # Call the service layer to handle business logic
        return create_diet_plan_service(diet_plan)
    except ValueError as e:
        # Handle validation errors raised by the service
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/modify", response_model=DietPlanResponse)
def modify_diet_plan(request: ModifyDietPlanRequest):
    # Call the service layer to handle modifications
    response = modify_diet_plan_service(request)

    if response.status == "failure":
        raise HTTPException(status_code=400, detail=response.message)

    return response
