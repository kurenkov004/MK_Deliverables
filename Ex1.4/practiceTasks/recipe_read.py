import pickle

with open("recipe_binary.bin", "rb") as my_file:
  recipe = pickle.load(my_file)

print("Quick cup of tea: ")
print("___________________")
print("Name: " + recipe["Ingredient Name"])
print("Ingredients: ")
for ingredient in recipe["Ingredients"]:
  print("-" + " " + ingredient)
print("Cooking time: " + str(recipe["Cooking time"]))
print("Difficulty: " + recipe["Difficulty"])