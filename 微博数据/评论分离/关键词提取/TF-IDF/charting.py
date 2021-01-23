# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pandas import Series
from matplotlib.font_manager import *

myfont = FontProperties(fname='C:/Windows/Fonts/Deng.ttf')
tf_idfSrc = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\TF-IDF\2021年1月TF-IDF.txt'


def getTF_IDF(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()[:101]
    terms = []
    freq = []
    tf = []
    idf = []
    tf_idfs = []
    for line in lines:
        aline = line.split(',')
        terms.append(aline[0][5:])
        freq.append(int(aline[1][5:]))
        tf.append(float(aline[2][3:]))
        idf.append(float(aline[3][4:]))
        tf_idfs.append(float(aline[-1][7:]))
    return [terms, freq, tf, idf, tf_idfs]


def doubleY():
    # 左Term count
    # 右TF-IDF
    terms = getTF_IDF(tf_idfSrc)[0]
    frequencies = getTF_IDF(tf_idfSrc)[1]
    tf_idfs = getTF_IDF(tf_idfSrc)[4]
    data1 = Series(frequencies, index=terms)

    x = terms  # 横坐标为词
    z = tf_idfs  # 一竖坐标为TF-IDF

    fig = plt.figure()

    ax = fig.add_subplot(111)
    data1.plot(kind='bar', use_index=True, ax=ax, label='Term Count')

    ax2 = ax.twinx()
    ax2.plot(x, z, '-r', label='TF-IDF')

    fig.legend(loc=1, bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = True

    ax.set_xlabel("Terms")
    ax.set_ylabel(r"Term Count")
    ax2.set_ylabel(r"TF-IDF")

    plt.grid(alpha=0.5, linestyle='-.')
    plt.show()


def tf_idf_chart():
    # 用于画出词汇的tf(left) & idf(right)分布图
    terms = getTF_IDF(tf_idfSrc)[0]
    tfs = getTF_IDF(tf_idfSrc)[2]
    idfs = getTF_IDF(tf_idfSrc)[3]
    data1 = Series(tfs, index=terms)

    x = terms  # 横坐标为词
    z = idfs  # 一竖坐标为TF-IDF

    fig = plt.figure()

    ax = fig.add_subplot(111)
    data1.plot(kind='bar', use_index=True, ax=ax, label='TF')

    ax2 = ax.twinx()
    ax2.plot(x, z, '-r', label='IDF', color='r')

    fig.legend(loc=1, bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = True

    ax.set_xlabel("Terms")
    ax.set_ylabel(r"TF")
    ax2.set_ylabel(r"IDF")

    plt.grid(alpha=0.5, linestyle='-.')
    plt.show()


def attitude():
    return


if __name__ == "__main__":
    doubleY()
    tf_idf_chart()
