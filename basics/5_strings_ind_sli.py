s="Hello World!"

#string index
print(s)
print(s[0]) #first index
print(s[7])
print(s[-1]) #last index --> negative index
print(s[-7])

#string slicing
print(s[0:]) #print entire string
print(s[6:]) #print from 6th ind to last
print(s[:6]) #print upto to 5th index

print(s[2:8]) #print from 2 to 7th ind
print(s[2:8:2]) #same with step value as 2
print(s[::3])

print(s[::-1]) #reverse a string
print(s[4:1:-1])
print(s[-8:-2:2])

# print(s[20]) #error: range out of index

#length & type of the string
print(len(s))
print(type(s))

print(s.upper()) #to make case upper
print(s.lower()) #to make case lower
print(s.split()) #split wrt space
print(s.split("l")) #split wrt l