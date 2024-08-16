def display(file):
  heroes = []
  for line in file:
    #remove newline characters
    line = line.rstrip("\n")

    # Here, we use the split(", ") method available to strings
    # to split the hero name and the year separately.
    # The separation occurs at ", ".

    #taking the first element of the split
    hero_name = line.split(", ")[0]
    #taking the second element of the split
    first_appearance = line.split(", ")[1]

    #pack the two results into a smaller, two-element list
    #then append it to the list "heroes"
    heroes.append([hero_name, first_appearance])
  
  #this will sort "heroes" by first appearance
  heroes.sort(key = lambda hero: hero[1])

  for hero in heroes:
    print("--------------------------------------")
    print("Superhero: " + hero[0])
    print("First year of appearance: " + hero[1])

filename = input("Enter the filename where you've stored your superheroes: ")
try:
  file = open(filename, 'r')
  display(file)
except FileNotFoundError:
  print("File doesn't exist - exiting.")
except:
  print("An unexpected error occured.")
else:
  file.close()
finally:
  print("Goodbye!")
