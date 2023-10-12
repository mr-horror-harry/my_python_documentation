# (1) LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def less2Even(x,y):
    if x%2==0 and y%2==0:
        return x if x<y else y
    else:
        return x if x>y else y

x,y=map(int, input("Enter two Nos:\n").split())
print( less2Even(x,y) )
