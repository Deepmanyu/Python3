#object oriented programming


# Class and Ojects 

#Naming convention of a class is a camel convention
#Classes in Python can have a special __init__ method, which gets 
# called everytime you create an instance of the class(instantiate)
#The self keyword refers to the current class instance. The parameter
# does not have to be called self, but it is a standard. Self must 
# always be the first parameter to __init__ and any methods and
# properties on class instances.

#defining the simplest possible class
class User:

	#class attributes are defined as below. They are defined once
	# when we want to access it we access it by using class User and not
	# with the User instance like user1, user2 etc
	active_users = 0

	#defining a class methods
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
		#adding 1 to the class attribute
		User.active_users += 1

	def __repr__(self):
		return f"{self.first}"

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):               #this is a instance method 
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}"

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, birthday {self.first}"

#printing a Class attribute 
print(User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
#again printing class attribute active users to see the count
print(User.active_users)
print(user1.logout())
print(User.active_users)


print(user1.first, user1.last)
print(user2.first, user1.last)
print(user2.full_name())

print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))

print(user1.initials())
print(user2.initials())

print(user2.is_senior())
print(user1.age)
print(user1.birthday())
print(user1.age)

#using the class method for creating a new user
tom = User.from_string("tom, jones, 34")
print(tom.first)
print(tom.full_name())
print(tom.birthday())

#by using repr - we would print the f string when we jsut print tom
# without repr this would print - __main__.User object at location
print(tom)



#userscores and dunder methods
# _name -> its just a way to telling that the variable is private
# __name -> name mangling. Its purpose is to make this attribute 
#          particular to the class. It helps in inheritance.
# __name__ -> Used for python specific methods. like __len__, __add__. 



#Class Attributes
# class attributes are shared by all instances of a class and the class
# itself


#class methods - @classmethod decorator
# class methods are not very common. They are not concerned with the 
# instances but the class itself


