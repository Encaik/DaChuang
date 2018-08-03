# -*- coding: utf-8 -*-
fp = open('static/data/sse/600008_2017_nzy.txt', 'rb+')
text = fp.read().decode('utf-8')
result = text.replace("\r", "").replace(" ", "")
fp.seek(0)
fp.truncate()
fp.write(result.encode('utf-8'))
