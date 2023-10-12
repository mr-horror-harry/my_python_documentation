#This python script is to view the working of the default args function

#>>>>>>>>>>>>>>>>>>>>
#Default arguements:

def defaultArgs(x,y,a=10,b=20):
    print(x+y+a+b)

defaultArgs(50,34)
defaultArgs(100,200,300)

#>>>>>>>>>>>>>>>>>>>>

def defaultArgs2(x,y,z=190):
    return x+y+x

print(defaultArgs2(10,90))
print(defaultArgs2(45,10,10))

#>>>>>>>>>>>>>>>>>>>>
#Keyword Arguements:

def keywordArgs(x,y,z):
    return x+y+z

print(keywordArgs(x=10, z=67, y=10))
print(keywordArgs(z=15, y=56, x=14))
print(keywordArgs(x=10, y=20, z=30))

#>>>>>>>>>>>>>>>>>>>>
#Positional Arguements:

def posArgs(x,y,z):
    print(z,y,x)

posArgs(10,30,20)

#>>>>>>>>>>>>>>>>>>>
#arbitrary Arguements:
def arbArgs(*args):
    if '200' in args:
        print('present')
    else:
        print('not present')

    print(type(args))
    print(args)
    for i in args:
        print(i, end=" ")
    print()

arbArgs('100', '550', '303', '404')

#keywords arbitrary Arguments:

def kwArbArgs(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
    for key,val in kwargs.items():
        print(f'The value of the key {key} is {val}')
    
    if '3' in kwargs.values():
        print('present')

    print(kwargs.keys())
    print(type(kwargs.keys()))

kwArbArgs(one='1', two='2', three='3', four='4', five='5')
