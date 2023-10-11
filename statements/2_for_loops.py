#This script is execute the for loop statements

#>>>>>> for
li = [1,2,3,4,5,6,7,8,9,0]
for i in li:
    if i%2==0:
        print(f'{i} is Even')
    else:
        print('Odd')

#>>>>>> sum of elts by for
res=0
for i in li:
    res+=i
print(f'Sum is {res}')

#>>>>> iterating over dictionary
dic = {'one':1, 'two':2, 'three':3}
dic['four']=4

for i in dic:
    print(i)    #by default access the keys alone

for i in dic.items():
    print("%s is of type %s" %(i, type(i)))
    
for key, value in dic.items():                  #packing
    print(f'Value of the key {key} is {value}')

#>>>>> iterating over string
for c in "Hello World!":
    print(c)

s="Hello World!"
for i in range(len(s)):
    print(f'{i}th character is {s[i]}')

#>>>>> packing in for
for [x,y,z] in [[1,2,3],[4,5,6],[7,8,9]]:  #packing feature
    print(x, '>>', y, '>>', z)

#>>>>>
for x,y,z in [[1,2,3],[4,5,6],[7,8,9]]:  #packing feature
    print(x)
