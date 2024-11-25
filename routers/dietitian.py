from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from custom_utilities.database import get_db
from custom_utilities.auth import verify_token
from dto.request_dto.dietitian_request_dto import DietPlanCreate
from dto.response_dto.dietitian_response_dto import DietPlanResponse
from services.diet_plan_service.diet_plan_service import DietPlanService

router = APIRouter()
app = FastAPI()

# @router.get("/{1}", response_model=DietitianDetailsResponse)
# def get_dietitian_details(dietitian_id: int, db: Session = Depends(get_db)):
#     dietitian_details = DietPlanService.get_dietitian_details(db, dietitian_id)
#     if not diet_plan:
#         raise HTTPException(status_code=404, detail="Dietitian not found")
#     return dietitian_details

@router.post("/", response_model=DietPlanResponse)
def create_diet_plan(diet_plan: DietPlanCreate, db: Session = Depends(get_db),token_payload: dict = Depends(verify_token)):
    return DietPlanService.create_diet_plan(db, diet_plan)

@router.get("/{diet_plan_id}", response_model=DietPlanResponse)
def get_diet_plan(diet_plan_id: int, db: Session = Depends(get_db),token_payload: dict = Depends(verify_token)):
    diet_plan = DietPlanService.get_diet_plan(db, diet_plan_id)
    if not diet_plan:
        raise HTTPException(status_code=404, detail="Diet plan not found")
    return diet_plan
