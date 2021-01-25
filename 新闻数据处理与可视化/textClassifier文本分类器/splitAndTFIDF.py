import jieba
def splitAndTFIDF(filename,stopwords_file,fencifile,cipinfile,TFIDFfile):
    stop_f = open(stopwords_file, "r", encoding='utf-8')
    stop_words = list()
    for line in stop_f.readlines():
        line = line.strip()
        if not len(line):
            continue
        stop_words.append(line)
    stop_f.close
    print(len(stop_words))
    f = open(filename, "r", encoding='utf-8')
    result = list()
    for line in f.readlines():
        line = line.strip()
        if not len(line):
            continue
        outstr = ''
        seg_list = jieba.cut(line, cut_all=False)
        for word in seg_list:
            if word not in stop_words:
                if word != '\t':
                    outstr += word
                    outstr += " "
        result.append(outstr.strip())
    f.close
    with open(fencifile, "w", encoding='utf-8') as fw:
        for sentence in result:
            sentence.encode('utf-8')
            data = sentence.strip()
            if len(data) != 0:
                fw.write(data)
                fw.write("\n")
    words_box = []
    words_box2 = []
    counts = {}
    with open(fencifile, 'rb') as f:
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
    with open(cipinfile, "w", encoding='utf-8') as f:
        for i in range(len(items)):
            word, count = items[i]
            f.write(word + "     " + str(count) + "\n")
    # TF-IDF方法抽取关键词
    tfidf = analyse.extract_tags
    analyse.set_stop_words("cn_stopwords.txt")
    content = open(fenifile, 'rb').read()
    keywords = tfidf(content, topK=100, withWeight=True)
    # 输出抽取出的关键词
    with open(TFIDFfile, "w", encoding='utf-8') as f:
        for keyword, weight in keywords:
            print(keyword + "/" + str(weight))
            f.write(keyword + "     " + str(weight) + "\n")
