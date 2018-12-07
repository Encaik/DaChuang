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
            path = 'static/report/sse/' + file_name
            print(path)
            if not os.path.exists(path):
                try:
                    f = open(path, mode='wb')
                    try:
                        while True:
                            buffer = u.read(8192)
                            if not buffer:
                                break
                            f.write(buffer)
                    except:
                        print('缓存文件失败' + file_name)
                        pass
                    f.close()
                    print("成功下载文件" + file_name)
                except:
                    print('创建文件失败' + file_name)
                    pass
        except:
            print('下载文件失败' + file_name)
            pass
