import sys
 
d = {}
d['python'] = 1
d[2] = 'hello'

for i in d.items():
    print(i[1])

li = ['1','3','3','-2','1','4','4']

# map 
t = list(map(int, li))
print(t)

print(type(t[0]))

# filter 
filtered_list = filter(lambda x: x % 2 == 0, t)
print(list(filtered_list))

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter(lambda x: x % 2 == 0, t)
even_numbers = list(filtered_list)
print(even_numbers) 


li.reverse()
print(li)



def isEvev(x):
    return x%2==0