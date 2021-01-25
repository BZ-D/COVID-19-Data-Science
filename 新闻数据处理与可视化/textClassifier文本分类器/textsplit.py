def textsplit(filename,Class):
    root="C:\\Users\jiyun\\Desktop\\数据科学大作业疫情下的情绪分析\\新闻分词及词频处理"+"\\"+"textClassifier\\Database\\Class"
    i=1
    with open(filename,"r",encoding="utf-8") as fw:
        lines=fw.readlines()
        string=""
        for line in lines:
            string=string+line
        set=string.split("*")
        for s in set:
            if s!='':
                with open(root+"\\"+Class+"\\"+str(i)+".txt","w",encoding="utf-8") as f:
                    f.write(s)
                f.close()
                i+=1
if __name__ == '__main__':
    textsplit("C:\\Users\\jiyun\\Desktop\\数据科学大作业疫情下的情绪分析\\新闻分词及词频处理\\Database\\最新一轮疫情.txt","C005")
