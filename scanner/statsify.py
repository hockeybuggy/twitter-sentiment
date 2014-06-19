#!/usr/bin/env python

# File       : statsify.py
# Author     : Douglas Anderson
# Description: Provides stats for every tweets tokens

from InvertedList import InvertedList

def __call__(tokens):
    stats = {}
    il = InvertedList()
    for t in tokens:
        il.add(t)
        try:
            stats[t.tweetid]["total"] += 1
        except KeyError:
            stats[t.tweetid] = {"total": 1}
        try:
            stats[t.tweetid][t.tokentype] += 1
        except KeyError:
            stats[t.tweetid][t.tokentype] = 1
    return stats

