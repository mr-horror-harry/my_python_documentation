'''

# (1) LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def less2Even(x,y):
    if x%2==0 and y%2==0:
        return x if x<y else y
    else:
        return x if x>y else y

x,y=map(int, input("Enter two Nos:\n").split())
print( less2Even(x,y) )



# (2) ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def isSame(x,y):
    return x==y

a,b=input("Enter two Strings:\n").split()
if isSame(a[0], b[0]):
    print("Same letter start!")
else:
    print("No Same letter start!")



# (3) MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def t20(li):
    return '20' in li or int(li[0])+int(li[1])==20
        
if(t20(input("Enter two Nos:\n").split())):
    print("Accepted!")
else:
    print("Not Accepted!")



# (4) OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def capitalise(s):
    res=""
    for i,c in enumerate(s):
        if i==0 or i==3:
            res+=s[i].upper()
        else:
            res+=s[i]
    return res

print( capitalise(input("Enter a name:\n")) )



# (5) MASTER YODA: Given a sentence, return a sentence with the words reversed

def reversal(s):
    return s[::-1]

print(reversal(input("Enter a word:\n")))


'''



