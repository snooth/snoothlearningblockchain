#!/usr/bin/env python3

import re
import os

def getPHash():
    myvars = {}
    with open("ledger.txt") as myfile:
        for line in myfile:
            name, var = line.partition(":")[::2]
            myvars[name.strip()] = str(var)
    newHash = myvars["NewHash"]
    return newHash

#print(myvars["NewHash"])
#newHash = myvars["NewHash"]
#return newHashyy


