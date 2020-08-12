 #guessing game - guess the number

from random import randint
number = randint(1, 10)

guess = None
play_again = "y"

while play_again == "y":
	
	while guess != number:
		guess = input("Enter a number between 1 and 10: ")
		if guess != "":
			guess = int(guess)
		if guess < number:
			print("Too Low")
		elif guess > number:
			print("Too High")
		else:
			print("You got it")
			play_again = input("Want to play again? (y/n): ").lower()
			if play_again == "y":
				number = randint(1, 10)
			else:
				print("Thank you")
				break