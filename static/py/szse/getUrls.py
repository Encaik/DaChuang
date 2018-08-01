# -*- coding: utf-8 -*-
import requests
import json


def getUrl(start, end, page):
    web = 'http://www.szse.cn/api/disc/announcement/annList'
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/51.0.2704.106 Safari/537.36',
        'Content-Type': 'application/json',
        'Host': 'www.szse.cn',
        'Referer': 'http://www.szse.cn/disclosure/listed/fixed/index.html'
    }
    payload = {
        "seDate": [start, end],
        "channelCode": ["fixed_disc"],
        "bigCategoryId": ["010301"],
        "pageSize": 30,
        "pageNum": page
    }
    urls = []
    req = requests.post(url=web, data=json.dumps(payload), headers = headers)
    text = json.loads(req.text)
    data = text['data']
    for pdf in data:
        url = 'http://disc.static.szse.cn'+pdf['attachPath']
        urls.append(url)
    return urls


def getUrls(start, end, page):
    allurls = []
    for i in range(page):
        i += 1
        result = getUrl(start, end, i)
        allurls += result
    allurls = list(set(allurls))
    return allurls

