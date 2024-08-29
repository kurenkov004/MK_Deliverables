#importing necessary packages & functions
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from sqlalchemy.sql import select

# Database credentials
USERNAME = 'cf-python'
PASSWORD = 'password'
HOSTNAME = 'localhost'
DATABASE = 'task_database'

# create_engine to connect to the DB through this URl
engine = create_engine("mysql://cf-python:password@localhost/task_database")

#generating & storing the Base class
Base = declarative_base()

#creating Session() then binding it to 'session' object (similar to cursor)
Session = sessionmaker(bind=engine)
session = Session()

#defining the Recipe() class
class Recipe(Base):
  __tablename__ = "final_recipes"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50))
  ingredients = Column(String(255))
  cooking_time = Column(Integer)
  difficulty = Column(String(20))

  #method to show a quick representation fo the recipe
  def __repr__(self):
    return f"<Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})>"
  
  #method to return a well-formatted version of the recipe
  def __str__(self):
    return( f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking time: {self.cooking_time} minutes.\n"
            f"Difficulty: {self.difficulty}\n")
  
  def return_ingredients_as_list(self):
    if self.ingredients == "":
      return []
    else:
      return self.ingredients.split(", ") 
  
  #calculates recipe difficulty based on cooking time and number of ingredients used
  def calculate_difficulty(self):
    ingredient_count = len(self.ingredients.split(", "))
    if self.cooking_time < 10 and ingredient_count < 4:
      self.difficulty = "Easy"
    elif self.cooking_time < 10 and ingredient_count >= 4:
      self.difficulty = "Medium"
    elif self.cooking_time >= 10 and ingredient_count < 4:
      self.difficulty = "Intermediate"
    elif self.cooking_time >= 10 and ingredient_count >= 4:
      self.difficulty = "Hard"
  
#_____________________MAIN CODE_____________________# 

#this initializes the "final_recipes" table
Base.metadata.create_all(engine)


#collect details of recipe from user
def name_input():
  name = input("Enter recipe name (max 50 characters): ")
  while len(name) > 50:
    name = input("Error. name is too long, please try again:  ")
  return name

def cooking_time_input():
  cooking_time = input("Enter recipe cooking time (in minutes): ")
  if not cooking_time.isnumeric():
    raise TypeError("Cooking time must be a numeric character")
  else:
    return int(cooking_time)
  
def ingredients_input():
  while True:
    try:
      n = int(input("How many ingredients would you like to enter?"))
      if n <= 0:
        raise ValueError
      break
    except ValueError:
      print("Number must be an integer greater than 0.")
  
  ingredients = []
  #loops through however many ingredients user wants to input, adds each one to empty "ingredients" list
  for i in range(0, n):
    ingredient = input("Enter ingredient: ")
    ingredients.append(ingredient)

  #returns the "ingredients" list as a string, joined by ", "  
  return ", ".join(ingredients)

def create_recipe():
  name = name_input()
  ingredients = ingredients_input()
  cooking_time = cooking_time_input()

  recipe_entry = Recipe(name=name, ingredients=ingredients, cooking_time=cooking_time)
  recipe_entry.calculate_difficulty()

  session.add(recipe_entry)
  session.commit()
  print()
  print("Success! Recipe added to database.")
  
def view_all_recipes():
  #fetch all recipe lines from DB
  all_recipes = session.query(Recipe).all()
  if not all_recipes: 
    print("No recipes in database.")
    return None
  for recipe in all_recipes:
    print(recipe)
    print("_"*50)

