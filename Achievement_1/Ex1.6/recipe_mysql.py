import mysql.connector

#initializing the connection object btwn the Python session and MySQL server
conn = mysql.connector.connect(
  host='localhost',
  user='cf-python',
  passwd='password'
)

#initializing the cursor object - lets me perform operations on the db using SQL queries
cursor = conn.cursor()
#creating DB and setting up access to it
cursor.execute("CREATE DATABASE IF NOT EXISTS  task_database")
cursor.execute("USE task_database")

#creating table named "Recipes" with appropriate columns
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)''')

#MAIN MENU ACTION METHODS

#calculates recipe difficulty based on cooking time and number of ingredients used  
def calculate_difficulty(cooking_time,ingredients):
  if cooking_time < 10 and len(ingredients) < 4:
    difficulty = "Easy"
  elif cooking_time < 10 and len(ingredients) >= 4:
    difficulty = "Medium"
  elif cooking_time >= 10 and len(ingredients) < 4:
    difficulty = "Intermediate"
  elif cooking_time >= 10 and len(ingredients) >= 4:
    difficulty = "Hard"
  return difficulty

#collecting data input
def create_recipe(conn, cursor):
  name = str(input("Enter recipe name: "))
  cooking_time = int(input("Enter recipe cooking time (in minutes): "))
  ingredients = (input("Enter list of ingredients, separated by commas: ")).split(", ")
  #re-work ingredients list into a string to use in SQL query
  sql_ingredients = ', '.join(ingredients)

  difficulty = calculate_difficulty(cooking_time, ingredients)

  #remember that %s are used as placeholder characters
  create_query = """
    INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
    VALUES (%s, %s, %s, %s)
  """
  cursor.execute(create_query, (name, sql_ingredients, cooking_time, difficulty))
  conn.commit()
  print("Recipe added to database.")

#searching for a recipe by ingredient
def search_recipe(conn, cursor):
  #fetching a list of all ingredients from every recipe in the DB
  cursor.execute("SELECT DISTINCT ingredients from Recipes")
  results = cursor.fetchall()

  #adding all ingredients into a big list, making sure there are no doubles
  all_ingredients = set()
  for row in results:
    ingredients = row[0]
    all_ingredients.update(ingredients.split(', '))
  
  #printing an enumerated ingredient list for the user
  print("List of available ingredients: ")
  for id, ingredient in enumerate(sorted(all_ingredients), start=1):
    print(f"{id}. {ingredient}")
  
  #taking user input, storing the selected index number in the "search_ingredient" object
  selection = int(input("Select an ingredient from the list by its id number: ")) -1
  search_ingredient = sorted(all_ingredients)[selection]

  #executing the search query
  query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
  cursor.execute(query, ("%" + search_ingredient + "%",))

  #fetching search results and printing them for the user
  search_results = cursor.fetchall()
  if search_results:
    for row in search_results:
      print(row)
  else:
    print("Could not find recipes with selected ingredient. Please double-check your selection")

#updating recipe info    
def update_recipe(conn, cursor):
  #fetching & printing all the recipes in the DB for user selection
  cursor.execute("SELECT id, name FROM Recipes")
  recipes = cursor.fetchall()

  print("\n List of available recipes: ")
  for row in recipes:
    print(f"ID: {row[0]}, Name: {row[1]}")

  selected_id = int(input("Please select recipe ID to be updated: "))
  selected_column = input("Please select column to be updated (name, ingredients, cooking_time):")

  #initializing a "new_value" object to be filled per user selection
  new_value = None
  if selected_column == "name":
    new_value = input("Enter new recipe name: ")
    update_query = "UPDATE Recipes SET name = %s WHERE id = %s"
    cursor.execute(update_query, (new_value, selected_id))
  elif selected_column == "ingredients":
    new_value = (input("Enter list of ingredients, separated by commas: ")).split(", ")
    #re-work new ingredients list into a string to use in SQL query
    new_sql_ingredients = ', '.join(new_value)
    update_query = "UPDATE Recipes SET ingredients = %s WHERE id = %s"
    cursor.execute(update_query, (new_sql_ingredients, selected_id))
  elif selected_column == "cooking_time":
    new_value = int(input("Enter NEW recipe cooking time (in minutes): "))
    update_query = "UPDATE Recipes SET cooking_time = %s WHERE id = %s"
    cursor.execute(update_query, (new_value, selected_id))
  else:
    print("Sorry, no valid column selected.")
    return
  
  #re-calculating & updating difficulty if the modified columns were "ingredients" or "cooking_time"
  if selected_column in ["ingredients", "cooking_time"]:
    cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (selected_id,))
    row = cursor.fetchone()
    difficulty = calculate_difficulty(row[0], row[1])
    update_query = "UPDATE Recipes SET difficulty = %s WHERE id = %s"
    cursor.execute(update_query, (difficulty, selected_id))

  conn.commit()
  print("Recipe updated.")

def delete_recipe(conn, cursor):
  #fetching & printing all the recipes in the DB for user selection
  cursor.execute("SELECT id, name FROM Recipes")
  recipes = cursor.fetchall()
  print("\n List of available recipes: ")
  for row in recipes:
    print(f"ID: {row[0]}, Name: {row[1]}")
  
  print()
  print("Be careful, this action cannot be undone.")
  print()
  selected_id = int(input("Select recipe ID to be deleted: "))

  delete_query = "DELETE FROM Recipes WHERE id = %s"
  cursor.execute(delete_query, (selected_id,))
  conn.commit()
  print()
  print("Recipe deleted successfully!")


#MAIN MENU LOGIC
def main_menu(conn, cursor):
  while True:
    print("\nM a i n  M e n u")
    print("-------------------------------------")
    print("1. Create a new recipe.")
    print("2. Search recipes by ingredient.")
    print("3. Update an existing recipe.")
    print("4. Delete a recipe.")
    print("5. Exit the app.")
    print("-------------------------------------")

    choice = input("How would you like to proceed (pick 1-5):  ")

    if choice == "1":
      create_recipe(conn, cursor)
    elif choice == "2":
      search_recipe(conn, cursor)
    elif choice == "3":
      update_recipe(conn, cursor)
    elif choice == "4":
      delete_recipe(conn, cursor)
    elif choice == "5":
      print("Exiting the app. Goodbye!")
      conn.commit()
      cursor.close()
      conn.close()
      break
    else:
      print("Something went wrong, please enter a number 1-5.")



main_menu(conn, cursor)