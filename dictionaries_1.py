# dictionaries 

#create 2 dictionaries called user_info and add at least 3 key value
# pairs to it

#list
user_info = [{"sno": 1, "name": "deep", "gender": "M"},
			{"sno": 2, "name": "ceep", "gender": "F"},
			{"sno": 3, "name": "feep", "gender": "M"},]
print(user_info)
print(type(user_info)) 

#dictionary
user_info2 = dict(sno = 1 , name = "deep", gender = "M")
print(user_info2)
print(type(user_info2))

print(user_info2["name"]) #accessing the value of the dict
print(user_info2["gender"]) 

#create a variable full_name using values in a dictionary
artist = {
    "first": "Neil",
    "last": "Young",
}

full_name1 = "{} {}".format(artist["first"], artist["last"])
full_name2 = artist["first"] + " " + artist["last"]
# attention to the single quotes for the dictionaty key
full_name3 = f"{artist['first']} {artist['last']}"

print(full_name1 + full_name2 + full_name3)


# looping a dictionary 

for i in user_info2.values():
	print(i)
for i in user_info2.keys():
	print(i)
for i in user_info2.items():
	print(i)

for k, v in user_info2.items():
	print(k, v)


# calculate total donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

#Use a loop to add together all the donations and store the 
# resulting number in a variable called total_donations

total_donations = 0
for v in donations.values():
    total_donations+= v
print(total_donations)

total_donations = sum(a for a in donations.values())
print(total_donations)

total_donations = sum(donations.values())

#using in and dictionaries

if "sam" in donations.keys():
	print(f"sam donated for the cause. amount: {donations.get('sam')}")
print(25.0 in donations.values())




