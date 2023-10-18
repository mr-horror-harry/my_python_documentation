#importing specific functions from a module as relative path
from functions import sumNum, fact

#import all under a module as relative path
from maths import *

#importing a module as relative path
import string

#direct use of import functions
print(sumNum(10, 5, 6, 25))
print(fact(5))

fibonaci(10)

#module functions accessing
print(string.slicer("HelloWorld!", 1, 7))
print(string.str_mul("Hello ",5))

#packages -> folder ( a collection of modules )
#modules -> files
#functions -> contents