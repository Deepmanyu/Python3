# data modelling using a list and dictionary

playlist = {
	"tiltle": "bollywood", 
	"author": "deep",
	"songs": [
		{"title": "song1", "artist": ["sonu"], "duration": 4.2},
		{"title": "song2", "artist": ["kishore"], "duration": 3.2},
		{"title": "song3", "artist": ["kishore", "lata"], "duration": 5.0}
	]
}


print(playlist) 

#total lenght of the playlist

total_length = 0
for i in playlist["songs"]:
	total_length += i["duration"]
print(total_length)