class Height(object):
  def __init__(self, feet, inches):
    self.feet = feet
    self.inches = inches
  
  def __str__(self):
    output = str(self.feet) + " feet, " + str(self.inches) + " inches"
    return output
  
  def __add__(self, other):
    #Converting both objects' heights into inches
    height_A_inches = self.feet * 12 + self.inches
    height_B_inches = other.feet * 12 + other.inches

    #adding the two together
    total_height_inches = height_A_inches + height_B_inches

    #putting the output into feet
    output_feet = total_height_inches // 12

    #getting the output of inches
    output_inches = total_height_inches - (output_feet * 12)

    #final output as a new Height object
    return Height(output_feet, output_inches)

  def __sub__(self, other):
    #Converting both objects' heights into inches
    height_A_inches = self.feet * 12 + self.inches
    height_B_inches = other.feet * 12 + other.inches

    #subtracting the two objects
    difference_inches = height_A_inches - height_B_inches

    #putting the output into feet:
    output_feet = difference_inches // 12

    #getting the output of inches
    output_inches = difference_inches - (output_feet * 12)

    #final output as a new Height object
    return Height(output_feet, output_inches)

  #comparison operators
  def __lt__ (self, other):
    height_A_inches = self.feet * 12 + self.inches
    height_B_inches = other.feet * 12 + other.inches
    return height_A_inches < height_B_inches
  def __le__(self, other):
    height_inches_A = self.feet * 12 + self.inches
    height_inches_B = other.feet * 12 + other.inches
    return height_inches_A <= height_inches_B
  def __eq__(self, other):
    height_inches_A = self.feet * 12 + self.inches
    height_inches_B = other.feet * 12 + other.inches
    return height_inches_A == height_inches_B
  def __gt__(self, other):
    height_A_inches = self.feet * 12 + self.inches
    height_B_inches = other.feet * 12 + other.inches
    return height_A_inches > height_B_inches
  def __ge__(self, other):
    height_A_inches = self.feet * 12 + self.inches
    height_B_inches = other.feet * 12 + other.inches
    return height_A_inches >= height_B_inches
  def __ne__(self, other):
    height_A_inches = self.feet * 12 + self.inches
    height_B_inches = other.feet * 12 + other.inches
    return height_A_inches != height_B_inches

# person_A_height = Height(5, 10)
# person_B_height = Height(3, 9)

# height_sum = person_A_height + person_B_height
# height_difference = person_A_height - person_B_height

# print("Total height: ", height_sum)
# print("Height difference: ", height_difference)

#comparison tests
heightA = Height(4, 6)
heightB = Height(4, 5)
height_comparisonA = heightA > heightB
print("Scenario A: " + str(height_comparisonA))


heightA = Height(4, 5)
heightB = Height(4, 5)
height_comparisonB = heightA >= heightB
print("Scenario B: " + str(height_comparisonB))


heightA = Height(5, 9)
heightB = Height(5, 10)
height_comparisonC = heightA != heightB
print("Scenario C: " + str(height_comparisonC))
