# -*- coding: UTF-8 -*-
import re


path = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\2021年1月微博数据（央视新闻）.txt'
txt = open(path, 'r', encoding='utf-8')
line = txt.readline()
newFile = open(r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\评论文本\2021年1月评论.txt', 'w', encoding='utf-8')
comments = []
while line:
    if line != '评论内容：\n':
        line = txt.readline()
        continue
    else:
        line = txt.readline()
        while line != '----------------------------------------------------------\n':
            line = ''.join(line.split())
            comments.append(line[2:])
            line = txt.readline()

validComments = filter(None, comments)

for comment in validComments:
    print(comment)
    newFile.write(comment + '\n')
txt.close()
newFile.close()