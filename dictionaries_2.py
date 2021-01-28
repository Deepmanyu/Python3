#dictionaries

d = dict(a = 1, b = 2, c = 3) 
c = d.copy() #copy the dictionary into another dictionary
print(c)

print(c == d) #tests for equality in values
print(c is d) #tests for equality in memory

d.clear() #empty the dictionary
print(d)
d = dict(a = 1, b = 2, c = 3) 


#fromkeys - used to create dictionaries with innitial defalut values
# it always iterates over the list[] and stores the value
new_user = {}.fromkeys(['name', 'score', 'email', 'profile'], 'unknown')
print(new_user)

game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

#Use the game_properties list and dict.fromkeys() to generate 
# a dictionary with all values set to 0. Save the result to a
# variable called initial_game_state
initial_game_state = dict.fromkeys(game_properties, 0)



#get
print(d["a"])
print(d.get("a"))

#try it out 
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock.keys():
	print("{} left".format(bakery_stock[food]))
else:
	print("We don't make that")


#pop - used to remove the key-value pair. It always takes an argument
#popitem this removes a randomly picked key-value pair from the dict. 
#popitem takes no argument
d.pop("a")
print(d)


#update
first = dict(a = 1, b = 2, c = 3, d = 4, e = 5)
second = {}

second.update(first)
print(second)

second["a"] = "amazing"
print(second)

third = {"l" : "long", "m": "my"}
print(third)

third.update(second) # adds second at the end of third
print(third)

forth = {"z": "zoo" , "a": 1}
print(forth)

forth.update(second) # updates a to amazing and adds all the other key-value pairs
print(forth)


forth.update({}) # does nothing 


#try it out 
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

stock_list = inventory.copy()


stock_list.update({"cookie" : 18})
stock_list.pop("cake")


# dictonary - adding new key-value pairs

new_1 = dict(greet = "hi", gender = "M")
print(new_1)

new_1["species"] = "Human"
print(new_1)













