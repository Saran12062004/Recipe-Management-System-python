import json
from utils.decorators import log_function_call, measure_time
from utils.generators import step_generator

# Load recipes from JSON file (for persistence)
def load_recipes():
    try:
        with open('data/recipes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save recipes to JSON file
def save_recipes(recipes):
    with open('data/recipes.json', 'w') as file:
        json.dump(recipes, file, indent=4)

# Add a recipe
@log_function_call
@measure_time
def add_recipe(recipes, name, ingredients, steps):
    recipes[name] = {
        'ingredients': ingredients.split(','),
        'steps': steps.split(',')
    }
    save_recipes(recipes)
    print("Recipe added successfully!")

# View a recipe
@log_function_call
@measure_time
def view_recipe(recipes, name):
    recipe = recipes.get(name)
    if recipe:
        print(f"Ingredients: {recipe['ingredients']}")
        print(f"Steps: {recipe['steps']}")
    else:
        print("Recipe not found!")

# Search for recipes by ingredient
@log_function_call
@measure_time
def search_by_ingredient(recipes, ingredient):
    found_recipes = [name for name, recipe in recipes.items() if ingredient in recipe['ingredients']]
    return found_recipes

