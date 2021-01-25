import os
import time
import random
import jieba  #处理中文
import sklearn
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from numpy import *
import pylab as pl
import matplotlib.pyplot as plt
def makestopworddai(filename):
    wordsdai = set()
    with open(filename, 'r',encoding='utf-8') as fp:
        for line in fp.readlines():
            word = line.strip()
            if len(word)>0 and word not in wordsdai: # 去重
                wordsdai.add(word)
    return wordsdai


def trainAndtesthuafen(folderpath, test_size):
    folderlist = os.listdir(folderpath)
    datalist = []
    classlist = []
    for folder in folderlist:
        newfolderpath = os.path.join(folderpath, folder)
        files = os.listdir(newfolderpath)
        j = 1
        for file in files:
            #if j > 100:  # 怕内存爆掉，只取100个样本文件，你可以注释掉取完
            #    break
            with open(os.path.join(newfolderpath, file), 'r',encoding='utf-8') as fp:
                raw = fp.read()
            ## 是的，随处可见的jieba中文分词
            wordcut = jieba.cut(raw, cut_all=False)  # 精确模式，返回的结构是一个可迭代的genertor
            wordlist = list(wordcut)  # genertor转化为list，每个词unicode格式

            datalist.append(wordlist)  # 训练集list
            classlist.append(folder)  # 类别
            j += 1

    ## 粗暴地划分训练集和测试集
    dataclasslist =list(zip(datalist, classlist))
    random.shuffle(dataclasslist)
    index = int(len(dataclasslist) * test_size) + 1
    trainlist = dataclasslist[index:]
    testlist = dataclasslist[:index]
    traindata, trainclass = zip(*trainlist)
    testdata, testclass = zip(*testlist)

    # 其实可以用sklearn自带的部分做
    # train_data_list, test_data_list, train_class_list, test_class_list = sklearn.cross_validation.train_test_split(data_list, class_list, test_size=test_size)

    # 统计词频放入all_words_dict
    wordsdict = {}
    for wordlist in traindata:
        for word in wordlist:
            if wordsdict.__contains__(word):
                wordsdict[word] += 1
            else:
                wordsdict[word] = 1

    # key函数利用词频进行降序排序
    allwordstuplelist = sorted(wordsdict.items(), key=lambda f: f[1], reverse=True)  # 内建函数sorted参数需为list
    alldata = list(zip(*allwordstuplelist))[0]

    return alldata, traindata, testdata, trainclass, testclass


def words_dict(all_words_list, deleteN, stopwords_set):
    # 选取特征词
    feature_words = []
    n = 1
    for t in range(deleteN, len(all_words_list), 1):
        if n > 2000:  # feature_words的维度1000
            break

        if not all_words_list[t].isdigit() and all_words_list[t] not in stopwords_set and 1 < len(all_words_list[t]) < 5:
            feature_words.append(all_words_list[t])
            n += 1
    return feature_words






'''通过方差的百分比来计算将数据降到多少维是比较合适的，
函数传入的参数是特征值和百分比percentage，返回需要降到的维度数num'''
def eigValPct(eigVals,percentage):
    sortArray=sort(eigVals) #使用numpy中的sort()对特征值按照从小到大排序
    sortArray=sortArray[-1::-1] #特征值从大到小排序
    arraySum=sum(sortArray) #数据全部的方差arraySum
    tempSum=0
    num=0
    for i in sortArray:
        tempSum+=i
        num+=1
        if tempSum>=arraySum*percentage:
            return num




