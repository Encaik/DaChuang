#!/usr/bin/env python
# encoding: utf-8
import os

from static.py import pdfText, getFileName
import re


# 关键词查找并返回结果字符串
def parse(str, name):
    try:
        # pdfText.getText(name)
        fp = open('static/data/' + name + '.txt', 'rb')
        inner = fp.read().decode('utf-8')
        text1 = re.findall('[\u4e00-\u9fa5, 0-z]{5,50}' + str + '[\u4e00-\u9fa5, 0-z]{5,50}', inner)
        text2 = sorted(set(text1), key=text1.index)
        highlight = "<b><font color='red'>" + str + "</font></b>"
        result = []
        for _ in text2:
            temp = re.sub(str, highlight, _)
            result.append([temp, name, name.split('/')[-1]])
        return result
    except:
        result = []
        return result


def finish(str):
    results = []
    names = getFileName.getsseFileNames()+getFileName.getszseFileNames()
    for name in names:
        result = parse(str, name)
        if not result:
            pass
        results += result
    return results
