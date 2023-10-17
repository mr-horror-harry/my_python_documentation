#This script is to view the working of the python inhertence

class SuperClass():
    
    def __init__(self, name, regno):
        self.name=name
        self.regno=regno

    def printDetails(self):
        print(self.name, self.name, "from the super class")

class SubClass(SuperClass):
    
    def __init__(self, gender):
        SuperClass.__init__()
        self.gender=gender

    def printDetails(self):
        print(self.)


