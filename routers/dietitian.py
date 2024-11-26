from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from custom_utilities.database import get_db
from dto.request_dto.dietitian_request_dto import DietPlanCreate
from dto.response_dto.dietitian_response_dto import DietPlanResponse
from services.diet_plan_service.diet_plan_service import DietPlanService

router = APIRouter()
app = FastAPI()

@router.post("/", response_model=DietPlanResponse)
def create_diet_plan(diet_plan: DietPlanCreate, db: Session = Depends(get_db)):
    return DietPlanService.create_diet_plan(db, diet_plan)

@router.get("/{diet_plan_id}", response_model=DietPlanResponse)
def get_diet_plan(diet_plan_id: int, db: Session = Depends(get_db)):
    diet_plan = DietPlanService.get_diet_plan(db, diet_plan_id)
    if not diet_plan:
        raise HTTPException(status_code=404, detail="Diet plan not found")
    return diet_plan
