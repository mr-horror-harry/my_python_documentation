li = []

for i in range(10):
    li.append(i)

li.insert(4,4)
print(*li)
print("Count of 4:", li.count(4))

#list is generic:
li.append([1,2,3,4,5])
print(li)

#similar to list concat
li.extend([1,2,3,4,5])
print(li)

#access by index
print(li.index(3))

li.insert(2, 'hello')
print(li)

#del the last elt 
li.pop()
print(li)

#remove first occuring element
li.remove(2)
# li.remove('hello world') #throws err for unpresent elt
print(li)

li.reverse() #occurs at memory
print(li)

li=[12,34,56,54,34,76]
li.sort() #at memory
print(li)

li.sort(reverse=True) #at memory
print(li)

