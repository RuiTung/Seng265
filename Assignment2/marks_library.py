'''
  For Assignment 2 : V00800795 Rui Ma, November 6th, 2015 
  marks_library.py
 '''


import libxml2
import sys

'''
purpose
	return the course mark for student s
preconditions
	student is a list of the form:
		[last_name, first_name, student_id, marks]
		where
		marks is a list of the form: [ [mark_id,score], ... ]
	assignments is a dictionary of the form:
		{mark_id:[points, percentage], ... }
'''
def compute_mark(student, assignments):

	courseMark = 0
	i = 0
	length = (len(student[3]))
	while(i < length):
		studentAssignment = student[3][i][1]
		assignmentPoints = float(assignments[student[3][i][0]][0])
		assignmentPercentage = assignments[student[3][i][0]][1]	
		courseMark += studentAssignment / assignmentPoints * assignmentPercentage
		i = i + 1
	return courseMark
	

'''
purpose
	extract the information from a and return it as a list:
		[mark_id, points, percentage]
preconditions
	a is an assignment element from a legal assignments XML file
'''
def extract_assignment(a):

	information = [0,1,2]	
	while a is not None:
		if a.name == "mark_id":
			information[0] = a.content
		if a.name == "points":
			information[1] = int(a.content)
		if a.name == "percentage":
			information[2] = float(a.content)
		a = a.next
	return information

'''
purpose
	extract the information from s and return it as a list:
		[last_name, first_name, student_id, marks]
		where
		marks is a list of the form: [ [assignment_id,score], ... ]
preconditions
	s is a student element from a legal students XML file
'''
def extract_student(s):

	information = range(0,4)
	information[3] = []
	while s is not None:
		if s.name == "last_name":
			information[0] = s.content
		if s.name == "first_name":
			information[1] = s.content
		if s.name == "student_id":
			information[2] = s.content
		if s.name == "marks":
			child = s.children
			smallList = range(0,2)
			for i in child:
				if i.name == "mark_id":
					smallList[0] = i.content
				if i.name == "score":
					smallList[1] = int(i.content)
				if smallList[0] != 0 and smallList[1] != 1:
						information[3].append(smallList)
						smallList = range(0,2)
		s = s.next
	return information

