#!/usr/bin/env python

import csv
from ScannerWrapper import ScannerWrapper

#count = 0
#limit = 2
#with open("../data/b.tsv") as f:
    #r = csv.reader(f, delimiter="\t")
    #for tweet in r:
        #if count < limit:
            #count += 1
            #print tweet[3]


sw = ScannerWrapper("This is a test")
print sw.get_token()

#for i in range(5):
    #print sw.get_token()
