from dc.views import *
from django.urls import path

app_name='anything'

urlpatterns=[
    path('pant/',pant,name='pant'),
    path('warner/',warner,name='warner'),
]