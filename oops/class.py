#This script is to view the usage of the class and instances

class Country(): #class structure

	x=10 #class level attribute

	def __init__(self, state, district): #constructor / initializer method
		self.state = state
		self.district = district
		self.y=20

	def printHello(self): #method syntax
		print("Hello")

cty1 = Country('TamilNadu','Thoothukudi') #instances for class
cty2 = Country('Kerala', 'Kochin')

print(cty1.state, cty1.district, cty1.x, cty1.y) #accessing values of instances

cty2.z=30 #instance level attribute
print(cty2.state, cty2.district, cty2.x, cty2.y, cty2.z)
cty1.printHello() #method call
