import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from pylab import mpl
import xlwt
def draw(x,y1,y2,y3,df):
    # plt.xticks(x, x_1,rotation=0)
    fig = plt.figure(figsize=(20, 10))
    ax1 = fig.add_subplot(111)
    df["TF"].plot(ax=ax1, style='bD--', alpha=0.4, label='TF')  # alpha表示点的透明程度
    df["IDF"].plot(ax=ax1, style='go-.', alpha=0.5, label='IDF')
    plt.xlabel('Words')
    ax1.set_yticks(np.arange(0, 10, 0.5))
    ax1.set_ylabel('TF or IDF')
    plt.legend(loc=2)

    ax2 = ax1.twinx()
    df["TF-IDF"].plot(ax=ax2, grid=True, label='TF-IDF', style='y>-.', alpha=0.7)
    ax2.set_yticks(np.arange(0, 0.01, 0.001))
    ax2.set_ylabel('TF-IDF')
    plt.legend(loc=1)
    plt.title('TF,IDF,TF-IDF\'s distribution')
    plt.show()
def writeexcel(x,y1,y2,y3):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('My Worksheet')

    # 写入excel
    # 参数对应 行, 列, 值
    worksheet.write(0, 0, label='Words')
    worksheet.write(0, 1, label='TF')
    worksheet.write(0, 2, label='IDF')
    worksheet.write(0, 3, label='TF-IDF')
    x1=1
    y11=1
    y21=1
    y31=1
    for xl in x:
        worksheet.write(x1, 0, label=xl)
        x1+=1
    for yl1 in y1:
        worksheet.write(y11, 1, label=yl1)
        y11+=1
    for yl2 in y2:
        worksheet.write(y21, 2, label=yl2)
        y21+=1
    for yl3 in y3:
        worksheet.write(y31, 3, label=yl3)
        y31+=1

    # 保存
    workbook.save('TF,IDF,TF-IDF.xls')
if __name__ == '__main__':
    x=[]
    y1=[]
    y2=[]
    y3=[]
    fw=open("最新阶段词频及TFIDF.txt",'r',encoding='utf-8')
    lines=fw.readlines()
    k=1
    for line in lines:
        if k<=200:
            line=line.strip()
            splitline=line.split(",")
            x.append(splitline[0][6:])
            y1.append(float(splitline[2][4:]))
            y2.append(float(splitline[3][5:]))
            y3.append(float(splitline[4][10:]))
        k=k+1
    writeexcel(x,y1,y2,y3)
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
    mpl.rcParams['axes.unicode_minus'] = False
    xls_file = pd.ExcelFile('TF,IDF,TF-IDF.xls')  # 打开工作簿
    table = xls_file.parse('My Worksheet')
    df = table.set_index('Words')
    draw(x,y1,y2,y3,df)