#!/usr/bin/env python3

'''
read info from your smar meter's P1

'''

import sys
import os
import serial # pyserial


p1_output = """
/ISK5\2M550E-1013

1-3:0.2.8(50)
0-0:1.0.0(240914115100S)
0-0:96.1.1(4530303533303037383337313538323231)
1-0:1.8.1(001842.492*kWh)
1-0:1.8.2(001548.736*kWh)
1-0:2.8.1(000860.613*kWh)
1-0:2.8.2(001798.134*kWh)
0-0:96.14.0(0001)
1-0:1.7.0(00.000*kW)
1-0:2.7.0(00.075*kW)
0-0:96.7.21(00008)
0-0:96.7.9(00003)
1-0:99.97.0(1)(0-0:96.7.19)(210316100736W)(0000000476*s)
1-0:32.32.0(00005)
1-0:32.36.0(00001)
0-0:96.13.0()
1-0:32.7.0(236.6*V)
1-0:31.7.0(001*A)
1-0:21.7.0(00.000*kW)
1-0:22.7.0(00.072*kW)
0-1:24.1.0(003)
0-1:96.1.0(4730303634303032303133343136383230)
0-1:24.2.1(240914115006S)(01259.019*m3)
!1365
/ISK5\2M550E-1013

1-3:0.2.8(50)
0-0:1.0.0(240914115101S)
0-0:96.1.1(4530303533303037383337313538323231)
1-0:1.8.1(001842.492*kWh)
1-0:1.8.2(001548.736*kWh)
1-0:2.8.1(000860.613*kWh)
1-0:2.8.2(001798.134*kWh)
0-0:96.14.0(0001)
1-0:1.7.0(00.000*kW)
1-0:2.7.0(00.075*kW)
0-0:96.7.21(00008)
0-0:96.7.9(00003)
1-0:99.97.0(1)(0-0:96.7.19)(210316100736W)(0000000476*s)
1-0:32.32.0(00005)
1-0:32.36.0(00001)
0-0:96.13.0()
1-0:32.7.0(236.8*V)
1-0:31.7.0(001*A)
1-0:21.7.0(00.000*kW)
1-0:22.7.0(00.068*kW)
0-1:24.1.0(003)
0-1:96.1.0(4730303634303032303133343136383230)
0-1:24.2.1(240914115006S)(01259.019*m3)
!E3F4
/ISK5\2M550E-1013

1-3:0.2.8(50)
0-0:1.0.0(240914115102S)
0-0:96.1.1(4530303533303037383337313538323231)
1-0:1.8.1(001842.492*kWh)
1-0:1.8.2(001548.736*kWh)
1-0:2.8.1(000860.613*kWh)
1-0:2.8.2(001798.134*kWh)
0-0:96.14.0(0001)
1-0:1.7.0(00.000*kW)
1-0:2.7.0(00.083*kW)
0-0:96.7.21(00008)
0-0:96.7.9(00003)
1-0:99.97.0(1)(0-0:96.7.19)(210316100736W)(0000000476*s)
1-0:32.32.0(00005)
1-0:32.36.0(00001)
0-0:96.13.0()
1-0:32.7.0(236.6*V)
1-0:31.7.0(001*A)
1-0:21.7.0(00.000*kW)
1-0:22.7.0(00.077*kW)
0-1:24.1.0(003)
0-1:96.1.0(4730303634303032303133343136383230)
0-1:24.2.1(240914115006S)(01259.019*m3)
!BB9A
/ISK5\2M550E-1013

1-3:0.2.8(50)
0-0:1.0.0(240914115103S)
0-0:96.1.1(4530303533303037383337313538323231)
1-0:1.8.1(001842.492*kWh)
1-0:1.8.2(001548.736*kWh)
1-0:2.8.1(000860.613*kWh)
1-0:2.8.2(001798.134*kWh)
0-0:96.14.0(0001)
1-0:1.7.0(00.000*kW)
1-0:2.7.0(00.079*kW)
0-0:96.7.21(00008)
0-0:96.7.9(00003)
1-0:99.97.0(1)(0-0:96.7.19)(210316100736W)(0000000476*s)
1-0:32.32.0(00005)
1-0:32.36.0(00001)
0-0:96.13.0()
1-0:32.7.0(236.7*V)
1-0:31.7.0(001*A)
1-0:21.7.0(00.000*kW)
"""

