# coding=gbk
import os
os.system("python 1_Clean.py review.train")
os.system("python 2_Sentiment.py 1.cleaned")
os.system("python 3_WordRestore.py 2.sentiment")
os.system("python 4_StopWords.py 3.restore")
os.system("rm 1.cleaned")
os.system("rm 2.sentiment")
os.system("rm 3.restore")
