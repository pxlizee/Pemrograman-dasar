from django.contrib import admin
from django.urls import path, include # Tambahkan include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jadwal.urls')), # TAMBAHKAN INI
]