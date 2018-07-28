import os
import os.path


def getszseFileNames():
    filenames = []
    root = os.walk('static/report/szse')
    for _1, _2, files in root:
        for file in files:
            path = 'szse/'+file.split('.')[-2]
            filenames.append(path)
    return filenames


def getsseFileNames():
    filenames = []
    root = os.walk('static/report/sse')
    for _1, _2, files in root:
        for file in files:
            path = 'sse/' + file.split('.')[-2]
            filenames.append(path)
    return filenames
