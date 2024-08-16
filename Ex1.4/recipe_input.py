import pickle

#composes a dictionary named "recipe" based on user input
def take_recipe():
  name = str(input("Enter recipe name: "))
  cooking_time = int(input("Enter recipe cooking time (in minutes): "))
  ingredients = list(input("Enter list of ingredients, separated by commas: ").split(", "))
  difficulty = calc_difficulty(cooking_time, ingredients)
  recipe = {
    "name": name,
    "cooking_time": cooking_time,
    "ingredients": ingredients,
    "difficulty": difficulty
  }

  return recipe

#calculates recipe difficulty based on cooking time and number of ingredients used
def calc_difficulty(cooking_time, ingredients):
  if cooking_time < 10 and len(ingredients) < 4:
    difficulty = "Easy"
  elif cooking_time < 10 and len(ingredients) >= 4:
    difficulty = "Medium"
  elif cooking_time >= 10 and len(ingredients) < 4:
    difficulty = "Intermediate"
  elif cooking_time >= 10 and len(ingredients) >= 4:
    difficulty = "Hard"
  return difficulty

#MAIN CODE -------------------------------------------------------------------

#take user filename input to find & read a bin file
filename = input("Enter filename where you've stored recipe info: ")

#this will try to open the file entered, and if it doesn't exist, create a new file
try:
  file = open(filename, 'rb')
  data = pickle.load(file)
except FileNotFoundError:
  print("File doesn't exist - will create new file.")
  data = {"recipes_list": [], "all_ingredients": []}
except:
  print("Oops, something went wrong.")
  data = {"recipes_list": [], "all_ingredients": []}
else:
  file(close)
finally:
  recipes_list = data["recipes_list"]
  all_ingredients = data["all_ingredients"]

#ask user how many recipes they want to enter
n = int(input("How many recipes would you like to enter?"))

#iterates through user input to determine if ingredients already exist, and appends "recipe" to recipes_list
for i in range(0, n):
  recipe = take_recipe()

  for ingredient in recipe["ingredients"]:
    if not ingredient in all_ingredients:
      all_ingredients.append(ingredient)
  
  recipes_list.append(recipe)

#new object with updated info
data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

#opens & updates recipe file
file_update = open(filename, 'wb')
pickle.dump(data, file_update)
file_update.close()
print("Recipe file updated successfully.")