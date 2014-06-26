#!/usr/bin/env python

# File       : wordselection.py
# Author     : Douglas Anderson
# Description: This file removes unnecessary tokens


def __call__(input_list):
    output_list = remove_stopwords(input_list)
    return output_list


def remove_stopwords(input_list):
    output_list = []
    stopwords = set()
    stopword_file = open("../data/english.stop", "r")
    for line in stopword_file:
        stopwords.add(line.strip())
    stopword_file.close()

    for pair in input_list:
        stopword_free_dict = {}
        for k in pair[0].keys():
            if k not in stopwords:
                stopword_free_dict[k] = pair[0][k]
        output_list.append([stopword_free_dict, pair[1]])
    return output_list
