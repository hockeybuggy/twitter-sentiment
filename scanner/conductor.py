#!/usr/bin/env python

# File       : conductor.py
# Author     : Douglas Anderson
# Description: Driver for my parser implementation

import os, sys
import argparse

import tokenize
import normalize
import statsify
from Token import Token

def parse_args():
    parser = argparse.ArgumentParser(description="Scan a tweet to determin it's tokens")
    parser.add_argument("--file", type=str, help="The file name containing the text to be scanned")
    parser.add_argument("start", type=int, help="The lower limit of the line number")
    parser.add_argument("end", type=int, nargs="?", help="The upper limit of the line number")
    args = parser.parse_args()
    if args.end == None:
        args.end = args.start + 1
    return args

if __name__ == "__main__":
    args = parse_args()
    tokens = tokenize.open_tweets_file("../data/b.tsv", args.start, args.end)
    tokens = normalize.__call__(tokens)
    stats  = statsify.__call__(tokens)

    for k in stats:
        print k, ": ", stats[k]
    #for token in tokens:
        #print token.__unicode__()

