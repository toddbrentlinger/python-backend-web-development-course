from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact/', views.contact, name = 'contact'),
    path('counter/', views.counter, name = 'counter')
]