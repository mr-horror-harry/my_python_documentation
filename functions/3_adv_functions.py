#This script is to leran the advanced functions in python

#map function
#type 1:
def square(n):
    return n**2

li = [ 1,2, 3, 4, 5, 6, 7, 8, 9 ]
print(*list(map(square, li)))

#type 2:
for i in map(square, li):   #map returns a list
    print(i, end=" ")
print()


#filter function:
#type 1:
def isEven(n):
    return 'even' if n%2==0 else 'odd'

def filterEven(n):
    return n%2==0

print(list(map(isEven, li)))
print(*list(filter(filterEven, li)))

#type 2:
for i in filter(filterEven, li):
    print(i, end=" ")
print()


#lambda function:
print(*list( map(lambda n:n**2, li) )) #as if anonymous function
print(*list( filter(lambda n:n%2==0, li) ))

# def square(n):
#     return(n**2)