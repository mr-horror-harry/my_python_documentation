st = set() #declaring a set

st.add(1) #add an elt to the set
st.add(2)
st.add('string')
print(st)
print(len(st))

st.remove(2) #remocve an elt from the set

print((2) in st) #existence of an element
print(set((1,2,3,4,3,2,1))) #tuple to set
print(set([1,2,3,4,3,2,1])) #list to set