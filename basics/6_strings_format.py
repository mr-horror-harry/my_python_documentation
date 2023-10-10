#string formating

#Method 1: using format() method
print("Hello {}! How are You ?".format(input("Enter you name: ")))

#format wrt index
name='Horror'
name2=input("Enter another name: ")

print("Hey {} {} {}".format('Harry', name, name2 ))
print("Hey {1} {2} {0}".format('Harry', name, name2))
print("Hey {0} {0} {0}".format('Harry', name, name2))

#alias for fomating
print("Hey {c} {b} {a}".format(a='Harry', b=name, c=name2))

# float formating
# alias:tot_width.precision
rad=int(input("Enter a radius value: "))
print("Area: {res}sq.m".format(res=(22*rad**2)/7))
print("Area: {res:.5f}sq.m".format(res=(22*rad**2)/7))
print("Area: {res:10.5f}sq.m".format(res=(22*rad**2)/7))

# Method 2: using formatted string and f-string
val=100 
print(f"This is a fromated string : {val}")
print(f"My name is {name}. Roll No is {val}")