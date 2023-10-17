#This script is to view the working of the python inhertence

class SuperClass():
    
    def __init__(self, name, regno):
        self.name=name
        self.regno=regno

    def printDetails(self):
        print(self.name, self.regno, "from the super class")

    def commonMssg(self):
        print("Im the spuermost unique method!")

class SubClass(SuperClass):
    
    def __init__(self, gender):
        self.gender=gender

    def printDetails(self):
        print(self.gender, "from the sub class")

spr = SuperClass('Harry', 2012094)
spr.printDetails()
spr.commonMssg()

sub = SubClass('Male')
sub.printDetails()
sub.commonMssg() #accessing method inherited from the super class

