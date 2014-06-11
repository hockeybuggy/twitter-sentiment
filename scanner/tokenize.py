#!/usr/bin/env python

import os, sys
import csv
import subprocess
import argparse

scanner_path = "./scanner"

def parse_args():
    parser = argparse.ArgumentParser(description="Scan a tweet to determin it's tokens")
    parser.add_argument("--file", type=str, help="The file name containing the text to be scanned")
    parser.add_argument("start", type=int, help="The lower limit of the line number")
    parser.add_argument("end", type=int, help="The upper limit of the line number")
    return parser.parse_args()

def scan_text(intext):
    tmp_f = os.tmpfile()
    tmp_f.write(intext)
    tmp_f.seek(0)
    subprocess.call([scanner_path], stdin=tmp_f)
    #subprocess.call(["cat"], stdin=tmp_f)
    tmp_f.close()


def open_tweets_file(filename, start, end):
    count = 0
    with open("../data/b.tsv") as f:
        r = csv.DictReader(f, delimiter="\t")
        for tweet in r:
            if count >= start and count < end:
                print
                print tweet["text"]
                scan_text(tweet["text"])
            count += 1


if __name__ == "__main__":
    args = parse_args()
    open_tweets_file("../data/b.tsv", args.start, args.end)

