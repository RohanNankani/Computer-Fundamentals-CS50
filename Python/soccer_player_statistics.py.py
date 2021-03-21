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

# Creating the function to take the input from the user about the players info and store it in the intialized list. 
def soccer_player_info(n):
		name[n] = input("What is the name of the player: ")
		team[n] = input("What is the team of the player: ")
		goals[n] = input("How many goals have the player scored: ")
		print("")

# Calling the 
soccer_player_info(n)

while True:
	userResponse = input("Do you want to add more players (Y/N)? ")
	if userResponse == "Y":
		n = n + 1
		name.insert(n, "")
		team.insert(n, "")
		goals.insert(n, "")
		print("")
		soccer_player_info(n)
	else:
		break

print("")

print(f'{"Player:":<17}{"Team:":<15}{"Goals:":>6}')
print("".center(38, "-"))

for z in range(0,n+1):
	print(f'{name[z]:<17}{team[z]:<15}{goals[z]:>6}')