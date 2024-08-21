class Recipe(object):
  #class attribute to group together all ingredients accross all recipes
  all_ingredients = set()

  #initializing Recipe class with base attributes
  def __init__(self, name, ingredients, cooking_time):
    self.name = name
    self.ingredients = ingredients
    self.cooking_time = cooking_time
    self.difficulty = None
    self.update_all_ingredients()

  #getter & setter methods
  def get_name(self):
    #return the name of the recipe
    return self.name
  def set_name(self, name):
    #set a new name for the recipe
    self.name = str(name)

  def get_cooking_time(self):
    #return the cooking time of recipe, in minutes
    return self.cooking_time
  def set_cooking_time(self, cooking_time):
    #set new cooking time, in minutes
    self.cooking_time = int(cooking_time)

  def get_ingredients(self):
    #returns a list of ingredients for given recipe
    return self.ingredients

  def get_difficuly(self):
    #returns recipe difficulty level, calculates it if not set yet
    if not self.difficulty:
      self.calculate_difficulty()
    return self.difficulty
  
  #other class methods
  def add_ingredients(self, *ingredients):
    #adds new ingredients to the recipe, updates global ingredients variable
    for ing in ingredients:
      self.ingredients.append(ing)
    self.update_all_ingredients()

  def search_ingredient(self, ingredient):
    #checks if a given ingredient is in the recipe already
    if ingredient in self.ingredients:
      return True
    if not ingredient in self.ingredients:
      return False

  def update_all_ingredients(self):
    for i in self.ingredients:
      if not i in Recipe.all_ingredients:
        Recipe.all_ingredients.update(i)
  
  def calculate_difficulty(self):
     #calculates recipe difficulty, output is used to generate the "difficulty" attribute
    ingredient_count = len(self.ingredients)
    if self.cooking_time < 10 and ingredient_count < 4:
      self.difficulty = "Easy"
    elif self.cooking_time < 10 and ingredient_count >= 4:
      self.difficulty = "Medium"
    elif self.cooking_time >= 10 and ingredient_count < 4:
      self.difficulty = "Intermediate"
    elif self.cooking_time >= 10 and ingredient_count >= 4:
      self.difficulty = "Hard"
  
  def __str__(self):
    #returns a string representation of the whole Recipe
    output = f"Recipe Name: {self.name} \nIngredients: {', '.join(self.ingredients)} \nCooking Time(in minutes): {self.cooking_time} \nDifficulty: {self.get_difficuly()}\n"
    return output

#MAIN CODE --------------------------------------------------------------------------->
def recipe_search(data, search_term):
  
  for recipe in data:
    if recipe.search_ingredient(search_term):
      print(recipe)
  
tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
banana_smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)
 
recipes_list = [tea, coffee, cake, banana_smoothie]

for recipe in recipes_list:
  print(recipe)


for ingredient in ["Water", "Sugar", "Bananas"]:
  print("Recipes containing " + ingredient + ": \n")
  recipe_search(recipes_list, ingredient)
  