'''
1-0:1.8.1(00185.000*kWh) (Totaal verbruik tarief 1 (nacht))
1-0:1.8.2(00084.000*kWh) (Totaal verbruik tarief 2 (dag))
1-0:2.8.1(00013.000*kWh) (Totaal geleverd tarief 1 (nacht))
1-0:2.8.2(00019.000*kWh) (Totaal geleverd tarief 2 (dag))
0-0:96.14.0(0001) (Actuele tarief (1))
1-0:1.7.0(0000.98*kW) (huidig verbruik)
1-0:2.7.0(0000.00*kW) (huidige teruglevering)
'''

def read_info_from_P1(device):
	P1_output = ""
	error = False
	try:
		ser = serial.Serial(device, 115200)
		# OK, got a connection
		# now read 60 lines
		for _ in range(60):
			myline = ser.readline()
			try:
				myline = myline.decode("ascii").strip()
				#print(myline)
				P1_output += f"{myline}\n"

			except:
				pass
	except:
		P1_output += f"errrrrrrrrrrrorrrrrrrrrrrrrr: could not read from {device}"
		error = True
	return P1_output, error

def parse_P1_info(p1_output):
	info = dict()

	for line in p1_output.split('\n'):
		if not line.startswith('!') and not line.startswith('/'):
			try:
				splitline = line.replace('(',' ').replace(')',' ').split()
				id = splitline[0]
				try:
					value, unity = splitline[-1].split('*')
					info[id] = [value, unity]
				except:
					# no '*', so just a value, no unity
					value = splitline[-1]
					info[id] = [value, None]
			except:
				pass
	return info

### MAIN ####

if __name__ == "__main__":

	if len(sys. argv)>1:
		# really read from P1
		device = sys.argv[1]
		if not os.path.exists('/dev/ttyUSB0'):
			print(f"Devide {device} does not exist")
			sys.exit(-1)
		if not os.access(device, os.R_OK):
			print(f"Device {device} does exist, but is not readable. Use 'sudo chmod 666 {device}' ")
			sys.exit(-1)
		print(f"Reading from device {device}")
		p1_output, error = read_info_from_P1(device)
		if error:
			print(f"error reading from P1 {device}")
			sys.exit(-1)
	else:
		print("No device specified, so using dummy P1 info")
	info = parse_P1_info(p1_output)

	# kWh info:
	'''
	1-0:1.8.1(00185.000*kWh) (Totaal verbruik tarief 1 (nacht))
	1-0:1.8.2(00084.000*kWh) (Totaal verbruik tarief 2 (dag))
	1-0:2.8.1(00013.000*kWh) (Totaal geleverd tarief 1 (nacht))
	1-0:2.8.2(00019.000*kWh) (Totaal geleverd tarief 2 (dag))
	'''
	totaal_kWh = float(info['1-0:1.8.1'][0]) + float(info['1-0:1.8.2'][0]) - float(info['1-0:2.8.1'][0]) - float(info['1-0:2.8.2'][0])
	print(f"totaal_kWh verbruik [kWh] {totaal_kWh:.2f}")

	# current usage in Watt
	'''
	1-0:1.7.0(0000.98*kW) (huidig verbruik)
	1-0:2.7.0(0000.00*kW) (huidige teruglevering)
	'''
	netto_momentaan_verbruik = 1000 * (float(info['1-0:1.7.0'][0]) - float(info['1-0:2.7.0'][0]))
	print(f"netto verbruik [W] {netto_momentaan_verbruik:.0f}")

	# spanning
	spanning = float(info['1-0:32.7.0'][0])
	print(f"spanning [V] {spanning}")


