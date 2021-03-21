# Author: Rohan Nankani
# Date: November 2, 2020
# Name of Program: GuessingGame
# Purpose: Create a game where the user tries to guess the random-generated number

# Using function to introduce the program, generate a random number, and let user guess the number
def guessing_game():
	# Briefly giving the user an introduction of the program
	print("".center(53, "-"))
	print("I am thinking of a number between 1 and 100...Got it!")
	print("Are you ready to guess the number?")
	input("Press enter to continue: ")
	print("".center(53, "-"))

	# Importing random library to use the random number generator
	import random
	randomNumber = random.randint(1, 100)

	# Intializing the variable userNumber to define it and use it in the while loop
	userNumber = ""

	# Using while statement to keep asking the user to until they guess the random number
	# Using if statements to tell the user whether they guessed low, high, or exact 
	while userNumber != randomNumber:
		userNumber = int(input("Guess the number: "))
		if userNumber > randomNumber:
			print("Guess lower!")
		elif userNumber < randomNumber:
			print("Guess higher!")
		else:
			print("Well done, you guessed the number!")
		print("")
			

# Printing the title of the program
print("The Guessing Game!".center(53))

# Calling the guessing game function to generate random number and let user guess it
guessing_game()

# Uses while and if loops to keep asking user whether they want to play again until they don't want to. 
while True:
	playAgain = input("Do you want to play again (Yes/No)? ")
	if playAgain == "Yes":
		guessing_game()
	else:
		print("".center(53, "-"))
		print("THANK YOU FOR PLAYING!".center(53))
		break