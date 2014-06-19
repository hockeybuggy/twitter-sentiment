#!/usr/bin/env python

# File       : InvertedList.py
# Author     : Douglas Anderson
# Description: Records the words in an inverted list structure

class InvertedList:
    words = []
    posting = []
    docs = []

    def __init__(self):
        pass

    def add(self, token):
        print token.__unicode__()
        if token.tokentype == "word":
            words.add()
        # Add the word to word list
        # Add that to the posting
        # Add the number of times the words occurs in the doc

