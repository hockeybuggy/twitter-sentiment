#!/usr/bin/env python

# File       : labelselect.py
# Author     : Douglas Anderson
# Description: Selects the label to keep

import re

def __call__(tokens, labels):
    if labels == "pnn":
        return selectPosNeuNeg(tokens)
    elif labels == "pn":
        return selectPosNeg(tokens)

def selectPosNeuNeg(tokens):
    selected_tokens = []
    for t in tokens:
        if t.label == "positive":
            selected_tokens.append(t)
        elif t.label == "neutral":
            selected_tokens.append(t)
        elif t.label == "objective" or t.label == "objective-OR-neutral":
            t.label = "neutral" # Coerce the labels to neutral
            selected_tokens.append(t)
        elif t.label == "negative":
            selected_tokens.append(t)
    return selected_tokens

def selectPosNeg(tokens):
    selected_tokens = []
    for t in tokens:
        if t.label == "positive":
            selected_tokens.append(t)
        elif t.label == "negative":
            selected_tokens.append(t)
    return selected_tokens

