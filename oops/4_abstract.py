class Polygon():
    def noOfSides(self):
        raise NotImplementedError("This methodod is Abstract!")

class Triangle(Polygon):
    def noOfSides(self):
        print("Three sides!")

class Square(Polygon):
    def noOfSides(self):
        print("Four sides!")

# pol = Polygon()
# pol.noOfSides() #throws err since abstract

tri = Triangle()
tri.noOfSides()

sq = Square()
sq.noOfSides()

