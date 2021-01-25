# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pandas import Series
from matplotlib.font_manager import *

myfont = FontProperties(fname='C:/Windows/Fonts/Deng.ttf')
Zan_Pinglun_Src = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\微博点赞评论数提取\2021年1月.txt'
tf_idfSrc = r'C:\Users\Ding\Desktop\COVID-19-Data-Science\微博数据\评论分离\关键词提取\TF-IDF\2020年5月TF-IDF.txt'
attitude_1 = r'C:\Users\Ding\Desktop\COVID-19-Data-Science\微博数据\评论分离\心态分析\各阶段心态词频\2020年1月心态词频.txt'
attitude_2 = r'C:\Users\Ding\Desktop\COVID-19-Data-Science\微博数据\评论分离\心态分析\各阶段心态词频\2020年2月心态词频.txt'
attitude_3 = r'C:\Users\Ding\Desktop\COVID-19-Data-Science\微博数据\评论分离\心态分析\各阶段心态词频\2020年3月心态词频.txt'
attitude_4 = r'C:\Users\Ding\Desktop\COVID-19-Data-Science\微博数据\评论分离\心态分析\各阶段心态词频\2020年4月心态词频.txt'
attitude_5 = r'C:\Users\Ding\Desktop\COVID-19-Data-Science\微博数据\评论分离\心态分析\各阶段心态词频\2020年5月心态词频.txt'
attitude_6 = r'C:\Users\Ding\Desktop\COVID-19-Data-Science\微博数据\评论分离\心态分析\各阶段心态词频\2020年12月及2021年1月心态词频.txt'


def readAttiLines(fileName):
    f = open(fileName, 'r', encoding='utf-8')
    content = f.readlines()
    f.close()

    # 去换行符
    lines = []
    length = len(content)
    for line in content:
        aline = line.split(' ')
        lines.append(aline[0] + ' ' + aline[2][:-1])

    return lines


def getTF_IDF(filename):
    # 根据排序好的TF-IDF文件获取相关数值
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
        freq.append(int(aline[1][6:]))
        tf.append(float(aline[2][3:]))
        idf.append(float(aline[3][4:]))
        tf_idfs.append(float(aline[-1][7:]))
    f.close()
    return [terms, freq, tf, idf, tf_idfs]


def get_Zan_Pinglun(filename):
    # 根据提取好的赞数和评论数文件获取某阶段赞数和评论数
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()[570:670]
    pinglun = []
    zan = []
    for line in lines:
        aline = line.split(' ')
        pinglun.append(int(aline[0][4:]))
        zan.append(int(aline[1][4:-1]))

    f.close()
    return [pinglun, zan]


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


