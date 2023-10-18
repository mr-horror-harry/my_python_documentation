#dividing a number

def divide(m, n):
    try:
        print(int(m)/int(n))
    except ZeroDivisionError:
        print("Can't divide by Zero!")
    except ValueError:
        print("String can't be divided!")
    except:
        print("Error found safe exit!")
    else:   
        print("Code handled and executed safely!")

m=input("Enter a Dividend: ")
n=input("Enter the Divisor: ")

divide(m, n)