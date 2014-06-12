#!/usr/bin/env python

# File       : statsify.py
# Author     : Douglas Anderson
# Description: Provides stats for every tweets tokens

def __call__(tokens):
    stats = {}
    for t in tokens:
        try:
            stats[t.tweetid]["total"] += 1
        except KeyError:
            stats[t.tweetid] = {"total": 1}
        try:
            stats[t.tweetid][t.tokentype] += 1
        except KeyError:
            stats[t.tweetid][t.tokentype] = 1
    return stats

