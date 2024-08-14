a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = input("Enter operator + or - ")

if c == "+":
  print(a + b)

elif c == "-":
  print(a - b)

else:
  print("Unknown operator, try again.")