P1
==

Tools to read information from your Dutch Smart Meter's ("slimme meter") P1 port.

Before even using the script on your Linux system, make sure "cu" is installed and "cu -l /dev/ttyUSB0 -s 9600 --parity=none" is working.

The python script will run the cu command until correct output is received from P1 (with a maximum of 100 tries).



Example output:

        /KMP5 KA6U001783948383
        
        0-0:96.1.1(204B413655303031373539343937393133)
        1-0:1.8.1(00965.580*kWh)
        1-0:1.8.2(00820.367*kWh)
        1-0:2.8.1(00195.543*kWh)
        1-0:2.8.2(00503.351*kWh)
        0-0:96.14.0(0002)
        1-0:1.7.0(0000.34*kW)
        1-0:2.7.0(0000.00*kW)
        0-0:17.0.0(999*A)
        0-0:96.3.10(1)
        0-0:96.13.1()
        0-0:96.13.0()
        0-1:24.1.0(3)
        0-1:96.1.0(4730303135353631323030393331373133)
        0-1:24.3.0(140916210000)(08)(60)(1)(0-1:24.2.1)(m3)
        (00540.726)
        0-1:24.4.0(1)
        !
        tries:  27 
        Elapsed time 9 seconds

