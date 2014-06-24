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

def binarize_labels(data_set, selected_label):
    new_data_set = []
    for k in data_set:
        if k[1] == selected_label:
            new_data_set.append([k[0], "true"])
        else:
            new_data_set.append([k[0], "false"])
    return new_data_set

