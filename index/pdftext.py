#!/usr/bin/env python
# encoding: utf-8
from . import getinner


# 去除txt文件中的空格及换行符
def gettext(name):
    getinner.gettext(name)
    fp = open('static/data/'+name+'.txt', 'rt+')
    text = fp.read().strip().replace("\n", "")
    fp.seek(0)
    fp.truncate()
    fp.write(text)
