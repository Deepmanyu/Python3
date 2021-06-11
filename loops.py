# loops in python

#range(start, stop, step): default start is 0 and step is 1
#range(7): would give numbers from 0 to 6

for x in range(1, 8, 2):
	print(x)
	print(x*x)

for letter in "coffee":
	print(letter*10)


# printing nums would print range(1, 5). 
nums = range(1, 5)
print(nums)

#
times = input("How many times: ") 
times = int(times)

for time in range(times):
	print(f"Time {time+1}: I will be a \"BILLIONAIRE\"") 

#unlucky numbers
for num in range(4, 14):
	if num == 4 or num == 13:
		print(f"{num} is unlucky")
	else:
		if num%2 == 0:
			print(f"{num} is even")
		else:
			print(f"{num} is odd")


#emogi art

for num in range(1, 11):
	print("\U0001f600" * num)


#printing the same emogi art using a while loop instead of string multiplication
for num in range(1, 11):
	counter = 1
	smiley = ""
	while counter <= num:
		smiley += "\U0001f600"
		counter += 1
	print(smiley)

