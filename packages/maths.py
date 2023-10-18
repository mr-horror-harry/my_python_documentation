def power(m,n):
    return m**n

def fibonaci(n):
    x,y=0,1
    n-=2
    print(x, y, end=" ")
    while n>0:
        tmp=x+y
        print(tmp, end=" ")
        x=y
        y=tmp
        n-=1
    print()