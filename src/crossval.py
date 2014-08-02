#!/usr/bin/env python

# File       : crossval.py
# Author     : Douglas Anderson
# Description: Cross validation driver for sentiment analysis implementation

import os, sys
import numpy
from itertools import permutations

import tokenize
import normalize
import labelselect
import statsify
import wordselection
import dictizer
import split_dataset
from Token import Token
from parse_args import parse_args
from train import maxent_classifier
from train import maxent_classifier_with_validation
from train import naive_bayes_classifier


def main(args):
    print "Opening dataset..."
    tokens = tokenize.open_tweets_file("../data/b.tsv", 0, args.items)

    print "Selecting labels..."
    tokens = labelselect.__call__(tokens, args.labels) # Select only the labels

    print "Normalizing dataset..."
    #tokens = normalize.__call__(tokens) # Normalize the tokens
    if args.normalize and args.normalize_words:
        normalize.normalize_words(tokens)
    if args.normalize and args.normalize_punct:
        normalize.normalize_punct(tokens)
    if args.normalize and args.normalize_emoticons:
        normalize.normalize_emoticons(tokens)
    if args.normalize and args.normalize_users:
        normalize.normalize_users(tokens)
    if args.normalize and args.normalize_hashtags:
        normalize.normalize_hashtags(tokens)
    if args.normalize and args.normalize_nums:
        normalize.normalize_nums(tokens)
    if args.normalize and args.normalize_urls:
        normalize.normalize_urls(tokens)

    print "Transforming dataset..."
    feature_list = dictizer.__call__(tokens)

    docfreq = wordselection.calculate_docfreq(feature_list)

    if args.stopword_removal:
        print "Removing stopwords from the dataset..."
        feature_list = wordselection.remove_stopwords(feature_list)

    if args.uncommon_selection:
        print "Removing uncommon words from the dataset..."
        feature_list = wordselection.remove_uncommon(feature_list, docfreq, args.df_cutoff)

    wordselection.print_reatined_features(docfreq, args.df_cutoff)

    # Write the features out to a file
    with open("filtered_docs.txt", "w") as w:
        for row in feature_list:
            w.write(str(row[0]) + "\n")

    print "Generating feature set statistics..."
    statsify.__call__(feature_list, args.labels)

    print "Splitting the dataset..."
    partitions = split_dataset.partition(feature_list, args.num_folds)

    #print len(partitions), "Partitions"
    #for p in partitions:
        #print
        #for t in p:
            #print t
    #return

    accumulation_dict = {}
    if args.classifier_type == "max_ent":
        validation = True
    else:
        validation = False

    for i, fold in enumerate(generate_folds(partitions, validation)):
        print "Fold number: {} looks like: {}".format(i, "".join(fold))
        #print fold
        print "Training fold", i
        train_set = select_set("t", fold, partitions)
        validation_set = select_set("v", fold, partitions)
        test_set = select_set("T", fold, partitions)
        if args.classifier_type == "max_ent":
            classifier = maxent_classifier_with_validation(train_set, validation_set,
                    args.validation_metric, 3)
        else:
            train_set += validation_set
            classifier = naive_bayes_classifier(train_set)
        print "Testing fold {}...".format(i),
        results_dict = classifier.test(test_set, args.labels, trace=False)
        #Add results to the accumulation dict
        for key in results_dict.keys():
         try:
             accumulation_dict[key].append(results_dict[key])
         except KeyError:
             accumulation_dict[key] = [results_dict[key]]
        print "done.\n"
        #classifier.show_informative_features(30)
        #classifier.inspect_errors(test_set)

    print "\n\nAccumulating Results"
    for key in sorted(accumulation_dict.keys(), reverse=True):
        print key, ":\t", accumulation_dict[key]
        print "{}-avg:\t".format(key), numpy.mean(accumulation_dict[key])
        print "{}-std:\t".format(key), numpy.std(accumulation_dict[key])


def select_set(set_type, fold, partitions):
    output_set = []
    for i,x in enumerate(fold):
        if x == set_type:
            output_set += partitions[i]
    return output_set


def generate_folds(partitions, validation):
    num_folds = len(partitions)
    if validation:
        if num_folds == 5:
            sets = "tttvT"
        elif num_folds == 10:
            sets = "ttttttttvT"
    else:
        if num_folds == 5:
            sets = "ttttT"
        elif num_folds == 10:
            sets = "tttttttttT"
    available = {}
    #range(len(partitions))
    for order in permutations(sets, num_folds):
        try:
            available["".join(order)]
        except KeyError:
            available["".join(order)] = True
            yield order

if __name__ == "__main__":
    args = parse_args()
    main(args)

