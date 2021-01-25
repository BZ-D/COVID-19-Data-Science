import sys
import re

print()
obj_file = input("\033[33m请输入文件路径及文件名：\033[35m");"\033[0m"
print()
obj_str = input("\033[33m请输入要查找的字符或字符串,多个以空格分隔：\033[35m");"\033[0m"
print()
file_obj = open('%s' % obj_file, 'r',encoding='utf-8').read()
str_re = "|".join(re.sub(' +', ' ', obj_str).split(" "))
all_str = re.finditer(r'%s' % str_re, file_obj)
count_dict = {}
for s in all_str:
    count_dict[s.group()] = count_dict.setdefault(s.group(), 0) + 1

# k[0]表示按key值，k[1]表示按value值排序，reverse为True表示倒序，False表示正序
count_dict = sorted(count_dict.items(), key=lambda k: k[1], reverse=True)

for c in count_dict:
    print("\033[32m【 %s 】 出现的次数为 : %d\033[0m" % (c[0], c[1]))

print()