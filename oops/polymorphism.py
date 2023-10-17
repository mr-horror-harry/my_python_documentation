class Dog():
    def __init__(self, name, weight):
        self.name=name
        self.weight=weight
    
    def printDetails(self):
        print(self.name, self.weight)
    def sound(self):
        print("Bow Bow")

class Cat():
    def __init__(self, name, weight):
        self.name=name
        self.weight=weight
    
    def printDetails(self):
        print(self.name, self.weight)
    def sound(self):
        print("Meow")

dog1 = Dog('Tommy', 12)
cat2 = Cat('Yoda', 8)
dog2 = Dog('Randy', 15)
cat1 = Cat('Linda', 7)

li = [dog1, dog2, cat1, cat2]
for pet in li:
    pet.printDetails()
    pet.sound() #method determined at runtime

