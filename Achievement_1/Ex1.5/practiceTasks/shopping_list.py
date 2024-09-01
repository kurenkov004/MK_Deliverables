#defining a class object
class ShoppingList(object):
  def __init__(self, list_name):
    self.list_name = list_name
    self.shopping_list = []
  
  def add_item(self, item):
    if not item in self.shopping_list:
      self.shopping_list.append(item)
      print(f"{item} added to shopping list. ")

    else:
      print(f"{item} is already on the list, cannot add it again. ")
  
  def remove_item(self, item):
    try:
      if item in self.shopping_list:
        self.shopping_list.remove(item)
        print(f"Removed {item} from list. ")
    except:
      print(f"{item} not on the list. ")

  def view_list(self):
    if self.shopping_list:
      print(f" Shopping list '{self.list_name}':")
      for item in self.shopping_list:
        print(f"- {item}")
    else: 
      print(f"The shopping list you're looking for is empty.")
  
  def merge_lists(self, obj):
    #creating a name for the new merged list
    merged_lists_name = 'Merged List - ' + str(self.list_name) + " + " + str(obj.list_name)

    #creating an empty ShoppingList object
    merged_lists_obj = ShoppingList(merged_lists_name)

    #adding the first shopping list's items to the new lsit
    merged_lists_obj.shopping_list = self.shopping_list.copy()

    # Adding the second shopping list's items to our new list -
    # we're doing this so that there won't be any repeated items
    # in the final list, if both source lists contain common
    # items between each other
    for item in obj.shopping_list:
      if not item in merged_lists_obj.shopping_list:
        merged_lists_obj.shopping_list.append(item)
    return merged_lists_obj


# MAIN CODE

#initializing empty shopping list objects
pet_store_list = ShoppingList("Pet Store List")
grocery_store_list = ShoppingList('Grocery Store List')

#adding some items to each object
for item in ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']:
  pet_store_list.add_item(item)

for item in ['fruits' ,'vegetables', 'bowl', 'ice cream']:
  grocery_store_list.add_item(item)

#one way to merge lists together
merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)

merged_list.view_list()

# pet_store_list = ShoppingList("Pet Store Shopping List")

# pet_store_list.add_item("dog food")
# pet_store_list.add_item("frisbee")
# pet_store_list.add_item("collars")
# pet_store_list.add_item("bowl")
# pet_store_list.add_item("flea collars")

# pet_store_list.remove_item("flea collars")

# pet_store_list.add_item("frisbee")

# pet_store_list.view_list()

