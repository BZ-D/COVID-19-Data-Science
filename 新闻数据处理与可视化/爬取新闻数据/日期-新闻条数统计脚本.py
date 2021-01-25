import os
import re
if __name__ == '__main__':
    f=open('最新一轮疫情.txt','r',encoding='utf-8')
    c=f.readlines()
    list_three = [[0 for i in range(31)] for j in range(12)]
    for line in c:
        if line[0]=='*':
            strmonth=line[10:12]
            strdate=line[13:15]
            print(strmonth+"\n")
            print(strdate + "\n")
            list_three[int(strmonth)-1][int(strdate)-1]+=1
    fp = open('2019.12.8-20206.30每日新闻条数.txt', 'w', encoding='utf-8')
    for i in range(0,12):
        for j in range(0,31):
            fp.write("2020."+str(i+1)+"."+str(j+1)+":"+str(list_three[i][j]))
            fp.write("\n")
