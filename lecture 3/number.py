while True:
  try:
    x = int(input("What's x? "))
    break
  except ValueError:
    print("x is not an integer")  
  #else:
    #break

print(f"x is {x}")

# ValueError is given for incorrect user inputs
# NameError occurs in python when you try to use a variable or function that hasn't been defined yet.

#def main():
# x = get_int("What's x?")
# print(f"x is {x})

#def get_int(prompt):
# while True:
#   try:
#     return int(input(prompt))
#   except ValueError:
#     print("x is not an integer") or pass