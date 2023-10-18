#dividing a number

def divide(m,n):
    try:
        return m//n
    except ZeroDivisionError:
        print("Cant divide by Zero!")

m=int(input("Enter a Quotient: "))
n=int(input("Enter the remainder: "))

print(divide(m,n))