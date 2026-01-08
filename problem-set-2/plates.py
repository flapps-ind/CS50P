def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    if not 2 <= len(s) <= 6:
        return False
    if not s.isalnum():
        return False
    for i in range(2):
        if not s[i].isalpha():
            return False
    for ch in s:
       
        if ch.isdigit:
            if i < 2 and ch == "0":
                return False
            elif s[len(s)-1].isalpha(): 
                return False
            i += 1    
        else:
            return True    
    
    return True

           


main()