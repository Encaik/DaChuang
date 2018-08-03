from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexPage),
    path('index.html', views.indexPage),
    path('search.html', views.searchPage),
    path('result.html', views.contentPage),
    path('filepage.html', views.filePage),
]
