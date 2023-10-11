#This script is to the ways by which while loop could be executed

#>>>>> while
x=1
while x<=10:
    print(x)
    x+=1

#>>>>> while else
x=7
while x<=10:
    print(x)
    x+=1
else:
    print("Value exceeded 10")

#>>>>> 

x=0
while x<=25:
    if x%5==0:
        x+=1
        continue
    elif x%2==0:
        # without pass the block leads to err
        pass
    else:
        print(x, end=" ")
    x+=1

#>>>>>
i=0
s="Hello Hola Hey!"
while i<len(s):
    if s[i]=='a':
        break
    else:
        print(s[i], end="")
    i+=1
