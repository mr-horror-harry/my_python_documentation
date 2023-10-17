#This script is to view the working of the python inhertence

class SuperClass():
    
    def __init__(self, name, regno):
        self.name=name
        self.regno=regno

    def printDetails(self):
        print(self.name, self.regno, "from the super class")

class SubClass():
    
    def __init__(self, SuperClass, name, regno,  gender):
        SuperClass.__init__(name, regno)
        self.gender=gender

    def printDetails(self):
        print(SuperClass.name, SuperClass.regno,"from the super class", self.gender, "from the sub class")

spr = SuperClass('Harry', 2012094)
spr.printDetails()

sub = SubClass(spr, 'Horror', 36937, 'Male')
sub.printDetails()

