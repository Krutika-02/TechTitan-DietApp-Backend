from fastapi import FastAPI, APIRouter, HTTPException
from dto.request_dto.ai_system_request_dto import RequestDTO, IngredientOptimizationRequestDTO
from dto.response_dto.ai_system_response_dto import ResponseDTO, IngredientOptimizationResponseDTO
from services.ai_system.ai_system import generate_diet_plan, generate_recipes

app = FastAPI()

router = APIRouter()

# Registering the diet plan endpoint
@router.post("/generate-diet-plan/", response_model=ResponseDTO)
async def get_diet_plan(request: RequestDTO):
    try:
        # Call the service to generate the diet plan
        result = generate_diet_plan(request)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Registering the ingredient optimization endpoint
@router.post("/optimize-ingredients/", response_model=IngredientOptimizationResponseDTO)
async def optimize_ingredients(request: IngredientOptimizationRequestDTO):
    """
    Generate recipes based on available ingredients and user preferences.
    """
    try:
        response = generate_recipes(request)
        return response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Add the router to the FastAPI app
app.include_router(router)
