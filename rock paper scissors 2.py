# making a rock paper scissors game

import random

player_score = 0
computer_score = 0


while True:
	min_score_to_win = input("Enter the min. score required to win the game: ")
	if min_score_to_win == "":
		print("Enter a number please") 
	elif int(min_score_to_win) < 1:
		print("Enter a number greater than 1")
	elif int(min_score_to_win) > 10:
		print("Enter a number smaller than 10") 
	else:
		break 



min_score_to_win = int(min_score_to_win)

#game display
print(".... Rock ....")
print(".... Paper ....")
print(".... Scissors ....") 
print("Enter q to quit the game at anytime")

while player_score < min_score_to_win and computer_score < min_score_to_win:

	#input from the player
	player = input("Player, make your move: ").lower()
	if player == "q":
		break

	# creating a random computer move 
	random_selection = random.randint(0, 2)
	if random_selection == 0:
		auto_player = "rock"
	elif random_selection == 1:
		auto_player = "paper"
	else:
		auto_player = "scissors"

	print(f"Computer played: {auto_player}")

	#logic for the game 
	if player == "rock" or player == "paper" or player == "scissors":
		if player == auto_player:
			print("Its a tie")
		elif player == "rock" and auto_player == "scissors":
			print("You win")
			player_score += 1
		elif player == "paper" and auto_player == "rock":
			print("You win")
			player_score += 1
		elif player == "scissors" and auto_player == "paper":
			print("You win")
			player_score += 1
		else:
			print("Computer wins")
			computer_score += 1 
	else:
		print("Enter a valid game move")

if player_score > computer_score:
	print("Congratulations! You won")
elif player_score < computer_score:
	print("Better luck next time")
else:
	print("Its a tie")

print(f"Final Scores: Player- {player_score}, Computer-{computer_score} ")


