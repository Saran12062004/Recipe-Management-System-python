from recipes.recipe_management import load_recipes, add_recipe, view_recipe, search_by_ingredient
from utils.generators import step_generator

def main():
    recipes = load_recipes()

    while True:
        print("\nOptions:")
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. Search Recipe by Ingredient")
        print("4. Generate Steps")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ")
            steps = input("Enter steps (comma-separated): ")
            add_recipe(recipes, name, ingredients, steps)
        
        elif choice == '2':
            name = input("Enter recipe name to view: ")
            view_recipe(recipes, name)
        
        elif choice == '3':
            ingredient = input("Enter ingredient to search: ")
            found_recipes = search_by_ingredient(recipes, ingredient)
            if found_recipes:
                print("Recipes found:", found_recipes)
            else:
                print("No recipes found with that ingredient.")
        
        elif choice == '4':
            name = input("Enter recipe name to generate steps: ")
            recipe = recipes.get(name)
            if recipe:
                steps_gen = step_generator(recipe['steps'])
                for step in steps_gen:
                    input(step)
            else:
                print("Recipe not found.")
        
        elif choice == '5':
            print("Exiting Recipe Management System.")
            break

if __name__ == "__main__":
    main()
