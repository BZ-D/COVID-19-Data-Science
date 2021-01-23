import math

# 评论文件，用于计算IDF
commentpath = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\评论文本\2021年1月评论.txt'
# 逆序词频文件
filepath = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\KeyWords\2021年1月评论关键词.txt'
# 未排序的TF-IDF
dest = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\TF-IDF\2021年1月词频.txt'
# 排序后的TF-IDF
dest_sorted = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\TF-IDF\2021年1月TF-IDF.txt'


def readLines(fileName):
    f = open(fileName, 'r', encoding='utf-8')
    content = f.readlines()
    f.close()

    # 去换行符
    length = len(content)
    for i in range(length):
        content[i] = ''.join(content[i].split())
        content[i] = content[i].replace('\u200b', '')
        content[i] = content[i].replace('\u200d', '')

    return content[:2099]


def tf_idf():
    lines = readLines(filepath)
    freq = 0

    destfile = open(dest, 'w', encoding='utf-8')
    comments = readLines(commentpath)

    # 计算词频总数
    for line in lines:
        aline = line.split(',')
        freq += int(aline[1])

    # 计算每个词的词频TF及IDF
    for line in lines:
        aline = line.split(',')
        TF = int(aline[1]) / freq

        # IDF
        count = 1
        # 文件总数即为当月评论总数
        for comment in comments:
            if aline[0] in comment:
                count += 1

        IDF = math.log(len(comments) / count, 10)

        destfile.write('Term: ' + aline[0] + ',Count: ' + aline[1] + ',TF: ' + str(TF)[0: 10] + ',IDF: '
                       + str(IDF)[0: 10] + ',TF × IDF: ' + str(TF * IDF)[0: 10] + '\n')

    destfile.close()

    # 总共：352689次
    # 1月：63432
    # 2月：89235
    # 3月：55353
    # 4月：52137
    # 5月：42781
    # 12月：20773
    # 2021年1月：28978


def keywords():
    # 排序方法
    lines = readLines(dest)
    dict = {}
    for line in lines:
        key = line[:-10]
        value = line[-10:]
        dict[key] = float(value)

    sorted_words = sorted(dict.items(), key=lambda d: d[1], reverse=True)
    f = open(dest_sorted, 'w', encoding='utf-8')
    for word in sorted_words:
        f.write(word[0] + str(word[1]) + '\n')
    f.close()

if __name__ == '__main__':
    keywords()
