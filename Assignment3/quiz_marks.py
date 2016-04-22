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
	For each log file
		write to standard output the course mark for the log file,
		in CSV format
preconditions
	Each command-line argument is the name of a legal, readable quiz log file.

	All of the log files have the same number of questions.
'''

# handle command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()
else:
	# loop the list according to the input 
	for i in range(len(sys.argv) - 1):
		mark = 0
		for j in quiz_library.compute_mark_list(quiz_library.load_quiz_log(sys.argv[i + 1])):
			# calculate mark according to the result in the list
			mark = mark + int(j)
		courseMark = sys.argv[i + 1] + "," + str(mark)	
		print courseMark

