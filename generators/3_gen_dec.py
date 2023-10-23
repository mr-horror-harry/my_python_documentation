def my_decor(func):  # ----------(3)
    
    def wrapper():  # ----------(1)
        #before
        li=[]
        n=int(input("Enter a number: "))
        for i in range(n):
            li.append(i)

        #func to be wrapped
        li = func(li)   # ----------(2)

        #after
        print("The cubes upto {n}:")
        for i in li:
            print(i, end=" ")
    return wrapper

@my_decor    # ----------(3)
def cubes(li):   # ----------(2)
    return list(map(lambda n:n**3, li))

cubes() # ----------(1)

#my_decor(cubes) #without annotation
# ----------(n) : func call and func called