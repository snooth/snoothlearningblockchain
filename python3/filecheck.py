#!/usr/bin/env python3

import re
import time
import os
import os.path

yesorno = ""

def checkFile():
    ## check to see if there is an existing ledger, if not then create the genesis block
    yesorno = ''
    file = 'ledger.txt'
    if os.path.isfile(file):
        pass
        #print("file there")
    else:
        yesorno = "no"
        #print("file not there")
        genTime = time.time()
        dateTime = time.ctime(int(genTime))
        file = open('ledger.txt', 'w+')
        genesisBlock = "** GENESIS_BLOCK **\n" + "Index: 0" + "\nTimeStamp: " + str(dateTime) + "\nTransaction: " + "\nTransactionValue: " + "\nPreviousHash: " + "\nNewHash:\n"
        file.write(genesisBlock)
        file.close()

#checkFile()
