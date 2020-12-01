#list comprehension 



numbers = [1, 2, 3, 4, 5, 6] 

# make even and odd strings from the list named numbers
even_no = [x for x in numbers if x % 2 == 0]
odd_no  = [x for x in numbers if x % 2 != 0]
print(f"even list: {even_no}, odd list: {odd_no}")


# multiply even numbers by 2 and devide odd numbers by 2
new_list_1 = [x * 2 if x % 2 == 0 else x / 2 for x in numbers]
print(new_list_1)


# remove the vovels from the below string
string_given = "This is so much fun"
new_string = ''.join(char for char in string_given if char not in "aeiou")
print(new_string)


#Given 2 lists [1, 2, 3, 4] and [3, 4, 5, 6], create a variable called answer,
# which is a new list that is the intersection of the two. 
# Your output should be [3, 4]
answer = [num for num in [1, 2, 3, 4] if num in [3, 4, 5, 6]]
print(answer)

#Given a list of words ["Elie", "Tim", "Matt"] create a variable
# called answer2, which is a new list with each word reversed and in 
# lower case. Output should be ["eile", 'mit', 'ttam'] 
answer2 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
print(answer2)

#For all the numbers between 1 and 100(including 100), create a 
# list with all the numbers that are divisible by 12.
answer3 =  [num for num in range(1, 101) if num % 12 == 0]
print(answer3)

#Given the string "amazing", create a variable called answer4, 
# which is a list containing all the letters from "amazing" but not
# the vowels (a, e, i , o, u). 
answer4 = [char for char in "amazing" if char not in "aeiou"]
answer4.reverse()
print(answer4)





