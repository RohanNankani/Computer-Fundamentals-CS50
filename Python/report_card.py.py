# Author: Rohan Nankani
# Date: October 23, 2020
# Name of Program: ReportCard
# Purpose: Output the report card and the total average using inputs from user

# Function to greet the user at the beginning of the program
def greeting_user():
	print("Hello and welcome to the Report Card program!")
	print("")
	print("I will print your report card and calculate ")
	print("your average based on the inputs you give me!")
	print("")
	input("Press enter to continue! ")
	print("".center(55, "-"))

# Function which allows input from the user about the first subject
def first_subject():
	global nameOfSubject1
	global teacherOfSubject1
	global finalMark1
	nameOfSubject1 = input("What is the name of the first subject? ")
	teacherOfSubject1 = input("What is the teacher's name for " + str(nameOfSubject1) + "? ")
	finalMark1 = input("What is the final mark for " + str(nameOfSubject1) + "? ")
	print("")

# Function which allows input from the user about the second subject
def second_subject():
	global nameOfSubject2
	global teacherOfSubject2
	global finalMark2
	nameOfSubject2 = input("What is the name of the second subject? ")
	teacherOfSubject2 = input("What is the teacher's name for " + str(nameOfSubject2) + "? ")
	finalMark2 = input("What is the final mark for " + str(nameOfSubject2) + "? ")
	print("")

# Function which allows input from the user about the third subject
def third_subject():
	global nameOfSubject3
	global teacherOfSubject3
	global finalMark3
	nameOfSubject3 = input("What is the name of the third subject? ")
	teacherOfSubject3 = input("What is the teacher's name for " + str(nameOfSubject3) + "? ")
	finalMark3 = input("What is the final mark for " + str(nameOfSubject3) + "? ")
	print("")

# Function which allows input from the user about the fourth subject
def fourth_subject():
	global nameOfSubject4
	global teacherOfSubject4
	global finalMark4
	nameOfSubject4 = input("What is the name of the fourth subject? ")
	teacherOfSubject4 = input("What is the teacher's name for " + str(nameOfSubject4) + "? ")
	finalMark4 = input("What is the final mark for " + str(nameOfSubject4) + "? ")
	print("")

# Function which allows input from the user about the fifth subject
def fifth_subject():
	global nameOfSubject5
	global teacherOfSubject5
	global finalMark5
	nameOfSubject5 = input("What is the name of the fifth subject? ")
	teacherOfSubject5 = input("What is the teacher's name for " + str(nameOfSubject5) + "? ")
	finalMark5 = input("What is the final mark for " + str(nameOfSubject5) + "? ")
	print("".center(55, "-"))

# Function which allows printing the course name, teacher's name and final mark
def print_report_card(): 
	print(f'{nameOfSubject1:<15}{teacherOfSubject1:<17}{finalMark1:>11}')
	print(f'{nameOfSubject2:<15}{teacherOfSubject2:<17}{finalMark2:>11}')
	print(f'{nameOfSubject3:<15}{teacherOfSubject3:<17}{finalMark3:>11}')
	print(f'{nameOfSubject4:<15}{teacherOfSubject4:<17}{finalMark4:>11}')
	print(f'{nameOfSubject5:<15}{teacherOfSubject5:<17}{finalMark5:>11}')

# Function which allows the total average to be calculated and printed
def average_grade():
	print("")
	totalAverage = (int(finalMark1) + int(finalMark2) + int(finalMark3) + int(finalMark4) + int(finalMark5)) / 5
	print("YOUR TOTAL AVERAGE IS: " + str(round(totalAverage)))

# Calling the function to greet the user 
greeting_user()

# Calling the function which ask user for input about first subject
first_subject()

# Calling the function which ask user for input about second subject
second_subject()

# Calling the function which ask user for input about third subject
third_subject()

# Calling the function which ask user for input about fourth subject
fourth_subject()

# Calling the function which ask user for input about fifth subject
fifth_subject()

# Giving the user a heads up before the final output 
print("Here is your report card!")
print("")

# Outputting the header
print(f'{"Course Name:":<15}{"Teachers Name:":<17}{"Final Mark:":>11}')
print("".center(43, "-"))

# Calling function to print the courses, teacher's name and final mark
print_report_card()

# Calling function to print the final average
average_grade()