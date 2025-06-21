from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('int:question/<int:question_id>/', views.results, name='results'),
    path('address/', views.address, name='address'),
    path('phone/', views.phone, name='phone'),
]
