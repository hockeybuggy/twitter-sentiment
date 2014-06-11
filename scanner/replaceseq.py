#!/usr/bin/env python

# File       : replaceseq.py
# Author     : Douglas Anderson
# Description: Replaces sequances with word equivlents

import re

def __call__(tokens):
    replace_ellipsis(tokens)
    replace_emoticons(tokens)
    replace_users(tokens)
    replace_hashtags(tokens)
    replace_urls(tokens)
    return tokens

def replace_users(tokens):
    for t in tokens:
        if t.tokentype == "user":
                t.text = "@USER"

def replace_urls(tokens):
    for t in tokens:
        if t.tokentype == "url ":
            t.text = "@URL"


def replace_hashtags(tokens):
    for t in tokens:
        if t.tokentype == "hash":
            t.text = "#OCTOTHORPE"

def replace_ellipsis(tokens):
    for t in tokens:
        if t.tokentype == "punc":
            if t.text == ".." or t.text == "...":
                t.text = "ELLIPSIS"

def replace_emoticons(tokens):
    happy      = re.compile(":-?\)+|:-?D+|B-?\)+|8-?\)+|:-?p+")
    sad        = re.compile(":-?\(+|8-?\(+|:'\(+")
    wink       = re.compile(";-?\)|;-?D|;-?p")
    love       = re.compile("<+3+")

    for t in tokens:
        if t.tokentype == "emot":
            if happy.match(t.text):
                t.text = "EM_HAPPY"
            elif sad.match(t.text):
                t.text = "EM_SAD"
            elif wink.match(t.text):
                t.text = "EM_WINK"
            elif surprise.match(t.text):
                t.text = "EM_SURPRISE"
            elif love.match(t.text):
                t.text = "EM_LOVE"

