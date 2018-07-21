#!/usr/bin/env python
# encoding: utf-8
from static.py import pdfText
import re


# 关键词查找并返回结果字符串
def parse(str, name):
    # name = '1204740858'
    # pdfText.getText(name)
    fp = open('static/data/'+name+'.txt', 'rt')
    inner = fp.read()
    text1 = re.findall('[\u4e00-\u9fa5,0-9,A-z]{5,}'+str+'[\u4e00-\u9fa5,0-9,A-z]{5,}', inner)
    text2 = sorted(set(text1), key=text1.index)
    highlight = "<b><font color='red'>"+str+"</font></b>"
    result = []
    for _ in text2:
        temp = re.sub(str, highlight, _)
        result.append([temp, name])
    return result


def finish(str):
    result = []
    result1 = parse(str, '1204740858')
    result2 = parse(str, '1204740820')
    result3 = parse(str, '1204740521')
    result4 = parse(str, '1204734306')
    result.append(result1)
    result.append(result2)
    result.append(result3)
    result.append(result4)
    return result
