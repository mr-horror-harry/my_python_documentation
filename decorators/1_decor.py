def my_decorator_func(func):    #decorator
    def wrapper_func():             #the wrapper
        print("1+1=2 You know that!") #code that excutes before
        func()                             #predefined code
        print("The given function is wrapped!") #code that excutes after
    return wrapper_func

@my_decorator_func
def my_func():   #the func to be wrapped
    i=0
    while(i<10):
        print(i)
        i+=1

my_func()       #function call