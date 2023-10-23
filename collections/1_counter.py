from collections import Counter

#Counter()
li=['1','1',1,1,1,3,3,3,3,6,'6',6,6,'6',9,'9']
print(Counter(li))  #returns a dict of values and count pair

s='The quick brown fox jumps over the lazy dog'
print(Counter(s))

sent='The quick brown fox jumps over the lazy dog'
print(Counter(sent.split()))

ctr=Counter(s)
print(type(ctr))

print(ctr.most_common(5)) #most frequently occured n elements
print(list(ctr)) #returns a list of ctr elements
