from django.db import models

# Model Question dan Choice sudah bagus untuk polling
class Question(models.Model):
    # Nama field diubah agar lebih deskriptif (Rekomendasi)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# Model Settings dengan perbaikan indentasi
class Settings(models.Model):
    nama = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=200)

    # Fungsi __str__ ini sekarang ada di dalam class Settings
    def __str__(self):
        return self.nama
    
    # Class Meta ini sekarang ada di dalam class Settings
    class Meta:
        verbose_name_plural = "Settings"