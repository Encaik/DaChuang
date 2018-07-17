from django.shortcuts import render
from . import models, search


def index(request):
    return render(request, 'index.html', {'user': models.user.objects.all(), 'new': models.new.objects.all(), 'text': search.parse('福建省厦门市中级人民法院')})


def table(request):
    return render(request, 'table.html')


def task(request):
    return render(request, 'task.html')


def form(request):
    return render(request, 'form.html')


def message(request):
    return render(request, 'message.html')


def activity(request):
    return render(request, 'activity.html')


def charts(request):
    return render(request, 'charts.html')


def other_login(request):
    return render(request, 'other-login.html')


def other_user_listing(request):
    return render(request, 'other-user-listing.html')


def other_user_profile(request):
    return render(request, 'other-user-profile.html')


def ui_button_icon(request):
    return render(request, 'other-user-listing.html')


def ui_typography(request):
    return render(request, 'other-user-profile.html')
