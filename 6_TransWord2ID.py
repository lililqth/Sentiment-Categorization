# coding=gbk
import string
import sys

def Word2ID(inputFileName, outputFileName, dictFileName):

        inputFile = open(inputFileName, "r") 
        inputLines = inputFile.readlines()
        inputFile.close()

        dictFile = open(dictFileName, "r")
        dictLines = dictFile.readlines()
        dic = dict()
            
        for line in dictLines:
            words = line.split()
            dic[words[0]] = words[1]
        dictFile.close()

        TFDict = list()
        f= open(outputFileName, "w+")
        for line in inputLines:
            label = line.split()[-1]
            f.write(label[label.rfind("#")+2:] + " ")
            terms= line.split()[1:-1]
            words = [dic.get(word[: word.rindex(":")]) for word in terms]
            tfs = [word[word.rindex(":")+1 :] for word in terms]
            TFDict.append(dict(zip(words, tfs)))
            for i in range(len(words)):
                f.write(str(words[i]) + ":" + str(tfs[i])+ " ")
            f.write("\n")
        f.close()
     
if __name__=="__main__":
    Word2ID(sys.argv[1], sys.argv[2], "5.wordict")
