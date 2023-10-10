dic = {} #empty dictionary

#sample dictionary
dic={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print(dic['d'])

#generic dictionaries
dic={'int':10, 'float':4.78, 'bool':True, 'str':"Harry", 'list':[1,[2,3,5,4,8],3, 'Hello'], 'tpl':(1,2,3,4), 'dict':{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}, 1:None, 2:2, 3:None}
print(dic['int'])
print(dic['str'][2::-1].upper())
print(dic['list'][1][2]==5)
print(dic['dict'].items())
print(dic[1]==dic[3])
print(dic[1], dic[2])

#dictionary methods
dic={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print(dic.keys()) #return the list of keys
print(dic.values()) #return the list of values
print(dic.items()) #return dict as a list of tuples
print(len(dic)) #return length of dict