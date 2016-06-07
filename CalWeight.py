# coding=gbk
import os
os.system("python 7_IDF.py TF.train 5.wordict")
os.system("python 8_Weight.py TF.train IDF.train")
os.system("rm IDF.train")
os.system("rm TF.train")
