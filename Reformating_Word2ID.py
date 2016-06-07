import os
# sentiment.train

os.system("python 5_GenerateWorDict.py 4.preprocess")
os.system("python 6_TransWord2ID.py 4.preprocess sentiment.train")
os.system("mv 4.preprocess preprocess")

# TF.train
# repeat preprocess

os.system("python 1_Clean.py review.train")
os.system("python 3_WordRestore.py 1.cleaned")
os.system("python 4_StopWords.py 3.restore")
os.system("rm 1.cleaned")
os.system("rm 3.restore")
# Word2ID
os.system("python 6_TransWord2ID.py 4.preprocess TF.train")
os.system("rm 4.preprocess")
