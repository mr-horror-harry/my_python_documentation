print('Conversion Methods:')
s='hello im gooD boy. HelLo hey dood!'
print(s.capitalize()) #capitalize the first letter of first word
print(s.upper())
print(s.lower())
print(s.title(),"\n") #capitalize the first letter of every word

#count of elts
print("Count of 'e':", s.count('e'))

print('Check Methods: ')
s='HEY DOOD!'
print(s.isupper())
print(s.islower(),'\n')
print(s.istitle())

print('AFHSJsdh'.isalpha())
print('12FG67h'.isalpha(),'\n')

print('123'.isdigit())
print('asd3'.isdigit(),'\n')

print('sfj256'.isalnum())
print('afewfw'.isalnum())
print('236713'.isalnum(), '\n')

print(' '.isspace())
print('\t'.isspace())
print('    '.isspace(), '\n')

print('akgdDY'.endswith('y'))
print('akgdDY'.endswith('Y'))

s='hihhihihiihihhhhihiiiihihih'
print(s.split('hi'))
print(s.partition('ihi')) #seperates wrt the first mentioned string