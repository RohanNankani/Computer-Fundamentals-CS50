# Author: Rohan Nankani
# Date: October 28, 2020
# Name of Program: LetterGrade
# Purpose: To create a program which determines and outputs the letter grade using the input of mark.

# Greeting user and informing them regarding the purpose of this program
print("Hello and welcome to the LetterGrade program!")
print("")
print("I will help you determine your letter grade based on your mark!")
print("")
input("Press enter to continue: ")

# Lines to seperate the greeting from the input of the user
print("".center(45, "-"))

# Getting input from the user about their mark
mark = int(input("What is your mark: "))
print("")

# Allowing computer to make a decision and give an output based on the user's input
# Letter grade A+, A, A- 
if mark >= 90:
	print("You received an A+!")
elif 89 >= mark >= 85:
	print("You receieved an A!")
elif 84 >= mark >= 80:
	print("You received an A-!")

# Letter grade B+, B, B-
elif 79 >= mark >= 77:
	print("You received a B+!")
elif 76 >= mark >= 73:
	print("You received a B!")
elif 72 >= mark >= 70:
	print("You received a B-!")

# Letter grade C+, C, C-
elif 69 >= mark >= 67:
	print("You received a C+!")
elif 66 >= mark >= 63:
	print("You received a C!")
elif 62 >= mark >= 60:
	print("You received a C-!")

# Letter grade D+, D, D-
elif 59 >= mark >= 57:
	print("You received a D+!")
elif 56 >= mark >= 53:
	print("You received a D!")
elif 52 >= mark >= 50:
	print("You received a D-!")

# Letter grade F
else:
	print("Sorry, you failed!")

# Lines to seperate the output of letter grade and good-bye section
print("".center(45, "-"))

# Signing off the program
print("Thank you for using the LetterGrade program.")