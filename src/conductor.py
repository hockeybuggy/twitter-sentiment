#!/usr/bin/env python

# File       : conductor.py
# Author     : Douglas Anderson
# Description: Driver for my parser implementation

import os, sys
import argparse
import math

import tokenize
import normalize
import labelselect
import statsify
import wordselection
import dictizer
from Token import Token
from train import multi_label_classifier, multi_label_naive_bayes_classifier, binary_classifier

def parse_args():
    parser = argparse.ArgumentParser(description="Scan a tweet to determine it's tokens")
    parser.add_argument("--file", type=str, help="The file name containing the text to be scanned")
    parser.add_argument("items", type=int, help="The number of items to use")
    parser.add_argument("--classifier_type", default="max_ent", help="Select classifer should be: max_ent, naive_bayes")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    print "Opening dataset..."
    tokens = tokenize.open_tweets_file("../data/b.tsv", 0, args.items)
    #stats  = statsify.__call__(tokens) # Count each category of token

    print "Selecting labels..."
    tokens = labelselect.__call__(tokens) # Select only the labels

    print "Normalizing dataset..."
    tokens = normalize.__call__(tokens) # Normalize the tokens

    #for k in stats:
        #print k, ": ", stats[k]

    #for token in tokens:
        #print token.__unicode__()

    print "Transforming dataset..."
    feature_list = dictizer.__call__(tokens)

    num_docs = len(feature_list)
    print "Number of documents:", num_docs
    num_pos = len([x for x in feature_list if x[1] == "positive"])
    print "% positive :", num_pos / float(num_docs)
    num_neu = len([x for x in feature_list if x[1] == "neutral"])
    print "% neutral  :", num_neu / float(num_docs)
    num_neg = len([x for x in feature_list if x[1] == "negative"])
    print "% negative :", num_neg / float(num_docs)

    print "Selecting features from the dataset..."
    feature_list = wordselection.__call__(feature_list)

    #for row in feature_list:
        #print row

    split_point = int(math.ceil(len(feature_list) * 0.8))
    #print split_point
    train_set = feature_list[:split_point]
    test_set = feature_list[split_point:]

    #for i in train_set:
        #print i

    if args.classifier_type == "max_ent":
        classifier = multi_label_classifier(train_set)
    else:
        classifier = multi_label_naive_bayes_classifier(train_set)

    #classifier.show_informitive_features()
    print "\nTesting"
    classifier.test(test_set)
    #classifier.inspect_errors(test_set)

    #classifier = binary_classifier(train_set)
    #classifier.test(test_set)

