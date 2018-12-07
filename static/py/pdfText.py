#!/usr/bin/env python
# encoding: utf-8
from static.py import getInner
from index.models import report


# 去除txt文件中的空格及换行符
def getText(name):
    # getInner.getText(name)
    fp = open('static/data/' + name + '.txt', 'rb+')
    text = fp.read().decode('utf-8')
    result = text.strip().replace("\r", "").replace(" ", "")
    fp.seek(0)
    fp.truncate()
    fp.write(result.encode('utf-8'))
    try:
        obj = report.objects.get(filename=name)
        obj.text = result
        obj.save()
    except:
        print('数据库同步失败')
        pass
