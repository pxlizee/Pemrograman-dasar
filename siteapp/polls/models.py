import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField("Pertanyaan", max_length=200)
    pub_date = models.DateTimeField("Tanggal publikasi")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Baru dipublikasi?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("Pilihan", max_length=200)
    votes = models.IntegerField("Jumlah Suara", default=0)

    def __str__(self):
        return self.choice_text