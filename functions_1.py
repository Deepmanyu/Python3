#functions - part1

def make_noise():
    """A simple function that prints a string in upper case"""
    print("the crowd goes wild".upper())
make_noise()
print(make_noise.__doc__)

#returning value from a function
# return exits the function
# outputs whatever value is placed after the return keyword
# pops the function off the call stack

def print_square_of_seven():
	print("i am befor the return".upper())
	return 7 ** 2
print(print_square_of_seven())


#coin flip
from random import random

def flip_coin():
	if random() > .5: # generates a randon number from 0 - 1
		return "Heads"
	else:
		return "Tails"
print(flip_coin())

# function that returns a list of even numbers between 1 and 5
def generate_evens():
    return [i for i in range(1, 5) if i % 2 == 0]
print(generate_evens())

#square function - inputting a value in the function
def square(num):
	return num ** 2
print(square(8))
print(square(4))


#parameters vs arguments
# parameter is in the declaration 
# argument is the actual value passed in the function


# default parameters - 1 is default for a and b
# default parameters can be anything - functions, lists, strings, boolean

def add(a = 1, b = 1):
	return a + b
print(add(10, 4))
print(add())

def subtract(a, b):
	return a - b

def math(a, b, fn = add):
	return fn(a,b)

print(math(2, 3))
print(math(2, 3, subtract))










