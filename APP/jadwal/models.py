from django.db import models

class Ruangan(models.Model):
    nama_ruangan = models.CharField(max_length=100, unique=True)
    gedung = models.CharField(max_length=50)
    lantai = models.IntegerField()
    kapasitas = models.IntegerField(default=30)

    def __str__(self):
        return self.nama_ruangan

class Jadwal(models.Model):
    mata_kuliah = models.CharField(max_length=200)
    nama_dosen = models.CharField(max_length=200)
    ruangan = models.ForeignKey(Ruangan, on_delete=models.CASCADE)
    hari = models.CharField(max_length=20)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()

    def __str__(self):
        return f"{self.mata_kuliah} - {self.ruangan}"