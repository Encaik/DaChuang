# -*- coding: utf-8 -*-
import urllib
import urllib.request
import re
import json
from index.models import report, company


def getUrl(start, end, page):
    if page == 1:
        web = 'http://query.sse.com.cn/infodisplay/queryLatestBulletinNew.do?&jsonCallBack=jsonpCallback82326&productId=&reportType2=DQGG&reportType=&beginDate=' + start + '&endDate=' + end + '&pageHelp.pageSize=25&pageHelp.pageCount=50&pageHelp.pageNo=' + page + '&pageHelp.beginPage=' + page + '&pageHelp.cacheSize=1&pageHelp.endPage=5'
    web = 'http://query.sse.com.cn/infodisplay/queryLatestBulletinNew.do?&jsonCallBack=jsonpCallback82326&productId=&reportType2=DQGG&reportType=&beginDate=' + start + '&endDate=' + end + '&pageHelp.pageSize=25&pageHelp.pageCount=50&pageHelp.pageNo=' + page + '&pageHelp.beginPage=' + page + '&pageHelp.cacheSize=1&pageHelp.endPage=' + page + '1'
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
        url = 'http://www.sse.com.cn' + info['URL']
        filename = 'sse/' + info['URL'].split('/')[-1].split('.')[0]
        rtype = info['bulletin_Type']
        rdate = info['SSEDate']
        year = info['bulletin_Year']
        cnum = info['security_Code']
        rtitle = info['title']
        object = company.objects.get(cnum=cnum)
        data = report(
            rcp_id=object.cid,
            filename=filename,
            rtype=rtype,
            rdate=rdate,
            year=year,
            rtitle=rtitle
        )
        data.save()
        urls.append(url)
        print(info['title'] + '获取完成')
    return urls


# 只能搜索日期间隔少于30天的
def getUrls(start, end, page):
    allurls = []
    for i in range(page):
        i += 1
        result = getUrl(start, end, str(i))
        allurls += result
    print('全部Url获取完成')
    return allurls
