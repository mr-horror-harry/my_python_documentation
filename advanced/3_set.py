s1=set()
s1.add(1)
s1.add(2)

s2={1,2,3}
print(type(s2))

print(s1, s2)
print(*s2)

# difference() : elts in A not in B
print("\nSet difference:")
print(s1.difference(s2)) # return empty set 
print(s2.difference(s1))

#updates s1 with (s1 - s2)
s1.difference_update(s2)
print(s1)

for i in range(10,0,-1):
    s1.add(i)

print(*s1)

#removes 9 and 2
s1.discard(9)
s1.discard(2)
print(s1)

s1.discard(9) #removes none as already removed

#intersection() : elts common to both sets
print("\nIntersection:\n", s1.intersection(s2))
#updates s2 with (s1 n s2)
s2.intersection_update(s1) #memory operation and returns none
print(s2)


s1={1,5,3,7,8,4,9}
s2={1,2,3,4,5,6,7}
#set union
print("\nUnion:")
print(s1.union(s2))

print(s1,s2)
print(s1.difference(s2), s2.difference(s1))
print(s1.symmetric_difference(s2), s2.symmetric_difference(s1)) #unique elts of each : inverse of intersection

s1={1,2,3,4,5,6,7}
s2={1,4,5}

print("\nSubset:")
print(s2.issubset(s1))
print(s1.issubset(s2))

print('\nSuperset:')
print(s2.issuperset(s1))
print(s1.issuperset(s2))

print("\nDisjoint:")
#disjoint: both sets have no common elts : intersection is one
print(s1.isdisjoint(s2))
s1={1,2,3}
s2={4,5,6}
print(s1.isdisjoint(s2))

print(s1.isdisjoint(s2) == s2.isdisjoint(s1)) #always true
print(s1.intersection(s2) == s2.intersection(s1)) #always true

#update : update the first set with all the elts
print(s1, s2)
s1.update(s2) #similar to union_update
print(s1, s2)

#clear: removes all the elt
s1.clear()
print(s1)