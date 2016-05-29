# coding=gbk
import sys
import math
import nltk
import string
from pattern.en import lemma
from pattern.en import sentiment
from string import maketrans

def RestoreWords(file):
    """ annotation the sentiment of the word

    The sentiment of a word is calculated by:
    sentiment * nums

    Args: 
        The cleaned training file

    Return:
        None
    """
    try:
        f = open(file, "r")
        lines = f.readlines()
    finally:
        if f:
            f.close()
    try:
        f = open("2.sentiment", "w+")
        for i in range(1, len(lines)+1):
            line = lines[i-1]
            label = line.split()[-1]
            words = [word[0 : word.rindex(":")] for word in line.split()[1:-1]]
            nums = [word[word.rindex(":")+1:] for word in line.split()[1:-1]]
            wordict = dict(zip(words, nums)) 

            for word in words:
                transTab = maketrans("_", " ")
                phrase = word.translate(transTab, "")
                senti = float(sentiment(phrase)[0])*float(wordict.get(word))
                wordict[word] = senti * float(wordict.get(word))

            f.write(str(i) + " ")
            for k,v in wordict.items():
                f.write(k + ":" + str(v) + " ")
            f.write(label)
            f.write("\n")
    finally:
        if f:
            f.close()

     
if __name__=="__main__":
    # review.train -> review.train.stopWords
    RestoreWords(sys.argv[1])

