# -*- coding: utf-8 -*-
import urllib
import urllib.request
import re
import json


def getUrl(start, end, page):
    web = 'http://query.sse.com.cn/infodisplay/queryLatestBulletinNew.do' \
          '?&jsonCallBack=jsonpCallback6133&productId=&reportType2=DQGG' \
          '&reportType=YEARLY&beginDate='+start+'&endDate='+end+'&pageHelp.pageSize=25' \
          '&pageHelp.pageCount=50&pageHelp.pageNo=1&pageHelp.beginPage=1&' \
          'pageHelp.cacheSize=1&pageHelp.endPage='+page+'1'
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/51.0.2704.106 Safari/537.36',
        'Cookie': web,
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Host': 'query.sse.com.cn',
        'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/'
    }
    urls = []
    req = urllib.request.Request(web, None, headers)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    text = the_page.decode("utf8")
    js = re.search('{"actionErrors(.*)', text).group()[:-1]
    content0 = json.loads(js)
    content = content0['result']
    for info in content:
        url = 'http://www.sse.com.cn'+info['URL']
        urls.append(url)
    return urls


def getUrls(start, end, page):
    try:
        allurls = []
        result = getUrl(start, end, page)
        allurls += result
        return allurls
    except:
        print('end')
