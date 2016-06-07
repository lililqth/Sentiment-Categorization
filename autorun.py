# coding:utf-8
import os
print "添加label"
os.system("python AddLabel.py review.unlabeled")

print "预处理"
os.system("python 1_Clean.py review.train")
os.system("python 3_WordRestore.py 1.cleaned")
os.system("python 4_StopWords.py 3.restore")

print "生成字典"
os.system("python 5_GenerateWorDict.py 4.preprocess")

print "Word 映射到 ID"
os.system("python 6_TransWord2ID.py 4.preprocess TF.train")

os.system("rm 1.cleaned")
os.system("rm 3.restore")
os.system("rm 4.preprocess")


print  "生成 Weight.train"
os.system("python 7_IDF.py TF.train 5.wordict")
os.system("python 8_Weight.py TF.train IDF.train")
os.system("rm IDF.train")
os.system("rm TF.train")
os.system("rm review.train")
