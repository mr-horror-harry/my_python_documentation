def my_decor(func):
    
    def wrapper():
        #before
        li=[]
        n=int(input("Enter a number: "))
        for i in range(n):
            li.append(i)

        #func to be wrapped
        li = func(li)

        #after
        print("The cubes upto {n}:")
        for i in li:
            print(i, end=" ")
    return wrapper

@my_decor
def cubes(li):
    return list(map(lambda n:n**3, li))

cubes()

#my_decor(cubes) #without annotation