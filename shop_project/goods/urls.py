# from django.contrib import admin
from django.urls import include, path


from .views import *

app_name = 'goods'

urlpatterns = [
    path('', catalog, name='index'),
    path('product/', product, name='product')
]