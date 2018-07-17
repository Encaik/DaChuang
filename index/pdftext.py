#!/usr/bin/env python
# encoding: utf-8
from . import getinner

# 去除txt文件中的空格及换行符
def gettext():
    # getinner.gettext()
    fp = open('static/data/600225_2017_n.txt', 'rt+')
    text = fp.read().strip().replace("\n", "")
    fp.seek(0)
    fp.truncate()
    fp.write(text)
