#!/usr/bin/env python
# encoding: utf-8
import re
from ..py.pdfText import getText
from ..py.sse import ssegetPdfs
from ..py.szse import szsegetPdfs
from index.models import report as rep


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
        for word in search_word.split(' '):
            highlight = "<b><font color='red'>" + word + "</font></b>"
            oldtitle = newtitle
            oldcontent = newcontent
            newtitle = re.sub(word, highlight, oldtitle)
            newcontent = re.sub(word, highlight, oldcontent)
            result.append([newtitle, newcontent, name, inner, id])
        return result


def finish(search_word, report, year):
    server()
    results = []
    names = []
    # names = getFileName.getsseFileNames()+getFileName.getszseFileNames()
    for name in names:
        try:
            print(name)
            object = rep.objects.get(filename='name')
            print(report)
            print(object.rtype)
            if object.rtype != report or object.year != year:
                pass
            result = parse(search_word, name)
            if not result:
                continue
            results += result
        except:
            results = [['未搜索到相关内容']]
    if not results:
        results = [['未搜索到相关内容']]
    return results


def server():
    #getText(name)
    ssegetPdfs.getpdf()
    # szsegetPdfs.getpdf()
    pass
