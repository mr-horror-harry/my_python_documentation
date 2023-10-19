from collections import namedtuple
import math

tpl=(1, 2, 3, 4, 5)
print(tpl[4])

#in large no. of input cases name access is better than indexing
vertices=namedtuple('vertices', ['x', 'y'])

v1=vertices(x=10, y=20)
v2=vertices(x=20, y=40)

dist=math.sqrt((v2.x-v1.x)**2 + (v2.y-v1.y)**2)
print(dist)