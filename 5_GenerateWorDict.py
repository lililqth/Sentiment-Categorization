# coding=gbk
import string

def words2Num(file):
    try:
        f = open(file, "r")
        lines = f.readlines()
    finally:
        if f:
            f.close()
    # 创建set
    wordSet = set()
    for line in lines:
        words = [word[0 : word.rindex(":")] for word in line.split()[1:-1]]
        wordSet |= set(words)

    # 创建字典
    numList = range(1, len(wordSet)+1)
    wordict = dict(zip(list(wordSet), numList))

    # 排序后写入到文件
    output = sorted(wordict.items(),key=lambda aa:aa[1])
    try:
        f = open('5.wordict','w+')
        for i in range(0,len(output)):
            f.write(output[i][0] + " " + str(output[i][1]) + "\n")
    finally:
        if f:
            f.close()
    return wordict, wordSet

     
if __name__=="__main__":
    wordict,wordSet = words2Num("4.preprocess")
