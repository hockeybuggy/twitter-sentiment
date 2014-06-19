#!/usr/bin/env python

# File       : finisher.py
# Author     : Douglas Anderson
# Description: This file cleans up the tokens and outputs strings for each tweet

def __call__(tokens):
    final = {}
    token_buffer = []
    currentlabel = tokens[0].label
    currentid = tokens[0].tweetid

    for t in tokens:
        if t.tweetid == currentid:
            token_buffer.append(t.text)
        else:
            final[currentid] = [create_feature_dict(token_buffer), currentlabel]
            currentid = t.tweetid
            currentlabel = t.label
            token_buffer = [t.text]
    final[currentid] = [create_feature_dict(token_buffer), currentlabel]
    return [final[k] for k in final]
    #return final

def create_feature_dict(token_buffer):
    return dict([(word, True) for word in token_buffer])

