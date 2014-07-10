#!/usr/bin/env python

# File       : labelselect.py
# Author     : Douglas Anderson
# Description: Selects the label

import re

def __call__(tokens):
    return selectPosNegNeu(tokens)

def selectPosNegNeu(tokens):
    selected_tokens = []
    for t in tokens:
        if t.label == "positive":
            selected_tokens.append(t)
        elif t.label == "negative":
            selected_tokens.append(t)
        elif t.label == "neutral":
            selected_tokens.append(t)
    return selected_tokens

