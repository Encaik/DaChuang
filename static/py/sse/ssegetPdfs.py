import os
import urllib.request
from static.py.sse import getUrls


def getpdf():
    urls = getUrls.getUrls('2018-7-1', '2018-7-30', 5)
    for url in urls:
        print(url)
        file_name = url.split('/')[-1]
        try:
            u = urllib.request.urlopen(url)
            path = '../../report/sse/' + file_name
            print(path)
            if not os.path.exists(path):
                print('创建pdf文件')
                f = open(path, 'wb')
                print('创建完成')
                while True:
                    print('1')
                    buffer = u.read(8192)
                    print(buffer)
                    if not buffer:
                        break
                    f.write(buffer)
                f.close()
                print("成功下载文件" + file_name)
        except:
            print('下载文件失败' + file_name)
            pass
