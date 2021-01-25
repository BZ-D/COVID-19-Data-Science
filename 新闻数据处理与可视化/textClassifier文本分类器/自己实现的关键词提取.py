import math
import os
commentpath = r'C:\Users\jiyun\Desktop\数据科学大作业疫情下的情绪分析\新闻分词及词频处理\Database\最新一轮疫情.txt'
filepath = r'C:\Users\jiyun\Desktop\数据科学大作业疫情下的情绪分析\新闻分词及词频处理\各阶段词频\最新阶段词频.txt'
dest = r'C:\Users\jiyun\Desktop\数据科学大作业疫情下的情绪分析\新闻分词及词频处理\TF-IDF\最新阶段词频及TFIDF.txt'
def readLines(fileName):
    f = open(fileName, 'r', encoding='utf-8')
    content = f.readlines()
    f.close()
    # 去换行符
    length = len(content)
    for i in range(length):
        content[i] = content[i].replace('\n', '')
        content[i] = content[i].replace('\u200b', '')
        content[i] = content[i].replace('\u200d', '')
    return content
def tf_idf():
    lines = readLines(filepath)
    freq = 0

    destfile = open(dest, 'w', encoding='utf-8')
    comments = readLines(commentpath)
    # 计算词频总数
    for line in lines:
        aline = line.split('     ')
        freq += int(aline[1])
    # 计算每个词的词频TF及IDF
    TFIDFdict={}
    for line in lines:
        aline = line.split('     ')
        TF = int(aline[1]) / freq
        # IDF
        count = 1
        # 文件总数即为当月评论总数
        for comment in comments:
            if aline[0] in comment:
                count += 1
        IDF = math.log(len(comments) / count, 10)
        TFIDFdict['Term: ' + aline[0] + ',Freq: ' + aline[1] + ',TF: ' + str(TF) + ',IDF: '
                       + str(IDF) + ',TF × IDF: ']=TF * IDF
    dictlist=TFIDFdict.items()
    dictlist=sorted(dictlist, key = lambda kv:kv[1],reverse=True)
    for x,num in dictlist:
        destfile.write(x+str(num)+'\n')
    destfile.close()
if __name__ == '__main__':
    tf_idf()