li = [] #empty list

#indexing & slicing
l1=input("Enter a sentence:\n").split()
print(l1[0])
print(l1[-1])
print(l1[3:6:2])
print(l1[::-1]) #return reversed list

#list methods
l1=['Hello', 10, 3.14]
print(len(l1)) #to find length of the list

l1.append(0) #to add at last
print(l1)

l1.insert(3,"Hola") #to add at specific index
print(l1)

l1.pop() #to remove last entry
l1.pop(2) #to remove specified entry
print(l1)

l1.reverse() #to reverse the list it occurs at memory and not on runtime
print(l1)

l1=[1,67,23,78,25,65,23]
l1.sort() #to sort the list it occurs at memory and not on runtime : inplace action
print(l1)
l1.sort(reverse=True) #sort in descending
print(l1)

# sorted -> return the data
# sort -> in place operation

print(l1.count(23))
print(l1.index(78)) #return the first index of '78'

print(len(l1))
print(type(l1))

#list concatenation
l1=[1,67,23,78,25,65]
l2=['a', 'r', 'r', 't', 'r']
l3=l1+l2
print(l1+l2)
print(l1, l2, l3)

#nested lists
l1=[[1,2,3], 3, [6,4,7,8], 'hey']
print(l1[2][3])
