dic = {x:x**2 for x in range(10)}
print(dic)

#pairing key nad value using zip
dic = {c:n for c, n in zip(['1','2','3','4'],[1,2,3,4])}
print(dic)

dic = {x:x**2 for x in range(10)}
#gives the keys
for elt in dic:
    print(elt, end=" ")
print()

#iterating thro the list keys
for elt in dic.keys():
    print(elt, end=" ")
print()

#iterating thro the list values
for elt in dic.values():
    print(elt, end=" ")
print()

#iterating thro the list entries
for tpl in dic.items():
    print(tpl, end=" ")
print()

#destructuring the tuple directly
for k,v in dic.items(): #returns a list
    print(k,v, end="   ---   ")
print()
