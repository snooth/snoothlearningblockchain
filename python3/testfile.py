#!/usr/bin/env python

import re
import os.path
import os

ledgerFile = open("ledger.txt", "r")

for line in ledgerFile:
	if re.match("Index",line):
		print line,



myvars = {}
with open("ledger.txt") as myfile:
    for line in myfile:
        name, var = line.partition(":")[::2]
        myvars[name.strip()] = str(var)

print(myvars["PreviousHash"])
#print(myvars["Index"])

def mk_prjDir():
	prjDir = "ledger.txt"
    	print "Checking to see if", prjDir, "exists.."
    	if os.path.isfile(prjDir):
        	print (prjDir, "exists!")
    	else:
        	print (prjDir, "does not exist!")

mk_prjDir()


