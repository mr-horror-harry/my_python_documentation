from collections import defaultdict

#dictionary
d = dict()
d['one']=1
d['two']=2
d['three']=3

print(d)
print(type(d))
# print(d['four']) #shows err for undefined key

#default dictionary
dd = defaultdict(int, {'one':1, 'two':2}) #int intialises value with default value 0 (int or lambda:0)
dd['three']=3

print(dd)
print(type(dd))
print(dd['four'])