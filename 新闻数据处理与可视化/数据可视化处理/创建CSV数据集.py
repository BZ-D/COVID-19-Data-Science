if __name__ == '__main__':
    fw=open("2019.12.31-2020.6.30每日新闻条数.txt",'r',encoding='utf-8')
    lines=fw.readlines()
    f=open("txt暂时存储.txt",'w',encoding='utf-8')
    f.write("DayN\n")
    p=1
    for line in lines:
        line=line.strip()
        linelist=line.split(":")
        for k in range(0,int(linelist[1])):
            f.write(str(p)+'\n')
        p+=1