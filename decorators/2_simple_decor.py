# internal working of simple decorator 
def decorator(func):
    print("This is printed before the function is called")
    func()
    print("This is printed after the function is called")

def say_hello():
  print("Hello! The function is executing")

decorator(say_hello)

# ----------------------------------------------------------------

# internal working of called wrapper 
def decor_mech(func):
    def wrapper():
        print("This is beg!")
        func()
        print("this is end!")
    return wrapper 

def greetings():
    print("Hello dood!")

called = decor_mech(greetings)
called()

# ----------------------------------------------------------------

# calling a decor using annotations
def decor_mech(func):
    def wrapper():
        print("This is beg!")
        func()
        print("this is end!")
    return wrapper 

@decor_mech
def greetings():
    print("Hello")

greetings()