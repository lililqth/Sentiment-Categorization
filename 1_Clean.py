# coding=gbk
import sys
import math
import nltk
import string
from string import maketrans

def cleanWord(word):
    """Removing all symbols, digits and spaces in a word
    Args: 
        The word 
    Returns: 
        word after cleaning
    """
    delset = string.punctuation.replace("'", "") + string.digits
    # replace dots with space
    transTab = maketrans(delset, " "*len(delset))
    output = word.translate(transTab, "").strip()
    # replace space with "_"
    output = " ".join(output.split())
    transTab = maketrans(" ", "_")
    output = output.translate(transTab, "")
    return output

def removingStopWords(file):
    """Removing stop words, digits and gots
        
       Args:
        file: The training file

    Returns:
        None
    """

    try:
        f = open(file, "r")
        lines = f.readlines()
        degreeLevelFile = open("dic/DegreeLevel.txt", "r")
        degreeLevelSet = [word[:-1] for word in degreeLevelFile.readlines()]
    finally:
        if degreeLevelFile:
            degreeLevelFile.close()
        if f:
            f.close()
    try:
        f = open("1.cleaned", "w+")
        stopWords = nltk.corpus.stopwords.words('english')
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
                    neWordict[cleanedWord] = int(neWordict.get(cleanedWord)) + int(wordict.get(word))
                else:
                    neWordict[cleanedWord] = int(wordict.get(word))

            for word in words:
                cleanedWord = cleanWord(word) 
                if cleanedWord.decode("gbk") not in stopWords:
                    addWord(cleanedWord, word)

            f.write(str(i) + " ")
            for k,v in neWordict.items():
                f.write(k + ":" + str(v) + " ")
            f.write(label)
            f.write("\n")
    finally:
        if f:
            f.close()

     
if __name__=="__main__":
    removingStopWords(sys.argv[1])

