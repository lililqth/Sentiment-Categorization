# coding=gbk
import sys
import math
import nltk
import string
from pattern.en import lemma

def RestoreWords(file):

    """Restore every words in phrases
    Using pattern.en

    Args: 
        The training file whose phrases sentiment are annotated 

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
        f = open("3.restore", "w+")
        for i in range(1, len(lines)+1):
            line = lines[i-1]
            # obtain TF
            label = line.split()[-1]
            words = [word[0 : word.rindex(":")] for word in line.split()[1:-1]]
            nums = [word[word.rindex(":")+1:] for word in line.split()[1:-1]]
            wordict = dict(zip(words, nums)) 

            neWordict = dict()

            def addWord(cleanedWord, word):
                if len(cleanedWord) == 0:
                    return
                if cleanedWord in neWordict.keys():
                    neWordict[cleanedWord] = float(neWordict.get(cleanedWord)) + float(wordict.get(word))
                else:
                    neWordict[cleanedWord] = float(wordict.get(word))

            for word in words:
                subWords = word.split("_")

                neWord = ""
                for subWord in subWords:
                    restoredSubWord = lemma(subWord)
                    neWord = neWord+ "_" + restoredSubWord
                neWord = neWord[1:]
                addWord(neWord, word)

            f.write(str(i) + " ")
            for k,v in neWordict.items():
                f.write(k + ":" + str(v) + " ")
            f.write(label)
            f.write("\n")
    finally:
        if f:
            f.close()

     
if __name__=="__main__":
    RestoreWords(sys.argv[1])
