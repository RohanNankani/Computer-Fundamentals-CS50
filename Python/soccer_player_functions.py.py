# Author: Rohan Nankani	
# Date: 2020/10/16
# Name of Program: SoccerStories-Functions
# Purpose: Output the soccer STORIES of some awesome players using functions.

def player_paragraph(pName, tName, gScored):
	print(str(pName) + " is an awesome soccer player.")
	print(str(pName) + " plays for " + str(tName) + ".")
	print(str(pName) + " has scored " + str(gScored) + " goals.")
	print("")


# Title and underline.
print("Soccer Stories".center(42))
print("----------------".center(42))
print("")

player_paragraph("Rohan","FC Barcelona","45")
player_paragraph("Ronaldo","FC Barcelona","32")
player_paragraph("Messi","FC Barcelona","5")
player_paragraph("Mbappe","Paris Saint Germain","20")

