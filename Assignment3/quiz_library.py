'''
For Assignment 3: V00800795 Rui Ma, Nov 19th, 2015
quiz_library.py
'''

import libxml2
import sys

'''
purpose
	store the information from an answer element
'''
class Answer:
	def __init__(self, index, path, result, answer, time):
		self.index = index
		self.path = path
		self.result = result
		self.answer = answer
		self.time = time

'''
purpose
	Store the information from a display element.
'''
class Display:
	def __init__(self, index, path, time):
		self.index = index
		self.path = path
		self.time = time

'''
purpose
	Extract the information from log_file and return it as a list
	of answer and display objects.
preconditions
	log_file is the name of a legal, readable quiz log XML file
'''
def load_quiz_log(log_file):

	# convert the content of xml file into element tree
	parse_tree = libxml2.parseFile(log_file)
	context = parse_tree.xpathNewContext()
	root = parse_tree.getRootElement()
	element = root.children

	information = []

	#initialize all attributes
	index, path, result, answer, time = 'None', 'None', 'None', 'None', 'None'
	
	# check whether the element tag is answer
	while element is not None:
		#index, path, result, answer, time = 'None', 'None', 'None', 'None', 'None'
		if element.name == 'answer':
			info = element.children
			while info is not None:
				#if info.content != '':
				if info.name == 'index' and info.content != '':
					index = info.content
				if info.name == 'path' and info.content != '':
					path = info.content
				if info.name == 'result' and info.content != '':
					result = info.content
				if info.name == 'answer' and info.content != '':
					answer = info.content
				if info.name == 'time' and info.content != '':
					time = info.content
				info = info.next
			information.append(Answer(index, path, result, answer, time))

		# check whether the element tag is display
		if element.name == 'display':
			info = element.children
			while info is not None:
				#if info.content != '':
				if info.name == 'index' and info.content != '':
					index = info.content
				if info.name == 'path' and info.content != '':
					path = info.content
				if info.name == 'time' and info.content != '':
					time = info.content
				info = info.next
			information.append(Display(index, path, time))
			#index, path, result, answer, time = 'None', 'None', 'None', 'None', 'None'
		element = element.next
	return information

'''
purpose
	Return the number of distinct questions in log_list.
preconditions
	log_list was returned by load_quiz_log
'''
def compute_question_count(log_list):
	i = 0
	count = 0
	while i in range(len(log_list)):
		# check whether the tag is answer and the series content is none
		if isinstance(log_list[i],Answer) and log_list[i].result == 'None' and log_list[i].answer == 'None'and log_list[i].time == 'None':
			count = count + 1
		i = i + 1
	return count
		

'''
purpose
	Extract the list of marks.
	For each index value, use the result from the last non-empty answer,
	or 0 if there are no non-empty results.
preconditions
	log_list was returned by load_quiz_log
'''
def compute_mark_list(log_list):
	
	'''
	version without checking time
	
	tempMark =['0'] * len(log_list)
	
	i = 0
	while i in range(len(log_list)):
		log_list[i] == '0'
		i = i + 1
		
	mark = []
	
	i = 0
	while i in range(len(log_list)):
		if isinstance(log_list[i],Answer):
			tempMarkIndex = int(log_list[i].index)
			if log_list[i].result == 'None' or log_list[i].result == '0':
				tempMark[tempMarkIndex] = int(tempMark[tempMarkIndex]) + 0
			if log_list[i].result == '1':
				tempMark[tempMarkIndex] = int(tempMark[tempMarkIndex]) + 1
		i = i + 1
	
	i = 0
	while i in range(len(tempMark)):
		if isinstance(tempMark[i], int):
			if tempMark[i] >= 1:
				mark.append(1)
			else:
				mark.append(0)
		i = i + 1
	return mark
	'''
	
	# initialize Mark list according to the length of questions list
	Mark =['0'] * (compute_question_count(log_list))
	
	i = 0
	tempTime = 0
	
	while i in range (len(log_list)):
		if isinstance(log_list[i], Answer):
			markIndex = int(log_list[i].index)
			if log_list[i].result == 'None':
				Mark[markIndex] = 0
			else:
				if int(log_list[i].time) >= tempTime:
					tempTime = int(log_list[i].time)
					Mark[markIndex] = int(log_list[i].result)

				else:
					# special case for ignoring smaller time
					specialCase = 0
		i = i + 1			
			
	return Mark
	