import openai
import os
from dotenv import load_dotenv
from dto.request_dto.ai_system_request_dto import RequestDTO, IngredientOptimizationRequestDTO
from dto.response_dto.ai_system_response_dto import ResponseDTO, IngredientOptimizationResponseDTO, RecipeDTO

# Load environment variables from a .env file
load_dotenv()

# Set API key from environment variable or directly
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to calculate BMI
def calculate_bmi(weight: float, height: float) -> float:
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    return round(weight / (height ** 2), 2)

# Function to generate diet plan using OpenAI API
def generate_diet_plan(data: RequestDTO) -> ResponseDTO:
    try:
        # Calculate BMI
        body_mass_index = calculate_bmi(data.weight, data.height)
        
        # Construct the prompt for OpenAI
        prompt = f"""
        Generate a personalized diet plan for a client who is {data.age} years old. 
        Health conditions: {data.health_conditions}. Activity level: {data.activity_level}. Preferences: {data.preferences}.
        Height: {data.height} m, Weight: {data.weight} kg, BMI: {body_mass_index}.
        Provide meal plans with recipes, portion sizes, and nutrient breakdown including calories, protein, carbs, and fats.
        """

        # Generate response from OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=1,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=1
        )
        
        # Extract the diet plan from the response
        diet_plan = response['choices'][0]['message']['content']
        return ResponseDTO(bmi=body_mass_index, diet_plan=diet_plan)
    except Exception as e:
        raise ValueError(f"Error generating diet plan: {str(e)}")

def generate_recipes(request: IngredientOptimizationRequestDTO) -> IngredientOptimizationResponseDTO:
    try:
        # Construct the prompt for OpenAI
        prompt = f"""
        You are a recipe generator. The user has the following ingredients: {', '.join(request.ingredients)}. 
        Their dietary preference is {request.dietary_preferences}, and their health goal is {request.health_goals}. 
        Generate recipes that align with these requirements and fit within a calorie limit of {request.calorie_limit} per recipe.
        Each recipe should include: 
        - A name
        - Ingredients used
        - Step-by-step instructions
        - Nutritional breakdown (calories, protein, carbs, fats)
        """

        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system", "content": "You are a helpful assistant for generating recipes."
            }, {
                "role": "user", "content": prompt
            }],
            temperature=0.7,
            max_tokens=1500
        )
        recipes_text = response['choices'][0]['message']['content']
        try:
            lines = recipes_text.split("\n")
            if len(lines) < 4:
                raise ValueError("Invalid recipe format: expected at least four lines of content.")
            name = lines[0].strip()
            ingredients = lines[1].split(", ")  
            instructions = "\n".join(lines[2:])  
            nutrition_info = {}
            nutrition_info_str = lines[-1].strip()  
            if nutrition_info_str:
                nutrition_lines = nutrition_info_str.split(", ")
                for item in nutrition_lines:
                    if ": " in item:
                        key, value = item.split(": ")
                        nutrition_info[key.lower()] = value
                    else:
                        print(f"Skipping invalid nutritional item: {item}")
            structured_recipes = [{
                "name": name,
                "ingredients": ingredients,
                "instructions": instructions,
                "nutrition_info": nutrition_info
            }]

        except Exception as e:
            raise ValueError(f"Error parsing recipes: {str(e)}")
        recipes = [
            RecipeDTO(
                name=recipe.get('name'),
                ingredients=recipe.get('ingredients'),
                instructions=recipe.get('instructions'),
                nutrition_info=recipe.get('nutrition_info'),
            )
            for recipe in structured_recipes
        ]

        return IngredientOptimizationResponseDTO(recipes=recipes)
    except Exception as e:
        raise ValueError(f"Error generating recipes: {str(e)}")
