
# File       : Token.py
# Author     : Douglas Anderson
# Description: Driver for my parser implementation

class Token:
    tweetid, label, tokentype, text, original = None, None, None, None, None
    def __init__(self, tweetid, label, tokentype, text):
        self.tokentype = tokentype
        self.text = text
        self.tweetid = tweetid
        self.label = label
        self.original = str(text)
    def __unicode__(self):
        return "\t".join([self.tweetid, self.label, self.tokentype, self.text])

