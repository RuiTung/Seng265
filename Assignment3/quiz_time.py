'''
For Assignment 3: V00800795 Rui Ma, Nov 21st, 2015
quiz_time.py
'''

import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	For each log file, compute the total time taken for each question. 

	Write to standard output, the average time spent for each question.
preconditions
	Each command-line argument is the name of a readable and
	legal quiz log file.

	All the log_files have the same number of questions.
'''

# handle command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()

else:
	answerTime = 0
	answerIndex = 0
	#displayIndex = 0

	# declare a list to store differences of display time
	displayTime = [0] * quiz_library.compute_question_count(quiz_library.load_quiz_log(sys.argv[1]))

	# declare a list to store the display time difference
	timeDifference = [0] * quiz_library.compute_question_count(quiz_library.load_quiz_log(sys.argv[1]))

	# declare a list to store the average time of each question
	avgTime = [0] * quiz_library.compute_question_count(quiz_library.load_quiz_log(sys.argv[1]))

	for i in range(1, len(sys.argv)):
		# loop every list to get information of display time
		for j in quiz_library.load_quiz_log(sys.argv[i]):
			if isinstance(j,quiz_library.Display):
				# get every display time and check whether it is the last display 
				if displayTime[int(j.index)] <= int(j.time) and displayTime[int(j.index)] != 0:
					specialCase = 0
				# store the display time if it is not the last one
				else:				
					displayTime[int(j.index)] = int(j.time)

			# check whether it is answer time and store the last answer time for the case of 
			# last display without another display
			if isinstance(j,quiz_library.Answer) and j.time != 'None':
				if (int(j.time) >= answerTime):
					answerTime = int(j.time)
					answerIndex = int(j.index)
		
		# loop display time and caluculate the difference then store the result in time Difference list
		for k in range(0,len(displayTime) - 1):
			if displayTime[k + 1] != 0:
				timeDifference[k] = timeDifference[k] + float(displayTime[k + 1]) - float(displayTime[k])
		timeDifference[answerIndex] = timeDifference[answerIndex] + float(answerTime) - displayTime[answerIndex]
		
		# initialization
		answerTime = 0
		displayTime = [0] * quiz_library.compute_question_count(quiz_library.load_quiz_log(sys.argv[1]))	
	
	# calculate the average time then store the result into avgTime list
	i = 0
	while i in range(len(timeDifference)):
		avgTime[i] = timeDifference[i] / (len(sys.argv) - 1)
		i = i + 1
	
	# print the result
	j = 0
	finalAvgTime = ''
	while j in range(len(timeDifference) - 1):
		finalAvgTime = finalAvgTime + str(avgTime[j]) + ','
		j = j + 1
		
	print finalAvgTime + str(avgTime[len(avgTime) - 1])
	
				
	
