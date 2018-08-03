#!/usr/bin/env python
# encoding: utf-8
from static.py import getInner


# 去除txt文件中的空格及换行符
def getText(name):
    # getInner.getText(name)
    fp = open('static/data/' + name + '.txt', 'rb+')
    text = fp.read().decode('utf-8')
    result = text.strip()
    fp.seek(0)
    fp.truncate()
    fp.write(result.encode('utf-8'))

