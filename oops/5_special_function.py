#special methods for classes

class Sample():
    def __init__(self, name):   #initializer
        self.name=name

    def __str__(self):  #string representation of object
        return f"The object Name is {self.name}"
    
    def __len__(self):  #len to specified if called
        return 0

    def __del__(self): #to delete the object itself
        print(f'Object {self.name} deleted successfully!')

obj = Sample('c45Rex54')
print(obj)  #without __str__() output would be the address
print( str(obj) )
print( len(obj) )
del(obj)
#del obj #both are right