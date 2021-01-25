import os
import time
import random
import jieba  #处理中文
import sklearn
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
filename = "最新一轮疫情.txt"
stopwords_file = "cn_stopwords.txt"

stop_f = open(stopwords_file,"r",encoding='utf-8')
stop_words = list()
for line in stop_f.readlines():
    line = line.strip()
    if not len(line):
        continue
    stop_words.append(line)
stop_f.close
print(len(stop_words))
f = open(filename,"r",encoding='utf-8')
result = list()
for line in f.readlines():
    line = line.strip()
    if not len(line):
        continue
    outstr = ''
    seg_list = jieba.cut(line,cut_all=False)
    for word in seg_list:
        if word not in stop_words:
            if word != '\t':
                outstr += word
                outstr += " "
    result.append(outstr.strip())
f.close
with open("最新阶段分词.txt","w",encoding='utf-8') as fw:
    for sentence in result:
        sentence.encode('utf-8')
        data=sentence.strip()
        if len(data)!=0:
            fw.write(data)
            fw.write("\n")