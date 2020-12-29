#Lambda - are a special case of a function
#is a single line functon that does not have a name. Generally
# not stored in a variable
#Syntax - lambda variables: single line 
#We can use lambda to save us from defining many single line functions

def square(num): 
	return num * num
print(square(9))

# doing the same in lambda
square2 = lambda num: num * num 
print(square2(7))

add = lambda a, b : a + b
print(add(1, 5))

print(square.__name__)
print(square2.__name__)
print(add.__name__) 

#Map
#Map - a standard function that accepts atleast 2 arguments 
# 1) a function and 2) an "iterable". iterable is something that 
# can iterate over(lists, strings, dictionaries, sets, tuples)
#Runs the lambda for each value in the iterable and returns a 
# map object which can be converted into another data structure

#map example 1
nums = [2, 4, 6, 8, 10]
doubles = map(lambda x: x*2, nums)
print(list(doubles))

#map example 2
people = ["deep", "mom", "anu", "anshu", "priyam"]
print(list(map(lambda i : i[0].upper() + i[1:].lower() , people)))
print(list(map(lambda i : i.upper(), people)))

#map example 2 - dictionaries in a list
names = [
	{"first" : "deep", "job" : "data scientist"},
	{"first" : "anshu", "job" : "pm"},
	{"first" : "anu", "job" : "consultant"},
]
#get first names of all dictionaries in the list
print(list(map(lambda l: l["first"], names))) 


#Filter 
#There is a lambda for each value in the iterable
#Returns filter object which can be converted into other iterables
#The object contains only the values that return true to the lambda
# example 1 - return even numbers
list_1 = [1, 2 , 3, 4]
evens = list(filter(lambda x: x % 2 == 0, list_1))
print(evens)
# example 2 - return names starting with a
people = ["deep", "mom", "anu", "anshu", "priyam"]
print(list(filter(lambda x: x[0].lower() == "a", people)))


# expample 3 - kind of twitter example
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#Get the inactive users - users with no tweets
inactive_users = list(filter(lambda u: len(u["tweets"]) == 0, users))
print(list(inactive_users))
#To get the active users - we use the truthy and falsy idea
active_users = list(filter(lambda u: u["tweets"], users))
print(list(active_users))
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))
#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]
# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))
# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]


#Combibing filter and map 
#Only get the usernames for the inactive users
inactive_usernames = list(map(lambda u: u["username"].upper(), 
	filter(lambda inactive: not inactive["tweets"], users)))
print(inactive_usernames) 

#practice creating a dectionary from 2 lists using 3 mehtods
names = ["deep", "anshu", "mom"]
relation = ["father", "uncle", "grandma"]
name_rel = dict(zip(names, relation))
print(name_rel)
print(type(name_rel))
#same thing as above using list comprehension
name_rel2 = {names[i]: relation[i] for i in range(0, len(names))}
print(name_rel2)
#same thing as above using naive method of loops
name_rel3 = {}
for n in names:
	for r in relation:
		name_rel3[n] = r
		relation.remove(r)
		break
print(name_rel3)

#practice list comprehension 
#name if its less than 3 - you are grandma

print([f"{n}: You are grandma" for n in names if len(n) < 4])




