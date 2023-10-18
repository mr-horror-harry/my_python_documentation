#dividing a number

def divide(m,n):
    try:
        return int(m)/int(n)
    except ZeroDivisionError:
        print("Can't divide by Zero!")
    except ValueError:
        print("String can't be divided!")

m=input("Enter a Dividend: ")
n=input("Enter the Divisor: ")

print(divide(m,n))