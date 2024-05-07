class Polygon():
    def noOfSides(self):
        pass

class Triangle(Polygon):
    def noOfSides(self):
        print("Three sides!")

class Square(Polygon):
    def noOfSides(self):
        print("Four sides!")

# pol = Polygon()
# pol.noOfSides() #the methododoly is abstract and is overidden by child classes

tri = Triangle()
tri.noOfSides()

sq = Square()
sq.noOfSides()

