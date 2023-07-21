# single * operator. its often called as *args. Its just a parameter, you can call it anything
# its a special operator we can pass to a function.                           
# Gathers the remaining arguments as a tuple


def sum_all_nums(num1, num2, num3): 
	return num1 + num2 + num3
print(sum_all_nums(1, 2, 3))

# what if i need to pass any number of argument to sum
# we use *args
def sum_all_nums1(*args):
	total = 0
	for num in args:
		total += num
	return total
print(sum_all_nums1(1, 4))
print(sum_all_nums1(1, 4, 19, 7, 3))

# correct info
def ensure_correct_info(*args):
	print(args)
	if "deep" in args and "suhag" in args:
		return "welcome back deep"
	return "not sure who you are"

print(ensure_correct_info("hello", 1, 1,7, ["a", "b"]))
print(ensure_correct_info(1, True, "deep", "suhag")) 

# **kwargs - keyword args
# gathers remaining keyword arguments as a dictionary

def fav_colors(**kwargs): 
	for person, color in kwargs.items():
		print(f"{person }'s fav color is {color}") 

fav_colors(deep = "green", mom = "blue", anu = "red") 

# another example
def special_greeting(**kwargs):
	if "deep" in kwargs and kwargs["deep"] == "special": 
		return "You have a special message"
	elif "deep" in kwargs:
		return f"message : {kwargs['deep']}" # remember to use single quotes in kwargs
	return "not sure who is this"

print(special_greeting(deep = "hello"))
print(special_greeting(deep = "special", anu = "hi"))


# parameters ordering
# 1 - parameters, 2- *args, 3- default parameters, 4- **kwargs
def display_info(a, b, *args, name = "deep", **kwargs):
	return(a, b, args, name, kwargs)
# a - 1
# b - 2
# args will be a tuple containing (3)
# name - "deep" as noting was passed in the function for name
# kwars will be a dictionary {'last_name' : "deep", 'job' ; "data scientist"}
print(display_info(1, 2, 3 , last_name = "deep", job = "data scientist"))


# Using * as an argument : Argument unpacking 
def sum_all_nums2(*args):
	total = 0
	for num in args:
		total += num
	return print(total)
nums = [1, 2, 3, 4, 5, 6]
# sum_all_nums2(nums) - will five an error 
# we will get an error if we pass nums to *args. its so because 
# the entire list is passed as the 1st argument to the tuple.
# so when the addition happens(in the function) entire list 
# is added to the total. this gives an error

# we need to unpack the arguments in list/tuple. Use *nums 
sum_all_nums2(*nums)


# using ** as an argument - Dictionary unpacking

def display_names(first, second):
	print(f"{first} says hello to {second}")
names = {"first" : "deep", "second" : "anu"}
display_names(first = "mom", second = "adi")
# display_names(names) - will give error (reason same as before)
display_names(**names)


# another example
def add_and_multiply_numbers(a, b, c):
	print(a + b * c)
data = dict(a = 1, b = 2, c = 3)
# add_and_multiply_numbers(data) - gives error
add_and_multiply_numbers(**data)


# good exaple 
# make float, a boolean which gives float if true else int
# operation, one of add, substract, multiply, devide
# first and second are the numbers for performing operation
# message is a string that can be added (def - The result is)



def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

calculate(make_float = False, operation = "add", message = "You just added", first = 2, second = 4) # you just added 6
calculate(make_float = True, operation = "devide", first = 3.5, second = 5) # The result is 0.7











































