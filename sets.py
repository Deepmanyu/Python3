#sets - collection of data that do not have duplicate values
# no order. cannot use index to access an item
# can be created by set()

#creating a set - using the set function
a = set({1, 4, 7 , 7, 7})

#creating a set - curly brackets with no colons 
a = {1, 4, 7, 7, 7 , "a", "b", 45.11, 10.1}
print(a) # print only unique values
print(4 in a)
print(10 in a)

#looping in set
for i in a:
	print(i) # dosent print duplicate values

# list of duplicates - change to set
list_a = {1, 4, 7, 7, 7 , "a", "b", 45.11, 10.1, "a", "b", "a"}
print(list_a)
print(type(list_a))
print(set(list_a))
print(list(set(list_a))) #getting a list of unique values
print(len(set(list_a))) # counting the unique values



#methods in sets

#add - dosent add if a value is already there(no error for this)
list_a.add("1stAdd")
print(list_a)
#remove - error if the item you want to remove is not there in the set
list_a.remove("b")
#discard - to remove a value, but does not give an error if the value is not there
#copy
list_copy = list_a.copy()
print(list_copy)
print(list_copy == list_a)
#clear - empties a set
list_copy.clear()
print(list_copy)
#set math - intersection, symmetric_difference, union
math_students = {"a", "b", "c"}
biology_students = {"a", "d", "l"}
print(type(math_students))
# all students without duplicates
all_students = math_students | biology_students
print(all_students)
#students in both the classes
common_students = math_students & biology_students
print(common_students)


#set comprehension

sq = {x ** 2 for x in range(10)}
print(sq)

sq_dictionary = sq = {x: x ** 2 for x in range(10)} # sets vs dictionary
print(sq_dictionary)

helo = {char.upper() for char in "helloo"}
print(helo)

 
string = "sequoia"
check = len({char for char in string if char in "aeiou"}) == 5
print(check)








