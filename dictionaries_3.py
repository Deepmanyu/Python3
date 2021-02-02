#dictionaries comprehension

# example 
numbers = dict(first = 1, second = 2, third = 3)
sq_numbers = {key1: values1 ** 2 for key1, values1 in numbers.items()}

print(f"{numbers}{sq_numbers}")

# creating a dictionary with dictionary comprehension

#1
d1 = {num: num ** 2 for num in [1, 2, 3, 4, 5]}
print(d1)

#2
str1 = "abc"
str2 = "123"
combo_str = {str1[i]: str2[i] for i in range(0, len(str1) -1 )} 
print(combo_str)

#3
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer = {list1[i]: list2[i] for i in range(0, len(list1))}
print(answer)
answer1 = dict(zip(list1, list2)) #we can use zip also as an advanced function
print(answer1)


# conditional logic with dictionaries 
num_list = [1, 2, 3, 4]
num_dict = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(num_dict)


#try it out : create a dictionary called answer2, that makes each 
# first item in each list a key and the second item a corresponding value
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer2 = {person[i][0]: person[i][-1] for i in range(0, len(person))}
print(answer2) 

#ascii values and numbers 
answer = {i: chr(i) for i in range(65, 91)}
print(answer)
