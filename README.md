
# Sentiment Analysis in Twitter data

This is the repository for an undergraduate research project that I have done
in the summer of 2014.

## Running it yourself

To acquire your own copy of this implementation follow these instructions. The
following instructions are written for Ubuntu 14.04 GNU/Linux, however it
should be able to run on any Unix-like system.


### 1. Download

The source code is hosted on github.com [here][github-repo]. Download the
source code either via git or a [zip file][zip-file]

    wget https://github.com/hockeybuggy/semantic_eval/archive/master.zip
    unzip master.zip
    cd master

### 2. Install Prerequisites

 If *python 2.7*, *pip*, and *flex* are not installed, they can be installed
easily via a package manger. Then the various required python packages can be
installed with pip:

    sudo apt-get install python2.7 pip flex
    sudo pip install numpy nltk

### 3. Compile Tokenizer

 The tokenizer is written in C for performance reasons and can be compiled with:

    make

### Run the Program

 The classifier can be executed in a number of ways.  There are two python
programs that are executable: 'conductor.py' and 'crossval.py'. These two
programs run the classifier in a simple fashion or with cross validation. There
are a large number of command line arguments that can be viewed with:

    python conductor -h

Since the command line arguments can be cumbersome many of the experiments can
be run via the make file:

    make tiny            # Quick running with only 100 examples
    make crossfolds-m000 # The MaxEnt baseline with cross-validation
    make crossfolds-m111 # MaxEnt with cross-validation & feature selection
    make crossfolds-b000 # The Naive Bayes baseline with cross-validation
    make crossfolds-b111 # Naive Bayes with cross-val & feature selection
    make crossfolds      # Run all of the cross-validation experiments

[github-repo]: https://github.com/hockeybuggy/semantic_evalhere.
[zipfile]: https://github.com/hockeybuggy/semantic_eval/archive/master.zip

