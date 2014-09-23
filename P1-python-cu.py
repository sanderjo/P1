#!/usr/bin/python
# Python script to get Smartmeter P1 info based on a "cu -l /dev/ttyUSB0 -s 9600 --parity=none" call
# Based on user3210303's work on http://stackoverflow.com/questions/20596908/serial-communication-works-in-minicom-but-not-in-python
# Pure Python seems to drop content from P1
# Tested on a Kamstrup 162JxC smart meter connected to a Raspberry Pi with Raspbian

import time
import os
import signal
#import sys
import subprocess
#from subprocess import Popen, PIPE

def getP1stuff():
	linecounter = 0
	stack = []
	#Use a process group so as to enable sending a signal to all the process in the groups.
	process = subprocess.Popen('cu -l /dev/ttyUSB0 -s 9600 --parity=none 2> /dev/null', shell=True, stdout=subprocess.PIPE, bufsize=1, preexec_fn=os.setsid) # send stderr to /dev/null
	#process = subprocess.Popen('cu -l /dev/ttyUSB0 -s 9600 --parity=none ', shell=True, stdout=subprocess.PIPE, bufsize=1, preexec_fn=os.setsid)

	inblock = slashfound = exclamfound = False

	while linecounter < 75: 	# max number of lines; if this is reached, something is wrong
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
trycounter = maxtry = 100 # try this amount of time to circumvent "cu: /dev/ttyUSB0: Line in use"
while trycounter > 0:
	result = getP1stuff()
	if len(result) > 15:
		break
	trycounter -= 1 # count down

if trycounter > 0:
	# we didn't reach 0, so there was OK output, so print it
	for line in result:
		print line + "\r"       # strangely enough a carriage return "\r" is needed
else:
	print "Something went wrong"

print "tries: ", maxtry+1-trycounter, "\r"
elapsed_time = time.time() - start_time
print "Elapsed time " + str(int(elapsed_time)) + " seconds\r\n"



'''
Typical output from this script, in this from a Kamstrup with electricty and gas meter:

/KMP5 KA6U001759732938

0-0:96.1.1(204B413655303031373539343937393133)
1-0:1.8.1(00991.194*kWh)
1-0:1.8.2(00841.457*kWh)
1-0:2.8.1(00197.128*kWh)
1-0:2.8.2(00512.722*kWh)
0-0:96.14.0(0002)
1-0:1.7.0(0000.35*kW)
1-0:2.7.0(0000.00*kW)
0-0:17.0.0(999*A)
0-0:96.3.10(1)
0-0:96.13.1()
0-0:96.13.0()
0-1:24.1.0(3)
0-1:96.1.0(4730303135353631323030393331373133)
0-1:24.3.0(140923220000)(08)(60)(1)(0-1:24.2.1)(m3)
(00543.774)
0-1:24.4.0(1)
!
tries:  1 
Elapsed time 5 seconds
'''

