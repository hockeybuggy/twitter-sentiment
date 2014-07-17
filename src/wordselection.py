#!/usr/bin/env python

# File       : wordselection.py
# Author     : Douglas Anderson
# Description: This file removes unnecessary tokens


def __call__(input_list):
    interm_list = remove_stopwords(input_list)
    output_list = remove_uncommon(interm_list, 1)
    return output_list
    #return interm_list


def remove_stopwords(input_list):
    output_list = []
    # Read the stop words into a set
    stopwords = set()
    #stopword_file = open("../data/stopwords.txt", "r")
    stopword_file = open("../data/stopwords.short.txt", "r")
    for line in stopword_file:
        stopwords.add(line.strip())
    stopword_file.close()

    # Remove stopwords from the dicts
    for pair in input_list:
        stopword_free_dict = {}
        for k in pair[0].keys():
            if k not in stopwords:
                stopword_free_dict[k] = pair[0][k]
        output_list.append([stopword_free_dict, pair[1]])
    return output_list

def remove_uncommon(input_list, count=1):
    output_list = []
    word_docfreq = {}

    # Count document frequency for each word
    for pair in input_list:
        for k in pair[0].keys():
            if k not in word_docfreq:
                word_docfreq[k] = 1
            else:
                word_docfreq[k] += 1

    # Print all the features in order
    with open("features.txt", "w") as w:
        for feature in sorted(word_docfreq, key=word_docfreq.get, reverse=True):
            w.write(feature + "\t" + str(word_docfreq[feature]) + "\n")

    # Count number of features
    num_features = 0
    for word in word_docfreq:
        if word_docfreq[word] > count:
            num_features += 1
    print "Total retained features:", num_features

    # Keep only the common words
    for pair in input_list:
        uncommon_free_dict = {}
        for k in pair[0].keys():
            if word_docfreq[k] > count:
                uncommon_free_dict[k] = pair[0][k]
        output_list.append([uncommon_free_dict, pair[1]])

    return output_list

