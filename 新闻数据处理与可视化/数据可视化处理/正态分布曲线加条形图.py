import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 # 正态分布的概率密度函数
 #   x      数据集中的某一具体测量值
 #   mu     数据集的平均值，反映测量值分布的集中趋势
 #   sigma  数据集的标准差，反映测量值分布的分散程度
def normfun(x, mu, sigma):
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf
if __name__ == '__main__':
    data = pd.read_csv('DayN.csv') # 载入数据文件
    DayN = data['DayN'] # 获得长度数据集
    mean = DayN.mean() # 获得数据集的平均值
    std = DayN.std()   # 获得数据集的标准差
    print(mean)
    print(std*std)
 # 设定X轴：前两个数字是X轴的起止范围，第三个数字表示步长
 # 步长设定得越小，画出来的正态分布曲线越平滑
    x = np.arange(1, 183, 0.1)
 # 设定Y轴，载入刚才定义的正态分布函数
    y = normfun(x, mean, std)
 # 绘制数据集的正态分布曲线
    plt.plot(x, y)
 # 绘制数据集的直方图
    plt.hist(length,color='red', bins=183, rwidth=0.7, density=True)
    plt.title('DayN distribution')
    plt.xlabel('Day N')
    plt.ylabel('Probability')
 # 输出正态分布曲线和直方图
    plt.show()