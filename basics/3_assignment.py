#dynamic typed language
a=20
print(a)
a=12.7
print(a)
a="hello"
print(a)

#comma assigning
x,y=10,4
a,b=x,4.0*y
print(a,b,x,y)
x+=y
print(x)

#split assigning
print("Enter two nos only: ")
x,y=map(int, input().split())
print("Your input:", x, y)

#on run time without assignment
print("Enter a number")
print(type(int(input())))

#swap assigning
m=100
n=101
print(m,n)
m,n=n,m         #swap without temp variable
print(m,n)