from django.shortcuts import render
from .models import Jadwal

def daftar_jadwal(request):
    semua_jadwal = Jadwal.objects.all()
    context = {
        'semua_jadwal': semua_jadwal
    }
    return render(request, 'list_jadwal.html', context)