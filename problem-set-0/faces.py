def main():
  x = input()
  smile = '\U0001F642'
  frown = '\U0001F641'
  print(x.replace(':)', smile).replace(':(', frown))

main()