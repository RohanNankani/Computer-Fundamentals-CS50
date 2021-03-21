# Author: Rohan Nankani
# Date: 15/10/2020
# Name of the program: Baseball-Players
# Purpose: Output the statistics of baseball players using functions

# Define a function to output players statistics line
def player_stat(pName, tName, pAvg):
	print(f'{pName:<12}{tName:<18}{pAvg:>10}')

# Column headings and underline
player_stat("Player:", "Team:", "Avg:")
print("".center(40,"-"))

# Player statistics
player_stat("Rohan", "Toronto Blue Jays", "0.391")
player_stat("Bill", "Houston Astros", "0.244")
player_stat("Jeff", "Tampa Bay Rays", "0.462")
player_stat("Barack", "New York Yankees", "0.281")
player_stat("Warren", "LA Dodgers", "0.250")


