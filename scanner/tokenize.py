#!/usr/bin/env python

import csv
import subprocess

scanner_path = "scanner"

#count = 0
#limit = 2
#with open("../data/b.tsv") as f:
    #r = csv.reader(f, delimiter="\t")
    #for tweet in r:
        #if count < limit:
            #count += 1
            #print tweet[3]

tweet = "This is the message. It needs to be tokenized #foreal"

subprocess.call([scanner_path], stdin=tweet)
