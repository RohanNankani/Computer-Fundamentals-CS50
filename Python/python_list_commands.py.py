# Author: Rohan Nankani
# Date: November 11, 2020
# Name of Program: SoccerPlayersStatistics
# Purpose: To allow the user to keep adding players statistics to the table until they want using lists. 

# Intializing the list 
name = [""]
team = [""]
goals = [""]

# Intializing the variable n 
n = 0

# Creating the function to get input from the user about the players info and store it in the intialized list 
def soccer_player_info(n):
	name[n] = input("What is the name of the player: ")
	team[n] = input("What is the team of the player: ")
	goals[n] = input("How many goals have the player scored: ")
	print("")

# Greeting the user at the beginning of program
print("Welcome to the Players Statisitcs Program!")
print("I will help you create player's statistic table!")
print("")
input("Press enter to continue: ")
print("".center(48, "-"))

# Calling the function
soccer_player_info(n)

# Using while loop which asks user whether they want to add players to the list.
# If yes, it creates space at the end of the list and calls the function again for the input of the user to be stored.
while True:
	userResponse = input("Do you want to add more players (Y/N)? ")
	if userResponse == "Y":
		n += 1
		name.append("")
		team.append("")
		goals.append("")
		print("")
		soccer_player_info(n)
	else:
		break

print("")

# Printing the heading of the table
print(f'{"Player:":<17}{"Team:":<15}{"Goals:":>6}')
print("".center(38, "-"))

# Printing the values stored in the name, team, and goals list
for z in range(0,n+1):
	print(f'{name[z]:<17}{team[z]:<15}{goals[z]:>6}')