from django.urls import path
from . import views # Pastikan import ini ada

app_name = 'polls'
urlpatterns = [
    # ... URL polling dari Pilihan 1 ...
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]