def search_by_ingredients():
  #count how many recipe entries there are in DB
  num_recipes = session.query(Recipe).count()  
  if num_recipes == 0:
    print("No recipes in database.")
    return None 

  #fetch all lines under "ingredients" column
  results = session.query(Recipe.ingredients).all()
  all_ingredients = []
  for row in results:
    ingredients = row[0].split(", ")
    for ingredient in ingredients:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

  #printing an enumerated ingredient list for the user
  print("Available ingredients:")
  for i, ingredient in enumerate(all_ingredients):
    print(f"{i+1}. {ingredient}")

  #taking user input, storing the selected index number in the "search_ingredients" object
  sel_ids = input("Enter the numbers of ingredients to search for, separated by spaces:  ").split()

  if not all(id.isnumeric() and 0 < int(id) <= len(all_ingredients) for id in sel_ids):
    print("Error. Please enter valid index number present on ingredients list.")
    return
  search_ingredients = [all_ingredients[int(i) - 1] for i in sel_ids]

  #making a list of all searched for ingredients
  conditions = [Recipe.ingredients.like(f"%{ingredient}%") for ingredient in search_ingredients]

  #sending a query using "conditions" list to find matching terms in DB
  recipes = session.query(Recipe).filter(*conditions).all()

  #printing results for user
  if recipes:
    for recipe in recipes:
      print()
      print(recipe)
      print("_"*50)
  else:
    print("No recipes found with the selected ingredients.")

def edit_recipe():
  #count how many recipe entries there are in DB, if there are none, exiting
  num_recipes = session.query(Recipe).count()  
  if num_recipes == 0:
    print("No recipes in databsae.")
    return None
  #fetch all IDs and Names stored in DB, display them to user   
  results = session.query(Recipe.id, Recipe.name).all()
  for recipe in results:
    print(f"ID: {recipe.id}, Name: {recipe.name}")

  #receive user selection of ID to be edited
  id_selected = input("Enter recipe ID to be edited from the list: ")
  recipe_to_edit = session.query(Recipe).filter_by(id=int(id_selected)).first()
  if not recipe_to_edit:
    print("Recipe not found, please double-check your selection.")
    return None

  print("[1] Name: ", recipe_to_edit.name)
  print("[2] Ingredients: ", recipe_to_edit.ingredients)
  print("[3] Cooking time: ", recipe_to_edit.cooking_time)

  attribute = int(input("Select which attribute you'd like to edit (by number 1-3): "))
  if attribute == 1:
    recipe_to_edit.name = name_input()
  elif attribute == 2:
    recipe_to_edit.ingredients = ingredients_input()
  elif attribute == 3:
    recipe_to_edit.cooking_time = cooking_time_input()
  else:
    print("Error. Please enter a valid number 1, 2, or 3.")

  recipe_to_edit.calculate_difficulty()
  session.commit()
  print()
  print("Recipe updated successfully.")

def delete_recipe():
  #count how many recipe entries there are in DB, if there are none, exiting
  num_recipes = session.query(Recipe).count()  
  if num_recipes == 0:
    print("No recipes in databsae.")
    return None
  #fetch all IDs and Names stored in DB, display them to user   
  results = session.query(Recipe.id, Recipe.name).all()
  for recipe in results:
    print(f"ID: {recipe.id}, Name: {recipe.name}")

  #receive user selection of ID to be deleted
  id_selected = input("Enter recipe ID to be deleted from the list: ")
  recipe_to_delete = session.query(Recipe).filter_by(id=int(id_selected)).first()
  if not recipe_to_delete:
    print("Recipe not found, please double-check your selection.")
    return None
  confirmation = input("Are you sure about this? This action cannot be undone. Please enter Yes or No.   ")
  if confirmation.lower() == 'yes':
    session.delete(recipe_to_delete)
    session.commit()
    print("Success, recipe deleted successfully.")
  else:
    print("Action aborted, exiting.")
    return None


#_____________________MAIN MENU LOGIC_____________________# 
def main_menu():
  while True:
    print("\nM a i n  M e n u")
    print("-"*40)
    print("1. Create a new recipe.")
    print("2. View all recipes in database.")
    print("3. Search recipes by ingredient.")
    print("4. Update an existing recipe.")
    print("5. Delete a recipe.")
    print("Type 'quit' to exit the app.")
    print("-"*40)

    choice = input("How would you like to proceed? (pick option 1-5 or quit) ")
    if choice == "1":
      create_recipe()
    elif choice == "2":
      view_all_recipes()
    elif choice == "3":
      search_by_ingredients()
    elif choice == "4":
      edit_recipe()
    elif choice == "5":
      delete_recipe()
    elif choice.lower() == "quit":
      print("Exiting the app. Goodbye!")
      break
    else:
      print("Something went wrong, please enter a number 1-5.")
  
  session.close()
  engine.dispose()

if __name__ == "__main__":
  main_menu()