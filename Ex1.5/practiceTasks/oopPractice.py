class Date(object):
  def __init__ (self, day, month, year):
    self.day = day
    self.month = month
    self.year = year
  
  def get_date(self):
    output = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
    return output
  
  def set_date(self):
    self.day = int(input("Enter the day of the month: "))
    self.month = int(input("Enter the month: "))
    self.year = int(input("Enter the year: "))
  
  #custom method to determine if the date is on a leap year
  def is_leap_year(self):
    return self.year % 4 == 0
  
  #custom method to check if the date is valid or not
  def is_valid_date(self):
    #check if some conditions are met; if any return "False", the date is not valid

    #check if all values are integers
    if not (type(self.day) == int and type(self.month) == int and type(self.year) == int):
      return False
    #make sure the year isn't negative
    if self.year < 0:
      return False
    #check that the month is between 1 and 12
    if self.month < 1 or self.month > 12:
      return False
    #verify that a day is valid for a given month
    last_dates = {
      1: 31,
      2: 29 if self.is_leap_year() else 28,
      3: 31,
      4: 30,
      5: 31,
      6: 30,
      7: 31,
      8: 31,
      9: 30,
      10: 31,
      11: 30,
      12: 31
    }
    if self.day < 1 or self.day > last_dates.get(self.month):
      return False
    #if none of the above are triggered, the method will return "True"
    return True


#MAIN CODE STARTS HERE -------------------------------------->

# We're now getting into the main section of our script, we'll initialize a few Date objects, with some of them having erroneous values.
date1 = Date(29, 2, 2000)           # Valid since it's a leap year.
date2 = Date(29, 2, 2001)           # Invalid since it's not a leap year.
date3 = Date('abc', 'def', 'ghi')   # Invalid since we're feeding in irrelevant values.

# Next, we'll call the is_valid_date() method for each object. If the date is valid, the method would return True. If any anomaly is found, it would return False.
print(str(date1.get_date()) + ": " + str(date1.is_valid_date()))
print(str(date2.get_date()) + ": " + str(date2.is_valid_date()))
print(str(date3.get_date()) + ": " + str(date3.is_valid_date()))

# #creating an instance of "Date" as an object called "first_moon_landing"
# first_moon_landing = Date(20, 7, 1969)

# #try to access the data inside first_moon_landing using dot notation
# print("Initial values in first_moon_landing -")
# print(first_moon_landing.day)
# print(first_moon_landing.month)
# print(first_moon_landing.year)

# # Next, we'll try modifying some of the values
# # inside 'first_moon_landing', using the
# # dot notation once again.
# first_moon_landing.day = 25
# first_moon_landing.month = 11
# first_moon_landing.year = 1800

# # Printing out the contents of 'first_moon_landing' again shows that we were able to modify its values
# print()
# print("Modified values in first_moon_landing -")
# print(first_moon_landing.day)
# print(first_moon_landing.month)
# print(first_moon_landing.year)


# #print out the date using the "getter" function
# print(first_moon_landing.get_date())

# #changing the date using the "setter" function
# first_moon_landing.set_date()

# #printing out modified date - 
# print(first_moon_landing.get_date())