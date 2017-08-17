# -*- coding: utf-8 -*-

import re

s = "wo shi xiaohongjun mmemem ,这是一个正则表达式, ceshi9527, 15517505563, 010-12345678, (010)23456788, (010)-23456788"

# 匹配数字
p = re.compile(r"\d+")

# 匹配电话号码
p1 = re.compile(r"[\(]\d{3}[\)]?-\d{8}|\d{3}?\d{8}")

# 匹配字母数字下划线
p2 = re.compile(r"\w")

# 非字母数字下划线
p3 = re.compile(r"\W")

# 非数字
p4 = re.compile(r"\D")

# 匹配空白的字符
p5 = re.compile(r"\s")

# 非空白的字符
p6 = re.compile(r"\S")

# 匹配单词的开始和结束位置
p7 = re.compile(r"\b")

# 匹配任意字符
p8 = re.compile(r".")

# 匹配单个字符串
p9 = re.compile(r"[xiaohongjun]")

# p10 = re.compile(r"[x-n]")

p11 = re.compile(r"[A-Za-z]{0, 2}")

print p11.findall(s)





