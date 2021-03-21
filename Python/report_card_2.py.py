# Author: Rohan Nankani
# Date: October 19, 2020
# Name of Program: ReportCard
# Purpose: To print a report card using inputs and functions 

# Using function to print the information provided
def report_card(count):
	if(count>=1):
		print("")
		nameOfSubject = input("Name of the subject: ")
		teacherName = input("What is the teacher's name? ")
		finalMark = input("Final mark in the course? ")
		report_card(count-1)
		print("")
	if count == 0: return
	print("Subject: " + str(nameOfSubject))
	print("Teacher: " + str(teacherName))
	print("Final Mark: " + str(finalMark))

# Calling the function and running it 8 times.
report_card(8) 