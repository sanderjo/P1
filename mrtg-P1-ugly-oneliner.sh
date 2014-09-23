#!/bin/sh
# Oneliner to get current nett electricity usage resp production (in Watt) and convert into MRTG format

python P1-python-cu.py | awk -F\( '/1-0:[12].7.0/{ print $2 * 1000  } END { print "none\nnone" } '

