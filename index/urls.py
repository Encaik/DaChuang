from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('table.html', views.table),
    path('task.html', views.task),
    path('form.html', views.form),
    path('message.html', views.message),
    path('activity.html', views.table),
    path('charts.html', views.task),
    path('other-login.html', views.other_login),
    path('other-user-listing.html', views.other_user_listing),
    path('other-user-profile.html', views.other_user_profile),
    path('ui-button-icon.html', views.ui_button_icon),
    path('ui-typography.html', views.ui_typography)
]
