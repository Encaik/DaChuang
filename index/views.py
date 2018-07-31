from django.shortcuts import render
from index.models import user, report,new
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from static.py import search


def index(request):
    if request.method == 'GET':
        str = request.GET.get('input')
        if str == '':
            return render(request, 'index.html')
        if str is None:
            return render(request, 'index.html')
    text = search.finish(str)
    page = request.GET.get('page', 1)
    cus_list = text
    paginator = Paginator(cus_list, 25)
    contacts = paginator.get_page(page)
    context = {
        'contacts': contacts,
        'str': str
    }
    return render(request, 'index.html', context)
