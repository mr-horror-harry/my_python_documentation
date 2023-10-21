import re

sent = '25-09-2002 is christmas 45-89-8926 isn\'t a date at all 01-01-2024 is not christmas'

x = re.search(r'\d\d-\d\d-\d\d\d\d', sent) # dob format
print(x.span())
print(x.group())

#quantifiers
x = re.search(r'\d{2}-\d{2}-\d{4}', sent) # reduced form
print(x.span())
print(x.group())

x = re.search(r'(\d{2})-(\d{2})-(\d{4})', sent) # more clear
print(x.span())
print(x.group())

for i in re.finditer(r'(\d{2})-(\d{2})-(\d{2})', sent): # multi search
    print(i.group(1), i.group(2)) # to print the 1st & 2nd part of group --> ( ) usage

x = re.search(r'(\d*-)', sent) #for 0 or more
print(x.group())

x = re.search(r'(\d+-)', sent) #for 1 or more
print(x.group())

# \d -> digit : kjsdhow
# \D -> alphabet : dfnJHhfHhf
# \w -> alphaNumeric : kjba8723j2k
# \W -> non alphanumeric : !&#^@*$

# \d{2} -> 2 digits together
# \d{2,6} -> 2 to 6 digits together
# \d+ -> 1 or more digits together
# \d* -> 0 or more digits together
# \d{2,} -> 2 or more digits together
# \d? -> 0 or 1 digit

#pattern genearation
mobile_pattern = re.compile('\d{10}')
input = "9378426175 78965 1457896541236 4578694588df *-7863219541"
for i in re.finditer(mobile_pattern, input):
    print(i.group())