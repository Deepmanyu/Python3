#debugging and error handling

#common python errors
#SyntaxError - when python encounters incorrect syntax

#NameError
#occurs when a variable is not defined, i.e. hasn't been assigned

#TypeError 
#An operation or function is applied to the wrong type. Python cannot
# interpret an operation on two data types
#example - len(5)
#example - "hello" + []

#IndexError 
#Occurs when you try to access an element ina  alist using an invalid
# index(i.e. one that is outside the range of the list or string)
#example - list = ["hello"] and we type list[2]. list has only 1 element


#ValueError 
#This occurs when a built-in operation or a function receives an argument
# that has the right type but an inappropriate value
#example - int("foo")


#KeyErrors 
#This occurs when a dictionary does not have a specific key:
#examle - d = {} and we do d["foo"]. foo is no key in d as its empty

#AttributeError
#This occurs when the variable does not have an attribute
#example - "awesome".foo
#string has no attribute called foo so it gives an errror


################## Raise your own Exception ################
#we raise it like below
# raise ValueError("invalid value")




################## Handling Errors ###############
#In python, it is strongly encouraged to use try/except blocks, to catch
# exceptions when we can do something about them.

try:
	foobar
except:
	print("PROBLEM")
print("after the error")



#example
def get_1(d, key):
	try:
		return d[key]
	except KeyError:
		return None
d = {"name" : "ricky"}

print(get_1(d, "name"))
print(get_1(d, "city")) #the program does not collapse 

#try:
#except:
#else:
#finally:

try:
	num = int(input("enter a number: "))
except:
	print("That's not a number")
else:
	print("I am in the else")
finally:
	print("Runs no matter what")

#we can use the blow for the guessing number game
while True:
	try:
		num = int(input("enter a number: "))
	except:
		print("That's not a number")
	else:
		print("Good job. You entered a number")
		break
	finally:
		print("Runs no matter what")
print("Rest of the game logic")

#example

def devide(a, b):
	try:
		result = a / b
	except ZeroDivisionError:
		print("division by zero not allowed")
	except TypeError as err:
		print("a and b must be ints or floats") 
		print(err)
	else:
		print(result)
print(devide(1, 2))
print(devide(1, "a"))






################### debugging with pdb ################ 

#helps us step through the code - python debugger, its a module just like randon 
#To set breakpoints in our code we can use pdb by insertong this line 
# import pdb; pdb.set_trace() - use like this in one line use
#Commands in pdb
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging and continue with the rest of code)


import pdb

first = "First"
second = "Second"
result = first + second
pdb.set_trace() # put it right before where you think code is breaking
third = "Third"
result += third
print(result)


# is c is a variable then in debugger use p c which means print c


































