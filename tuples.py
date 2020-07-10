#tuples- ordered collection or group of items(immutable)
# tuples are faster than lists. Makes code safer. Valid keys in a dictionary
# can be created by tuple()

#you cannot use a list as a key in a dictionary 
# you can use a tuple though

#tuple - immutable
alphabet = ("a", "b", "c", "d")
print(alphabet)
print(type(alphabet))
# alphabet[0] = "f"  - not permitted

months = ("jan", "feb", "mar", "apr", "may", "jun")
print(months[0])
print(months[-2])




#tuple methods

#looping
for m in months:
	print(m)

#count - returns the number of times a value appears in a tuple
x = (1, 2, 3, 4, 2, 3, 3, 3)
print(x.count(1))
print(x.count(3))

#index - gives you the index of the value entered in the method
print(x.index(1))
print(x.index(2)) #gives index of the first occurance
#x.index(8) # gives a valueError: tuple.index(x): x not in tuple

#tuple inside a tuple
nums = (1, 2, 3, (4, 5), 6, 7)
print(nums[3])
print(nums[3][0])
print(nums[0:4])


