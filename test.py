# -*- coding: utf-8 -*-
fp = open('static/data/sse/600008_2017_n.txt', 'rt+')
text = fp.read()
result = text.strip().replace("\n", "")
print(result)
fp.seek(0)
fp.truncate()
fp.write(result)
