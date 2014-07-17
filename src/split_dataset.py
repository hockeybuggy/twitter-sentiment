#!/usr/bin/env python

# File       : split_dataset.py
# Author     : Douglas Anderson
# Description: Divides the dataset into sections

import math
import random

def __call__(feature_list, test_size, validation_size=0.0):
    train_set = []
    test_set = []
    validation_set = []
    random.seed()
    while len(test_set) < int(math.ceil((len(feature_list) * test_size))):
        x = random.randint(0, len(feature_list)-1)
        test_set.append(feature_list[x])
        del feature_list[x]
    #TODO validation set
    train_set = feature_list
    return train_set, test_set

