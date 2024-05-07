# file_1
import tmp_pack as pck

def welcome():
    print("Welcome to the file_1 script!")

def greeting():
    print("Hello User!")

def helloWorld():
    print("The first program is Hello world printing!")

if __name__=="__main__":
    print("Main script is run directly!")
    welcome()
    greeting()
    helloWorld()
else:
    print("Main script is being imported and called!")

pck.call()