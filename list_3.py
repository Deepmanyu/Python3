# nested list comprehension 

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

#print each item of the nested list
[[print(val) for val in l] for l in nested_list]

#create a nested list of 4 list items each having values 1, 2, 3 

nested_list_1 = [[num for num in range(1, 4)] for val in range(1, 5)]
print(nested_list_1)

# one more example of creating a list with comprehension
print([["X" if num % 2 == 0 else "0" for num in range(1, 6)] for val in range(1, 3)])


# more lists with list comprehension
answer = [[x for x in range(0, 3)] for i in [1, 2, 3]]
print(answer)

answer2 = [[i for i in range(0, 10)] for j in range(0, 10)]
print(answer2)
print(len(answer2))