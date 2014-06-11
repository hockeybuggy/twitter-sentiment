#!/usr/bin/env python

import os, sys
import csv
import subprocess
import tempfile

scanner_path = "./scanner"

def scan_text(intext):
    tmp_f = os.tmpfile()
    tmp_f.write(intext)
    tmp_f.seek(0)
    subprocess.call([scanner_path], stdin=tmp_f)
    #subprocess.call(["cat"], stdin=tmp_f)
    tmp_f.close()


count = 0
start = 2
end = 3
with open("../data/b.tsv") as f:
    r = csv.DictReader(f, delimiter="\t")
    for tweet in r:
        if count >= start and count < end:
            print
            print tweet["text"]
            scan_text(tweet["text"])
        count += 1


#tweet = "This is the message. It needs to be tokenized #foreal"
#scan_text(tweet)

