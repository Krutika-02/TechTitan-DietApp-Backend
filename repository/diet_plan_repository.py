# Simulated database
database = []

def find_diet_plan(diet_plan_id: str):
    for diet_plan in database:
        if diet_plan["diet_plan_id"] == diet_plan_id:
            return diet_plan
    return None

def update_diet_plan(diet_plan_id: str, modifications: dict):
    diet_plan = find_diet_plan(diet_plan_id)
    if not diet_plan:
        return False

    # Apply modifications
    for key, value in modifications.items():
        diet_plan[key] = value
    return True
