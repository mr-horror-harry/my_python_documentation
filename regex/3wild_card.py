#wild card characters

import re

sent = "Hi all how are you Im doing good here! Alieans are not bad! Allies are British! Alice in wonderland! How about a halwa!"

x = re.search(r'al', sent) #check for the first occurence (i.e) atleast one
print(x.group())

x = re.findall(r'al', sent) #check for all occurences (i.e) total occurences
print(x) #return a list

for i in re.finditer(r'al', sent): #as an iterator
    print(i.group())
    
x = re.search(r'are|ere|bad', sent)
print(x.span())
print(x.group())

x = re.findall(r'are|ere|bad', sent)
print(x)

# x and n preceeding chars too
print(re.findall(r'.er', sent), re.findall(r'..er', sent), re.findall(r'...er', sent), re.findall(r'....er', sent))
# x and n succeeding chars too
print(re.findall(r'er.', sent), re.findall('er..', sent), re.findall(r'er...', sent), re.findall(r'er....', sent))
# x and both side chars too
print(re.findall(r'.er..', sent), re.findall(r'..er.', sent), re.findall(r'...er.', sent), re.findall(r'....er.....', sent))

sent1 = "56 Hello Im good at 1 yp"
sent2 = "Hello Im 34 good at 1 yp"
sent3 = "Hello Im4 good at 1 year23"

#sentence starts with a pttern
print(re.findall('^\d', sent1), re.findall('^\d', sent2), re.findall('^\d', sent3)) #sent1 is true
#sentence ends with a pttern
print(re.findall(r'\d$', sent1), re.findall('\d$', sent2), re.findall('\d$', sent3)) #sent3 is true

#exclusion
print(*re.findall(r'[^\d]+', sent1)) #to remove the digits

sent = "It is $ not bad %^ to code is it ? am i right $"
print(*re.findall(r'[^!@#$%^&*()_+?<>:":"{}|]', sent),sep="") #igonre punctuations 

sent = "This is 193.23 or 369.45.15"
print(re.findall(r'[\d]+.[\d]+', sent))

sent="This is batman in search of batwheel"
print(re.findall(r'bat(man|wheel)', sent))