#Inheritance
#A key feature of OOP is the ability to define a class which inherits
# from another class(a "base" or "parent" class)

#In Python, inheritance words by passing the perent class as an argument
# to the defination of a child class

class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")

class Cat(Animal):
	def __init__(self, name, species, breed, toy):
		super().__init__(name, species)
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


blue = Cat("blue", "cat", "jungle_cat", "string")
print(blue)
print(blue.species)
print(blue.breed)
print(blue.toy)
blue.play()





#
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age >= 0:
			self._age = age
		else:
			self._age = 0

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			raise ValueError("age can't be negative!")

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

	@full_name.setter
	def full_name(self, name):
		self.first, self.last = name.split(" ")





jane = Human("Jane", "Goodall", 50)
print(jane.age)
print(jane.first)
jane.age = 20
print(jane.age)
jane.full_name = "Spider Man"
print(jane.__dict__)






