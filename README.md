# DATA-SCIENCE-PROJECT: COVID-19-ATTITUDE-ANALYSIS

## 项目名称

### 基于新闻及微博评论大数据分析的疫情下中国大众网络社会心态的剖析

## 一、任务清单

| 任务名称                                                     | 完成情况 |
| :----------------------------------------------------------- | :------: |
| basic1、爬取数据：自己爬取数据，官方新闻3w条左右，微博评论12w条左右 |    √     |
| basic2、数据解析：数据分词，列词频，解析                     |    √     |
| basic3、关键词提取：利用TF-IDF原理计算TF和IDF，自己实现关键词提取 |    √     |
| basic4、心态分析：列出21种疫情下的心态并建立心态词典对关键词进行心态分析 |    √     |
| basic5、可视化：对新闻与评论数据与反映的心态进行可视化处理，得出图表 |    √     |
| basic6、拟合：对新闻条数-疫情开始第N天进行卡方拟合分布，拟合高斯分布 |    √     |
| bonus1、数据分析扩张：增加额外阶段，即2020年12月中旬到2021年1月中旬的疫情反扑阶段 |    √     |
| bonus2、机器学习：利用机器学习的方法建立一个文本分类器       |    √     |
| ①先验为多项式分布的朴素贝叶斯，公式如下：                    |    √     |
| ![](./README.assets/QQ截图20210125115910.png)                |          |
| ②根据五个阶段文本特征对各阶段新闻文本进行归类，采用朴素贝叶斯的原理以及PCA降维 |    √     |
| bonus3、汇报：提交汇报申请和完成汇报PPT                      |    √     |

## 二、工作流程：

### 说明：疫情主要分为五个阶段，即

#### 2019.12.8-2020.1.22新闻，不重视与无奈扩散阶段

#### 2020.1.23-2020.2.7新闻，资源缺乏阶段

#### 2020.2.8-2020.3.9新闻，严格统一管控和物资配给

#### 2020.3.10-2020.6.30新闻，有序复工阶段

#### 2020年12月中旬-2021年1月中旬疫情反扑阶段（本次作业中我们额外分析的阶段）

##### 由于有序复工阶段在大众评论方面有两个阶段划分，第四阶段前期评论聚焦于国内复工，后期评论偏向于关注国外疫情，因此评论处理是针对六个（将第四阶段分为两部分）阶段处理，新闻处理仍对原来五个阶段处理。

#### 评论处理：

综合文本 → 评论分离（生成评论纯文本） → jieba分词（去停用词） → 词频统计（生成词语+频数） → TF-IDF（生成未排序的TF-IDF） → TF-IDF（生成排序后的TF-IDF） → 心态分析（生成心态值+心态词+频数） → 作图Charting（生成五种图：左词汇Count右TF-IDF条形折线图，左TF右IDF条形折线图，左总心态Count右Frequency条形折线图，积极心态六阶段折线图，消极心态六阶段折线图）
#### 新闻处理：

爬取官方新闻数据（人民日报，荔枝网，新华网） → jieba分词→词频统计（生成词语+频数） → TF-IDF（生成未排序的TF-IDF） → TF-IDF（生成排序后的TF-IDF） → 机器学习：生成文本分类器（对各个阶段关键词特征提取，传入新闻文本即可检测属于五个阶段中哪个阶段） → 可视化处理，做出图表（五个阶段词云图，新闻数-疫情持续天数高斯分布拟合图，整体阶段新闻数目条形图，五个阶段TF,IDF,TF-IDF折线图）

## 三、项目目录结构

```python
由于新闻和评论反映的信息不同，新闻更具官方性和客观性，评论更具情绪性
大作业主要分为两个部分，即疫情期间各阶段新闻和评论的处理，文件目录主要也分为这两个部分
├─.idea
│  └─inspectionProfiles
├─figures                           #评论数据关键词提取及心态分析可视化图
│  ├─TF-IDF及词数分布图
│  ├─TF及IDF分布图
│  ├─各阶段关键词表
│  ├─各阶段心态分布图
│  ├─积极&消极心态在各阶段的分布
│  └─评论点赞分布图
├─studyfiles                        #前期爬虫学习实践程序及微博爬取相关代码
│  ├─.idea
│  │  └─inspectionProfiles
│  └─src
│      ├─关键词提取
│      │  └─.idea
│      │      └─inspectionProfiles
│      ├─前期学习
│      │  ├─异步操作
│      │  ├─数据解析
│      │  └─验证码 反扒机制
│      └─微博数据测试				     #微博数据获取主要工作文件
├─微博数据处理与可视化                  #评论部分的分析
│  ├─综合内容                         #微博数据库
│  └─评论分离						  #从微博中分离热评
│      ├─关键词提取                   #用TF-IDF算法获取热评关键词
│      │  ├─FinalKeyWords
│      │  ├─KeyWords
│      │  └─TF-IDF
│      ├─微博点赞评论数提取
│      ├─心态分析                    #大作业核心：心态分析
│      │  └─各阶段心态词频
│      └─评论文本
└─新闻数据处理与可视化                 #新闻部分的分析
    ├─Database                      #内嵌新闻数据库，程序方便使用
    ├─textClassifier文本分类器        #大作业bonus：用机器学习的方法对五个阶段做了文本分类器，传入一个												新闻可以自动检测是哪个阶段的并归好类
    │  └─Database                   
    │      └─Class
    │          ├─C001
    │          ├─C002
    │          ├─C003
    │          ├─C004
    │          └─C005
    ├─数据可视化处理                  #新闻可视化处理，内含可执行程序和可视化数据
    │  ├─可视化图片数据
    │  └─可视化文档数据
    ├─新闻分词及词频TF-IDF处理         #对新闻数据的第一步处理
    │  ├─Database
    │  ├─TF-IDF
    │  ├─各阶段分词
    │  └─各阶段词频
    └─爬取新闻数据
```

