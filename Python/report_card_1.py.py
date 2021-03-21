# Author: Rohan Nankani
# Date: October 19, 2020
# Name of Program: ReportCard
# Purpose: To print a report card using inputs and functions 

# Using function to get input from the user
def get_input():
	nameOfSubject = input("Name of the subject: ")
	teacherName = input("What is the teacher's name? ")
	finalMark = input("Final Mark: ")
	print("")
	return nameOfSubject, teacherName, finalMark

# Using function to print the information gotten from the user through input
def report_card(nSubject, tName, fMark):
	print("Subject: " + str(nSubject))
	print("Teacher: " + str(tName))
	print("Final Mark: " + str(fMark))
	print("")

# Using functions to calculate the average by taking all the inputs for finalMark and dividing by 8 (number of courses)
def average_grade():
	totalAverage = (int(finalMark1) + int(finalMark2) + int(finalMark3) + int(finalMark4) + int(finalMark5) + int(finalMark6) +int(finalMark7) + int(finalMark8)) / 8
	print("YOUR TOTAL AVERAGE IS: " + str(round(totalAverage)))


nameOfSubject1, teacherName1, finalMark1 = get_input() 
nameOfSubject2, teacherName2, finalMark2 = get_input() 
nameOfSubject3, teacherName3, finalMark3 = get_input() 
nameOfSubject4, teacherName4, finalMark4 = get_input() 
nameOfSubject5, teacherName5, finalMark5 = get_input() 
nameOfSubject6, teacherName6, finalMark6 = get_input() 
nameOfSubject7, teacherName7, finalMark7 = get_input() 
nameOfSubject8, teacherName8, finalMark8 = get_input() 

# Calling the funtion to use the input for each subject and print it
report_card(nameOfSubject1, teacherName1, finalMark1) 
report_card(nameOfSubject2, teacherName2, finalMark2) 
report_card(nameOfSubject3, teacherName3, finalMark3) 
report_card(nameOfSubject4, teacherName4, finalMark4) 
report_card(nameOfSubject5, teacherName5, finalMark5) 
report_card(nameOfSubject6, teacherName6, finalMark6) 
report_card(nameOfSubject7, teacherName7, finalMark7) 
report_card(nameOfSubject8, teacherName8, finalMark8) 

# Calling the function to output the average grade
average_grade()
