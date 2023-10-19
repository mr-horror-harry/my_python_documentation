def yielder(n):
    for i in range(n):
        yield i**2

#next() --> to iterate throught the yield itr
y = yielder(10)
while True:
    try:
        print(next(y)) #works similar to a iterator
    except:
        break

#for loop implicitly handle the next() err by exception

# iter() --> to convert to normal iterable to yield iterable
s='The quick brown fox jumps over the lazy dog!'
s=iter(s)
while True:
    try:
        print(next(s), end=" ") #works similar to a iterator
    except:
        break

#next()
#iter()

