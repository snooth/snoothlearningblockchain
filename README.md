# USAGE
- Clone to local directory
- Run the run_blockchain.py file 
	## ./run_blockchain.py
- It will prompt you for senders address, receipents address and amount.
- If you want to change the difficulty:
	- Open run_blockchain.py
	- change "difficulty" level to the number of '0's you want to try and solve. 
	# vim run_blockchain.py
	# difficulty = '00' # this is set to default

# snoothlearningblockchain
# python blockchain script that I wrote to help me learn/understand the concept of blockchain
#!/usr/bin/env python

# VERY simple demo of BlockChain + Proof of Work concept using sha256 hashing
# This is NOT Bitcoin's PoW algorithm, this is a very simple test that I built to help me learn/understand the blockchain concepts
# SnoothDogg Sept 2018 - 

import string
import random
import hashlib
import time
import re
import os
import nonce_gen
import getPrevHash

sender = raw_input("What is the sender's privatekey?  \n")
receiver = raw_input("What is the receipient's wallet address?  \n")
amount = raw_input("How much do you want to send?   \n")
getHash = getPrevHash.getPHash()
nonce = nonce_gen.generate_nonce()

challenge = getHash + nonce
#challenge = str(sender)+str(receiver)+str(nonce)
#challenge = '9K3hdiHGEEFSdfewefdf3Fdfh354Gf3df2efg22wegy434tfaseEwfF'
difficulty = '00'

## this function generations a random string of characters to create a #hash (256Bit number or 32octects)
def gen_String(challenge=challenge,size=32):
	answer = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(size))
	attempt = challenge+answer
	return attempt, answer

## creates a hash object
shaHash = hashlib.sha256()

## nonce generator, this will generate a 32 digit random number each time a challenge is created
def generate_nonce(length=32):
    return ''.join([str(random.randint(0, 9)) for i in range(length)])

## add the next winning block to the blockchain
def appendLedger(index, timestamp, pHash, nHash, senderAddress, receiverAddress, coinValue):
	file = open("ledger.txt", "a")
	datetime = time.ctime(int(timestamp))
	appendBlock = "\nIndex:" + str(index) + "\nTimeStamp:" + str(datetime) + "\nTransaction:" + str(senderAddress) + " --> " + str(receiverAddress) + "\n" + "TransactionValue:" + str(coinValue) + "\n" + "PreviousHash:" + pHash + "NewHash:" + nHash +  "\n"
	file.write(appendBlock)

## reward the miner with 12 SnoothDogg Coin
def rewardMiner(minedCoin):
	file = open("miner.txt", "w")
	minerAddress = " "
	rewardCoin = "MinerAddress:" + minerAddress + "SnoothCoins: " + str(minedCoin) + "\n"
	file.write(rewardCoin)

## get last index value
def lastBlockIndex():
	## check to see if there is an existing ledger, if not then create the genesis block
	filename = "ledger.txt"
    	if os.path.isfile(filename):
    		pass
	else:
		genTime = time.time()
        	dateTime = time.ctime(int(genTime))
        	file = open('ledger.txt', 'w+')
        	genesisBlock = "** GENESIS_BLOCK **\n" + "Index: 0" + "\nTimeStamp: " + str(dateTime) + "\nTransaction: " + "\nTransactionValue: " + "\nPreviousHash: " + "\nNewHash:\n"
        	file.write(genesisBlock)
        	file.close()

	## search for the last index value in ledger.txt
	myvars = {}
        with open("ledger.txt") as myfile:
                for line in myfile:
                        name, var = line.partition(":")[::2]
                        myvars[name.strip()] = str(var)
	lastIndex = myvars["Index"]

	return lastIndex

## gets the previous hash to append the next block
def getPrevHash():
	myvars = {}
        with open("ledger.txt") as myfile:
                for line in myfile:
                        name, var = line.partition(":")[::2]
                        myvars[name.strip()] = str(var)
        lastHash = myvars["NewHash"]

        return lastHash

## this function calls the gen_string() function, creates a sha256 hash and tries to find the answer with a has starting with x number of '0'
def runBlockChainPoW(sender, receiver, amount):
	found = False
	earnedCoin = 0
	startTime = time.time()
	lastIndex = int(lastBlockIndex()) + int(1)
	previousHash = getPrevHash()
	index, transaction = "0",""
	noOfAttempts = 0
	while found == False:
		noOfAttempts = noOfAttempts + 1
		attempt, answer = gen_String()
		shaHash.update(attempt)
		newHashBlock = shaHash.hexdigest()
		#print 'Trying: ', newHashBlock
		if newHashBlock.startswith(difficulty):
			timeTook = time.time() - startTime
			earnedCoin = 12
			rewardMiner(earnedCoin)
			appendLedger(lastIndex, startTime, previousHash, newHashBlock, sender, receiver, amount)
			print '\nNumber of attempts: ', noOfAttempts
			print '\nThe challenge is: ', challenge
			print '\nThe correct hash is: ', newHashBlock
			print 'Time taken to find correct hash: ', timeTook
			print 'Number of SnoothDogg Coins allocated: ', earnedCoin
			found = True

	print 'The correct answer to the challenge: ', answer, '\n'

## init call
runBlockChainPoW(sender, receiver, amount)

