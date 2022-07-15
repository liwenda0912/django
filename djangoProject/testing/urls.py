from django.contrib import admin
from django.urls import path
from .views import index,add
from . import views

# 快捷键 alt+enter
urlpatterns = [
    path('index/', index),
    path('add', add)
]
