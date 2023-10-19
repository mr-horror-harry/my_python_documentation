'''
#as a function returning list takes more memory
def listElt(n) -> list:
    li=[]
    i=1
    while i<n:
        li.append(i)
        i+=1
    return li
'''

#as a function yielding the list takes less memory
def listElt(n):
    i=1
    while i<n:
        yield i
        i+=1

for i in listElt(10):
    print(i)