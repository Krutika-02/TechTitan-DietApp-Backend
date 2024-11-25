from sqlalchemy.orm import Session
from models.user_management import DietPlan
from dto.request_dto.dietitian_request_dto import DietPlanCreate

class DietPlanRepository:
    # @staticmethod
    # def get_dietitian_details(db: Session, diet_plan_id: int):
    #     return db.query(dietitian).filter(dietitian.id == diet_plan_id).first()
    
    @staticmethod
    def create_diet_plan(db: Session, diet_plan: DietPlanCreate) -> DietPlan:
        new_diet_plan = DietPlan(
            client_id=diet_plan.client_id,
            title=diet_plan.title,
            meals=diet_plan.meals,
            nutrient_goals=diet_plan.nutrient_goals,
            restrictions=diet_plan.restrictions
        )
        db.add(new_diet_plan)
        db.commit()
        db.refresh(new_diet_plan)
        return new_diet_plan

    @staticmethod
    def get_diet_plan_by_id(db: Session, diet_plan_id: int) -> DietPlan:
        return db.query(DietPlan).filter(DietPlan.id == diet_plan_id).first()
