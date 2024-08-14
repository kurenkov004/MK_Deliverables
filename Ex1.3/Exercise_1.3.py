# initialize empty lists for recipes and ingredients
recipes_list = []
ingredients_list = []

# function to take user input for recipe elements
def take_recipe():
  name = str(input("Enter recipe name: "))
  cooking_time = int(input("Enter recipe cooking time (in minutes): "))
  ingredients = list(input("Enter list of ingredients, separated by commas: ").split(", "))
  recipe = {
    "name": name,
    "cooking_time": cooking_time,
    "ingredients": ingredients
  }

  return recipe

#ask user how many recipes they want to enter
n = int(input("How many recipes would you like to enter?"))

#iterates through user input to determine if ingredients already exist, and appends recipe to recipes_list
for i in range(n):
  recipe = take_recipe()

  for ingredient in recipe["ingredients"]:
    if not ingredient in ingredients_list:
      ingredients_list.append(ingredient)
  
  recipes_list.append(recipe)

#iterates through recipe list to determine recipe difficulty
for recipe in recipes_list:
  cooking_time = recipe["cooking_time"]
  ingredient_count = len(recipe["ingredients"]
  )
  if cooking_time < 10 and ingredient_count < 4:
    recipe["difficulty"] = "Easy"
  elif cooking_time < 10 and ingredient_count >= 4:
    recipe["difficulty"] = "Medium"
  elif cooking_time >= 10 and ingredient_count < 4:
    recipe["difficulty"] = "Intermediate"
  elif cooking_time >= 10 and ingredient_count >= 4:
    recipe["difficulty"] = "Hard"

#iterates through recipes_list to print their info
for recipe in recipes_list:
  print("Recipe: ", recipe["name"])
  print("Cooking time: ", recipe["cooking_time"])
  print("Ingredients: ", )
  for ingredient in recipe["ingredients"]:
    print(ingredient)
  print("Difficulty level: ", recipe["difficulty"])

#function to print all ingredients avaialble in an attractive layout
def print_ingredients():
  print("Ingredients available accross all recipes:")
  print("------------------------------------------")
  ingredients_list.sort()
  for ingredient in ingredients_list:
    print(ingredient)

print_ingredients()

  