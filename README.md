P1
==

Tools to read information from your Dutch Smart Meter's ("slimme meter") P1 port. The script uses some standards from the Dutch Smart Meter Requirements (DSMR) P1 standard.





Example output:


        sander@nanopineo2:~/git/P1$ ./p1-reading.py 
        No device specified, so using dummy P1 info
        totaal_kWh verbruik [kWh] 732.48
        netto verbruik [W] -79
        spanning [V] 236.7



        sander@nanopineo2:~/git/P1$ ./p1-reading.py /dev/ttyUSB0 
        Reading from device /dev/ttyUSB0
        totaal_kWh verbruik [kWh] 735.04
        netto verbruik [W] 229
        spanning [V] 230.9

        