def attitude_overall():
    # 画某一阶段的心态分布图
    f = open(attitude_6, 'r', encoding='utf-8')
    lines = f.readlines()
    length = len(lines)

    attitudes = []
    counts = []
    freqs = []
    count = 0
    for i in range(0, length):
        lines[i] = lines[i][:-1]  # 去换行符

    for line in lines:
        aline = line.split(' ')
        attitudes.append(aline[1])
        counts.append(int(aline[2]))
        count += int(aline[2])

    for line in lines:
        aline = line.split(' ')
        freqs.append(int(aline[2]) / count)

    # 左 Count
    # 右 Frequency
    data1 = Series(counts, index=attitudes)

    x = attitudes  # 横坐标为心态词
    z = freqs  # 一竖坐标为频率

    fig = plt.figure()

    ax = fig.add_subplot(111)
    data1.plot(kind='bar', use_index=True, ax=ax, label='Count')

    ax2 = ax.twinx()
    ax2.plot(x, z, '-r', label='Frequency')

    fig.legend(loc=1, bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = True

    ax.set_xlabel("Attitudes", fontsize=20)
    ax.set_ylabel(r"Count", fontsize=20)
    ax2.set_ylabel(r"Frequency", fontsize=20)

    plt.grid(alpha=0.5, linestyle='-.')
    plt.show()


def negative():
    # 六阶段消极心态分布
    attitude_freq_dict = {0.0: [], 0.05: [], 0.1: [], 0.15: [], 0.2: [], 0.25: [], 0.3: [], 0.35: [], 0.4: [], 0.45: []}

    files = [attitude_1, attitude_2, attitude_3, attitude_4, attitude_5, attitude_6]

    for i in range(0, 6):
        count = 0
        lines = readAttiLines(files[i])[:10]  # 取前十个消极心态

        for line in lines:
            # 算出总频数
            aline = line.split(' ')
            count += int(aline[1])

        for line in lines:
            # 算出每个心态的频数并加到字典里
            aline = line.split(' ')
            attitude_freq_dict[float(aline[0])].append(int(aline[1]) / count)

    index = [1, 2, 3, 4, 5, 6]
    y1 = attitude_freq_dict[0.0]
    y2 = attitude_freq_dict[0.05]
    y3 = attitude_freq_dict[0.1]
    y4 = attitude_freq_dict[0.15]
    y5 = attitude_freq_dict[0.2]
    y6 = attitude_freq_dict[0.25]
    y7 = attitude_freq_dict[0.3]
    y8 = attitude_freq_dict[0.35]
    y9 = attitude_freq_dict[0.4]
    y10 = attitude_freq_dict[0.45]

    plt.plot(index, y1, linewidth = 3)
    plt.plot(index, y2, linewidth = 3)
    plt.plot(index, y3, linewidth = 3)
    plt.plot(index, y4, linewidth = 3)
    plt.plot(index, y5, linewidth = 3)
    plt.plot(index, y6, linewidth = 3)
    plt.plot(index, y7, linewidth = 3)
    plt.plot(index, y8, linewidth = 3)
    plt.plot(index, y9, linewidth = 3)
    plt.plot(index, y10, linewidth = 3)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = True
    plt.legend(['绝望', '愤怒', '恐惧', '嘲讽\n &\n厌恶', '悲伤', '担忧',
                '焦虑', '慌张', '惊讶', '迷茫'], loc=2, bbox_to_anchor=(1.0, 1.0), borderaxespad = 0., fontsize = 20)
    plt.grid(alpha=0.5, linestyle='-.')
    plt.xlabel('Stages', fontsize=20)
    plt.ylabel('Frequency', fontsize=20)
    plt.title('Chart of Negative Attitudes Variation Trend', fontsize = 20)
    plt.show()


def positive():
    # 六阶段积极心态分布
    attitude_freq_dict = {0.55: [], 0.6: [], 0.65: [], 0.7: [], 0.75: [], 0.8: [], 0.85: [], 0.9: [], 0.95: [], 1.0: []}

    files = [attitude_1, attitude_2, attitude_3, attitude_4, attitude_5, attitude_6]

    for i in range(0, 6):
        count = 0
        lines = readAttiLines(files[i])[11:]  # 取后十个积极心态

        for line in lines:
            # 算出总频数
            aline = line.split(' ')
            count += int(aline[1])

        for line in lines:
            # 算出每个心态的频数并加到字典里
            aline = line.split(' ')
            attitude_freq_dict[float(aline[0])].append(int(aline[1]) / count)

    index = [1, 2, 3, 4, 5, 6]
    y1 = attitude_freq_dict[0.55]
    y2 = attitude_freq_dict[0.6]
    y3 = attitude_freq_dict[0.65]
    y4 = attitude_freq_dict[0.7]
    y5 = attitude_freq_dict[0.75]
    y6 = attitude_freq_dict[0.8]
    y7 = attitude_freq_dict[0.85]
    y8 = attitude_freq_dict[0.9]
    y9 = attitude_freq_dict[0.95]
    y10 = attitude_freq_dict[1.0]

    plt.plot(index, y1, linewidth=3)
    plt.plot(index, y2, linewidth=3)
    plt.plot(index, y3, linewidth=3)
    plt.plot(index, y4, linewidth=3)
    plt.plot(index, y5, linewidth=3)
    plt.plot(index, y6, linewidth=3)
    plt.plot(index, y7, linewidth=3)
    plt.plot(index, y8, linewidth=3)
    plt.plot(index, y9, linewidth=3)
    plt.plot(index, y10, linewidth=3)

    plt.title('Chart of Positive Attitudes Variation Trend', fontsize = 20)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = True
    plt.legend(['积极', '鼓励', '祝愿', '敬佩', '感激', '乐观',
                '期待', '渴望', '喜悦', '热爱'], loc=2, bbox_to_anchor=(1.0, 1.0), borderaxespad=0., fontsize=20)
    plt.grid(alpha=0.5, linestyle='-.')
    plt.xlabel('Stages', fontsize=20)
    plt.ylabel('Frequency', fontsize=20)
    plt.show()


def zan_pinglun_chart():
    # 用于画出各阶段的赞数和评论数分布图
    terms = [i for i in range(1, 101)]
    pinglun = get_Zan_Pinglun(Zan_Pinglun_Src)[0]
    zan = get_Zan_Pinglun(Zan_Pinglun_Src)[1]
    data1 = Series(pinglun, index=terms)

    x = terms  # 横坐标为词
    z = zan  # 一竖坐标为TF-IDF

    fig = plt.figure()

    ax = fig.add_subplot(111)
    data1.plot(kind='bar', use_index=True, ax=ax, label='评论数')

    ax2 = ax.twinx()
    ax2.plot(x, z, '-r', label='点赞数', color='r')

    fig.legend(loc=1, bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = True

    ax.set_xlabel("")
    ax.set_ylabel(r"评论数", fontsize=20)
    ax2.set_ylabel(r"点赞数", fontsize=20)

    plt.grid(alpha=0.5, linestyle='-.')
    plt.show()


if __name__ == "__main__":
    positive()
