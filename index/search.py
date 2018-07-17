#!/usr/bin/env python
# encoding: utf-8
from . import pdftext

# 关键词查找并返回结果字符串
def parse(str):
    pdftext.gettext()
    fp = open('static/data/600225_2017_n.txt', 'rt')
    inner = fp.read()
    key = inner.find(str)
    text = inner[key-10:key+len(str)+10]
    return text
