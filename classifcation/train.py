#!/usr/bin/env python

import nltk

from nltk.featstruct import FeatStruct

train_set_old = [("with j davlar 11th . main rivals are team poland . hopefully we an make it a successful end to a tough week of training tomorrow .", "positive"),
 ("its not that i'm a gsp fan , i just hate nick diaz . can't wait for february .", "negative"),
 ("iranian general says israel's iron dome can't deal with their missiles ( keep talking like that and we may end up finding out )", "negative"),
 ("theo walcott is still shit , watch rafa and johnny deal with him on saturday .", "negative")]

train_set = []
for x, l in train_set_old:
    x_vec = x.split(" ")
    train_dict = dict([(word, True) for word in x_vec])
    print train_dict
    train_set.append((train_dict, l))

for i, v in train_set:
    print i


classifier = nltk.MaxentClassifier.train(train_set)
#print nltk.classify.accuracy(classifier, devtest_set)
