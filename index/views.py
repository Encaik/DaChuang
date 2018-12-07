from django.shortcuts import render
from index.models import user, report, new
from django.core.paginator import Paginator
from static.py import search


def indexPage(request):
    return render(request, 'index.html')


def searchPage(request):
    if request.method == 'GET':
        search_word = request.GET.get('input')
        report = request.GET.get('report')
        year = request.GET.get('year')
    text = search.finish(search_word, report, year)
    page = request.GET.get('page', 1)
    cus_list = text
    paginator = Paginator(cus_list, 10)
    contacts = paginator.get_page(page)
    context = {
        'contacts': contacts,
        'str': search_word
    }
    return render(request, 'search.html', context)


# 0标题 1高亮副标题 2文件名 3全文 4id
def contentPage(request):
    if request.method == 'GET':
        search_word = request.GET.get('input')
        id = request.GET.get('id')
    text = search.finish(search_word)
    if id == '':
        context = {
            'text': []
        }
        return render(request, 'result.html', context)
    temp = int(id) - 1
    context = {
        'text': text[temp]
    }
    return render(request, 'result.html', context)


def filePage(request):
    if request.method == 'GET':
        file_name = request.GET.get('filename')
        file_mode = request.GET.get('filemode')
        file_path = request.GET.get('fileset')
    context = {
        'file_name': file_name,
        'file_mode': file_mode,
        'file_path': file_path
    }
    return render(request, 'filepage.html', context)
