#!/usr/bin/env python
# encoding: utf-8

from static.py import pdfText, getFileName
import re
from index.models import report
from static.py.sse import ssegetPdfs
from static.py.szse import szsegetPdfs



# 关键词查找并返回结果字符串
def parse(search_word, name):
    fp = open('static/data/' + name + '.txt', 'rb')
    inner = fp.read().decode('utf-8')
    search = search_word.replace(" ", ".*")
    rstr = "[^。]*" + search + "[^。]*"
    text1 = re.findall(rstr, inner)
    text2 = sorted(set(text1), key=text1.index)

    result = []
    id = 0
    for _ in text2:
        id += 1
        if len(_) > 40:
            newtitle = _[0:30]+'...'
            newcontent = _[0:110]+'...'
        else:
            newtitle = _
            newcontent = _
        full = _
        for word in search_word.split(' '):
            highlight = "<b><font color='red'>" + word + "</font></b>"
            oldtitle = newtitle
            oldcontent = newcontent
            newtitle = re.sub(word, highlight, oldtitle)
            newcontent = re.sub(word, highlight, oldcontent)
            result.append([newtitle, newcontent, name, full, id])
        return result


def finish(search_word):
    results = []
    names = [
        'sse/600008_2017_n',
        'sse/600008_2017_nzy',
        'sse/600016_2017_nzy',
        'sse/600022_2017_n',
        'sse/600022_2017_nzy',
        'sse/600058_2017_n',
        'sse/600058_2017_nzy',
        'sse/600059_2017_n',
        'sse/600059_2017_nzy',
        'sse/600068_2017_n',
        'sse/600068_2017_nzy',
        'sse/600077_2017_n',
        'sse/600077_2017_nzy',
        'sse/600101_2017_n',
        'sse/600101_2017_nzy',
        'sse/600104_2017_n',
        'sse/600104_2017_nzy',
        'sse/600125_2017_n',
        'sse/600125_2017_nzy',
    ]
    # names = getFileName.getsseFileNames()+getFileName.getszseFileNames()
    for name in names:
        result = parse(search_word, name)
        if not result:
            continue
        results += result
    if not results:
        results = [['未搜索到相关内容']]
    return results

def server(name):
    # pdfText.getText(name)
    # ssegetPdfs.getpdf()
    # szsegetPdfs.getpdf()
    pass
