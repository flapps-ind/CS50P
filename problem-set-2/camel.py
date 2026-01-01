x = input("camelCase: ")

snake_case = ""

for ch in x:
    if ch.isupper():
        snake_case += "_" + ch.lower()
    else:
        snake_case += ch

print("snake_case:", snake_case)
