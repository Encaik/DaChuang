from django.shortcuts import render
from index.models import user, report, new
from django.core.paginator import Paginator
from static.py import search


def indexPage(request):
    return render(request, 'index.html')


def searchPage(request):
    if request.method == 'GET':
        search_word = request.GET.get('input')
        if search_word == '':
            return render(request, 'index.html')
        if search_word is None:
            return render(request, 'index.html')
    text = search.finish(search_word)
    page = request.GET.get('page', 1)
    cus_list = text
    paginator = Paginator(cus_list, 25)
    contacts = paginator.get_page(page)
    context = {
        'contacts': contacts,
        'str': search_word
    }
    return render(request, 'search.html', context)


def contentPage(request):
    if request.method == 'GET':
        file_name = request.GET.get('filename')
    text = report.objects.get(filename=file_name)
    context = {
        'text': text
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
