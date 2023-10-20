import random as rd 

print(rd.randint(10, 100),"\n")

rd.seed(101) #the intial value
print(rd.randint(10,100))
print(rd.randint(10,100))
print(rd.randint(10,100))
print(rd.randint(10,100))
print(rd.randint(10,100))
print(rd.randint(10,100),"\n")

rd.seed(101) #follows the same pattern
print(rd.randint(10,100))
print(rd.randint(10,100))
print(rd.randint(10,100))
print(rd.randint(10,100))
print(rd.randint(10,100))
print(rd.randint(10,100),"\n")

li="The brown little fox jumed over the lazy dog!".split()
print(len(li))
print(rd.choice(li))
print(rd.choices(population=li, k=10)) #repetition allowed 
print(rd.choices(li, k=10))
print(rd.sample(li, k=8)) #no repetition k <= len(li)

print(li)
rd.shuffle(li) #shuffle the list
print(li)