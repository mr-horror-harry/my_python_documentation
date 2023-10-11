#This script is to check out the way in which list comprehension works

li=[x for x in range(10)]
print(*li)

li=[x for x in range(10) if x%2==0]
print(*li)

li=[x**2 for x in range(10)]
print(*li)

li=[x**2 for x in range(10) if x%2==0]
print(*li)

li=[c for c in "Hello World!"]
print(*li, sep="")

li=[x if x%2==0 else 'None' for x in range(25)]
print(*li)

celsius=[100, 110, 90, 85]
far=[(cel*9/5 + 32) for cel in celsius]
print(*far)
