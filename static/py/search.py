#!/usr/bin/env python
# encoding: utf-8
import re

from static.py import getFileName
from ..py.pdfText import getText
from ..py.sse import ssegetPdfs
from ..py.szse import szsegetPdfs
from index.models import report as rep


# 关键词查找并返回结果字符串
def parse(search_word, name, id):
    # fp = open('static/data/' + name + '.txt', 'rb')
    # inner = fp.read().decode('utf-8')
    inner = rep.objects.get(filename=name).text
    search = search_word.replace(" ", ".*")
    rstr = "[^。]*" + search + "[^。]*"
    text1 = re.findall(rstr, inner)
    text2 = sorted(set(text1), key=text1.index)
    result = []
    id += 1
    for _ in text2:
        if len(_) > 40:
            newtitle = _[0:30]+'...'
            newcontent = _[0:110]+'...'
        else:
            newtitle = _
            newcontent = _
        for word in search_word.split(' '):
            highlight = "<b><font color='red'>" + word + "</font></b>"
            oldtitle = newtitle
            oldcontent = newcontent
            newtitle = re.sub(word, highlight, oldtitle)
            newcontent = re.sub(word, highlight, oldcontent)
            result.append([id, newtitle, newcontent, name, inner, rep.objects.get(filename=name).rdate, rep.objects.get(filename=name).rtype])
        return result


#0id 1标题 2高亮副标题 3文件名 4全文 5日期 6类型
def finish(search_word, report, year):
    results = []
    names = getFileName.getsseFileNames()
    id = 0
    for name in names:
        obj = rep.objects.get(filename=name)
        if obj.rtype != report or obj.year != year:
            continue
        result = parse(search_word, name, id)
        id += 1
        if not result:
            continue
        results += result
    if not results:
        results = [['未搜索到相关内容']]
    return results


def server(name):
    # getText(name)
    # ssegetPdfs.getpdf()
    # szsegetPdfs.getpdf()
    pass
