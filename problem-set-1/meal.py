def main():
    x = input("What time is it? ")
    result = convert(x)
    if(7 <= result <= 8):
        print("breakfast time")
    elif(12 <= result <= 13):
        print("lunch time")
    elif(18 <= result <= 19):
        print("dinner time")        
   


def convert(time):
    hour, _, minute = time.partition(':')
    minute = int(int(minute) / 6)

    result = hour + '.' + str(minute)
    return float(result)

if __name__ == "__main__":
    main()