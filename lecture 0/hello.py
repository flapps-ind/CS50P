"""
name = input("Whats your name? ") #combines printf and scanf

#remove whitespace from str
name = name.strip().capitalize().title() #this is called a method, title capitalizes each word's first letter


print("hello, " + name) #concatenation
# print("hello,", name)  this also works and adds space automatically
# print(*objects, sep=' ', end='\n') this is the argument for print function
print("hello, \"friend\"")
print(f"hello, {name}") #this is a f string


#split user's name into first name and last name

first, last = name.split()
print(first, last)

"""



def main():
  hello()
  hello("mahgooz")

def hello(to="world"):
  print("hello", to)
  

main()  