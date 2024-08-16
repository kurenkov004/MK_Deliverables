import pickle

#prints the recipe
def display_recipe(recipe):
  print("\n Recipe: ", recipe["name"])
  print("Cooking time (in minutes): ",  recipe["cooking_time"])
  print("Ingredients: ", )
  for ingredient in recipe["ingredients"]:
    print("- ", ingredient)
  print("Difficulty: ", recipe["difficulty"])

#searches for an ingredient in the given data
def search_ingredient(data):
  #extract all_ingredients out of "data", enumerate & make a list of tuples
  all_ingredients = enumerate(data["all_ingredients"])
  ingredients_enumerated = list(all_ingredients)

  #prints list of all ingredients & their indices
  print("Available Ingredients: ")
  for element in ingredients_enumerated:
    print(element[0], element[1])
  try:
    i = int(input("Enter number from list to search for an ingredient: "))
    ingredient_searched = ingredients_enumerated[i][1]
  except ValueError:
    print("Warning! Please enter integer present on list.")
  except:
    print("Oops, something went wrong.")
  else:
    for recipe in data["recipes_list"]:
      if ingredient_searched in recipe["ingredients"]:
        print(recipe)

#MAIN CODE -------------------------------------------------------------------

filename = input("Please enter filename that contains the recipe data: ")

try:
  file = open(filename, 'rb')
  data = pickle.load(file)
except FileNotFoundError:
  print("File doesn't exist - exiting.")
except:
  print("Oops, something went wrong.")
else:
  search_ingredient(data)
  file.close()

