# AWK program to parse P1 output ("Slimme Meter")

function getfloat(line)
{
	# we search for the numeric value between round brackets:
	# (02015.641*kWh)
	# (0000.45*kW)
	# (01463.190)
	#match($0, /\([0-9]+\.[0-9]+/ )
	match($0, /\(.*[\*)]/ )		# Anything starting with '(' ... up to  '*' or ')'
	value= substr($0, RSTART+1, RLENGTH-2) +1 -1	# the +1-1 are needed to convert to a number (removing leading 0's)
	return value
}

/1-0:1.8.1/ { print "Electra: Totaal verbruik tarief 1 (nacht) KWh: " getfloat($0) }
/1-0:1.8.2/ { print "Electra: Totaal verbruik tarief 2 (dag) KWh: "   getfloat($0) }
/1-0:2.8.1/ { print "Electra: Totaal geleverd tarief 1 (nacht) KWh: " getfloat($0) }
/1-0:2.8.2/ { print "Electra: Totaal geleverd tarief 2 (dag) KWh: "   getfloat($0) }

/1-0:1.7.0/ { print "Electra: Huidig verbruik [W]: "             1000*getfloat($0) }
/1-0:2.7.0/ { print "Electra: Huidige teruglevering [W]: "       1000*getfloat($0) }

/^\(/       { print "Gas: Totaal verbruik gas in m3: "                getfloat($0) }