'''pca函数有两个参数，其中dataMat是已经转换成矩阵matrix形式的数据集，列表示特征；
其中的percentage表示取前多少个特征需要达到的方差占比，默认为0.9'''
def pca(dataMat,percentage=0.9):
    meanVals=mean(dataMat,axis=0)  #对每一列求平均值，因为协方差的计算中需要减去均值
    meanRemoved=dataMat-meanVals
    covMat=cov(meanRemoved,rowvar=0)  #cov()计算方差
    eigVals,eigVects=linalg.eig(mat(covMat))  #利用numpy中寻找特征值和特征向量的模块linalg中的eig()方法
    k=eigValPct(eigVals,percentage) #要达到方差的百分比percentage，需要前k个向量
    eigValInd=argsort(eigVals)  #对特征值eigVals从小到大排序
    eigValInd=eigValInd[:-(k+1):-1] #从排好序的特征值，从后往前取k个，这样就实现了特征值的从大到小排列
    redEigVects=eigVects[:,eigValInd]   #返回排序后特征值对应的特征向量redEigVects（主成分）
    lowDDataMat=meanRemoved*redEigVects #将原始数据投影到主成分上得到新的低维数据lowDDataMat
    reconMat=(lowDDataMat*redEigVects.T)+meanVals   #得到重构数据reconMat
    return lowDDataMat,reconMat





# 文本特征
def text_features(train_data_list, test_data_list, feature_words, flag='nltk'):
    def text_features(text, feature_words):
        text_words = set(text)
        if flag == 'nltk':
            ## nltk特征 dict
            features = {word:1 if word in text_words else 0 for word in feature_words}
        elif flag == 'sklearn':
            ## sklearn特征 list
            features = [1 if word in text_words else 0 for word in feature_words]
        else:
            features = []
        return features
    train_feature_list = [text_features(text, feature_words) for text in train_data_list]
    test_feature_list = [text_features(text, feature_words) for text in test_data_list]
    return train_feature_list, test_feature_list
# 分类，同时输出准确率等
def text_classifier(train_feature_list, test_feature_list, train_class_list, test_class_list, flag='nltk'):
    if flag == 'nltk':
        ## 使用nltk分类器
        train_flist = zip(train_feature_list, train_class_list)
        test_flist = zip(test_feature_list, test_class_list)
        classifier = nltk.classify.NaiveBayesClassifier.train(train_flist)
        test_accuracy = nltk.classify.accuracy(classifier, test_flist)
    elif flag == 'sklearn':
        ## sklearn分类器
        #classifier = GaussianNB().fit(train_feature_list, train_class_list)
        classifier = MultinomialNB().fit(train_feature_list, train_class_list)
        test_accuracy = classifier.score(test_feature_list, test_class_list)
    else:
        test_accuracy = []
    return test_accuracy
if __name__ == '__main__':
    print("start")

    ## 文本预处理
    folder_path = './Database/Class'
    alldata, traindata, testdata, trainclass, testclass = trainAndtesthuafen(folder_path,test_size=0.2)

    # 生成stopwords_set
    stopwords_file = './cn_stopwords.txt'
    stopwords_set = makestopworddai(stopwords_file)

    ## 文本特征提取和分类
    # flag = 'nltk'
    flag = 'sklearn'
    deleteNs = range(0, 2000, 20)
    test_accuracy_list = []
    for deleteN in deleteNs:
        # feature_words = words_dict(all_words_list, deleteN)
        feature_words = words_dict(alldata, deleteN, stopwords_set)
        train_feature_list, test_feature_list = text_features(traindata, testdata, feature_words, flag)
        test_accuracy =text_classifier(train_feature_list, test_feature_list, trainclass, testclass, flag)
        test_accuracy_list.append(test_accuracy)
        #feature_words = words_dict(alldata, deleteN, stopwords_set)
        #train_feature_list, test_feature_list = text_features(traindata, testdata, feature_words, flag)
        #train_feature_listAfterpca, afterplace1 = pca(train_feature_list)
        #test_feature_listAfterpca, afterplace2 = pca(test_feature_list)
        #train_feature_listAfterpca = np.asarray(train_feature_listAfterpca).astype(float)
        #test_feature_listAfterpca = np.asarray(test_feature_listAfterpca).astype(float)
        #test_accuracy = text_classifier(train_feature_listAfterpca, test_feature_listAfterpca, trainclass, testclass,flag)
        test_accuracy_list.append(test_accuracy)
    print(test_accuracy_list)

    # 结果评价
    # plt.figure()
    plt.plot(deleteNs, test_accuracy_list)
    plt.title('Relationship of deleteNs and test_accuracy')
    plt.xlabel('deleteNs')
    plt.ylabel('test_accuracy')
    plt.show()
    plt.savefig('result.png')

    print("finished")