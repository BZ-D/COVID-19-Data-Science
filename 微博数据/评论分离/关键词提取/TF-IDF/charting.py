# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import numpy as np
from matplotlib.font_manager import *

myfont = FontProperties(fname='C:/Windows/Fonts/Deng.ttf')
src = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\KeyWords\2021年1月评论关键词.txt'


def getFrequencies(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()[0: 105] # 每个月的关键词截取到频数40左右
    terms = []
    frequencies = []
    for line in lines:
        terms.append(line.split(',')[0])
        frequencies.append(int(line.split(',')[1][:-1])/28978) # -1是为了去除换行符，int是转成整形，以便图形根据数据变化
    return [terms, frequencies]

def histogram():
    plt.xlabel('Terms')
    plt.ylabel('Frequency of Occurrence')
    # 添加标题
    terms = getFrequencies(src)[0]
    frequencies = getFrequencies(src)[1]
    plt.title('Chart of Frequency Distribution')
    # 添加文字
    plt.bar(terms, frequencies,facecolor='g')
    plt.grid(alpha=0.5, linestyle='-.')
    plt.xticks(terms[::2],rotation=90, fontproperties=myfont)
    plt.show()


if __name__ == "__main__":
    histogram()
