#!/usr/bin/env python
# encoding: utf-8
from static.py import getInner


# 去除txt文件中的空格及换行符
def getText(name):
    getInner.getText(name)
    try:
        fp = open('static/data/' + name + '.txt', 'rt+')
        text = fp.read().strip().replace("\n", "")
        fp.seek(0)
        fp.truncate()
        fp.write(text)
    except:
        pass
