# coding=gbk
import math
import string
import sys

def Weight(TF, IDF):
    try:
        f = open(TF, "r")
        TFs = f.readlines()
        f = open(IDF, "r")
        IDFDict = f.readlines()

        output = open("Weight.train", "w+")
        for i in range(len(TFs)):
            line = TFs[i]
            label = line.split()[0]
            words = [word[: word.rindex(":")] for word in line.split()[1:]]
            TF = [word[word.rindex(":")+1:] for word in line.split()[1:]]
            tfSum = 0.0
            for num in TF:
                tfSum = tfSum + float(num)
            weightDict = dict(zip(words, TF))

            for (k,v) in weightDict.items():
                idf = IDFDict[int(k)-1]
                weight = float(v)/tfSum*float(idf)
                weightDict[k] = weight
                
            output.write(label+" ")
            for (k,v) in weightDict.items():
                output.write(str(k)+":"+str(v)+" ")
            output.write("\n")

    finally:
        if f:
            f.close()
        if output:
            output.close()


if __name__=="__main__":
    # 创建 IDF 字典
    IDFDict = Weight(sys.argv[1], sys.argv[2])
