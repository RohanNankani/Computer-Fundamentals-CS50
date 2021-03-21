# Author: Rohan Nankani
# Date: October 13, 2020
# Name of Program: AddNumbers-Input
# Purpose: To practise using input from user.

# Ask the user for the name
name = input("Hello, what is your name? ")
print("")
print("Welcome " + name + "!")

# Tell user what this program will do
print ("I will now calculate your age!")


# Create variables and initializing them
num1 = 0
num2 = 0
total = 0

# Ask the user for the first number
print("")
num1 = int(input("What is the current year? "))

# Ask the user for the second input number
num2 = int(input("When were you born? "))

# Find the difference between the two input numbers.
total = num1 - num2

# Tell the user their age
print("")
print("You are: " + str(total) + " years old!")




