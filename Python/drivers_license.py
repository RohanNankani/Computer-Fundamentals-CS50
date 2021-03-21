# Author: Rohan Nankani
# Date: October 27, 2020
# Name of Program: DriverLicense
# Purpose: To determine if the user is able to get a driver's license

# Greets user and gives brief detail on what the program does
print("Hello and welcome to the Driver License program!")
print("")
print("I will help you determine if you can get your driver's license!")
print("")
input("Press enter to continue: ")
print("".center(60, "-"))

# Gets input from the user about their age
age = int(input("What is your age? "))
print("")

# Determines whether the user is able to get a driver's license
if age >= 16:
	print("You are able to get the driver's license!")
else:
	print("You are not able to get a driver's license!")
