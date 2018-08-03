#!/usr/bin/env python
# encoding: utf-8

from static.py import pdfText, getFileName
import re


# 关键词查找并返回结果字符串
def parse(search_word, name):
    try:
        # pdfText.getText(name)
        fp = open('static/data/' + name + '.txt', 'rb')
        inner = fp.read().decode('utf-8')
        text1 = re.findall(r'[^。]*' + search_word + r'[^。]*', inner)
        text2 = sorted(set(text1), key=text1.index)
        highlight = "<b><font color='red'>" + search_word + "</font></b>"
        result = []
        for _ in text2:
            if len(_) > 40:
                title = _[0:30]+'...'
                content = _[0:110]+'...'
                full = _
                hl_title = re.sub(search_word, highlight, title)
                hl_content = re.sub(search_word, highlight, content)
                result.append([hl_title, hl_content, name, full])
                return result
            title = _
            content = _
            full = _
            hl_title = re.sub(search_word, highlight, title)
            hl_content = re.sub(search_word, highlight, content)
            result.append([hl_title, hl_content, name, full])
        return result
    except:
        result = []
        return result


def finish(search_word):
    results = []
    names = getFileName.getsseFileNames()+getFileName.getszseFileNames()
    for name in names:
        result = parse(search_word, name)
        if not result:
            pass
        results += result
    return results
