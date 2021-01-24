# -*- coding: UTF-8 -*-

def getcomments():
    path = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\综合内容\2021年1月微博数据（人民日报）.txt'
    txt = open(path, 'r', encoding='utf-8')
    line = txt.readline()
    newFile = open(r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\评论文本\2020年12月及2021年1月评论.txt', 'a', encoding='utf-8')
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

def getotherInfos():
    # 统计点赞数和评论数
    path = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\综合内容\2021年1月微博数据（央视新闻）.txt'
    txt = open(path, 'r', encoding='utf-8')
    line = txt.readline()
    newFile = open(r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\微博点赞评论数提取\2021年1月.txt', 'a', encoding='utf-8')

    while line:
        if '转发数：' not in line:
            line = txt.readline()
            continue
        else:
            line = txt.readline()
            count = 0
            while line != '评论内容：\n':
                if count == 1:
                    newFile.write(line[:-1] + '\n')
                else:
                    newFile.write(line[:-1] + ' ')
                count += 1
                line = txt.readline()

    txt.close()
    newFile.close()

if __name__ == '__main__':
    getcomments()