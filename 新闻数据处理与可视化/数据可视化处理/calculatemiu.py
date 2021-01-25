def cal(x,y):
    sum=0
    res=0
    for i in y:
        sum=sum+i
    jishu=0
    for j in y:
        res=res+jishu*j/sum
        jishu+=1
    print(res)
    return res
if __name__ == '__main__':
    fw = open('2019.12.31-2020.6.30每日新闻条数.txt', 'r', encoding='utf-8')
    x = []
    y = []
    lines = fw.readlines()
    for line in lines:
        listline = line.split(':')
        x.append(listline[0])
        y.append(int(listline[1]))
    miu=cal(x,y)