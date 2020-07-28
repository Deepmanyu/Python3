# built in functions
#Any and all

#All - returns True if all elements of the iterable are truthy
# or the iterable is empty
all([0, 1, 2, 3 ]) # false as 0 is falsy
print(all([char for char in "eio" if char in "aeiou"])) # True 
print(all([num for num in [4, 2, 10, 8, 6] if num % 2 == 0])) # True

# another example
people = ["deep", "anu", "anshu", "mom", "pri"]
print([n[0] == "d" for n in people])

#Any - takes an iterable and returns True if any item of iterable
# is true. If iterable is empty it returns Fasle
print(any([name[0] == "d" for name in people]))
print(all([name[0] == "d" for name in people]))


#list and generatoar expression
#Use list comprehensions when the result needs to be iterated 
# over multiple times, or where speed is paramount. Use generator
# expressions where the range is large or infinite. 
import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_comp = sys.getsizeof(x * 10 for x in range(1000))
print("To do the same thing, it takes")
print(f"List Comprehension: {list_comp} bytes")
print(f"General Comprehension: {gen_comp} bytes")


#Sorted - its a list method(works on anything that is iterable)
#Returns a new sorted list from the items in iterable
nums = [6, 2, 10, 5]
print(sorted(nums))
print(sorted(nums, reverse = True))

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

print(sorted(users, key = len)) # sorts on the basis of no of key-value pairs
print(sorted(users, key = lambda u: u["username"]))
print(sorted(users, key = lambda u: len(u["tweets"])))



#Min and Max 
people = ["deep", "anu", "anshu", "mom", "pri"]
print(min(people))
print([len(l) for l in people])
print(max(len(l) for l in people))
print(max(people, key = lambda n : len(n)))


#Reversed - returns a reversed iterable
#We can use it with strings, etc. reverse only works
reversed("hello")

for char in reversed("hi"):
	print(char)

print("hello"[::-1])

#len - returns the length of an object
"hello".__len__()

#abs - returns the absolute value of a number. argument can be
# int or float. It means the absolute value. fabs in math
abs(-5)
abs(3.4444)
abs(-3.55)


#sum - take an iterable and an optional start. fsums in math
# returns the sum of the start and the items from left to right
# start by default is 0
sum([1, 2, 3]) #6
sum([1, 2, 3], 10) #16
sum([1, 2, 3], -6) #0
sum([1.5, 2, 3.7]) #7.2
#sum(["hi", "there"]) #error use - "".join(["hi", "there"])

#round - returns number rounded to ndigits precision after decimal
# if digits is none, it returns to the nearest integer
round(10.2) #10
round(3.5123) # 4
round(3.51234, 3) #3.512


#zip - make an iterator that aggregates elementss from each of
# the iterables. Returns an iterator of tuples, where i-th tuple
# contains the i-th element from each of the argument sequence
#The iterator stops when the shortest input iterable is exhausted

first_zip = zip([1, 2, 3], [4, 5, 6]) #makes a list of tuples
print(list(first_zip))
print(dict(first_zip))

#we can unpack using zip
#very common when working with complex data structures

five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
list(zip(*five_by_two)) #[(0,1,2,3,4), (1,2,3,4,5)]

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["deep", "anshu", "yoyo"]

#getting the highest marks for each student - using comprehension
final_grades1 = {pair[0] : max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}
print(final_grades1)

#same as above using lambda and using map

final_grades2 = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)
print(final_grades2)

#getting the average grades

avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0] + pair[1]) / 2),
			zip(midterms, finals)
		)
	)
)
print(avg_grades)

#excersice 1
#Write a function interleave that accepts two strings. It should return 
# a new string containing the 2 strings interwoven. example below
# interleave("hi", "ha") - hhia

def interleave(string1, string2):
	list1 = [i for i in string1]
	list2 = [i for i in string2]
	list_inter = list(zip(list1, list2))
	final = ""
	for i in list_inter:
		final += (i[0] + i[1])
	return print(final)
interleave("hi", "ha")
interleave("aaa", "zzz")

#another way for the above
#First join the individual tuples into strings, which is what the 
# first join() does. t results in a list of strings: ['hn', 'io'] 

#Second, join all the remaining strings into one large string. results
# in 'hnio'
def interleave1(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))


#for detailes on individual joins see below
ans = ("".join(x) for x in (zip("abc", "hel")))
print(tuple(ans))

print("".join("".join(x) for x in (zip("abc", "hel"))))


#excersice 2
#Write a function called triple_and_filter. This function should accept
# a list of numbers, filter out every number that is not divisible by 
# 4, and return a new list where every remaining number is tripled

def triple_and_filter(num_list):
    new_list = filter(lambda i: i % 4 == 0, num_list)
    return [i*3 for i in new_list]
print(triple_and_filter([4, 8, 1, 3]))








  	












