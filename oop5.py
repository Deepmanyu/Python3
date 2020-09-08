#inheritance

class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first, last, age = data_str.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}"

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"

class Moderator(User):
	total_mods = 0
	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.total_mods += 1

	@classmethod
	def display_active_mods(cls):
		return f"There are currently {cls.total_mods} active mods"

	def remove_post(self):
		return f"{self.full_name()} removed a post from {self.community} community"



u1 = User("tom", "garcia", 35)
u2 = User("tom", "garcia", 35)
u3 = User("tom", "garcia", 35)
jasmine = Moderator("Jasmine", "O'conner", 61, "Piano")
jasmine2 = Moderator("Jasmine", "O'conner", 61, "Piano")
# print(User.display_active_users())
# print(Moderator.display_active_mods())
# print(jasmine.full_name())
# print(jasmine.community)





#Multiple Inheritance

class Aquatic:
	def __init__(self, name):
		self.name = name

	def swim(self):
		return f"{self.name} is swimming"

	def greet(self):
		return f"I am {self.name} of the sea!"


class Ambulatory:
	def __init__(self, name):
		self.name = name
	
	def walk(self):
		return f"{self.name} is walking"

	def greet(self):
		return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):
	def __init__(self, name):
		super().__init__(name = name)


jaws = aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")




#Method Resolution Order (MRO)

class A:
	def do_somehting(self):
		print("Method Defined In: A")

class B(A):
	def do_somehting(self):
		print("Method Defined In: B")

class C(A):
	def do_somehting(self):
		print("Method Defined In: C")

class D(B, C):
	def do_somehting(self):
		print("Method Defined In: D")

thing = D()
thing.do_something()










