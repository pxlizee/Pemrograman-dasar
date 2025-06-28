from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_jadwal, name='daftar_jadwal'),
]