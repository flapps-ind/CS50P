def main ():
  print("Amount Due: 50")
  machine()

def machine():
  balance = 50
  while balance > 0:
    y = int(input("Insert Coin: "))
    if y == 25 or y == 10 or y == 5:
      balance -= y
      if balance > 0:
        print(f"Amount Due: {balance}")
    else:
      print(f"Amount Due: {balance}")
      
  print("Change owed: 0")      
main()        
      