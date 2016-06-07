# coding=gbk
import math
import string
import sys


def IDF(trainingList, wordSetDict):
    try:
        f = open(wordSetDict, "r")
        wordSet = f.readlines()
        IDFDict = [0.0]*(len(wordSet)+1)
        f = open(trainingList, "r")
        lines = f.readlines()
        for line in lines:
            words = [word[: word.rindex(":")] for word in line.split()[1:]]
            # How many articles contains the word
            for word in words:
                IDFDict[int(word)] = IDFDict[int(word)] + 1
    finally:
        if f:
            f.close();
    # 写入文件
    try:
        f = open("IDF.train", "w+")
        sum = len(lines)
        for i in IDFDict:
            f.write(str(math.log(float(sum)/(i+1))) + "\n")
    finally:
        if f:
            f.close()
    return IDFDict 
     
if __name__=="__main__":
    # 创建 IDF 字典
    IDFDict = IDF(sys.argv[1], sys.argv[2])
