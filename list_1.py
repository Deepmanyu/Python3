#lists

# 1st example of list 
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ""
for i in sounds:
    result += i.upper()
print(result)

# to add to an existing list 
# listname.append() - adds one value to the end
# listname.extend() - adds multiple values to the end
# listname.insert(position, value) - adds a vlaue at a specified position


# to remove from an existing list
# listname.clear() - removes all items and empties the list
# listname.pop(index_number) - if index_number is left blank, the last item is removed.  new_var = listname.pop()
# listname.remove(value_to_remove) - removes the first instance of the value. If no occurance found, it gives an error. Cannot be used to get it into  new variable.

# listname.index(value) , listname.index(value, start_index, end_index) - gives the index of the value in the list
# listname.count(value) - counts the number of occurances of the value in the list
# listname.reverse() - reverses the order of the list
# listname.sort() - sorts the list in the ascending order (more to come on sorts on later sections)

# join - it concatenates, also used to convert a list into a string and adds some specific character in between the list values

words = ["coding", "is", "fun"]
joined_words = " ".join(words)
print(f"{words} , {joined_words}")

instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])
# Remove the last value in the list
instructors.pop()
# Remove the first value in the list
instructors.pop(0)

# Add the string "Done" to the beginning of the list
instructors.insert(0, "Done")


# slicing
# listname[start:end:step] - even if 1 argument is given, we have to use a :
numbers = [1, 2, 3, 4, 5, 6]
numbers[2:]
numbers[4:]
numbers[-2]

numbers[:2] # end is exclusive
numbers[:4]
numbers[1:3]
numbers[:-1]
numbers[1:-1]

numbers[1::2]
numbers[::2]
numbers[1::-1]
numbers[:1:-1]
numbers[2::-1]


#swapping/shuffelling values in a list

names = ["deepam", "anshu", "superman"]
print(names)
names[0], names[1] = names[1], names[0]
print(names)




