#simple try except syntax

n=input("Please enter a number: ")

try:
    print(type(int(n)))
except:
    print("Oops thats not number!")