#!/usr/bin/env python
# encoding: utf-8
from static.py import pdfText
import re


# 关键词查找并返回结果字符串
def parse(str, name):
    # pdfText.getText(name)
    fp = open('static/data/'+name+'.txt', 'rt')
    inner = fp.read()
    text1 = re.findall('[\u4e00-\u9fa5, 0-z]{5,50}'+str+'[\u4e00-\u9fa5, 0-z]{5,50}', inner)
    text2 = sorted(set(text1), key=text1.index)
    highlight = "<b><font color='red'>"+str+"</font></b>"
    result = []
    for _ in text2:
        temp = re.sub(str, highlight, _)
        result.append([temp, name])
    return result


def finish(str):
    results = []
    name = [
        '1204740858',
        '1204740820',
        '1204740521',
        '1204734306',
        '600225_2017_n',
        '600869_2017_n',
        '603315_2017_n',
        '603895_2017_n'
    ]
    for _ in name:
        result = parse(str, _)
        results.append(result)
    return results
