xin_tai_ci_dian = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\心态分析\心态词典.txt'
xin_tai_value = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\心态分析\心态值.txt'
locationsrc = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\provinces&cities.txt'

# 已经排好序的tf—idf文件路径
tf_idfSrc = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\TF-IDF\2020年12月及2021年1月TF-IDF.txt'
# 碰撞后的心态频数存放处
dest = r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\心态分析\各阶段心态词频\2020年12月及2021年1月心态词频.txt'


def readLines(filename):
    f = open(filename, 'r', encoding='utf-8')
    content = f.readlines()
    f.close()

    # 去换行符
    length = len(content)
    for i in range(length):
        content[i] = content[i][:-1]

    return content


def getTerm(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()[:101]
    terms = []
    freq = []
    for line in lines:
        aline = line.split(',')
        terms.append(aline[0][5:])
        freq.append(int(aline[1][6:]))
    return [terms, freq]


def writedict():
    attitude_dict = {}
    value_dict = {}
    attitudes = readLines(xin_tai_ci_dian)
    values = readLines(xin_tai_value)

    # 向attitude_dict录入 term -- attitude 字典字，注意一个term可能对应多个心态，需用list包装心态
    for line in attitudes:
        tmp = line.split(' ')
        length = len(tmp)
        attitude = []
        for i in range(1, length):
            attitude.append(float(tmp[i]))
        attitude_dict[tmp[0]] = attitude

    # 向value_dict中录入 value -- attitude 字典字
    for value in values:
        tmp = value.split(' ')
        value_dict[float(tmp[1])] = tmp[0]

    return [attitude_dict, value_dict]


def analyse():
    '''
        绝望 0.00
        愤怒 0.05
        恐惧 0.10
        厌恶&嘲讽 0.15
        悲伤 0.20
        担忧 0.25
        焦虑 0.30
        慌张 0.35
        惊讶 0.40
        迷茫 0.45
        平静 0.50
        积极 0.55
        鼓励 0.60
        祝愿 0.65
        敬佩 0.70
        感激 0.75
        乐观 0.80
        期待 0.85
        渴望 0.90
        喜悦 0.95
        热爱 1.00
    '''

    dicts = writedict()
    attitude_dict = dicts[0]  # 词语→心态值
    value_dict = dicts[1]  # 心态值→心态词

    # 该dict用于存放每个心态值的频数
    attitude_freq_dict = {0.00: 0, 0.05: 0, 0.10: 0, 0.15: 0, 0.20: 0, 0.25: 0, 0.30: 0, 0.35: 0, 0.40: 0, 0.45: 0,
                          0.50: 0,
                          0.55: 0, 0.60: 0, 0.65: 0, 0.70: 0, 0.75: 0, 0.80: 0, 0.85: 0, 0.90: 0, 0.95: 0, 1.00: 0}
    tmp = getTerm(tf_idfSrc)
    terms = tmp[0]  # 待碰撞词汇
    counts = tmp[1]  # 词数 term count
    locations = readLines(locationsrc)  # 心态词典补充：地名

    length = len(terms)

    # 碰撞过程
    for i in range(0, length):
        if terms[i] in attitude_dict:
            # 碰撞成功
            attList = attitude_dict[terms[i]]  # 一个term对应一个心态列表
            for attitude in attList:
                attitude_freq_dict[attitude] += counts[i]
        if terms[i] in locations:
            # 评论中若出现地名，表现出什么心态？
            attitude_freq_dict[0.30] += counts[i]
            attitude_freq_dict[0.25] += counts[i]
            attitude_freq_dict[0.60] += counts[i]

    # 碰撞结果写入文件
    f = open(dest, 'w', encoding='utf-8')
    for item in attitude_freq_dict.items():
        attitude = value_dict[item[0]]
        count = item[1]
        f.write(str(item[0]) + ' ' + str(attitude) + ' ' + str(count) + '\n')

    f.close()

if __name__ == '__main__':
    analyse()
