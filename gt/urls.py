from gt.views import *
from django.urls import path

app_name='anything'

urlpatterns=[
    path('pandya/',pandya,name='pandya'),
    path('gill/',gill,name='gill'),
]