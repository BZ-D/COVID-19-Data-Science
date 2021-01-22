
f = open(r'C:\Users\Ding\Desktop\Crawler-Studying\微博数据\评论分离\关键词提取\KeyWords\2021年1月评论关键词.txt', 'r', encoding='utf-8')
lines = f.readlines()
count = 0
for line in lines:
    count += int(line.split(',')[1])
print(count)
f.close()

# 总共：352689次
# 1月：63432
# 2月：89235
# 3月：55353
# 4月：52137
# 5月：42781
# 12月：20773
# 2021年1月：28978