#another creation of class

class Pet:
	
	allowed = ["cat", "dog", "fish", "rat"]

	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"You cannot have {species} as a pet!")
		self.name = name
		self.species = species

	def set_species(self, species):
		if species not in Pet.allowed:
			raise ValueError(f"You cannot have {species} as a pet!")
		self.species = species


cat1 = Pet("kitty1", "cat") 

Pet.allowed.append("tiger")
cat2 = Pet("kitty2", "tiger")

print(cat2.species)
print(Pet.allowed)

print(id(cat1.allowed))
print(id(Pet.allowed))

cat2.set_species("rat")
print(cat2.species)


#string representation method
# The __repr__ method is on eof several ways to provide a nicer string
# representation

class Human:

	def __init__(self, name = "someday"):
		self.name = name

	def __repr__(self):
		return self.name

dude = Human()
print(dude) # "someday"

deep = Human(name = "deep")
print()

















