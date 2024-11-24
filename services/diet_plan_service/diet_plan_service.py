from sqlalchemy.orm import Session
from dto.request_dto.dietitian_request_dto import DietPlanCreate
from dto.response_dto.dietitian_response_dto import DietPlanResponse
from repository.diet_plan_repository import DietPlanRepository

class DietPlanService:
    @staticmethod
    def create_diet_plan(db: Session, diet_plan: DietPlanCreate) -> DietPlanResponse:
        new_diet_plan = DietPlanRepository.create_diet_plan(db, diet_plan)
        return DietPlanResponse(
            id=new_diet_plan.id,
            client_id=new_diet_plan.client_id,
            title=new_diet_plan.title,
            meals=new_diet_plan.meals,
            nutrient_goals=new_diet_plan.nutrient_goals,
            restrictions=new_diet_plan.restrictions
        )

    @staticmethod
    def get_diet_plan(db: Session, diet_plan_id: int) -> DietPlanResponse:
        return DietPlanRepository.get_diet_plan_by_id(db, diet_plan_id)
