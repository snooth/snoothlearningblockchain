#!/usr/bin/env python

import re
import time
import os

yesorno = ""

def checkFile():
        ## check to see if there is an existing ledger, if not then create the genesis block
	yesorno = ''
	file = 'ledger.txt'
    	if os.path.isfile(file):
		pass
    	else:
		yesorno = "no"
		genTime = time.time()
                dateTime = time.ctime(int(genTime))
                file = open('ledger.txt', 'w+')
                genesisBlock = "** GENESIS_BLOCK **\n" + "Index: 0" + "\nTimeStamp: " + str(dateTime) + "\nTransaction: " + "\nTransactionValue: " + "\nPreviousHash: " + "\nNewHash:\n"
                file.write(genesisBlock)
                file.close()
	

