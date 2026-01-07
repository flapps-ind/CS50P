def main():
  x = input("Input: ").lower()
  arr = ["a", "e", "i", "o", "u"]
  for ch in x:
    if(ch in arr):
      x = x.replace(ch, "")

  print("Output: ",x)  
main()  