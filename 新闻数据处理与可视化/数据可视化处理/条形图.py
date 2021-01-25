import matplotlib.pyplot as plt
from matplotlib import font_manager
#C:\Users\jiyun\Desktop\数据科学大作业疫情下的情绪分析\实战冲冲冲
# 关键词：标题:
def paint(x,y,title):
    plt.figure(figsize=(20, 10), dpi=80)
    # 这两行代码解决 plt 中文显示的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.grid(True)
    plt.bar(x,y)
    #plt.xticks(x[::5],color='black',rotation=60)
    plt.xticks(color='black', rotation=90)
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.show()
if __name__ == '__main__':
    fw=open('最新阶段词频.txt', 'r', encoding='utf-8')
    x=[]
    y=[]
    lines=fw.readlines()
    i=1
    for line in lines:
        if i<110:
            listline=line.split('     ')
            x.append(listline[0])
            y.append(int(listline[1]))
        i+=1
    paint(x,y,"最新阶段词频条形图（已排序）")

