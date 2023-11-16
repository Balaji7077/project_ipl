from kolkata.views import *
from django.urls import path

app_name='anything'

urlpatterns=[
    path('iyer/',iyer,name='iyer'),
    path('rinku/',rinku,name='rinku')
]