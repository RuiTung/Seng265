'''
For Assignment 3: V00800795 Rui Ma, Nov 20th, 2015
quiz_time.py
'''

import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	Accumulate across all the log files the pass ratio for each question.

	A question result is considered a pass if it is not 0 or None
	and fail otherwise.

	The pass ratio for a question is the number of passes
	divided by the number of passes + fails.
preconditions
	Each command-line argument is the name of a
	readable and legal quiz log file.

	All the log_files have the same number of questions.
'''

# check number of command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()
else:

	marks = 0
	ratio = ''
	
	# loop the list according to the input
	for i in range(len(quiz_library.compute_mark_list(quiz_library.load_quiz_log(sys.argv[1])))):
		for j in range(len(sys.argv) - 1):
			marks = marks + int(quiz_library.compute_mark_list(quiz_library.load_quiz_log(sys.argv[j + 1]))[i])

		# calculate the ratio and store the result to string ratio	
		ratio = ratio + ',' + str(float(marks) / (len(sys.argv) - 1))

		# initialize marks
		marks = 0
	
	# print the ratio
	i = 1
	finalRatio = ''
	while i in range(len(ratio)):
		finalRatio = finalRatio + ratio[i]
		i = i + 1
	print finalRatio	
	
