#!/usr/bin/env python

# File       : tokenize.py
# Author     : Douglas Anderson
# Description: Driver for my parser implementation

import os, sys
import csv
import subprocess

from Token import Token

scanner_path = "./scanner"

def scan_text(tweetid, label, intext):
    tokens = []
    tmp_f = os.tmpfile()
    tmp_f.write(intext)
    tmp_f.seek(0)
    output = subprocess.check_output([scanner_path], stdin=tmp_f)
    #subprocess.call(["cat"], stdin=tmp_f)
    tmp_f.close()
    outlines = output.split("\n")
    for line in outlines:
        try:
            tokentype, text = line.split("\t")
            tokens.append(Token(tweetid, label, tokentype, text))
        except ValueError:
            pass
    return tokens


def create_tweetid(sid, uid):
    return sid + "-" + uid

def open_tweets_file(filename, start, end):
    count = 0
    tokens = []
    with open(filename) as f:
        r = csv.DictReader(f, delimiter="\t")
        for tweet in r:
            if count >= start and count < end:
                #print
                #print tweet["text"]
                newtokens = scan_text(create_tweetid(tweet["sid"], tweet["uid"]), tweet["class"], tweet["text"])
                tokens += newtokens
            count += 1
    return tokens

