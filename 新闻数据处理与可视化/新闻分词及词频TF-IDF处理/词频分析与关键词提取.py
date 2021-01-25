from jieba import analyse
import collections
if __name__ == '__main__':
    filename = "最新阶段分词.txt"
    words_box = []
    words_box2 = []
    counts = {}
    with open(filename, 'rb') as f:
        for line in f:
            line.decode("utf-8")
            words_box.extend(line.strip().split())
        for word in words_box:
            word2 = word.decode("utf-8")
            words_box2.append(word2)
    for word in words_box2:
        if len(word) == 1:  # 单个词语不计算在内
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    with open("最新阶段词频.txt","w",encoding='utf-8') as f:
        for i in range(len(items)):
            word, count = items[i]
            f.write(word+"     "+str(count)+"\n")
    # TF-IDF方法抽取关键词
    tfidf = analyse.extract_tags
    analyse.set_stop_words("cn_stopwords.txt")
    filename = "最新阶段分词.txt"
    content = open(filename, 'rb').read()
    keywords = tfidf(content,topK=100,withWeight=True)
    # 输出抽取出的关键词
    with open("最新阶段关键词即TF-IDF权重.txt","w",encoding='utf-8') as f:
        for keyword,weight in keywords:
            print (keyword + "/"+str(weight))
            f.write(keyword + "     "+str(weight)+"\n")