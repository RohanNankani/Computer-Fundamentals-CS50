# Author: Rohan Nankani
# Date: November 11, 2020
# Name of Program: MadLibTheater
# Purpose: To create a mad lib theater game which ask user for input, store their input using list, and print the story. 

# Intializing the list
grammar = []

# List of prompts that describe the category of the next word
# to be substituted in the story 
prompts = [
	"an adjective: ",
	"an another adjective: ",
	"a type of bird: ",
	"a room in a house: ",
	"a past tense verb: ",
	"a verb: ",
	"a name: ",
	"a noun: ",
	"a type of liquid: ",
	"a verb ending in -ing: ",
	"a plural part of the body: ",
	"a plural noun: ",
	"a verb ending in -ing: ",
	"a noun: "
]

# Function to ask user for input for each of the prompts 
def grammar_input():
	for prompt in prompts:
		grammar.append(input("Enter " + prompt))

# Function to print the story with the user's input
def story_template():
	print("It was a " + grammar[0] + ", cold November day.")
	print("")
	print("I woke up to the " + grammar[1] + " smell of " + grammar[2] + " roasting in the " + grammar[3] + " downstairs.")
	print("")
	print("I " + grammar[4] + " down the stairs to see if I could help " + grammar[5] + " the dinner.") 
	print("")
	print("My mom said, 'See if " + grammar[6] + " needs a fresh " + grammar[7] + ".'")
	print("")
	print("So I carried a tray of glasses full of " + grammar[8] + " into the " + grammar[9] + " room.") 
	print("")
	print("When I got there, I couldn't believe my " + grammar[10] + "! There were " + grammar[11] + " " + grammar[12] + " on the " + grammar[13] + "!")

# Greeting the user at the beginning of program
print("Welcome to the Mad Lib Theater!".center(53))
print("")
print("I want you to give me the first word that comes to your mind for described category.")
print("")
print("Are you ready?")
print("")
input("Press enter to continue: ")
print("".center(48, "-"))

# Calling the grammar input function to get input from user
grammar_input()

print("")

# Calling story template function to print the story
story_template()

# Using while loop to ask the user if they want to play again
while True:
	print("")
	userResponse = input("Do you want to play again (Y/N)? ")
	if userResponse == "Y":
		print("".center(48, "-"))
		grammar = []
		grammar_input()
		print("")
		story_template()
	else:
		print("".center(48, "-"))
		print("Thank you for playing!".center(53))
		break