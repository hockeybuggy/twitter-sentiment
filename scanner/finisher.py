#!/usr/bin/env python

# File       : finisher.py
# Author     : Douglas Anderson
# Description: This file cleans up the tokens and outputs strings for each tweet

def __call__(tokens):
    final = {}
    token_buffer = []
    currentid = tokens[0].tweetid

    for t in tokens:
        if t.tweetid == currentid:
            token_buffer.append(t.text)
        else:
            final[currentid] = collapse_tokens(token_buffer)
            currentid = t.tweetid
            token_buffer = [t.text]
    final[currentid] = collapse_tokens(token_buffer)
    return final

def collapse_tokens(token_buffer):
    return " ".join(token_buffer)
