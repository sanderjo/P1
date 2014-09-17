#!/usr/bin/python
# Python to get Smartmeter P1 info based on a "cu -l /dev/ttyUSB0 -s 9600 --parity=none" call
# based on user3210303's work on http://stackoverflow.com/questions/20596908/serial-communication-works-in-minicom-but-not-in-python
# Pure Python seems to drop content from P1
# Tested on a Kamstrup 162JxC smart meter

import time
import os
import signal
import sys
import subprocess
from subprocess import Popen, PIPE

def getP1stuff():
	linecounter = 0
	stack = []
	#Use a process group so as to enable sending a signal to all the process in the groups.
	process = subprocess.Popen('cu -l /dev/ttyUSB0 -s 9600 --parity=none 2> /dev/null', shell=True, stdout=PIPE, bufsize=1, preexec_fn=os.setsid) # send stderr to /dev/null
	#process = subprocess.Popen('cu -l /dev/ttyUSB0 -s 9600 --parity=none ', shell=True, stdout=PIPE, bufsize=1, preexec_fn=os.setsid)

	inblock = False
	slashfound = False
	exclamfound = False

	while linecounter < 50: 	# max number of lines; if this is reached, something is wrong
	    line = process.stdout.readline().rstrip()
	    if line.find('/')==0:
		# smart meter data block starts with '/'
		inblock = True
		slashfound = True
	    if line.find('!')==0:
		# smart meter data block ends with '!'
		stack.append(line)
		inblock = False
		exclamfound = True
		break
	    if inblock:
	    	stack.append(line)
	    linecounter = linecounter + 1

	#if slashfound and exclamfound:
	#	print "Good output found"

	os.killpg(process.pid, signal.SIGTERM) 
	return stack

# MAIN

start_time = time.time()
maxtry=100
trycounter = maxtry # try this amount of time to circumvent "cu: /dev/ttyUSB0: Line in use"
while trycounter > 0:
	result = getP1stuff()
	if len(result) > 5:
		break
	trycounter = trycounter - 1

if trycounter > 0:
	for line in result:
		print line + "\r"       # strangely enough a carriage return "\r" is needed
else:
	print "Something went wrong"

print "tries: ", maxtry+1-trycounter, "\r"
elapsed_time = time.time() - start_time
print "Elapsed time " + str(int(elapsed_time)) + " seconds\r\n"



