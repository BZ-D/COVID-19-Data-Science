# -!- coding: utf-8 -!-

import re

str = "\n                                                                                                                        #在微博看联播#【直播！#新闻联播#】 O央视新闻的微博直播 . \u200b\u200b\u200b\u200b                                            "

# 消去换行符等冗余符号，得到微博内容
realContent = "".join(str.split())
print(realContent)
