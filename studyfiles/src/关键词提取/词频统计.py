# -*- coding: UTF-8 -*-
import jieba
from collections import Counter
import json

srcFile = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\评论文本\1月评论.txt'
stpWord = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\cn_stopwords（更新版）.txt'
newWord = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\new_words.txt'
destFile = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\KeyWords\2020年1月评论关键词.txt'
cities = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\provinces&cities.txt'


# 读取文件，返回文件的行字符串列表
def readFile(fileName):
    f = open(fileName, 'r', encoding='utf-8')
    content = f.readlines()
    f.close()

    # 去换行符
    length = len(content)
    for i in range(length):
        content[i] = ''.join(content[i].split())
        content[i] = content[i].replace('\u200b', '')
        content[i] = content[i].replace('\u200d', '')

    return content


# 剔除停用词
def delete_stopwords(lines):
    stopwords = readFile(stpWord)
    allWords = []

    jieba.load_userdict(newWord)

    for line in lines:
        allWords += [word for word in jieba.cut(line) if word not in stopwords]

    dict_words = dict(Counter(allWords))
    return dict_words


# main
if __name__ == '__main__':
    lines = readFile(srcFile)
    validWords = delete_stopwords(lines)
    sorted_words = sorted(validWords.items(), key=lambda d: d[1], reverse=True)

    f = open(destFile, 'w', encoding='utf-8')
    for word in sorted_words:
        f.write(word[0] + "," + str(word[1]) + '\n')

    f.close()