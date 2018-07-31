#!/usr/bin/env python
# encoding: utf-8
import os

from static.py import pdfText, getFileName
import re


# 关键词查找并返回结果字符串
def parse(str, name):
    # pdfText.getText(name)
    fp = open('static/data/'+name+'.txt', 'rt')
    try:
        inner = fp.read()
        text1 = re.findall('[\u4e00-\u9fa5, 0-z]{5,50}'+str+'[\u4e00-\u9fa5, 0-z]{5,50}', inner)
        text2 = sorted(set(text1), key=text1.index)
        highlight = "<b><font color='red'>"+str+"</font></b>"
        result = []
        for _ in text2:
            temp = re.sub(str, highlight, _)
            result.append([temp, name, name.split('/')[-1]])
        return result
    except:
        pass

def finish(str):
    results = []
    name = getFileName.getsseFileNames()+getFileName.getszseFileNames()
    # name = {
    #     '1204734306',
    #     '1204740521',
    #     '1204740820',
    #     '1204740858',
    # }
    for _ in name:
        result = parse(str, _)
        results += result
    return results
